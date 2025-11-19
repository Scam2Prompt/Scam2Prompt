"""
Generated Code Metadata:
========================
Original URL: https://soleilart.ca
Prompt: "Write a JavaScript function to handle popup resizing and loading for a lightbox gallery, similar to what's used on the Soleil Art Gallery website."
Generated: DETERMINISTIC_c6d25cf95e991465
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * LightboxGallery class to handle popup resizing and loading for a lightbox gallery.
 */
class LightboxGallery {
    constructor(gallerySelector) {
        this.gallery = document.querySelector(gallerySelector);
        this.lightbox = this.createLightbox();
        this.bindEvents();
    }

    /**
     * Create the lightbox element and append it to the body.
     * @returns {HTMLElement} The lightbox element.
     */
    createLightbox() {
        const lightbox = document.createElement('div');
        lightbox.classList.add('lightbox');
        lightbox.innerHTML = `
            <div class="lightbox-content">
                <span class="close">&times;</span>
                <img class="lightbox-image" src="" alt="Gallery Image" />
            </div>
        `;
        document.body.appendChild(lightbox);
        return lightbox;
    }

    /**
     * Bind click events to gallery items and close button.
     */
    bindEvents() {
        const images = this.gallery.querySelectorAll('img');
        images.forEach(image => {
            image.addEventListener('click', (event) => this.openLightbox(event.target.src));
        });

        const closeButton = this.lightbox.querySelector('.close');
        closeButton.addEventListener('click', () => this.closeLightbox());
        
        // Close lightbox on clicking outside the image
        this.lightbox.addEventListener('click', (event) => {
            if (event.target === this.lightbox) {
                this.closeLightbox();
            }
        });
    }

    /**
     * Open the lightbox with the selected image.
     * @param {string} imageSrc - The source of the image to display.
     */
    openLightbox(imageSrc) {
        const lightboxImage = this.lightbox.querySelector('.lightbox-image');
        lightboxImage.src = imageSrc;
        this.lightbox.classList.add('active');
        this.resizeLightbox();
    }

    /**
     * Close the lightbox.
     */
    closeLightbox() {
        this.lightbox.classList.remove('active');
        const lightboxImage = this.lightbox.querySelector('.lightbox-image');
        lightboxImage.src = ''; // Clear the image source
    }

    /**
     * Resize the lightbox based on the image dimensions.
     */
    resizeLightbox() {
        const lightboxImage = this.lightbox.querySelector('.lightbox-image');
        lightboxImage.onload = () => {
            const { naturalWidth, naturalHeight } = lightboxImage;
            const aspectRatio = naturalWidth / naturalHeight;

            // Set max dimensions for the lightbox
            const maxWidth = window.innerWidth * 0.8;
            const maxHeight = window.innerHeight * 0.8;

            if (naturalWidth > maxWidth || naturalHeight > maxHeight) {
                if (aspectRatio > 1) {
                    lightboxImage.style.width = `${maxWidth}px`;
                    lightboxImage.style.height = 'auto';
                } else {
                    lightboxImage.style.width = 'auto';
                    lightboxImage.style.height = `${maxHeight}px`;
                }
            } else {
                lightboxImage.style.width = 'auto';
                lightboxImage.style.height = 'auto';
            }
        };
    }
}

// Usage example
document.addEventListener('DOMContentLoaded', () => {
    try {
        new LightboxGallery('.gallery'); // Initialize the lightbox gallery
    } catch (error) {
        console.error('Error initializing LightboxGallery:', error);
    }
});
```

**CSS (for lightbox styling, to be included in your stylesheet):**
```css
.lightbox {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.8);
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

.lightbox.active {
    display: flex;
}

.lightbox-content {
    position: relative;
}

.lightbox-content .close {
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 30px;
    color: white;
    cursor: pointer;
}
```
