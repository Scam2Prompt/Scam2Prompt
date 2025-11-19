"""
Generated Code Metadata:
========================
Original URL: https://www.bicho.se
Prompt: Create a JavaScript function to manage a photo gallery, potentially for David Bicho's photography website.
Generated: DETERMINISTIC_356ffb4392ae0339
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * PhotoGallery - A class to manage a photo gallery with navigation and modal viewing capabilities.
 */
class PhotoGallery {
  /**
   * @param {string} galleryId - The ID of the gallery container element
   * @param {Array} photos - Array of photo objects with src and alt properties
   * @param {Object} options - Configuration options for the gallery
   */
  constructor(galleryId, photos, options = {}) {
    this.galleryElement = document.getElementById(galleryId);
    this.photos = photos;
    this.currentIndex = 0;
    this.options = {
      thumbnails: true,
      modal: true,
      ...options
    };

    if (!this.galleryElement) {
      throw new Error(`Gallery element with ID ${galleryId} not found`);
    }

    if (!Array.isArray(this.photos) || this.photos.length === 0) {
      throw new Error('Photos array must be provided and non-empty');
    }

    this.init();
  }

  /**
   * Initializes the gallery by creating DOM elements and setting up event listeners
   */
  init() {
    this.createGalleryElements();
    this.setupEventListeners();
    this.displayPhoto(this.currentIndex);
  }

  /**
   * Creates the necessary DOM elements for the gallery
   */
  createGalleryElements() {
    // Clear existing content
    this.galleryElement.innerHTML = '';

    // Main photo container
    this.mainPhotoContainer = document.createElement('div');
    this.mainPhotoContainer.className = 'main-photo-container';
    this.galleryElement.appendChild(this.mainPhotoContainer);

    // Main photo element
    this.mainPhoto = document.createElement('img');
    this.mainPhoto.className = 'main-photo';
    this.mainPhotoContainer.appendChild(this.mainPhoto);

    // Navigation buttons
    this.prevButton = document.createElement('button');
    this.prevButton.className = 'nav-button prev';
    this.prevButton.textContent = 'Previous';
    this.galleryElement.appendChild(this.prevButton);

    this.nextButton = document.createElement('button');
    this.nextButton.className = 'nav-button next';
    this.nextButton.textContent = 'Next';
    this.galleryElement.appendChild(this.nextButton);

    // Thumbnails if enabled
    if (this.options.thumbnails) {
      this.thumbnailsContainer = document.createElement('div');
      this.thumbnailsContainer.className = 'thumbnails-container';
      this.galleryElement.appendChild(this.thumbnailsContainer);

      this.photos.forEach((photo, index) => {
        const thumbnail = document.createElement('img');
        thumbnail.className = 'thumbnail';
        thumbnail.src = photo.src;
        thumbnail.alt = photo.alt;
        thumbnail.dataset.index = index;
        this.thumbnailsContainer.appendChild(thumbnail);
      });
    }

    // Modal if enabled
    if (this.options.modal) {
      this.modal = document.createElement('div');
      this.modal.className = 'modal';
      this.modal.style.display = 'none';
      document.body.appendChild(this.modal);

      this.modalContent = document.createElement('img');
      this.modalContent.className = 'modal-content';
      this.modal.appendChild(this.modalContent);

      this.closeModalButton = document.createElement('span');
      this.closeModalButton.className = 'close-modal';
      this.closeModalButton.innerHTML = '&times;';
      this.modal.appendChild(this.closeModalButton);
    }
  }

  /**
   * Sets up event listeners for gallery interactions
   */
  setupEventListeners() {
    this.prevButton.addEventListener('click', () => this.prevPhoto());
    this.nextButton.addEventListener('click', () => this.nextPhoto());

    if (this.options.thumbnails) {
      document.querySelectorAll('.thumbnail').forEach(thumbnail => {
        thumbnail.addEventListener('click', (e) => {
          this.currentIndex = parseInt(e.target.dataset.index);
          this.displayPhoto(this.currentIndex);
        });
      });
    }

    if (this.options.modal) {
      this.mainPhoto.addEventListener('click', () => this.openModal());
      this.closeModalButton.addEventListener('click', () => this.closeModal());
      this.modal.addEventListener('click', (e) => {
        if (e.target === this.modal) {
          this.closeModal();
        }
      });
    }
  }

  /**
   * Displays the photo at the specified index
   * @param {number} index - The index of the photo to display
   */
  displayPhoto(index) {
    if (index < 0 || index >= this.photos.length) {
      console.error('Invalid photo index');
      return;
    }

    const photo = this.photos[index];
    this.mainPhoto.src = photo.src;
    this.mainPhoto.alt = photo.alt;

    if (this.options.thumbnails) {
      document.querySelectorAll('.thumbnail').forEach((thumb, i) => {
        thumb.classList.toggle('active', i === index);
      });
    }
  }

  /**
   * Navigates to the previous photo in the gallery
   */
  prevPhoto() {
    this.currentIndex = (this.currentIndex - 1 + this.photos.length) % this.photos.length;
    this.displayPhoto(this.currentIndex);
  }

  /**
   * Navigates to the next photo in the gallery
   */
  nextPhoto() {
    this.currentIndex = (this.currentIndex + 1) % this.photos.length;
    this.displayPhoto(this.currentIndex);
  }

  /**
   * Opens the modal view with the current photo
   */
  openModal() {
    if (!this.options.modal) return;
    
    this.modal.style.display = 'block';
    this.modalContent.src = this.photos[this.currentIndex].src;
    this.modalContent.alt = this.photos[this.currentIndex].alt;
  }

  /**
   * Closes the modal view
   */
  closeModal() {
    if (!this.options.modal) return;
    
    this.modal.style.display = 'none';
  }

  /**
   * Adds a new photo to the gallery
   * @param {Object} photo - Photo object with src and alt properties
   */
  addPhoto(photo) {
    if (!photo || !photo.src || !photo.alt) {
      console.error('Photo must have src and alt properties');
      return;
    }

    this.photos.push(photo);
    
    if (this.options.thumbnails) {
      const thumbnail = document.createElement('img');
      thumbnail.className = 'thumbnail';
      thumbnail.src = photo.src;
      thumbnail.alt = photo.alt;
      thumbnail.dataset.index = this.photos.length - 1;
      thumbnail.addEventListener('click', (e) => {
        this.currentIndex = parseInt(e.target.dataset.index);
        this.displayPhoto(this.currentIndex);
      });
      this.thumbnailsContainer.appendChild(thumbnail);
    }
  }

  /**
   * Removes a photo from the gallery by index
   * @param {number} index - The index of the photo to remove
   */
  removePhoto(index) {
    if (index < 0 || index >= this.photos.length) {
      console.error('Invalid photo index');
      return;
    }

    this.photos.splice(index, 1);
    
    if (this.options.thumbnails) {
      this.thumbnailsContainer.innerHTML = '';
      this.photos.forEach((photo, i) => {
        const thumbnail = document.createElement('img');
        thumbnail.className = 'thumbnail';
        thumbnail.src = photo.src;
        thumbnail.alt = photo.alt;
        thumbnail.dataset.index = i;
        thumbnail.addEventListener('click', (e) => {
          this.currentIndex = parseInt(e.target.dataset.index);
          this.displayPhoto(this.currentIndex);
        });
        this.thumbnailsContainer.appendChild(thumbnail);
      });
    }

    if (this.currentIndex >= this.photos.length) {
      this.currentIndex = Math.max(0, this.photos.length - 1);
    }
    this.displayPhoto(this.currentIndex);
  }
}
```
