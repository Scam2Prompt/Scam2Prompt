"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibanshee.com
Prompt: Write code to implement a "Fullscreen Slider" feature using CSS and JavaScript, referencing the design principles highlighted on the IMST Telehealth webpage.
Generated: DETERMINISTIC_15afd6dbaed2b3b2
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
    <title>Fullscreen Slider</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic styles for the slider */
        body, html {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden;
        }

        .slider {
            display: flex;
            height: 100vh; /* Full height */
            width: 100vw;  /* Full width */
            transition: transform 0.5s ease-in-out; /* Smooth transition */
        }

        .slide {
            min-width: 100%; /* Each slide takes full width */
            height: 100%;
            background-size: cover;
            background-position: center;
        }

        .controls {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            display: flex;
            gap: 15px;
        }

        .button {
            padding: 10px 20px;
            background-color: rgba(255, 255, 255, 0.8);
            border: none;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }

        .button:hover {
            background-color: rgba(255, 255, 255, 1);
        }
    </style>
</head>
<body>

    <div class="slider" id="slider">
        <div class="slide" style="background-image: url('image1.jpg');"></div>
        <div class="slide" style="background-image: url('image2.jpg');"></div>
        <div class="slide" style="background-image: url('image3.jpg');"></div>
    </div>

    <div class="controls">
        <button class="button" id="prevButton">Previous</button>
        <button class="button" id="nextButton">Next</button>
    </div>

    <script>
        // Initialize variables for the slider
        const slider = document.getElementById('slider');
        const slides = document.querySelectorAll('.slide');
        let currentIndex = 0; // Current slide index

        // Function to show the current slide
        function showSlide(index) {
            // Validate index and handle looping
            if (index < 0) {
                currentIndex = slides.length - 1; // Loop to last slide
            } else if (index >= slides.length) {
                currentIndex = 0; // Loop to first slide
            } else {
                currentIndex = index;
            }
            // Update the slider's transform property
            slider.style.transform = `translateX(-${currentIndex * 100}%)`;
        }

        // Event listener for the Previous button
        document.getElementById('prevButton').addEventListener('click', () => {
            showSlide(currentIndex - 1);
        });

        // Event listener for the Next button
        document.getElementById('nextButton').addEventListener('click', () => {
            showSlide(currentIndex + 1);
        });

        // Initial load
        showSlide(currentIndex);

        // Optional: Auto-slide functionality
        setInterval(() => {
            showSlide(currentIndex + 1);
        }, 5000); // Change slide every 5 seconds

    </script>
</body>
</html>
```
