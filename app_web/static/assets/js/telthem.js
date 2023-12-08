
function element(type) {

	var element = document.createElement(type);
	return element;
}
function hide(id) {
	 var x = getById(id);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}
function getById(id) {
	return document.getElementById(id);
}
function byId(id) {
	return document.getElementById(id);
}

function getByClass(cls) {
	
	return document.getElementsByClassName(cls);
}

function push(element,elements){
	for (var i = 0; i < elements.length; i++) {
		element.appendChild(elements[i]);
	}

	return element;
}

function document_detailsTable() {


return '<tr><th id="c1"></th><th id="c2"></th><th id="c3"></th></tr>';
	
}
function document_detailsTableReciept() {


return '<tr><th id="rc1"></th><th id="rc2"></th><th id="rc3"></th></tr>';
	
}
function document_detailsTableDnote() {


return '<tr><th id="dc1"></th><th id="dc2"></th><th id="dc3"></th></tr>';
	
}
function document_detailsTableQoute() {


return '<tr><th id="qc1"></th><th id="qc2"></th><th id="qc3"></th></tr>';
	
}
function create_Tr(){

	return '<tr><td id="c1r2"></td><td id="c2r2"></td><td id="c3r2"></td></tr>';
}
function create_TrReciept(){

	return '<tr><td id="rc1r2"></td><td id="rc2r2"></td><td id="rc3r2"></td></tr>';
}
function create_TrDnote(){

	return '<tr><td id="dc1r2"></td><td id="dc2r2"></td><td id="dc3r2"></td></tr>';
}
function create_TrQoute(){

	return '<tr><td id="qc1r2"></td><td id="qc2r2"></td><td id="qc3r2"></td></tr>';
}

function orderSpecifications() {
	
	return '<div id="order_details" style="border-top: 2px solid #3591FF   "><table id="orderspecifications"><tr><th>Description</th><th>Unit of Cost</th><th>Qty</th><th>Total</th></tr><tbody></tbody></table></div>';
}
function orderSpecificationsDnote() {
	
	return '<div id="order_details" style="border-top: 2px solid #3591FF   "><table id="orderspecifications"><tr><th style="text-align:left">Description</th><th></th><th></th><th>Qty</th></tr><tbody></tbody></table></div>';
}

function orderSpecificationsRow() {
	return '<tr><td></td><td></td><td></td><td></td></tr>';
}
function orderSpecificationsDnoteRow() {
	return '<tr style="bord-bottm:1px solid "><td style="text-align:left"></td><td></td><td></td><td></td></tr>';
}

function getStyle() {
	
	return "<style type='text/css'> #side_navBar{ float: left } #main_container{ float: left; } #documents_selection{ margin-top: 15vh; padding-left: 5vw; font-size: 1.5vh; } .reports{ float: left; width: 30vw; margin-right: 2vw; height: 67vh; position: relative; border: 1px solid #E8E8E7; margin-bottom: 2vh; border-top-left-radius: 10%; border-top-right-radius: 10%; } .reports label{ font-size: 2vw; } .reports input{ position: absolute; bottom: 5px; left: 14vw; } .report img{ top: 4px } #message_buttons_container{ padding-top: 2vh } #send_edit_order button{ width: 10vw; height: 4vh; border-radius: 10px } #send { background-color: #000000; color: #fff; border:1px solid #000; font-size: 1.5vh; } #edit_order{ color: #fff; font-size: 1.5vh; } #edit_order:hover{ color: #000; } .head{ height: 12vh; background-color: #5EA6FC; border-top-left-radius: 15%; border-top-right-radius: 15%; padding-left: 2vw; padding-right: 2vw; padding-top: 2vh } .contact, .address{ width: 8vw; color: white; float: left; font-size: 1vw; } .label{ float: left; margin-right: 2vw } #details_table tr{ width: 20vw; font-size: 1vw; text-align: center; } #details_table{ width: 30vw; } #order_details table{ width: 30vw; font-size: 1vw; } #order_details table tbody{ height: 20vh; border: 1px solid #000; overflow-y: hidden; } #bank_details p{ width: 10vw; font-size: 1.16; } @media screen and (max-width: 660px) { .reports{ float: none; width: 60vw; height: 50vh; overflow-y: scroll; } .reports input{ position: absolute; bottom: 5px; left: 50%; } #documents_selection{ margin-top: 3vh; } } </style>";
}

function sumaryTr() {
	
	return '<td></td><td></td><td></td>';
}
function setWidth(element,sizeO) {
	element.style['width']=sizeO;
}

function setFontSize(element,fontSize) {
	element.style['font-size']=fontSize;
}
function AutoComplete(array,element) {
	
	dataList=getById('addresses');
	dataList.innerHTML="";
	for (var i = 0; i < array.length; i++) {
		var option = document.createElement('option');
        
        option.value = array[i];
        dataList.appendChild(option);
	}
}
/*Include files dynamically**************************************************/
function loadjscssfile(path, filetype){
    if (filetype=="js"){ //if filename is a external JavaScript file
        var fileref=document.createElement('script')
        fileref.setAttribute("type","text/javascript")
        fileref.setAttribute("src", path)
    }
    else if (filetype=="css"){ //if filename is an external CSS file
        var fileref=document.createElement("link")
        fileref.setAttribute("rel", "stylesheet")
        fileref.setAttribute("type", "text/css")
        fileref.setAttribute("href", path)
    }
    if (typeof fileref!="undefined")
        document.getElementsByTagName("head")[0].appendChild(fileref)
}



