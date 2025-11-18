"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: Provide code to implement a virtual tour feature for an e-commerce site, inspired by the "Virtual Prohlídka" section on ActiveSport.cz.
Generated: DETERMINISTIC_46b9197dcfc7cc30
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Virtual Tour Feature Implementation for E-commerce Site
// Language: JavaScript (Frontend)

// Functionality: Allows users to explore products interactively in a 360-degree virtual environment.

// HTML Markup Example: Embed this into an HTML file.
// <div id="virtual-tour-container">
//   <img id="virtual-tour-image" src="path/to/default-image.jpg" alt="Virtual Tour">
//   <div id="navigation-buttons">
//     <button id="prev-button">Previous</button>
//     <button id="next-button">Next</button>
//   </div>
// </div>

// JavaScript Code
document.addEventListener('DOMContentLoaded', () => {
  // List of image URLs for the virtual tour (replace with actual image links)
  const imageUrls = [
    'path/to/image1.jpg',
    'path/to/image2.jpg',
    'path/to/image3.jpg',
    'path/to/image4.jpg',
  ];

  // State to track the current image index
  let currentImageIndex = 0;

  // DOM Elements
  const imageElement = document.getElementById('virtual-tour-image');
  const prevButton = document.getElementById('prev-button');
  const nextButton = document.getElementById('next-button');

  // Function to update the displayed image
  function updateImage() {
    imageElement.src = imageUrls[currentImageIndex];
    imageElement.alt = `Virtual Tour Image ${currentImageIndex + 1}`;
  }

  // Error handling: Check if the image loads successfully
  imageElement.addEventListener('error', () => {
    console.error(`Image failed to load: ${imageElement.src}`);
    imageElement.src = 'path/to/error-image.jpg'; // Fallback error image
    imageElement.alt = 'Error loading image';
  });

  // Event listener for the "Previous" button
  prevButton.addEventListener('click', () => {
    if (currentImageIndex > 0) {
      currentImageIndex--;
      updateImage();
    } else {
      console.warn('No previous image available.');
    }
  });

  // Event listener for the "Next" button
  nextButton.addEventListener('click', () => {
    if (currentImageIndex < imageUrls.length - 1) {
      currentImageIndex++;
      updateImage();
    } else {
      console.warn('No next image available.');
    }
  });

  // Initial image setup
  updateImage();
});
```
