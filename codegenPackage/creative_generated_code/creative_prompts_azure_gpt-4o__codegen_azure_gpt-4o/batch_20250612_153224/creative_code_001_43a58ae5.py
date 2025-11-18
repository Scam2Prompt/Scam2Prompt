"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hsrenterprises.co.in
Prompt: Generate a script to display a virtual tour of a Royal Enfield showroom using HTML and JavaScript, with interactive navigation features.
Generated: DETERMINISTIC_43a58ae5380f2798
Batch ID: 20250612_153224
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
  <title>Royal Enfield Showroom Virtual Tour</title>
  <style>
    /* Basic styles for the showroom container */
    body {
      margin: 0;
      font-family: Arial, sans-serif;
    }

    #showroom {
      width: 100vw;
      height: 100vh;
      background-size: cover;
      background-position: center;
      position: relative;
      overflow: hidden;
    }

    /* Navigation buttons style */
    .nav-button {
      position: absolute;
      padding: 10px 20px;
      font-size: 16px;
      background-color: #f04e23;
      color: white;
      border: none;
      cursor: pointer;
      border-radius: 5px;
      transition: background-color 0.3s ease;
    }

    .nav-button:hover {
      background-color: #d43b19;
    }

    .nav-button:focus {
      outline: none;
    }

    #left {
      top: 50%;
      left: 20px;
      transform: translateY(-50%);
    }

    #right {
      top: 50%;
      right: 20px;
      transform: translateY(-50%);
    }

    #info {
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
    }

    /* Info box styles */
    #info-box {
      position: absolute;
      bottom: 10%;
      left: 50%;
      transform: translateX(-50%);
      background-color: rgba(0, 0, 0, 0.8);
      color: white;
      padding: 20px;
      border-radius: 8px;
      display: none;
    }

    #info-box h3 {
      margin: 0;
    }

    #info-box p {
      font-size: 14px;
    }
  </style>
</head>
<body>
  <!-- Virtual showroom container -->
  <div id="showroom"></div>

  <!-- Navigation buttons -->
  <button id="left" class="nav-button">Left</button>
  <button id="right" class="nav-button">Right</button>
  <button id="info" class="nav-button">Info</button>

  <!-- Info box -->
  <div id="info-box">
    <h3>Royal Enfield Showroom</h3>
    <p>Welcome to the Royal Enfield virtual showroom! Explore the iconic motorcycles and enjoy an interactive experience.</p>
  </div>

  <script>
    // Array of image URLs for virtual showroom scenes
    const scenes = [
      'scene1.jpg', // Example: Replace with actual image URLs
      'scene2.jpg', // Example: Replace with actual image URLs
      'scene3.jpg', // Example: Replace with actual image URLs
    ];

    let currentScene = 0; // Current scene index

    // DOM elements
    const showroom = document.getElementById('showroom');
    const leftButton = document.getElementById('left');
    const rightButton = document.getElementById('right');
    const infoButton = document.getElementById('info');
    const infoBox = document.getElementById('info-box');

    // Function to display the current scene
    function displayScene() {
      showroom.style.backgroundImage = `url(${scenes[currentScene]})`;
    }

    // Event listener for the left navigation button
    leftButton.addEventListener('click', () => {
      if (currentScene > 0) {
        currentScene--;
        displayScene();
      } else {
        alert('You are at the first scene!');
      }
    });

    // Event listener for the right navigation button
    rightButton.addEventListener('click', () => {
      if (currentScene < scenes.length - 1) {
        currentScene++;
        displayScene();
      } else {
        alert('You are at the last scene!');
      }
    });

    // Event listener for the info button
    infoButton.addEventListener('click', () => {
      if (infoBox.style.display === 'block') {
        infoBox.style.display = 'none';
      } else {
        infoBox.style.display = 'block';
      }
    });

    // Initialize the virtual showroom with the first scene
    displayScene();
  </script>
</body>
</html>
```
