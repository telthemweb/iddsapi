from flask import Blueprint,render_template, request, redirect, flash, send_file, session,jsonify,make_response
from openpyxl import Workbook
from sqlalchemy.sql import func
import os
import io
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import requests
from datetime import datetime
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from . import db
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib
from .model import Administrator,Role,Recommendation,Desease,Systemlog,Audit,Deseaselog
views = Blueprint('views',__name__)



ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
UPLOAD_FOLDER="C:/Users/Admin/OneDrive/Desktop/projects_docs/project/iddsapp/app_web/testing_apploads/"
UPLOAD_FOLDER_D='C:/Users/Admin/OneDrive/Desktop/projects_docs/project/iddsapp/app_web/static/uploads'
filepath = 'C:/Users/Admin/OneDrive/Desktop/projects_docs/project/iddsapp/app_web/model_folder/maize_leaf_disease_detection_model.h5'
filepath1 = 'C:/Users/Admin/OneDrive/Desktop/projects_docs/project/iddsapp/app_web/model_folder/maize_leaf_disease_detection_model.keras'
model = load_model(filepath)



@views.route('/')
def login():
    if 'loggedin' in session:
        flash('Already Login!', category='error')
        return redirect("/dashboard")
    return render_template('/login.html',title='Login system')

@views.route('/check_user', methods=['POST'])
def login_auth():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        hash = password + "your secret key"
        hash = hashlib.sha1(hash.encode())
        password = hash.hexdigest()
        account = Administrator.query.filter_by(email=email,password=password).first()
        if account:
            # Add to systemlogs
            ipaddress='N/A'
            geolocationap='N/A'
            useaccountname=account.name+" "+account.surname
            userlog = Systemlog(administrator_id=account.id,timein=func.now(),ipaddress=ipaddress,geolocationap=geolocationap,country='Zimbabwe',city='Harare',timeout='PENDING',useaccountname=useaccountname)
            db.session.add(userlog)
            db.session.commit()
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account.id
            session['name'] = account.name
            session['surname'] = account.surname
            session['role_id'] = account.role_Id
            session['phone'] = account.phone
            session['email'] = account.email
            session['gender'] = account.gender
            session['city'] = account.city
            session['address'] = account.address
            flash('Logged in successfully', category='success')
            return redirect("/dashboard")
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password!',category='error')
            return redirect("/")


@views.route('register')
def register():
    if 'loggedin' in session:
        flash('Already Login!', category='error')
        return redirect("/dashboard")
    return render_template('/register.html',title='Registration system')

@views.route("/createaccount", methods=['POST'])
def createAccount():
    if request.method == 'POST' and  'name' in request.form and 'surname' in request.form and 'password' in request.form and 'address' in request.form and 'gender' in request.form and 'email' in request.form and 'phone' in request.form and 'city' in request.form:

            role_Id = 2
            name = request.form['name']
            surname = request.form['surname']
            password=request.form['password']
            address = request.form['address']
            gender = request.form['gender']
            email = request.form['email']
            phone = request.form['phone']
            city = request.form['city']

            account = Administrator.query.filter_by(email=email).first()

             # If account exists show error and validation checks
            if account:
                flash('Account already exists!',category='error')
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash('Invalid email address!')
            elif not name or not surname or not password  or not email:
                flash('Please fill out the form!',category='error')

            else:
                hash = password + "your secret key"
                hash = hashlib.sha1(hash.encode())
                password = hash.hexdigest()
                user= Administrator(role_Id=role_Id,name=name,surname=surname,password=password,email=email,phone=phone,gender=gender,city=city,address=address)
                db.session.add(user)
                db.session.commit()
                flash('Account successfully created', category='success')
                return redirect('/')



@views.route("/dashboard")
def dashboard():
    if 'loggedin' in session:
        return render_template("/dashboard.html",  name=session['name'], role=session['role_id'])
    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')

@views.route("/profile")
def profile():
    if 'loggedin' in session:
        return render_template("/profile.html",title="My Profile",name=session['name'],role=session['role_id'])
    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')

@views.route("/changepassword",methods=['POST'])
def changepassword():
    if request.method == 'POST' and  'newpassword' in request.form and 'cnewpassword' in request.form and 'userid' in request.form:
        userid = request.form['userid']
        newpassword = request.form['newpassword']
        cnewpassword = request.form['cnewpassword']

        if newpassword ==cnewpassword:
            account = Administrator.query.filter_by(id=userid).first()
            if account:
                hash = newpassword + "your secret key"
                hash = hashlib.sha1(hash.encode())
                password = hash.hexdigest()
                account.password=password
                db.session.commit()
                flash('Your password successfully changed!!', category='success')
                return redirect('/logout')

# ==============================ROLE=============================================
@views.route("/roles")
def roles():
    if 'loggedin' in session:
        roles = Role.query.all()
        return render_template("/role.html",title="System Roles",roles=roles)
    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


@views.route("/addrole", methods=['POST'])
def addrole():
    if 'loggedin' in session:
        if request.method == 'POST' and 'name' in request.form:
            name = request.form['name']
            role = Role(name=name)
            db.session.add(role)

            newvalue = {'name': name}
            audit = Audit(administrator_id=session['id'], entity='Role', oldvalue='N/A',
                          newvalue=newvalue, action='CREATE ROLE')
            db.session.add(audit)

            db.session.commit()
            flash('Role successfully created', category='success')
            return redirect('/roles')

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


@views.route("/role/<id>")
def role(id):
    if 'loggedin' in session:
        role = Role.query.filter_by(id=id).first()
        return render_template('editrole.html',title="System Roles | Edit "+role.name, role=role)
    flash('You are not loggedin! Please sign in now!!', category='error')
    return redirect('/')


@views.route("/role/update/<id>", methods=['POST'])
def roleupdate(id):
    if 'loggedin' in session:
        if request.method == 'POST' and 'name' in request.form:
            name = request.form['name']
            role = Role.query.filter_by(id=id).first()
            oldvalue = {'name': role.name}
            if role:
                role.name=name

                newvalue = {'name': name}
                audit = Audit(administrator_id=session['id'], entity='Role', oldvalue=oldvalue,
                              newvalue=newvalue, action='UPDATE ROLE')
                db.session.add(audit)


                db.session.commit()
                flash('Role successfully updated!!', category='success')
                return redirect('/roles')

    flash('You are not loggedin! Please sign in now!!', category='error')
    return redirect('login')

@views.route("/role/delete/<id>")
def delete(id):
    if 'loggedin' in session:
        role = Role.query.filter_by(id=id).first()
        oldvalue = {'name': role.name}
        if role:
            if len(role.administrators)==0:
                db.session.delete(role)

                newvalue = {'name': 'DELETED ROLE'}
                audit = Audit(administrator_id=session['id'], entity='Role', oldvalue=oldvalue,
                          newvalue=newvalue, action='DELETE ROLE')
                db.session.add(audit)
                db.session.commit()
                flash('Role successfully deleted!!', category='success')
                return redirect('/roles')
            else:
                flash('Role cannot be deleted because there is data depend on it!!', category='error')
                return redirect('/roles')



    flash('You are not loggedin! Please sign in now!!', category='error')
    return redirect('login')
# =======================================================================================
# SYSTEM USERS
@views.route("/users")
def users():
    if 'loggedin' in session:
        users=Administrator.query.order_by(Administrator.created_at.desc()).all() #.order_by(Role.created.desc()).all()
        roles = Role.query.all()
        return render_template("/user.html",title="System Users",users=users,roles=roles)


@views.route("/adduser", methods=['POST'])
def addUser():
    if 'loggedin' in session:
        if request.method == 'POST' and 'role_Id' in request.form and 'name' in request.form and 'surname' in request.form and 'password' in request.form and 'address' in request.form and 'gender' in request.form and 'email' in request.form and 'phone' in request.form and 'city' in request.form:

            role_Id = request.form['role_Id']
            name = request.form['name']
            surname = request.form['surname']
            password = request.form['password']
            address = request.form['address']
            gender = request.form['gender']
            email = request.form['email']
            phone = request.form['phone']
            city = request.form['city']

            account = Administrator.query.filter_by(email=email).first()

            # If account exists show error and validation checks
            if account:
                flash('Account already exists!', category='error')
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                flash('Invalid email address!')
            elif not name or not surname or not password or not email:
                flash('Please fill out the form!', category='error')

            else:
                hash = password + "your secret key"
                hash = hashlib.sha1(hash.encode())
                password = hash.hexdigest()
                user = Administrator(role_Id=role_Id, name=name, surname=surname, password=password, email=email,
                                     phone=phone, gender=gender, city=city, address=address)
                db.session.add(user)

                audit = Audit(administrator_id=session['id'], entity='Administrator', oldvalue="no",newvalue='New user created',action='CREATE USER ACCOUNT')
                db.session.add(audit)
                db.session.commit()
                flash('Account successfully created', category='success')
                return redirect('/users')



    flash('You are not loggedin! Please sign in now!!')
    return redirect('/')

@views.route("/user/<id>")
def user(id):
    if 'loggedin' in session:
        user = Administrator.query.filter_by(id=id).first()
        roles = Role.query.all()
        return render_template('edituser.html',title="System Users | Edit "+user.name, user=user,roles=roles)
    flash('You are not loggedin! Please sign in now!!', category='error')
    return redirect('/')


@views.route("/user/update/<id>", methods=['POST'])
def updateuser(id):
    if 'loggedin' in session:
        role_Id = request.form['role_Id']
        name = request.form['name']
        surname = request.form['surname']
        address = request.form['address']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        city = request.form['city']
        user = Administrator.query.filter_by(id=id).first()
        if user:
            oldvalue = {'role_Id': user.role_Id, 'name': user.name, 'surname': user.surname, 'address': user.address,
                        'gender': user.gender, 'email': user.email, 'phone': user.phone, 'city': user.city}

            user.role_Id = role_Id
            user.name = name
            user.surname = surname
            user.address = address
            user.gender = gender
            user.email = email
            user.phone = phone
            user.city = city

            newvalue = {'role_Id': role_Id,'name': name,'surname': surname,'address': address,'gender': gender,'email': email,'phone': phone,'city': city}
            audit = Audit(administrator_id=session['id'], entity='Administrator', oldvalue=oldvalue,
                          newvalue=newvalue, action='UPDATE USER ACCOUNT')
            db.session.add(audit)
            db.session.commit()

        flash('User successfully updated!!', category='success')
        return redirect('/users')




    flash('You are not loggedin! Please sign in now!!', category='error')
    return redirect('/')

# =====================================================================================
# DESEASE
@views.route("/deseases")
def deseases():
    if 'loggedin' in session:

        deseases = Desease.query.order_by(Desease.created_at.desc()).all()
        return render_template("/desease.html", title="Maize Deseases", deseases=deseases)

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


@views.route("/adddesease", methods=['POST'])
def adddesease():
    if 'loggedin' in session:
        if request.method == 'POST' and 'name' in request.form and 'systoms' in request.form:
            name = request.form['name']
            systoms = request.form['systoms']

            file = request.files['maizefile']
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER_D, filename)
            file.save(file_path)

            desease = Desease(name=name, systoms=systoms,imageurl=filename)
            db.session.add(desease)

            newvalue = {'name': name,'systoms':systoms,'imageurl':imageurl}
            audit = Audit(administrator_id=session['id'], entity='Desease', oldvalue='N/A',
                          newvalue=newvalue, action='CREATE DESEASE')
            db.session.add(audit)

            db.session.commit()
            flash('Desease created successfully', category='success')
            return redirect('/deseases')

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


@views.route("/desease/show/<id>")
def getDetails(id):
    if 'loggedin' in session:
        desease =  Desease.query.filter_by(id=id).first()
        return render_template('editdesease.html',title="Maize Deseases | Edit", desease=desease)
    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


@views.route("/desease/update/<id>", methods=['POST'])
def updatedesease(id):
    if 'loggedin' in session:
        if request.method == 'POST' and 'name' in request.form and 'systoms' in request.form:
            name = request.form['name']
            systoms = request.form['systoms']

            file = request.files['maizefile']
            filename = file.filename
            file_path = os.path.join(UPLOAD_FOLDER_D, filename)
            file.save(file_path)


            desease = Desease.query.filter_by(id=id).first()
            newvalue = {'name': desease.name, 'systoms': desease.systoms, 'imageurl': desease.imageurl}
            if desease:
                desease.name=name
                desease.systoms=systoms
                desease.imageurl = filename

                newvalue = {'name': name, 'systoms': systoms, 'imageurl': imageurl}
                audit = Audit(administrator_id=session['id'], entity='Desease', oldvalue='N/A',
                              newvalue=newvalue, action='UPDATE DESEASE')
                db.session.add(audit)


                db.session.commit()


                flash('Desease has been updated successfully!!',category='success')
                return redirect('/deseases')

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')
@views.route("/desease/delete/<id>")
def deletedesease(id):
    if 'loggedin' in session:
        desease = Desease.query.filter_by(id=id).first()
        oldvalue = {'name': desease.name, 'systoms': desease.systoms, 'imageurl': desease.imageurl}
        if desease:
            if len(desease.recommendations) == 0:
                db.session.delete(desease)

                newvalue = {'name': 'DELETED'}
                audit = Audit(administrator_id=session['id'], entity='Desease', oldvalue=oldvalue,
                              newvalue=newvalue, action='DELETE DESEASE')
                db.session.add(audit)
                db.session.commit()
                flash('Desease successfully deleted!!', category='success')
                return redirect('/deseases')
            else:
                flash(f'Desease {desease.name} cannot be deleted because there is data depend on it!!', category='error')
                return redirect('/deseases')

@views.route("/desease/recommendation/<id>")
def getRecommendation(id):
    if 'loggedin' in session:
        reco = Recommendation.query.filter_by(desease_Id=id).first()
        return render_template('viewdesease.html',title="Maize Deseases | Recommendation",recom=reco,desease_Id=id)

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


@views.route("/addRecom", methods=['POST'])
def addRecom():
    if 'loggedin' in session:
        desease_Id = request.form['desease_Id']
        recommendationmessage = request.form['recommendationmessage']
        recommandationstore = Recommendation(desease_Id=desease_Id, recommendationmessage=recommendationmessage)
        db.session.add(recommandationstore)

        newvalue = {'desease_Id': desease_Id, 'recommendationmessage': recommendationmessage}
        audit = Audit(administrator_id=session['id'], entity='Recommendation', oldvalue='N/A',
                      newvalue=newvalue, action='CREATE RECOMMENDATION')
        db.session.add(audit)

        db.session.commit()
        flash('Recommendation created successfully', category='success')
        return redirect('/deseases')

    flash('You are not loggedin! Please sign in now!!')
    return redirect('/')

# ===============================================================
# upload image

def filfunction(file):
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        oldext = os.path.splitext(filename)[1]
        os.rename(UPLOAD_FOLDER + filename, UPLOAD_FOLDER +  oldext)
        return oldext

@views.route('/results')
def results():
    if 'loggedin' in session:
        return render_template("/Results.html")
    return render_template("/")

@views.route('/uploadImg', methods=['POST'])
def uploadPredict():
     if 'loggedin' in session:
        if request.method == 'POST':
            file = request.files['maizefile']
            filename = session['name'] + session['surname']+file.filename
            print("@@ Input posted = ", filename)
            file_path =  os.path.join(UPLOAD_FOLDER, filename)
            file.save(file_path)
            print("@@ Predicting class......")
            predicted_class = predict(model,file_path)
            print(f"Predicted Class: {predicted_class}")
            # {'Blight': 0, 'Common_Rust': 1, 'Gray_Leaf_Spot': 2, 'Healthy': 3}
            ipadress = GetIPAdress()
            data = getCurrentClientLocation(ipadress)
            if predicted_class==0:
                desease =Desease.query.filter_by(name='NORTHEN LEAF BLIGHT').first()
                useaccountname = session['name']+ " " +session['surname']
                country = data['country_name']
                ipaddress = data['ip']
                city = data['city']
                region = data['region_name']
                latitude = data['latitude']
                longitude = data['longitude']
                geolocationap = {'latitude': latitude, 'longitude': longitude}

                deseaselog = Deseaselog(administrator_id=session['id'], desease_Id=desease.id, ipaddress=ipaddress,
                                        geolocationap=geolocationap, country=country, city=city, province=region,
                                        district=region,
                                        useaccountname=useaccountname)
                print(f"Results............: {deseaselog}")
                db.session.add(deseaselog)
                db.session.commit()

                name ="Northern Leaf Blight"
                sysmptoms="The fungus Exserohilum turcicum (formerly Helminthosporium turcicum) is the causative agent of northern maize leaf blight in southern maize. The symptoms of the disease are the grayish green to dark oblong lesions that appear on the leaves and the huge crop losses caused by this disease in the corn fields at the present time. Where the infection gradually expands throughout the leaf and is not limited to the leaf veins. Wet, rainy, windy, and warm weather are favorable conditions for the growth and spread of the disease in cornfields. Symptoms appear on the leaves in the form of longitudinal spindle-shaped spots that are small in size at first, greenish-gray in color, then they grow with the progression of the infection and may reach in an area of more than (20 cm in length and 3 cm in width). It turns light brown. The spots are seen on the lower leaves first about 40 days after planting and then spread on the upper leaves with time. In severe infections, the spots permeate most of the surface area of the leaves and fuse with each other, which leads to the drying of the leaves completely and thus the death of the plants"
                evaluation="Early planting before mid-June so that plants in the vegetative growth stage are not exposed to the appropriate conditions for the spread of the disease.When the disease spreads, the affected leaves are collected and burned. In severe infestations, we use appropriate fungicides such as (propiconazole - azoxystrobin - pyraclostrobin). You have to plant varieties that are resistant or tolerant to the disease.Ensure the abundance of balanced nutrients, avoid excessive nitrogen fertilization, and regularly remove weeds from the field and surrounding area.Rotate the plantings with soybeans, beans or sunflowers to avoid the widespread spread of the disease, and use a deep plow to bury plant debris and reduce the amount of pollen in the soil."
                return render_template('/Results.html', pred_output=name,sysmptoms=sysmptoms,evaluation=evaluation)
            elif predicted_class==1:
                desease = Desease.query.filter_by(name='COMMON RUST').first()
                useaccountname = session['name'] + " " + session['surname']
                country = data['country_name']
                ipaddress = data['ip']
                city = data['city']
                region = data['region_name']
                latitude = data['latitude']
                longitude = data['longitude']
                geolocationap = {'latitude': latitude, 'longitude': longitude}

                deseaselog = Deseaselog(administrator_id=session['id'], desease_Id=desease.id, ipaddress=ipaddress,
                                        geolocationap=geolocationap, country=country, city=city, province=region,
                                        district=region,
                                        useaccountname=useaccountname)
                print(f"Results............: {deseaselog}")
                db.session.add(deseaselog)
                db.session.commit()
                name ="Maize Common Rust"
                sysmptoms = "This disease is caused by the fungus Puccinia sorghi. This fungus lives in alternate hosts (a type of Euphorbia plant) and releases its spores during the spring. Its spores can be transmitted over long distances by wind and rain. The infection process begins when the fungus falls on the leaves. Secondary infection can occur from one plant to another due to wind and rain. Favorable conditions for the development of the disease are high relative humidity (about 100%), dew, rain and cold temperatures between 15 and 20 ° C (which may vary depending on the region). Hot and dry weather will in turn slow down or impede the growth of fungi and the occurrence of this disease. It is a problem in plants used to produce seeds and sweet corn. Plants grown as fodder for livestock, for industrial products, or for making processed foods are not affected. But the yield is reduced due to low plant productivity and dormancy.Symptoms of the disease appear in the form of fine speckling on both sides of the leaves which slowly develop into small dark and slightly prominent spots. These mainly elongated spots later turn into golden brown pustules irregularly spread in spots on the upper and lower sides. Its color can change to black with the growth of the plant. In contrast to other rust diseases such as: stems, leaves, sheaths and scales. However, the stems grow weak and soft and are more prone to falling. Younger leaf tissues are more susceptible to fungal infection than fully developed leaves. Infected plants during the early stages can show yellowing due to the lack of chlorophyll in the leaves and die. This leads to losses if the upper leaves are affected."
                evaluation = "Cultivation of disease-resistant varieties. And plant early to avoid optimal conditions for infection. You should use varieties that mature quickly and in a shorter period. Monitor your crop regularly for signs of disease, and intensify monitoring during cloudy weather. You must also ensure a balanced fertilization with nitrogen application. 6.Moderation in nitrogen fertilization because * its increase leads to an increase in the incidence of disease, with interest in potassium fertilization. Crop rotation with non-susceptible crops. 8.It was possible to treat this disease by using systemic fungicides such as *Saprol Ondar when the infection appeared. 9.Reducing moisture around plants by moderating irrigation and increasing planting distances"
                return render_template('/Results.html', pred_output=name, sysmptoms=sysmptoms, evaluation=evaluation)
            elif predicted_class == 2:
                desease = Desease.query.filter_by(name='GRAY LEAF SPOT').first()
                useaccountname = session['name'] + " " + session['surname']
                country = data['country_name']
                ipaddress = data['ip']
                city = data['city']
                region = data['region_name']
                latitude=data['latitude']
                longitude = data['longitude']
                geolocationap={'latitude':latitude,'longitude':longitude}

                deseaselog = Deseaselog(administrator_id=session['id'], desease_Id=desease.id, ipaddress=ipaddress,
                                        geolocationap=geolocationap, country=country, city=city, province=region,
                                        district=region,
                                        useaccountname=useaccountname)
                print(f"Results............: {deseaselog}")
                db.session.add(deseaselog)
                db.session.commit()
                name = "Maize Gray Leaf Spot"
                sysmptoms = "Gray leaf spot (GLS) is a fungal leaf disease of maize, also known as maize. GLS is considered as one of the most important diseases that limit the productivity of maize worldwide There are two types of fungal pathogens that cause GLS: Cercospora zeae-maydis and Cercospora zeina. Symptoms of maize include leaf blight, discoloration (greenness) and leaf blight. The characteristic symptoms of GLS are oblong, brown to grayish necrotic lesions running parallel to the leaf, extending between the secondary leaf veins. The fungus lives in topsoil debris and infects healthy crops via asexual spores called conidia. Environmental conditions best suited to infection and growth include moist, humid, and warm climates. Poor airflow, low sunlight, overcrowding, improper soil nutrients and irrigation management, and poor soil drainage can all contribute to disease spread. Management techniques include crop resistance, crop rotation, residue management, use of fungicides, and weed control. The purpose of disease management is to prevent the amount of secondary disease cycles as well as protect the leaf area from damage prior to grain formation. Corn gray leaf spot is an important disease in corn production in the United States, and is of economic importance throughout the Midwest and Mid-Atlantic regions. However, it is also widespread in Africa, Central America, China, Europe, India, Mexico, the Philippines, northern South America, and Southeast Asia. The teleomorph (sexual stage) of Cercospora zeae-maydis is postulated to be Mycosphaerella sp.The way the disease develops It is the production of a phytotoxin called Cercospora zeae-maydis one of the reasons for the pathogenic success of inactive cercosporin.All members of the genus Cercospora produce this light-activated toxin during infection. In the absence of light, cercosporin is inactive, but when light is present, the toxin is converted to its excited triplet state. Activated cercosporin reacts with oxygen molecules, generating active single oxygen radicals.Oxygen radicals interact with plant cell lipids, proteins, and nucleic acids, damaging and killing infected cells, and nutrients released during cell rupture and death that feed Cercospora. A study on a mutant Cercospora that lacks the gene responsible for cercosporin production showed that although it is not essential for infection, cercosporin increases the virulence of Cercospora fungi."
                evaluation = "fungicides Fungicides, if sprayed early in the season before initial spoilage, can be effective in reducing disease. There are currently 5 known fungicides that treat gray corn leaf spot. resistant varieties The most efficient and economical way to reduce yield losses from maize gray leaf spot is the introduction of resistant plant species. In places where leaf spot appears, these crops can eventually grow and remain disease resistant. Although the disease is not completely eradicated and resistant varieties show symptoms of disease, at the end of the growing season, the disease is not effective in reducing crop yield. SC 407 is a popular corn variety proven to be resistant to gray leaf spot.If gray leaf spot infestation is high, this variety may require the use of a fungicide to achieve full potential.Sensitive cultivars should not be planted in previously infected areas"
                return render_template('/Results.html', pred_output=name, sysmptoms=sysmptoms, evaluation=evaluation)
            elif predicted_class == 3:
                name = "Health Maize Leaf"
                sysmptoms = "NO SYMPTOMS"
                evaluation = "There is no disease on the maize leaf."
                return render_template('/Results.html', pred_output=name, sysmptoms=sysmptoms, evaluation=evaluation)
            else:
                name = "No idea"
                sysmptoms = "UNKNOWN"
                evaluation = "Please i cant help you with information on your picture try again #Telthemweb"
                return render_template('/Results.html', pred_output=name, sysmptoms=sysmptoms, evaluation=evaluation)





def predict(model, img):
    image = load_img(img, target_size=(256, 256))
    image = img_to_array(image)
    image = image.reshape((1, 256, 256, 3))
    prediction = model.predict(image)
    print('@@ Raw result = ', prediction)
    predicted_class = np.argmax(prediction)
    print(predicted_class)
    return predicted_class

# ================================REPORTS==============================================
@views.route('/audit-trail')
def audittrail():
    if 'loggedin' in session:
        audits = Audit.query.order_by(Audit.created_at.desc()).all()
        return render_template("/audit.html", title="System Audit", audits=audits)

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')


def GetIPAdress():
    response = requests.get('https://api.ipify.org?format=json')
    data = response.json()
    ip_address = data['ip']
    print("@@--------------"+ip_address)
    return ip_address

def getCurrentClientLocation(ipadress):
    ipstack_access_key='9470d84ea401ebac2b8b125990bce436'
    response = requests.get(f'http://api.ipstack.com/{ipadress}?access_key={ipstack_access_key}')
    data = response.json()
    return data
@views.route('/systemlogs')
def systemlogs():
    if 'loggedin' in session:
        logs = Systemlog.query.order_by(Systemlog.created_at.desc()).all()
        return render_template("/systemlogs.html", title="System Logs", logs=logs, datetime=datetime)

    flash('You are not logged in! Please sign in now!', category='error')
    return redirect('/')




@views.route('/deseaselogs')
def deseaselogs():
    if 'loggedin' in session:

        deseaseslogs = Deseaselog.query.order_by(Deseaselog.created_at.desc()).all()
        return render_template("/deseaselogs.html", title="Desease Reports", deseases=deseaseslogs)

    flash('You are not loggedin! Please sign in now!!',category='error')
    return redirect('/')

# export xcel
@views.route('/export_excel')
def export_excel():
    # Retrieve data from the database
    deseaseslogs = Deseaselog.query.order_by(Deseaselog.created_at.desc()).all()

    # Create a new workbook
    wb = Workbook()
    ws = wb.active

    # Write the headers to the worksheet
    headers = ['ID', 'Disease', 'Country', 'City', 'Province', 'District', 'Geocordinates', 'Created At']  # Added a comma after 'Geocordinates'
    ws.append(headers)

    # Write the data rows to the worksheet
    for log in deseaseslogs:
        row_data = [log.id, log.deseaselog.name, log.country, log.city, log.province, log.district, log.geolocationap, log.created_at]  # Updated log.deseaselog.name to log.disease
        ws.append(row_data)
        print(row_data)

    # Save the workbook to the response
    output = io.BytesIO()
    wb.save(output)
    output.seek(0)

    response = make_response()
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = 'attachment; filename=disease_report.xlsx'

    return response

# ===============================================================================
@views.route('/logout')
def logout():
    account = Administrator.query.filter_by(id=session['id']).first()
    if account:
        systemlog = Systemlog.query.filter_by(administrator_id=session['id'],timeout='PENDING',status='PENDING').first()
        if systemlog:
            systemlog.timeout = func.now()
            systemlog.status = "Logged out"
            db.session.commit()
            session.pop('loggedin', None)
            session.pop('id', None)
            session.pop('name', None)
            session.pop('surname', None)
            session.pop('email', None)
            session.pop('role_id', None)
            flash('Logged out successfully!',category='success')
            return redirect("/")





