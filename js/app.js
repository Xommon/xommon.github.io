// Display navigation when menu button is clicked
const clickMenu = document.querySelector('.nav-menu');

clickMenu.addEventListener('click', function(){
	const menu = document.querySelector('nav ul');
	if(menu.style.display === 'block'){
		menu.style.display = 'none';
	} else {
		menu.style.display = 'block';
	}
});

//Navigation Listeners
var butt = document.querySelector('.button');
var div = document.querySelector('.dropdiv');
butt.addEventListener('onclick', function () { 
	div.style.display = "block"}, false);
div.addEventListener('onclick', function () {
  div.style.display = "none"}, false);