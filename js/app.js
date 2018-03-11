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