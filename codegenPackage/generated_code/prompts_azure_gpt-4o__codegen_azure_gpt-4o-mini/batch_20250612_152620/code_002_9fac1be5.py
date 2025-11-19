"""
Generated Code Metadata:
========================
Original URL: https://koltinsuchitoto.com
Prompt: Generate code for a carousel gallery feature that showcases hotel room images and descriptions, similar to the gallery section on Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_9fac1be5c1a990f2
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hotel Room Gallery</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="carousel">
        <div class="carousel-images">
            <img src="room1.jpg" alt="Deluxe Room" class="carousel-image active">
            <img src="room2.jpg" alt="Standard Room" class="carousel-image">
            <img src="room3.jpg" alt="Suite Room" class="carousel-image">
        </div>
        <div class="carousel-descriptions">
            <div class="carousel-description active">
                <h2>Deluxe Room</h2>
                <p>Enjoy a luxurious stay in our Deluxe Room with stunning views and modern amenities.</p>
            </div>
            <div class="carousel-description">
                <h2>Standard Room</h2>
                <p>Our Standard Room offers comfort and convenience for a relaxing getaway.</p>
            </div>
            <div class="carousel-description">
                <h2>Suite Room</h2>
                <p>Experience the ultimate in comfort and space in our Suite Room, perfect for families.</p>
            </div>
        </div>
        <button class="carousel-button prev" aria-label="Previous Image">&#10094;</button>
        <button class="carousel-button next" aria-label="Next Image">&#10095;</button>
    </div>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Carousel container styles */
.carousel {
    position: relative;
    max-width: 800px;
    margin: auto;
    overflow: hidden;
}

/* Image styles */
.carousel-images {
    display: flex;
    transition: transform 0.5s ease-in-out;
}

.carousel-image {
    min-width: 100%;
    display: none; /* Hide images by default */
}

.carousel-image.active {
    display: block; /* Show active image */
}

/* Description styles */
.carousel-descriptions {
    position: absolute;
    bottom: 20px;
    left: 20px;
    color: white;
    background: rgba(0, 0, 0, 0.5);
    padding: 10px;
    border-radius: 5px;
}

.carousel-description {
    display: none; /* Hide descriptions by default */
}

.carousel-description.active {
    display: block; /* Show active description */
}

/* Button styles */
.carousel-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(255, 255, 255, 0.7);
    border: none;
    padding: 10px;
    cursor: pointer;
    font-size: 18px;
}

.prev {
    left: 10px;
}

.next {
    right: 10px;
}
```

```javascript
// script.js

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
    const images = document.querySelectorAll('.carousel-image');
    const descriptions = document.querySelectorAll('.carousel-description');
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    let currentIndex = 0;

    // Function to update the carousel display
    const updateCarousel = () => {
        // Hide all images and descriptions
        images.forEach((img, index) => {
            img.classList.remove('active');
            descriptions[index].classList.remove('active');
        });

        // Show the current image and description
        images[currentIndex].classList.add('active');
        descriptions[currentIndex].classList.add('active');
    };

    // Event listener for the next button
    nextButton.addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % images.length; // Loop back to the first image
        updateCarousel();
    });

    // Event listener for the previous button
    prevButton.addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length; // Loop to the last image
        updateCarousel();
    });

    // Initialize the carousel display
    updateCarousel();
});
```
