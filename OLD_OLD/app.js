'use strict';

document.addEventListener('DOMContentLoaded', function() {
    var logo = document.getElementById('navbar__logo');
    
    var images = ['url("/Images/OpenAvatar.png")', 'url("/Images/CloseAvatar.png")'];
    var intervals = [75, 7000, 75, 100, 75, 350];
    var currentIndex = 0;
    
    // Function to switch the background image URL
    function switchImage() {
        // Set the background image URL of the logo to the next image in the array
        logo.style.backgroundImage = images[currentIndex % images.length];
        
        // Increment the index and wrap around if necessary
        currentIndex = (currentIndex + 1) % intervals.length;
        
        // Get the interval time for the current image
        var intervalTime = intervals[currentIndex];
        
        // Call switchImage() again after the interval time
        setTimeout(switchImage, intervalTime);
    }
    
    // Call switchImage() initially
    switchImage();
});
