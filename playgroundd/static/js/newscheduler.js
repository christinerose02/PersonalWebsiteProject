var nameError = document.getElementById('name-error');
var emailError = document.getElementById('email-error');
var passwordError = document.getElementById('password-error');
var password2Error = document.getElementById('password2-error');
var submitError = document.getElementById('submit-error');
var fnameError = document.getElementById('fname-error');
var lnameError = document.getElementById('lname-error');

function validateName(){

  var user = document.getElementById('username').value;

  if(user.length == 0){
    nameError.innerHTML ='username is required';
    return false;
  }

  nameError.innerHTML = '<i class="fas fa-check-circle"></i>';
    return true;
}




function validateEmail(){
  var email = document.getElementById('email').value;

  if (email.length ==0 ){
    emailError.innerHTML ='Email is required';
    return false;
  }

  if(!email.match(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/)){
    emailError.innerHTML = 'Invalid Email';
    return false;
  }
  emailError.innerHTML ='<i class="fas fa-check-circle"></i>';
    return true;
}



function validatePassword(){
  var password1 = document.getElementById('passwordf').value;

  if(password1.length ==0){
    password1Error.innerHTML = 'Password is required';
    return false
  }

  if(password1.length <=7){
    password1Error.innerHTML = 'Password must atleat 8 characters';
    return false;
  }

  if(!password1.match(/[0-9]/)){
    password1Error.innerHTML = "atleast 1 number";
    return false;
  }

  if(!password1.match(/[A-Z]/)){
    password1Error.innerHTML = "atleast 1 uppercase";
    return false;
  }
}


function validatePassword2(){
  var password2 = document.getElementById ('password2').value;
  var password1 = document.getElementById('password').value;

  if(password2.length = 0){
    password2Error.innerHTML ='Password is requried';
  }

  if (password1!== password2){
    password2Error.innerHTML='Password does not match';
  }

  password2Error.innerHTML = '<i class = "fas fa-check-circle"></i>';
    return false;
}