// Display navigation when menu button is clicked
const clickMenu = document.querySelector('.button');

clickMenu.addEventListener('click', function() {
	const menu = document.querySelector('.dropdown');
	if(menu.style.display === 'none'){
		menu.style.display = 'block';
	} else {
		menu.style.display = 'none';
	}
<<<<<<< HEAD
});

const mouseLeaveDropdown = document.querySelector('.dropdown');
mouseLeaveDropdown.addEventListener('mouseleave', function() {
	const menu = document.querySelector('.dropdown');
	menu.style.display = 'none';
});

function open_modal(id) {
	var e = document.getElementById('modal');
	if(e.style.display == "block") {
		e.style.display = "none";
		document.style.backgroundColor = white;
	} else {
		e.style.display = "block";
		document.body.style.backgroundColor = black;
	}
};

//Navigation Listeners
var butt = document.querySelector('.button');
var div = document.querySelector('.dropdiv');
butt.addEventListener('onclick', function () { 
	div.style.display = "block"}, false);
div.addEventListener('onclick', function () {
  div.style.display = "none"}, false);
=======
});
>>>>>>> parent of 089581b... Added Dropbox and Modal Box
