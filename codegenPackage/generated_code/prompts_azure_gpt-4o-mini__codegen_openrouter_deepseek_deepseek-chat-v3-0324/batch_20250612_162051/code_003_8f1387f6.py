"""
Generated Code Metadata:
========================
Original URL: https://hsrenterprises.co.in
Prompt: Develop a JavaScript code to implement a virtual tour feature for a Royal Enfield showroom, highlighting the Himalayan and Thunderbird models.
Generated: DETERMINISTIC_8f1387f6b73fbb19
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Virtual Tour for Royal Enfield Showroom
 * Highlights the Himalayan and Thunderbird models
 */

class VirtualTour {
  constructor() {
    this.models = {
      himalayan: {
        name: 'Himalayan',
        description: 'Built for adventure, the Himalayan is designed to conquer the toughest terrains with ease.',
        features: [
          '411cc Engine',
          'Long-travel Suspension',
          'Upright Riding Position',
          'Spoked Wheels'
        ],
        images: [
          'himalayan_1.jpg',
          'himalayan_2.jpg',
          'himalayan_3.jpg'
        ]
      },
      thunderbird: {
        name: 'Thunderbird',
        description: 'The Thunderbird combines classic cruiser styling with modern performance.',
        features: [
          '350cc Engine',
          'Cruiser Ergonomics',
          'Classic Styling',
          'Comfortable Ride'
        ],
        images: [
          'thunderbird_1.jpg',
          'thunderbird_2.jpg',
          'thunderbird_3.jpg'
        ]
      }
    };
    this.currentModel = null;
    this.currentImageIndex = 0;
  }

  /**
   * Initialize the virtual tour
   */
  init() {
    try {
      this.setupEventListeners();
      this.showModel('himalayan'); // Default to Himalayan
      console.log('Virtual Tour initialized successfully');
    } catch (error) {
      console.error('Failed to initialize Virtual Tour:', error);
    }
  }

  /**
   * Set up event listeners for model selection and navigation
   */
  setupEventListeners() {
    document.getElementById('himalayan-btn').addEventListener('click', () => this.showModel('himalayan'));
    document.getElementById('thunderbird-btn').addEventListener('click', () => this.showModel('thunderbird'));
    document.getElementById('prev-btn').addEventListener('click', () => this.showPreviousImage());
    document.getElementById('next-btn').addEventListener('click', () => this.showNextImage());
  }

  /**
   * Display the selected model
   * @param {string} modelKey - Key of the model to display
   */
  showModel(modelKey) {
    try {
      if (!this.models[modelKey]) {
        throw new Error(`Model ${modelKey} not found`);
      }

      this.currentModel = this.models[modelKey];
      this.currentImageIndex = 0;
      this.updateDisplay();
    } catch (error) {
      console.error('Error showing model:', error);
    }
  }

  /**
   * Show the previous image in the gallery
   */
  showPreviousImage() {
    if (!this.currentModel) return;

    this.currentImageIndex = (this.currentImageIndex - 1 + this.currentModel.images.length) % this.currentModel.images.length;
    this.updateDisplay();
  }

  /**
   * Show the next image in the gallery
   */
  showNextImage() {
    if (!this.currentModel) return;

    this.currentImageIndex = (this.currentImageIndex + 1) % this.currentModel.images.length;
    this.updateDisplay();
  }

  /**
   * Update the display with current model and image
   */
  updateDisplay() {
    try {
      if (!this.currentModel) return;

      // Update model info
      document.getElementById('model-name').textContent = this.currentModel.name;
      document.getElementById('model-description').textContent = this.currentModel.description;
      
      // Update features list
      const featuresList = document.getElementById('model-features');
      featuresList.innerHTML = '';
      this.currentModel.features.forEach(feature => {
        const li = document.createElement('li');
        li.textContent = feature;
        featuresList.appendChild(li);
      });

      // Update image
      const imagePath = `assets/images/${this.currentModel.images[this.currentImageIndex]}`;
      document.getElementById('model-image').src = imagePath;
      document.getElementById('model-image').alt = `${this.currentModel.name} - Image ${this.currentImageIndex + 1}`;
    } catch (error) {
      console.error('Error updating display:', error);
    }
  }
}

// Initialize the virtual tour when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
  const tour = new VirtualTour();
  tour.init();
});
```

```html
<!-- Sample HTML structure that would work with the above JavaScript -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Royal Enfield Virtual Tour</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }
    .model-container {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .model-image-container {
      position: relative;
      margin: 20px 0;
    }
    .model-image {
      max-width: 100%;
      height: auto;
      max-height: 500px;
    }
    .nav-button {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(0,0,0,0.5);
      color: white;
      border: none;
      padding: 10px 15px;
      cursor: pointer;
    }
    #prev-btn {
      left: 10px;
    }
    #next-btn {
      right: 10px;
    }
    .model-selector {
      margin: 20px 0;
    }
    .model-selector button {
      padding: 10px 20px;
      margin: 0 10px;
      cursor: pointer;
    }
    .model-info {
      text-align: center;
      max-width: 800px;
    }
    .features-list {
      text-align: left;
      display: inline-block;
    }
  </style>
</head>
<body>
  <h1>Royal Enfield Virtual Tour</h1>
  
  <div class="model-selector">
    <button id="himalayan-btn">Himalayan</button>
    <button id="thunderbird-btn">Thunderbird</button>
  </div>
  
  <div class="model-container">
    <div class="model-image-container">
      <img id="model-image" class="model-image" src="" alt="Royal Enfield Model">
      <button id="prev-btn" class="nav-button">Previous</button>
      <button id="next-btn" class="nav-button">Next</button>
    </div>
    
    <div class="model-info">
      <h2 id="model-name"></h2>
      <p id="model-description"></p>
      <h3>Features</h3>
      <ul id="model-features" class="features-list"></ul>
    </div>
  </div>

  <script src="virtual-tour.js"></script>
</body>
</html>
```
