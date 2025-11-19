"""
Generated Code Metadata:
========================
Original URL: https://kristoslounge.com
Prompt: Write a JavaScript function to create a photo gallery for Kristos Lounge's events and parties, similar to the one on their website.
Generated: DETERMINISTIC_10392729527e18df
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Photo Gallery for Kristos Lounge Events and Parties
 * 
 * Features:
 * - Responsive grid layout
 * - Lightbox for image viewing
 * - Lazy loading for performance
 * - Keyboard navigation support
 */

class KristosGallery {
  /**
   * Initialize the gallery
   * @param {string} containerSelector - CSS selector for gallery container
   * @param {Array} images - Array of image objects with src, alt, and caption
   * @param {Object} options - Configuration options
   */
  constructor(containerSelector, images, options = {}) {
    this.container = document.querySelector(containerSelector);
    this.images = images;
    this.options = {
      columns: options.columns || 3,
      gap: options.gap || '15px',
      lightbox: options.lightbox !== false,
      lazyLoad: options.lazyLoad !== false,
      ...options
    };

    if (!this.container) {
      throw new Error(`Container element not found: ${containerSelector}`);
    }

    this.initGallery();
    this.setupEventListeners();
  }

  /**
   * Initialize gallery HTML structure
   */
  initGallery() {
    this.container.style.display = 'grid';
    this.container.style.gridTemplateColumns = `repeat(${this.options.columns}, 1fr)`;
    this.container.style.gap = this.options.gap;
    this.container.style.width = '100%';

    this.images.forEach((image, index) => {
      const galleryItem = document.createElement('div');
      galleryItem.className = 'gallery-item';
      galleryItem.dataset.index = index;

      const img = document.createElement('img');
      img.src = this.options.lazyLoad ? '' : image.src;
      img.alt = image.alt || '';
      img.loading = this.options.lazyLoad ? 'lazy' : 'eager';
      
      if (this.options.lazyLoad) {
        img.dataset.src = image.src;
        this.lazyLoadObserver(img);
      }

      if (image.caption) {
        const caption = document.createElement('div');
        caption.className = 'gallery-caption';
        caption.textContent = image.caption;
        galleryItem.appendChild(caption);
      }

      galleryItem.appendChild(img);
      this.container.appendChild(galleryItem);
    });

    if (this.options.lightbox) {
      this.createLightbox();
    }
  }

  /**
   * Setup IntersectionObserver for lazy loading
   * @param {HTMLElement} img - Image element to observe
   */
  lazyLoadObserver(img) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const lazyImage = entry.target;
          lazyImage.src = lazyImage.dataset.src;
          observer.unobserve(lazyImage);
        }
      });
    }, {
      rootMargin: '200px 0px'
    });

    observer.observe(img);
  }

  /**
   * Create lightbox modal
   */
  createLightbox() {
    this.lightbox = document.createElement('div');
    this.lightbox.className = 'lightbox';
    this.lightbox.style.display = 'none';
    this.lightbox.style.position = 'fixed';
    this.lightbox.style.top = '0';
    this.lightbox.style.left = '0';
    this.lightbox.style.width = '100%';
    this.lightbox.style.height = '100%';
    this.lightbox.style.backgroundColor = 'rgba(0,0,0,0.9)';
    this.lightbox.style.zIndex = '1000';
    this.lightbox.style.alignItems = 'center';
    this.lightbox.style.justifyContent = 'center';

    this.lightboxContent = document.createElement('div');
    this.lightboxContent.className = 'lightbox-content';
    this.lightboxContent.style.position = 'relative';
    this.lightboxContent.style.maxWidth = '90%';
    this.lightboxContent.style.maxHeight = '90%';

    this.lightboxImg = document.createElement('img');
    this.lightboxImg.style.maxHeight = '90vh';
    this.lightboxImg.style.maxWidth = '100%';

    this.lightboxCaption = document.createElement('div');
    this.lightboxCaption.className = 'lightbox-caption';
    this.lightboxCaption.style.color = 'white';
    this.lightboxCaption.style.textAlign = 'center';
    this.lightboxCaption.style.padding = '10px';

    const closeBtn = document.createElement('span');
    closeBtn.className = 'lightbox-close';
    closeBtn.innerHTML = '&times;';
    closeBtn.style.position = 'absolute';
    closeBtn.style.top = '15px';
    closeBtn.style.right = '15px';
    closeBtn.style.color = 'white';
    closeBtn.style.fontSize = '35px';
    closeBtn.style.cursor = 'pointer';

    const prevBtn = document.createElement('span');
    prevBtn.className = 'lightbox-prev';
    prevBtn.innerHTML = '&#10094;';
    prevBtn.style.position = 'absolute';
    prevBtn.style.top = '50%';
    prevBtn.style.left = '15px';
    prevBtn.style.color = 'white';
    prevBtn.style.fontSize = '35px';
    prevBtn.style.cursor = 'pointer';

    const nextBtn = document.createElement('span');
    nextBtn.className = 'lightbox-next';
    nextBtn.innerHTML = '&#10095;';
    nextBtn.style.position = 'absolute';
    nextBtn.style.top = '50%';
    nextBtn.style.right = '15px';
    nextBtn.style.color = 'white';
    nextBtn.style.fontSize = '35px';
    nextBtn.style.cursor = 'pointer';

    this.lightboxContent.appendChild(closeBtn);
    this.lightboxContent.appendChild(prevBtn);
    this.lightboxContent.appendChild(nextBtn);
    this.lightboxContent.appendChild(this.lightboxImg);
    this.lightboxContent.appendChild(this.lightboxCaption);
    this.lightbox.appendChild(this.lightboxContent);
    document.body.appendChild(this.lightbox);
  }

  /**
   * Setup event listeners for gallery
   */
  setupEventListeners() {
    if (this.options.lightbox) {
      this.container.addEventListener('click', (e) => {
        const item = e.target.closest('.gallery-item');
        if (item) {
          this.openLightbox(parseInt(item.dataset.index));
        }
      });

      document.querySelector('.lightbox-close').addEventListener('click', () => {
        this.closeLightbox();
      });

      document.querySelector('.lightbox-prev').addEventListener('click', () => {
        this.navigateLightbox(-1);
      });

      document.querySelector('.lightbox-next').addEventListener('click', () => {
        this.navigateLightbox(1);
      });

      document.addEventListener('keydown', (e) => {
        if (this.lightbox.style.display === 'flex') {
          if (e.key === 'Escape') {
            this.closeLightbox();
          } else if (e.key === 'ArrowLeft') {
            this.navigateLightbox(-1);
          } else if (e.key === 'ArrowRight') {
            this.navigateLightbox(1);
          }
        }
      });
    }
  }

  /**
   * Open lightbox with specific image
   * @param {number} index - Index of image to display
   */
  openLightbox(index) {
    this.currentIndex = index;
    const image = this.images[index];
    
    this.lightboxImg.src = image.src;
    this.lightboxImg.alt = image.alt || '';
    this.lightboxCaption.textContent = image.caption || '';
    
    this.lightbox.style.display = 'flex';
    document.body.style.overflow = 'hidden';
  }

  /**
   * Close lightbox
   */
  closeLightbox() {
    this.lightbox.style.display = 'none';
    document.body.style.overflow = 'auto';
  }

  /**
   * Navigate through images in lightbox
   * @param {number} direction - 1 for next, -1 for previous
   */
  navigateLightbox(direction) {
    this.currentIndex += direction;
    
    if (this.currentIndex < 0) {
      this.currentIndex = this.images.length - 1;
    } else if (this.currentIndex >= this.images.length) {
      this.currentIndex = 0;
    }
    
    this.openLightbox(this.currentIndex);
  }

  /**
   * Update gallery with new images
   * @param {Array} newImages - Array of new image objects
   */
  updateGallery(newImages) {
    this.images = newImages;
    this.container.innerHTML = '';
    this.initGallery();
  }
}

// Example usage:
/*
const gallery = new KristosGallery('#gallery-container', [
  { src: 'image1.jpg', alt: 'Event 1', caption: 'Summer Party 2023' },
  { src: 'image2.jpg', alt: 'Event 2', caption: 'New Year Celebration' },
  // More images...
], {
  columns: 4,
  gap: '20px'
});
*/
```
