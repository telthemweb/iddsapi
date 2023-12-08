from . import db
from sqlalchemy.sql import func


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    administrators = db.relationship('Administrator', backref='role_user', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, name):
        self.name = name


class Administrator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role_Id = db.Column(db.Integer, db.ForeignKey('role.id'))
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    email = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    gender = db.Column(db.String(255))
    city = db.Column(db.String(255))
    address = db.Column(db.String(255))
    logs = db.relationship('Systemlog', backref='ownedby', lazy=True)
    trails = db.relationship('Audit', backref='trailedby', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, role_Id, name, surname, username, password, email, phone, gender, city, address):
        self.role_Id = role_Id
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.gender = gender
        self.city = city
        self.address = address


class Desease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    systoms = db.Column(db.String(2055), nullable=True)
    imageurl = db.Column(db.String(2055), nullable=True)
    recommendations = db.relationship('Recommendation', backref='deseaseolny', lazy=True)
    dlogs = db.relationship('Deseaselog', backref='deseaselog', lazy=True)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, name, systoms, imageurl):
        self.name = name
        self.systoms = systoms
        self.imageurl = imageurl


class Recommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recommendationmessage = db.Column(db.String(255), nullable=False)
    desease_Id = db.Column(db.Integer, db.ForeignKey('desease.id'))
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, name, desease_Id):
        self.name = name
        self.desease_Id = desease_Id


class Audit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    entity = db.Column(db.String(255), nullable=False)
    oldvalue = db.Column(db.String(2255), nullable=False)
    newvalue = db.Column(db.String(2255), nullable=False)
    action = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, administrator_id, entity, newvalue, action):
        self.administrator_id = administrator_id
        self.entity = entity
        self.newvalue = newvalue
        self.action = action


class Systemlog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    timein = db.Column(db.String(255), nullable=False)
    ipaddress = db.Column(db.String(255), nullable=False)
    geolocationap = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    timeout = db.Column(db.String(255), nullable=False)
    useaccountname = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), default="PENDING")
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, administrator_id, timein, ipaddress, geolocationap, country, city, timeout, useaccountname,status):
        self.administrator_id = administrator_id
        self.timein = timein
        self.ipaddress = ipaddress
        self.geolocationap = geolocationap
        self.country = country
        self.city = city
        self.timeout = timeout
        self.useaccountname = useaccountname
        self.status=status


class Deseaselog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    administrator_id = db.Column(db.Integer, db.ForeignKey('administrator.id'))
    desease_Id = db.Column(db.Integer, db.ForeignKey('desease.id'))
    ipaddress = db.Column(db.String(255), nullable=False)
    geolocationap = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    province = db.Column(db.String(255), nullable=False)
    district = db.Column(db.String(255), nullable=False)
    useaccountname = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), nullable=True)

    def __int__(self, administrator_id, desease_Id, ipaddress, geolocationap, country, city,province,district, useaccountname):
        self.administrator_id = administrator_id
        self.desease_Id = desease_Id
        self.ipaddress = ipaddress
        self.geolocationap = geolocationap
        self.country = country
        self.city = city
        self.useaccountname = useaccountname
