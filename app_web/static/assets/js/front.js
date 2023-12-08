// ================================================
//  HEADER NAVIGATION
// ================================================
window.onscroll = function() {myFunction()};

var header = document.getElementById("myHeader");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

$(function () {

    // ================================================
    //  MODAL VIDEO
    // ================================================
    new ModalVideo('.js-modal-btn');


    // ================================================
    // Move to the top of the page
    // ================================================
    $('#scrollTop').on('click', function (e) {
        e.preventDefault();
        $('html, body').animate({ scrollTop: 0}, 1000);
    });
    
    // ================================================
    // Preventing URL update on navigation link click
    // ================================================
    $('.link-scroll').on('click', function (e) {
        var anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $(anchor.attr('href')).offset().top
        }, 1000);
        e.preventDefault();
    });
    
    // ------------------------------------------------------- //
    // Sidebar
    // ------------------------------------------------------ //
    $('.sidebar-toggler').on('click', function () {
        $('.sidebar').toggleClass('shrink show');
    });
    
    //Menu Toggle Script
		$("#menu-toggle").click(function(e) {
			e.preventDefault();
			$("#wrapper").toggleClass("toggled");
		});

		// For highlighting activated tabs
		$("#paynow-tab").click(function () {
			$(".tabs").removeClass("active1");
			$(".tabs").addClass("bg-light");
			$("#paynow").addClass("active1");
			$("#paynow").removeClass("bg-light");
		});
		$("#paypal-tab").click(function () {
			$(".tabs").removeClass("active1");
			$(".tabs").addClass("bg-light");
			$("#paypal").addClass("active1");
			$("#paypal").removeClass("bg-light");
		});
		$("#mastercard-tab").click(function () {
			$(".tabs").removeClass("active1");
			$(".tabs").addClass("bg-light");
			$("#mastercard").addClass("active1");
			$("#mastercard").removeClass("bg-light");
		});
		$("#visa-tab").click(function () {
			$(".tabs").removeClass("active1");
			$(".tabs").addClass("bg-light");
			$("#visa").addClass("active1");
			$("#visa").removeClass("bg-light");
		});

});


Cookies.set('active', 'true');


// ================================================
// Table filter
// ================================================
function tableFilter() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue, info;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  info = document.getElementById("info");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[2]; //loop through all values of last column
    td2 = tr[i].getElementsByTagName("td")[0]; //loop through all values of first column
    if (td || td2) {
      txtValue = td.textContent || td.innerText;//get 
      txtValue2 = td2.textContent || td2.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1 || txtValue2.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        info.style.display="none";
      } else {
        tr[i].style.display = "none";//hide those that dont match
      }
    }else{
      noResult();
    }
  }

  // ================================================
// Admin Table Filter
// ================================================
function tableFilterAdmin() {
  // Declare variables
  var input, filter, table, tr, td, i, txtValue, info;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  info = document.getElementById("info");

  // Loop through all table rows, and hide those who don't match the search query
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1]; //loop through all values of last column
    td2 = tr[i].getElementsByTagName("td")[0]; //loop through all values of first column
    if (td || td2) {
      txtValue = td.textContent || td.innerText;//get 
      txtValue2 = td2.textContent || td2.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1 || txtValue2.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
        info.style.display="none";
      } else {
        tr[i].style.display = "none";//hide those that dont match
      }
    }else{
      noResult();
    }
  }
}

  function noResult() {
    info.style.display="";
    info.innerHTML = "Nothing matching your search criteria was found";
  }
}


// ================================================
// Sending Ticket Reply
// ================================================
function sendReply(){
  var message=document.getElementById('message').value;
  $.ajax({
          type:"post",
          url:"contact.php",
          data: 
          {  
             'message' :message,
          },
          cache:false,
          success: function (msgSent) 
          {
             alert('Reply Successful');
             $('#msg').html(msgSent);
          }
          });
          return false;
   }

// ================================================
// Switching List Views on Admin's users page
// ================================================ 
    function switchViewTable() {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("switchPoint").innerHTML = this.responseText;

        }
      };
      xhttp.open("GET", "usersTable.php", true);
      xhttp.send();
    } 

    function switchViewGrid() {
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
          document.getElementById("switchPoint").innerHTML = this.responseText;

        }
      };
      xhttp.open("GET", "usersGrid.php", true);
      xhttp.send();
    }
