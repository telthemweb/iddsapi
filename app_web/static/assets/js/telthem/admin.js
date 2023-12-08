var BASEURL='localhost:9001/';
function rviewCustomerTicketDetails(id){
    //tickets/{id}

    var xhr= new XMLHttpRequest();
    xhr.open('GET',BASEURL+'v1/ticket/'+id,true);
    xhr.onreadystatechange = function (){
        if (xhr.readyState ==4 && xhr.status==200){
            if (this.responseText !=null) {
                var resp = JSON.parse(this.responseText);
                alert(resp)
            }


        }
    }
    xhr.send();
}