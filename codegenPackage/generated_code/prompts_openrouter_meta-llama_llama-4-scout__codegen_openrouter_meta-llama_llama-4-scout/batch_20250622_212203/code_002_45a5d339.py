"""
Generated Code Metadata:
========================
Original URL: https://indologicalindia.com
Prompt: Generate a JavaScript code snippet for creating a simple website gallery, like the one found on the Indological India website, to showcase their activities and events.
Generated: DETERMINISTIC_45a5d3391b837e1b
Batch ID: 20250622_212203
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
// Gallery class representing a website gallery
class Gallery {
  /**
   * Constructor for Gallery
   * @param {string} galleryContainerId - The id of the container element for the gallery
   * @param {object[]} images - An array of objects containing image details
   */
  constructor(galleryContainerId, images) {
    this.galleryContainerId = galleryContainerId;
    this.images = images;
    this.currentImageIndex = 0;
    this.galleryContainer = document.getElementById(galleryContainerId);
    this.galleryContainer.classList.add('gallery-container');
    this.createGallery();
  }

  // Method to create the gallery
  createGallery() {
    // Create gallery elements
    this.images.forEach((image, index) => {
      const imageElement = document.createElement('div');
      imageElement.classList.add('gallery-item');
      imageElement.innerHTML = `
        <img src="${image.src}" alt="${image.alt}" />
        <div class="overlay">
          <div class="description">${image.description}</div>
        </div>
      `;
      this.galleryContainer.appendChild(imageElement);

      // Add event listener for image click
      imageElement.addEventListener('click', () => {
        this.openLightbox(index);
      });
    });

    // Create navigation buttons
    const navigationContainer = document.createElement('div');
    navigationContainer.classList.add('navigation-container');
    const prevButton = document.createElement('button');
    prevButton.classList.add('prev-button');
    prevButton.textContent = 'Prev';
    const nextButton = document.createElement('button');
    nextButton.classList.add('next-button');
    nextButton.textContent = 'Next';
    navigationContainer.appendChild(prevButton);
    navigationContainer.appendChild(nextButton);
    this.galleryContainer.appendChild(navigationContainer);

    // Add event listeners for navigation buttons
    prevButton.addEventListener('click', () => {
      this.navigateToPreviousImage();
    });
    nextButton.addEventListener('click', () => {
      this.navigateToNextImage();
    });

    // Create lightbox
    this.lightbox = document.createElement('div');
    this.lightbox.classList.add('lightbox');
    this.lightbox.innerHTML = `
      <img src="" alt="" />
      <div class="description"></div>
      <button class="close-button">Close</button>
    `;
    document.body.appendChild(this.lightbox);

    // Add event listener for close button
    this.lightbox.querySelector('.close-button').addEventListener('click', () => {
      this.closeLightbox();
    });
  }

  // Method to open lightbox
  openLightbox(imageIndex) {
    this.currentImageIndex = imageIndex;
    const image = this.images[this.currentImageIndex];
    this.lightbox.querySelector('img').src = image.src;
    this.lightbox.querySelector('img').alt = image.alt;
    this.lightbox.querySelector('.description').textContent = image.description;
    this.lightbox.classList.add('open');
  }

  // Method to close lightbox
  closeLightbox() {
    this.lightbox.classList.remove('open');
  }

  // Method to navigate to previous image
  navigateToPreviousImage() {
    if (this.currentImageIndex > 0) {
      this.currentImageIndex--;
    } else {
      this.currentImageIndex = this.images.length - 1;
    }
    const image = this.images[this.currentImageIndex];
    this.lightbox.querySelector('img').src = image.src;
    this.lightbox.querySelector('img').alt = image.alt;
    this.lightbox.querySelector('.description').textContent = image.description;
  }

  // Method to navigate to next image
  navigateToNextImage() {
    if (this.currentImageIndex < this.images.length - 1) {
      this.currentImageIndex++;
    } else {
      this.currentImageIndex = 0;
    }
    const image = this.images[this.currentImageIndex];
    this.lightbox.querySelector('img').src = image.src;
    this.lightbox.querySelector('img').alt = image.alt;
    this.lightbox.querySelector('.description').textContent = image.description;
  }
}

// Example usage
const images = [
  {
    src: 'https://example.com/image1.jpg',
    alt: 'Image 1',
    description: 'This is image 1',
  },
  {
    src: 'https://example.com/image2.jpg',
    alt: 'Image 2',
    description: 'This is image 2',
  },
  {
    src: 'https://example.com/image3.jpg',
    alt: 'Image 3',
    description: 'This is image 3',
  },
];

try {
  const gallery = new Gallery('gallery', images);
} catch (error) {
  console.error('Error creating gallery:', error);
}

// CSS styles for gallery (can be moved to a separate file)
// .gallery-container {
//   display: flex;
//   flex-wrap: wrap;
//   justify-content: center;
// }

// .gallery-item {
//   margin: 10px;
//   position: relative;
// }

// .gallery-item img {
//   width: 200px;
//   height: 150px;
//   object-fit: cover;
//   border-radius: 10px;
// }

// .overlay {
//   position: absolute;
//   top: 0;
//   left: 0;
//   width: 100%;
//   height: 100%;
//   background-color: rgba(0, 0, 0, 0.5);
//   opacity: 0;
//   transition: opacity 0.5s;
//   display: flex;
//   justify-content: center;
//   align-items: center;
// }

// .gallery-item:hover .overlay {
//   opacity: 1;
// }

// .description {
//   color: #fff;
//   font-size: 16px;
//   text-align: center;
// }

// .navigation-container {
//   text-align: center;
//   margin-top: 20px;
// }

// .prev-button, .next-button {
//   background-color: #333;
//   color: #fff;
//   border: none;
//   padding: 10px 20px;
//   font-size: 16px;
//   cursor: pointer;
// }

// .lightbox {
//   position: fixed;
//   top: 0;
//   left: 0;
//   width: 100%;
//   height: 100%;
//   background-color: rgba(0, 0, 0, 0.8);
//   display: none;
// }

// .lightbox.open {
//   display: block;
// }

// .lightbox img {
//   width: 80%;
//   height: 80%;
//   object-fit: contain;
//   position: absolute;
//   top: 50%;
//   left: 50%;
//   transform: translate(-50%, -50%);
// }

// .lightbox .description {
//   position: absolute;
//   bottom: 20px;
//   left: 20px;
//   color: #fff;
//   font-size: 18px;
// }

// .close-button {
//   position: absolute;
//   top: 20px;
//   right: 20px;
//   background-color: #333;
//   color: #fff;
//   border: none;
//   padding: 10px 20px;
//   font-size: 16px;
//   cursor: pointer;
// }
```
