"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Create a simple HTML template for showcasing a gallery with media sliders, tailored for Strikingly's editor.
Generated: DETERMINISTIC_8f8efe5247c6153e
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- 
  Gallery Template for Strikingly Editor
  ======================================
  This template creates a simple gallery with a media slider.
-->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gallery Template</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- 
    Gallery Container
    =================
  -->
  <div class="gallery-container">
    <!-- 
      Slider Container
      ================
    -->
    <div class="slider-container">
      <!-- 
        Slider Items
        ============
      -->
      <div class="slider-item active">
        <img src="image1.jpg" alt="Image 1">
      </div>
      <div class="slider-item">
        <img src="image2.jpg" alt="Image 2">
      </div>
      <div class="slider-item">
        <img src="image3.jpg" alt="Image 3">
      </div>
      <!-- Add more slider items as needed -->
    </div>
    <!-- 
      Navigation Controls
      ===================
    -->
    <div class="nav-controls">
      <button class="prev-btn">&#10094;</button>
      <button class="next-btn">&#10095;</button>
    </div>
    <!-- 
      Dot Navigation
      ==============
    -->
    <div class="dot-nav">
      <span class="dot active"></span>
      <span class="dot"></span>
      <span class="dot"></span>
      <!-- Add more dots as needed -->
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* 
  Gallery Styles
  =============
*/

/* Global Styles */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
}

/* Gallery Container */
.gallery-container {
  max-width: 800px;
  margin: 40px auto;
  position: relative;
}

/* Slider Container */
.slider-container {
  position: relative;
  width: 100%;
  height: 500px;
  overflow: hidden;
}

.slider-item {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: none;
}

.slider-item.active {
  display: block;
}

.slider-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Navigation Controls */
.nav-controls {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  justify-content: space-between;
  width: 100px;
}

.prev-btn, .next-btn {
  background-color: #333;
  color: #fff;
  border: none;
  padding: 10px 20px;
  font-size: 16px;
  cursor: pointer;
}

.prev-btn:hover, .next-btn:hover {
  background-color: #444;
}

/* Dot Navigation */
.dot-nav {
  position: absolute;
  bottom: 50px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
}

.dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background-color: #ccc;
  margin: 0 5px;
  cursor: pointer;
}

.dot.active {
  background-color: #333;
}
```

```javascript
// 
//  Gallery Script
//  ==============
//

const sliderContainer = document.querySelector('.slider-container');
const sliderItems = document.querySelectorAll('.slider-item');
const navControls = document.querySelector('.nav-controls');
const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const dotNav = document.querySelector('.dot-nav');
const dots = document.querySelectorAll('.dot');

let activeIndex = 0;

// 
//  Show Slider Item
//  ==============
// 
function showSliderItem(index) {
  sliderItems.forEach((item, i) => {
    if (i === index) {
      item.classList.add('active');
    } else {
      item.classList.remove('active');
    }
  });

  dots.forEach((dot, i) => {
    if (i === index) {
      dot.classList.add('active');
    } else {
      dot.classList.remove('active');
    }
  });
}

// 
//  Prev Button Click
//  ================
// 
prevBtn.addEventListener('click', () => {
  activeIndex = (activeIndex - 1 + sliderItems.length) % sliderItems.length;
  showSliderItem(activeIndex);
});

// 
//  Next Button Click
//  ================
// 
nextBtn.addEventListener('click', () => {
  activeIndex = (activeIndex + 1) % sliderItems.length;
  showSliderItem(activeIndex);
});

// 
//  Dot Click
//  =========
// 
dotNav.addEventListener('click', (e) => {
  if (e.target.classList.contains('dot')) {
    const index = Array.prototype.indexOf.call(dots, e.target);
    activeIndex = index;
    showSliderItem(activeIndex);
  }
});

// 
//  Autoplay
//  ========
// 
setInterval(() => {
  activeIndex = (activeIndex + 1) % sliderItems.length;
  showSliderItem(activeIndex);
}, 3000);
```
