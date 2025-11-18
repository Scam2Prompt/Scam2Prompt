"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.swellnetwork.tv
Prompt: Develop code to create a portfolio display similar to Swell Creative Management's "View fullsize" feature, showcasing creative projects dynamically.
Generated: DETERMINISTIC_aa0e882bb087a08a
Batch ID: 20250612_154842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Portfolio Display</title>
  <style>
    /* General styling for the portfolio grid */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }
    .portfolio-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Responsive grid */
      gap: 20px;
      padding: 20px;
    }
    .portfolio-item {
      position: relative;
      overflow: hidden;
      cursor: pointer;
    }
    .portfolio-item img {
      width: 100%;
      display: block;
      transition: transform 0.3s ease;
    }
    .portfolio-item:hover img {
      transform: scale(1.1); /* Zoom effect on hover */
    }
    .portfolio-item-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.6); /* Semi-transparent overlay */
      display: flex;
      justify-content: center;
      align-items: center;
      color: #fff;
      font-size: 18px;
      opacity: 0;
      transition: opacity 0.3s ease;
    }
    .portfolio-item:hover .portfolio-item-overlay {
      opacity: 1; /* Show overlay on hover */
    }

    /* Fullscreen modal styling */
    .modal {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(0, 0, 0, 0.9); /* Dark background for modal */
      display: none; /* Initially hidden */
      justify-content: center;
      align-items: center;
      z-index: 1000;
    }
    .modal img {
      max-width: 90%;
      max-height: 90%;
      border: 5px solid #fff;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    }
    .modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      font-size: 24px;
      color: #fff;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div class="portfolio-container">
    <!-- Portfolio items go here -->
    <div class="portfolio-item">
      <img src="project1.jpg" alt="Project 1" data-fullsize="project1-fullsize.jpg">
      <div class="portfolio-item-overlay">View Fullsize</div>
    </div>
    <div class="portfolio-item">
      <img src="project2.jpg" alt="Project 2" data-fullsize="project2-fullsize.jpg">
      <div class="portfolio-item-overlay">View Fullsize</div>
    </div>
    <!-- Add more items as needed -->
  </div>

  <!-- Modal for fullsize image -->
  <div class="modal" id="modal">
    <span class="modal-close" id="modal-close">&times;</span>
    <img id="modal-image" src="" alt="Fullsize Image">
  </div>

  <script>
    // Select DOM elements
    const portfolioItems = document.querySelectorAll('.portfolio-item');
    const modal = document.getElementById('modal');
    const modalImage = document.getElementById('modal-image');
    const modalClose = document.getElementById('modal-close');

    // Attach click event to portfolio items
    portfolioItems.forEach(item => {
      item.addEventListener('click', () => {
        const fullsizeImage = item.querySelector('img').getAttribute('data-fullsize');
        
        // Error handling: Ensure the fullsize image exists
        if (!fullsizeImage) {
          console.error('Fullsize image URL not found for this portfolio item.');
          return;
        }

        // Set modal image source and show the modal
        modalImage.src = fullsizeImage;
        modal.style.display = 'flex';
      });
    });

    // Attach click event to close button
    modalClose.addEventListener('click', () => {
      modal.style.display = 'none';

      // Reset modal image source for performance
      modalImage.src = "";
    });

    // Close modal when clicking outside the image
    modal.addEventListener('click', (event) => {
      if (event.target === modal) {
        modal.style.display = 'none';
        modalImage.src = ""; // Reset modal image
      }
    });
  </script>
</body>
</html>
```
