"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Create a simple HTML template for showcasing a gallery with media sliders, tailored for Strikingly's editor.
Generated: DETERMINISTIC_8f8efe5247c6153e
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Media Gallery Slider</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .gallery-container {
            max-width: 800px;
            margin: 20px auto;
            overflow: hidden;
            position: relative;
        }
        .slider {
            display: flex;
            transition: transform 0.5s ease-in-out;
        }
        .slide {
            min-width: 100%;
            box-sizing: border-box;
        }
        img {
            width: 100%;
            display: block;
        }
        .nav-buttons {
            position: absolute;
            top: 50%;
            width: 100%;
            display: flex;
            justify-content: space-between;
            transform: translateY(-50%);
        }
        .nav-button {
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            padding: 10px;
            cursor: pointer;
            font-size: 18px;
            border-radius: 5px;
        }
        .nav-button:hover {
            background-color: rgba(255, 255, 255, 1);
        }
    </style>
</head>
<body>

    <div class="gallery-container">
        <div class="slider" id="slider">
            <div class="slide"><img src="image1.jpg" alt="Gallery Image 1"></div>
            <div class="slide"><img src="image2.jpg" alt="Gallery Image 2"></div>
            <div class="slide"><img src="image3.jpg" alt="Gallery Image 3"></div>
        </div>
        <div class="nav-buttons">
            <button class="nav-button" id="prevBtn"><i class="fas fa-chevron-left"></i></button>
            <button class="nav-button" id="nextBtn"><i class="fas fa-chevron-right"></i></button>
        </div>
    </div>

    <script>
        // Initialize current slide index
        let currentSlide = 0;

        // Get slider and slide elements
        const slider = document.getElementById('slider');
        const slides = document.querySelectorAll('.slide');

        // Function to show the current slide
        function showSlide(index) {
            // Ensure index is within bounds
            if (index < 0) {
                currentSlide = slides.length - 1; // Loop to last slide
            } else if (index >= slides.length) {
                currentSlide = 0; // Loop to first slide
            } else {
                currentSlide = index; // Set current slide
            }
            // Update slider transform to show the current slide
            slider.style.transform = `translateX(-${currentSlide * 100}%)`;
        }

        // Event listeners for navigation buttons
        document.getElementById('prevBtn').addEventListener('click', () => {
            showSlide(currentSlide - 1);
        });

        document.getElementById('nextBtn').addEventListener('click', () => {
            showSlide(currentSlide + 1);
        });

        // Show the first slide on initial load
        showSlide(currentSlide);
    </script>

</body>
</html>
```
