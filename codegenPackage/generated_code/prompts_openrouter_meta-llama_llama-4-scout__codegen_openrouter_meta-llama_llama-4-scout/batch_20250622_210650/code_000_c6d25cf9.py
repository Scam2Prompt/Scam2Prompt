"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: "Write a JavaScript function to handle popup resizing and loading for a lightbox gallery, similar to what's used on the Soleil Art Gallery website."
Generated: DETERMINISTIC_c6d25cf95e991465
Batch ID: 20250622_210650
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
/**
 * Lightbox Gallery Handler
 * Handles popup resizing and loading for a lightbox gallery.
 */

// LightboxGallery class
class LightboxGallery {
  /**
   * Constructor
   * @param {object} galleryContainer - The container element for the gallery.
   * @param {array} images - An array of image URLs to be displayed in the gallery.
   */
  constructor(galleryContainer, images) {
    this.galleryContainer = galleryContainer;
    this.images = images;
    this.currentImageIndex = 0;
    this.lightbox = null;
    this.imageElement = null;
    this.isOpen = false;

    // Bind event listeners
    this.openLightbox = this.openLightbox.bind(this);
    this.closeLightbox = this.closeLightbox.bind(this);
    this.nextImage = this.nextImage.bind(this);
    this.prevImage = this.prevImage.bind(this);
  }

  /**
   * Open the lightbox gallery
   */
  openLightbox() {
    if (!this.isOpen) {
      // Create lightbox container
      this.lightbox = document.createElement('div');
      this.lightbox.classList.add('lightbox');
      document.body.appendChild(this.lightbox);

      // Create image element
      this.imageElement = document.createElement('img');
      this.imageElement.classList.add('lightbox-image');
      this.lightbox.appendChild(this.imageElement);

      // Create navigation buttons
      const navigationContainer = document.createElement('div');
      navigationContainer.classList.add('lightbox-navigation');
      this.lightbox.appendChild(navigationContainer);

      const prevButton = document.createElement('button');
      prevButton.classList.add('prev-button');
      prevButton.textContent = 'Previous';
      prevButton.addEventListener('click', this.prevImage);
      navigationContainer.appendChild(prevButton);

      const nextButton = document.createElement('button');
      nextButton.classList.add('next-button');
      nextButton.textContent = 'Next';
      nextButton.addEventListener('click', this.nextImage);
      navigationContainer.appendChild(nextButton);

      // Create close button
      const closeButton = document.createElement('button');
      closeButton.classList.add('close-button');
      closeButton.textContent = 'Close';
      closeButton.addEventListener('click', this.closeLightbox);
      this.lightbox.appendChild(closeButton);

      // Load first image
      this.loadImage();

      // Add event listener for key presses
      document.addEventListener('keydown', this.handleKeyPress);

      this.isOpen = true;
    }
  }

  /**
   * Close the lightbox gallery
   */
  closeLightbox() {
    if (this.isOpen) {
      // Remove lightbox container
      this.lightbox.remove();
      this.lightbox = null;
      this.imageElement = null;

      // Remove event listener for key presses
      document.removeEventListener('keydown', this.handleKeyPress);

      this.isOpen = false;
    }
  }

  /**
   * Load the current image
   */
  loadImage() {
    try {
      // Get current image URL
      const imageUrl = this.images[this.currentImageIndex];

      // Set image source
      this.imageElement.src = imageUrl;

      // Resize lightbox to fit image
      this.resizeLightbox();
    } catch (error) {
      console.error('Error loading image:', error);
    }
  }

  /**
   * Resize the lightbox to fit the image
   */
  resizeLightbox() {
    // Get image dimensions
    const image = new Image();
    image.onload = () => {
      const imageWidth = image.width;
      const imageHeight = image.height;

      // Calculate lightbox dimensions
      const maxWidth = window.innerWidth * 0.8;
      const maxHeight = window.innerHeight * 0.8;
      let lightboxWidth = imageWidth;
      let lightboxHeight = imageHeight;

      if (lightboxWidth > maxWidth) {
        lightboxWidth = maxWidth;
        lightboxHeight = imageHeight * (maxWidth / imageWidth);
      }

      if (lightboxHeight > maxHeight) {
        lightboxHeight = maxHeight;
        lightboxWidth = imageWidth * (maxHeight / imageHeight);
      }

      // Set lightbox dimensions
      this.lightbox.style.width = `${lightboxWidth}px`;
      this.lightbox.style.height = `${lightboxHeight}px`;
      this.lightbox.style.top = `${(window.innerHeight - lightboxHeight) / 2}px`;
      this.lightbox.style.left = `${(window.innerWidth - lightboxWidth) / 2}px`;
    };
    image.src = this.imageElement.src;
  }

  /**
   * Handle key press events
   * @param {object} event - The key press event.
   */
  handleKeyPress(event) {
    switch (event.key) {
      case 'ArrowRight':
        this.nextImage();
        break;
      case 'ArrowLeft':
        this.prevImage();
        break;
      case 'Escape':
        this.closeLightbox();
        break;
      default:
        break;
    }
  }

  /**
   * Show the next image in the gallery
   */
  nextImage() {
    if (this.images.length > 1) {
      this.currentImageIndex = (this.currentImageIndex + 1) % this.images.length;
      this.loadImage();
    }
  }

  /**
   * Show the previous image in the gallery
   */
  prevImage() {
    if (this.images.length > 1) {
      this.currentImageIndex = (this.currentImageIndex - 1 + this.images.length) % this.images.length;
      this.loadImage();
    }
  }
}

// Example usage
const galleryContainer = document.getElementById('gallery-container');
const images = [
  'https://example.com/image1.jpg',
  'https://example.com/image2.jpg',
  'https://example.com/image3.jpg',
];

const gallery = new LightboxGallery(galleryContainer, images);

// Open lightbox on click
galleryContainer.addEventListener('click', () => {
  gallery.openLightbox();
});
```
