"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Generate a JavaScript code snippet to create a responsive image grid for a photography website, using Officine dell'Immagine's photography styles and services as examples.
Generated: DETERMINISTIC_b411859b29f5d602
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Responsive Image Grid for Photography Website
 * Inspired by Officine dell'Immagine's photography styles
 */

class ResponsiveImageGrid {
  /**
   * Initialize the image grid
   * @param {Object} options - Configuration options
   * @param {string} options.containerSelector - CSS selector for the container
   * @param {Array} options.images - Array of image objects
   * @param {number} options.columns - Default number of columns
   * @param {number} options.gutter - Space between images in pixels
   */
  constructor(options) {
    this.options = {
      columns: 3,
      gutter: 20,
      breakpoints: {
        mobile: 480,
        tablet: 768,
        desktop: 1024
      },
      ...options
    };

    this.container = document.querySelector(this.options.containerSelector);
    if (!this.container) {
      throw new Error(`Container element not found: ${this.options.containerSelector}`);
    }

    this.init();
    this.setupEventListeners();
  }

  /**
   * Initialize the grid
   */
  init() {
    this.updateColumns();
    this.renderGrid();
  }

  /**
   * Update number of columns based on screen size
   */
  updateColumns() {
    const width = window.innerWidth;
    
    if (width < this.options.breakpoints.mobile) {
      this.currentColumns = 1;
    } else if (width < this.options.breakpoints.tablet) {
      this.currentColumns = 2;
    } else if (width < this.options.breakpoints.desktop) {
      this.currentColumns = this.options.columns - 1;
    } else {
      this.currentColumns = this.options.columns;
    }
  }

  /**
   * Render the image grid
   */
  renderGrid() {
    this.container.innerHTML = '';
    this.container.style.display = 'grid';
    this.container.style.gridTemplateColumns = `repeat(${this.currentColumns}, 1fr)`;
    this.container.style.gap = `${this.options.gutter}px`;

    this.options.images.forEach(image => {
      const gridItem = this.createGridItem(image);
      this.container.appendChild(gridItem);
    });
  }

  /**
   * Create a grid item element
   * @param {Object} image - Image data
   * @returns {HTMLElement} Grid item element
   */
  createGridItem(image) {
    const item = document.createElement('div');
    item.className = 'grid-item';
    item.style.position = 'relative';
    item.style.overflow = 'hidden';
    item.style.borderRadius = '4px';
    item.style.transition = 'transform 0.3s ease';

    const img = document.createElement('img');
    img.src = image.src;
    img.alt = image.alt || '';
    img.style.width = '100%';
    img.style.height = '100%';
    img.style.objectFit = 'cover';
    img.style.display = 'block';
    img.loading = 'lazy';

    const overlay = document.createElement('div');
    overlay.className = 'image-overlay';
    overlay.style.position = 'absolute';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.3)';
    overlay.style.opacity = '0';
    overlay.style.transition = 'opacity 0.3s ease';
    overlay.style.display = 'flex';
    overlay.style.flexDirection = 'column';
    overlay.style.justifyContent = 'center';
    overlay.style.alignItems = 'center';
    overlay.style.color = 'white';
    overlay.style.padding = '20px';
    overlay.style.textAlign = 'center';

    if (image.title) {
      const title = document.createElement('h3');
      title.textContent = image.title;
      title.style.margin = '0 0 10px 0';
      title.style.fontSize = '1.2rem';
      overlay.appendChild(title);
    }

    if (image.description) {
      const desc = document.createElement('p');
      desc.textContent = image.description;
      desc.style.margin = '0';
      desc.style.fontSize = '0.9rem';
      overlay.appendChild(desc);
    }

    item.appendChild(img);
    item.appendChild(overlay);

    // Hover effects
    item.addEventListener('mouseenter', () => {
      overlay.style.opacity = '1';
      item.style.transform = 'scale(1.03)';
    });

    item.addEventListener('mouseleave', () => {
      overlay.style.opacity = '0';
      item.style.transform = 'scale(1)';
    });

    return item;
  }

  /**
   * Setup event listeners for responsiveness
   */
  setupEventListeners() {
    window.addEventListener('resize', () => {
      this.updateColumns();
      this.renderGrid();
    });
  }
}

// Example usage with Officine dell'Immagine style images
document.addEventListener('DOMContentLoaded', () => {
  try {
    const imageGrid = new ResponsiveImageGrid({
      containerSelector: '#photography-grid',
      columns: 4,
      gutter: 15,
      images: [
        {
          src: 'images/portrait.jpg',
          alt: 'Portrait Photography',
          title: 'Portrait',
          description: 'Elegant portrait photography capturing personality'
        },
        {
          src: 'images/fashion.jpg',
          alt: 'Fashion Photography',
          title: 'Fashion',
          description: 'Stylish fashion photography for brands and designers'
        },
        {
          src: 'images/commercial.jpg',
          alt: 'Commercial Photography',
          title: 'Commercial',
          description: 'Professional product and commercial photography'
        },
        {
          src: 'images/editorial.jpg',
          alt: 'Editorial Photography',
          title: 'Editorial',
          description: 'Storytelling through editorial photography'
        },
        {
          src: 'images/event.jpg',
          alt: 'Event Photography',
          title: 'Events',
          description: 'Capturing special moments at corporate and private events'
        },
        {
          src: 'images/architecture.jpg',
          alt: 'Architecture Photography',
          title: 'Architecture',
          description: 'Stunning architectural photography'
        }
      ]
    });
  } catch (error) {
    console.error('Error initializing image grid:', error);
  }
});
```
