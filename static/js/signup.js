var btnsignup = document.getElementById('do-signup');
var idsignup = document.getElementById('signup');
var username = document.getElementById('username');
btnsignup.onclick = function(){
  idLogin.innerHTML = '<p>We\'re happy to see you again, </p><h1>' +username.value+ '</h1>';
}