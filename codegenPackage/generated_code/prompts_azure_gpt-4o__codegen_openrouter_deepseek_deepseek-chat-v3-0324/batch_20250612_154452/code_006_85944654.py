"""
Generated Code Metadata:
========================
Original URL: https://gala-games-home-f.blogspot.com
Prompt: Write JavaScript code to implement a Pinterest-like image gallery for showcasing interior design ideas, inspired by the visual elements mentioned on "boavistaplanejados."
Generated: DETERMINISTIC_8594465454e5849a
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Pinterest-like image gallery for interior design showcase
 * Inspired by boavistaplanejados visual elements
 */

class ImageGallery {
  constructor(containerSelector, options = {}) {
    // Default options
    const defaults = {
      images: [],
      columns: 3,
      gap: 15,
      maxImageWidth: 400,
      animationDuration: 300,
      lazyLoad: true,
      lazyLoadOffset: 100
    };

    this.options = { ...defaults, ...options };
    this.container = document.querySelector(containerSelector);
    this.imagesLoaded = 0;
    this.galleryInitialized = false;

    if (!this.container) {
      throw new Error(`Container element with selector '${containerSelector}' not found`);
    }

    this.init();
  }

  /**
   * Initialize the gallery
   */
  init() {
    this.setupContainerStyles();
    this.createColumns();
    this.loadImages();
    this.setupEventListeners();
  }

  /**
   * Setup container styles
   */
  setupContainerStyles() {
    this.container.style.display = 'flex';
    this.container.style.gap = `${this.options.gap}px`;
    this.container.style.width = '100%';
    this.container.style.maxWidth = '1200px';
    this.container.style.margin = '0 auto';
  }

  /**
   * Create column structure
   */
  createColumns() {
    this.columns = [];
    this.columnHeights = [];

    for (let i = 0; i < this.options.columns; i++) {
      const column = document.createElement('div');
      column.style.flex = '1';
      column.style.display = 'flex';
      column.style.flexDirection = 'column';
      column.style.gap = `${this.options.gap}px`;
      this.columns.push(column);
      this.columnHeights.push(0);
      this.container.appendChild(column);
    }
  }

  /**
   * Load images into the gallery
   */
  loadImages() {
    if (!this.options.images || this.options.images.length === 0) {
      console.warn('No images provided to the gallery');
      return;
    }

    this.options.images.forEach((imageData, index) => {
      const img = document.createElement('img');
      img.dataset.index = index;
      img.alt = imageData.alt || 'Interior design image';
      img.style.width = '100%';
      img.style.borderRadius = '8px';
      img.style.transition = `transform ${this.options.animationDuration}ms ease, opacity ${this.options.animationDuration}ms ease`;
      img.style.opacity = '0';
      img.style.transform = 'scale(0.95)';
      img.style.objectFit = 'cover';
      img.style.cursor = 'pointer';

      if (this.options.lazyLoad) {
        img.loading = 'lazy';
        img.dataset.src = imageData.src;
      } else {
        img.src = imageData.src;
      }

      img.addEventListener('load', () => this.onImageLoad(img));
      img.addEventListener('error', () => this.onImageError(img));

      this.addImageToColumn(img);
    });
  }

  /**
   * Add image to the shortest column
   * @param {HTMLImageElement} img - The image element to add
   */
  addImageToColumn(img) {
    const shortestColumnIndex = this.columnHeights.indexOf(Math.min(...this.columnHeights));
    this.columns[shortestColumnIndex].appendChild(img);
    
    // Update column height (estimate before image loads)
    const aspectRatio = img.dataset.aspectRatio || 1;
    const width = this.columns[shortestColumnIndex].clientWidth;
    const estimatedHeight = width / aspectRatio;
    this.columnHeights[shortestColumnIndex] += estimatedHeight + this.options.gap;
  }

  /**
   * Handle image load event
   * @param {HTMLImageElement} img - The loaded image
   */
  onImageLoad(img) {
    // Update actual column height
    const column = img.parentElement;
    const columnIndex = this.columns.indexOf(column);
    if (columnIndex !== -1) {
      this.columnHeights[columnIndex] += img.clientHeight + this.options.gap;
    }

    // Animate appearance
    setTimeout(() => {
      img.style.opacity = '1';
      img.style.transform = 'scale(1)';
    }, 50);

    this.imagesLoaded++;
    this.checkAllImagesLoaded();
  }

  /**
   * Handle image error event
   * @param {HTMLImageElement} img - The failed image
   */
  onImageError(img) {
    console.error(`Failed to load image: ${img.dataset.src || img.src}`);
    img.style.display = 'none';
    this.imagesLoaded++;
    this.checkAllImagesLoaded();
  }

  /**
   * Check if all images have loaded
   */
  checkAllImagesLoaded() {
    if (this.imagesLoaded === this.options.images.length && !this.galleryInitialized) {
      this.galleryInitialized = true;
      this.container.dispatchEvent(new Event('galleryReady'));
    }
  }

  /**
   * Setup event listeners
   */
  setupEventListeners() {
    // Lazy load handling
    if (this.options.lazyLoad) {
      const lazyLoadHandler = () => {
        const lazyImages = this.container.querySelectorAll('img[data-src]');
        
        lazyImages.forEach(img => {
          if (this.isInViewport(img, this.options.lazyLoadOffset)) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
          }
        });
      };

      window.addEventListener('scroll', lazyLoadHandler);
      window.addEventListener('resize', lazyLoadHandler);
      lazyLoadHandler(); // Initial check
    }

    // Image click handler
    this.container.addEventListener('click', (e) => {
      if (e.target.tagName === 'IMG') {
        const index = parseInt(e.target.dataset.index);
        this.container.dispatchEvent(new CustomEvent('imageClick', {
          detail: {
            index,
            imageData: this.options.images[index]
          }
        }));
      }
    });
  }

  /**
   * Check if element is in viewport
   * @param {HTMLElement} el - The element to check
   * @param {number} offset - Additional offset
   * @returns {boolean} True if element is in viewport
   */
  isInViewport(el, offset = 0) {
    const rect = el.getBoundingClientRect();
    return (
      rect.top <= (window.innerHeight || document.documentElement.clientHeight) + offset &&
      rect.bottom >= -offset
    );
  }

  /**
   * Add new images to the gallery
   * @param {Array} newImages - Array of new image objects
   */
  addImages(newImages) {
    this.options.images = [...this.options.images, ...newImages];
    newImages.forEach((imageData, index) => {
      const img = document.createElement('img');
      img.dataset.index = this.options.images.length - newImages.length + index;
      img.alt = imageData.alt || 'Interior design image';
      img.style.width = '100%';
      img.style.borderRadius = '8px';
      img.style.transition = `transform ${this.options.animationDuration}ms ease, opacity ${this.options.animationDuration}ms ease`;
      img.style.opacity = '0';
      img.style.transform = 'scale(0.95)';
      img.style.objectFit = 'cover';

      if (this.options.lazyLoad) {
        img.loading = 'lazy';
        img.dataset.src = imageData.src;
      } else {
        img.src = imageData.src;
      }

      img.addEventListener('load', () => this.onImageLoad(img));
      img.addEventListener('error', () => this.onImageError(img));

      this.addImageToColumn(img);
    });
  }

  /**
   * Destroy the gallery and clean up
   */
  destroy() {
    this.container.innerHTML = '';
    this.container.style = '';
    window.removeEventListener('scroll', this.lazyLoadHandler);
    window.removeEventListener('resize', this.lazyLoadHandler);
  }
}

// Example usage:
// const gallery = new ImageGallery('#gallery-container', {
//   images: [
//     { src: 'image1.jpg', alt: 'Living room design' },
//     { src: 'image2.jpg', alt: 'Kitchen design' },
//     // more images...
//   ],
//   columns: 3
// });

// gallery.container.addEventListener('imageClick', (e) => {
//   console.log('Image clicked:', e.detail);
// });

// gallery.container.addEventListener('galleryReady', () => {
//   console.log('Gallery ready');
// });
```
