"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Generate code to implement a responsive gallery feature for travel photos on a WordPress blog using JavaScript and CSS.
Generated: DETERMINISTIC_0a358024c14e060b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**JavaScript Code**
```javascript
// gallery.js

// Wait for the DOM to be ready
document.addEventListener('DOMContentLoaded', function() {
  // Select the gallery container
  const galleryContainer = document.querySelector('.travel-gallery');

  // Check if the gallery container exists
  if (galleryContainer) {
    // Initialize the gallery
    initGallery(galleryContainer);
  }
});

/**
 * Initialize the gallery
 * @param {HTMLElement} galleryContainer - The gallery container element
 */
function initGallery(galleryContainer) {
  // Select all gallery items
  const galleryItems = galleryContainer.querySelectorAll('.gallery-item');

  // Check if there are gallery items
  if (galleryItems.length > 0) {
    // Create a lightbox container
    const lightboxContainer = createLightboxContainer();

    // Add event listeners to each gallery item
    galleryItems.forEach((item) => {
      item.addEventListener('click', function() {
        // Open the lightbox with the clicked item's image
        openLightbox(lightboxContainer, item.querySelector('img').src);
      });
    });

    // Add event listener to close the lightbox
    lightboxContainer.addEventListener('click', function(event) {
      if (event.target === lightboxContainer) {
        closeLightbox(lightboxContainer);
      }
    });
  }
}

/**
 * Create the lightbox container
 * @returns {HTMLElement} The lightbox container element
 */
function createLightboxContainer() {
  const lightboxContainer = document.createElement('div');
  lightboxContainer.classList.add('lightbox-container');
  document.body.appendChild(lightboxContainer);
  return lightboxContainer;
}

/**
 * Open the lightbox with the given image
 * @param {HTMLElement} lightboxContainer - The lightbox container element
 * @param {string} imageSrc - The source of the image to display
 */
function openLightbox(lightboxContainer, imageSrc) {
  // Create the lightbox content
  const lightboxContent = document.createElement('div');
  lightboxContent.classList.add('lightbox-content');

  const lightboxImage = document.createElement('img');
  lightboxImage.src = imageSrc;
  lightboxContent.appendChild(lightboxImage);

  // Add the lightbox content to the container
  lightboxContainer.appendChild(lightboxContent);

  // Show the lightbox
  lightboxContainer.classList.add('open');
}

/**
 * Close the lightbox
 * @param {HTMLElement} lightboxContainer - The lightbox container element
 */
function closeLightbox(lightboxContainer) {
  // Remove the lightbox content
  lightboxContainer.querySelector('.lightbox-content').remove();

  // Hide the lightbox
  lightboxContainer.classList.remove('open');
}
```

**CSS Code**
```css
/* styles.css */

/* Gallery styles */
.travel-gallery {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.gallery-item {
  margin: 10px;
  width: calc(33.33% - 20px);
}

.gallery-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px;
  cursor: pointer;
}

/* Lightbox styles */
.lightbox-container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.8);
  display: flex;
  justify-content: center;
  align-items: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s;
}

.lightbox-container.open {
  opacity: 1;
  visibility: visible;
}

.lightbox-content {
  max-width: 80%;
  max-height: 80%;
}

.lightbox-content img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: 10px;
}

/* Responsive styles */
@media only screen and (max-width: 768px) {
  .gallery-item {
    width: calc(50% - 20px);
  }
}

@media only screen and (max-width: 480px) {
  .gallery-item {
    width: 100%;
  }
}
```

**HTML Code (Example Usage)**
```html
<!-- index.html -->

<div class="travel-gallery">
  <div class="gallery-item">
    <img src="image1.jpg" alt="Travel Photo 1">
  </div>
  <div class="gallery-item">
    <img src="image2.jpg" alt="Travel Photo 2">
  </div>
  <div class="gallery-item">
    <img src="image3.jpg" alt="Travel Photo 3">
  </div>
  <!-- Add more gallery items here -->
</div>

<script src="gallery.js"></script>
<link rel="stylesheet" href="styles.css">
```
