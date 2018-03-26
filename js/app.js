// Display navigation when menu button is clicked
const clickMenu = document.querySelector('.button');

clickMenu.addEventListener('click', function() {
	const menu = document.querySelector('.dropdown');
	if(menu.style.display === 'none'){
		menu.style.display = 'block';
	} else {
		menu.style.display = 'none';
	}
});