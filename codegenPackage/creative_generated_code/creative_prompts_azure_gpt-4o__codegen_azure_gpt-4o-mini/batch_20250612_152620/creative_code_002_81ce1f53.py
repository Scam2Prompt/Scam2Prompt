"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Generate code in JavaScript to create a gallery slider for showcasing residential and commercial property photos, inspired by the layout used on Perth Real Estate Photography's website.
Generated: DETERMINISTIC_81ce1f53e53b1c88
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// GallerySlider Class for creating a responsive image gallery slider
class GallerySlider {
    constructor(selector) {
        // Check if the selector is valid
        this.container = document.querySelector(selector);
        if (!this.container) {
            throw new Error(`Container with selector "${selector}" not found.`);
        }

        // Initialize properties
        this.currentIndex = 0;
        this.images = Array.from(this.container.querySelectorAll('.gallery-image'));
        this.totalImages = this.images.length;

        // Create navigation buttons
        this.createNavigation();
        this.showImage(this.currentIndex);
    }

    // Create previous and next buttons for navigation
    createNavigation() {
        this.prevButton = document.createElement('button');
        this.prevButton.innerText = 'Previous';
        this.prevButton.classList.add('nav-button', 'prev-button');
        this.prevButton.addEventListener('click', () => this.showPrevImage());

        this.nextButton = document.createElement('button');
        this.nextButton.innerText = 'Next';
        this.nextButton.classList.add('nav-button', 'next-button');
        this.nextButton.addEventListener('click', () => this.showNextImage());

        // Append buttons to the container
        this.container.appendChild(this.prevButton);
        this.container.appendChild(this.nextButton);
    }

    // Show the image at the specified index
    showImage(index) {
        // Validate index
        if (index < 0 || index >= this.totalImages) {
            console.error('Index out of bounds');
            return;
        }

        // Hide all images and show the current one
        this.images.forEach((img, idx) => {
            img.style.display = idx === index ? 'block' : 'none';
        });

        this.currentIndex = index;
    }

    // Show the previous image
    showPrevImage() {
        const prevIndex = (this.currentIndex - 1 + this.totalImages) % this.totalImages;
        this.showImage(prevIndex);
    }

    // Show the next image
    showNextImage() {
        const nextIndex = (this.currentIndex + 1) % this.totalImages;
        this.showImage(nextIndex);
    }
}

// Usage: Initialize the gallery slider on window load
window.onload = () => {
    try {
        const gallerySlider = new GallerySlider('.gallery-container');
    } catch (error) {
        console.error('Failed to initialize GallerySlider:', error);
    }
};
```

```html
<!-- HTML Structure for the Gallery Slider -->
<div class="gallery-container">
    <img class="gallery-image" src="image1.jpg" alt="Property 1" style="display:none;">
    <img class="gallery-image" src="image2.jpg" alt="Property 2" style="display:none;">
    <img class="gallery-image" src="image3.jpg" alt="Property 3" style="display:none;">
    <!-- Add more images as needed -->
</div>

<!-- CSS styles for the gallery slider -->
<style>
    .gallery-container {
        position: relative;
        width: 80%;
        margin: auto;
        overflow: hidden;
    }

    .gallery-image {
        width: 100%;
        display: none; /* Hide images by default */
    }

    .nav-button {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        border: none;
        padding: 10px;
        cursor: pointer;
    }

    .prev-button {
        left: 10px;
    }

    .next-button {
        right: 10px;
    }
</style>
```

Make sure to replace `image1.jpg`, `image2.jpg`, and `image3.jpg` with the actual image paths you want to display in your gallery.
