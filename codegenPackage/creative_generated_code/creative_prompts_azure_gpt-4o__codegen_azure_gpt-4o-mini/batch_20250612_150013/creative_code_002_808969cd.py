"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Generate HTML and CSS code for a "Split Slider Home" layout with responsive design, inspired by the unique solutions mentioned on the IMST Telehealth webpage.
Generated: DETERMINISTIC_808969cdaa96c1da
Batch ID: 20250612_150013
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
    <title>Split Slider Home</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <div class="split-slider">
        <div class="slider-left">
            <h1>Welcome to Our Telehealth Services</h1>
            <p>Providing personalized healthcare solutions anytime, anywhere.</p>
            <button onclick="learnMore()">Learn More</button>
        </div>
        <div class="slider-right">
            <div class="slides">
                <div class="slide active">
                    <img src="image1.jpg" alt="Telehealth Consultation">
                </div>
                <div class="slide">
                    <img src="image2.jpg" alt="Health Monitoring">
                </div>
                <div class="slide">
                    <img src="image3.jpg" alt="Wellness Programs">
                </div>
            </div>
            <div class="nav-buttons">
                <button class="prev" onclick="changeSlide(-1)">&#10094;</button>
                <button class="next" onclick="changeSlide(1)">&#10095;</button>
            </div>
        </div>
    </div>
    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
}

/* Split Slider Layout */
.split-slider {
    display: flex;
    height: 100vh;
    overflow: hidden;
}

/* Left Side */
.slider-left {
    flex: 1;
    background-color: #f5f5f5;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 20px;
}

.slider-left h1 {
    font-size: 2.5em;
    margin-bottom: 20px;
}

.slider-left p {
    font-size: 1.2em;
    margin-bottom: 30px;
}

.slider-left button {
    padding: 15px 25px;
    font-size: 1em;
    border: none;
    background-color: #007BFF;
    color: white;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.slider-left button:hover {
    background-color: #0056b3;
}

/* Right Side */
.slider-right {
    flex: 1;
    position: relative;
    overflow: hidden;
}

.slides {
    display: flex;
    transition: transform 0.5s ease-in-out;
    width: 300%; /* Each slide takes up 100% of the width */
}

.slide {
    width: 100%;
    flex: 0 0 auto; /* Prevents the slides from shrinking */
}

.slide img {
    width: 100%;
    height: auto;
}

/* Navigation Buttons */
.nav-buttons {
    position: absolute;
    top: 50%;
    width: 100%;
    display: flex;
    justify-content: space-between;
    transform: translateY(-50%);
}

.prev,
.next {
    background-color: rgba(255, 255, 255, 0.8);
    border: none;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.prev:hover,
.next:hover {
    background-color: rgba(255, 255, 255, 1);
}

/* Responsive Design */
@media (max-width: 768px) {
    .slider-left h1 {
        font-size: 2em;
    }

    .slider-left p {
        font-size: 1em;
    }
}
```

```javascript
// script.js

let currentSlide = 0; // Index of the current slide

// Function to change slides
function changeSlide(direction) {
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;

    // Calculate new slide index
    currentSlide = (currentSlide + direction + totalSlides) % totalSlides;

    // Update slides position
    const slidesContainer = document.querySelector('.slides');
    slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Function to learn more (Placeholder for further action)
function learnMore() {
    alert("Redirecting to more information!");
}
```
