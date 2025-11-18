"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mystrikingly.com
Prompt: Create a simple HTML template for showcasing a gallery with media sliders, tailored for Strikingly's editor.
Generated: DETERMINISTIC_8f8efe5247c6153e
Batch ID: 20250612_154752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery Slider</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <style>
        /* Basic reset for the gallery */
        body, h1, h2, h3, p {
            margin: 0;
            padding: 0;
        }

        /* Gallery container */
        .gallery-container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }

        /* Slider styles */
        .slider {
            position: relative;
            overflow: hidden;
            border: 2px solid #ccc;
            border-radius: 10px;
        }

        .slides {
            display: flex;
            transition: transform 0.5s ease;
        }

        .slide {
            min-width: 100%;
            box-sizing: border-box;
            display: none; /* Hide all slides initially */
        }

        .active {
            display: block; /* Display only the active slide */
        }

        /* Navigation buttons */
        .nav-button {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            cursor: pointer;
            padding: 10px;
            border-radius: 50%;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            z-index: 10;
        }

        .prev {
            left: 10px;
        }

        .next {
            right: 10px;
        }

        /* Caption styles */
        .caption {
            margin-top: 10px;
            font-size: 1.2em;
            color: #333;
        }
    </style>
</head>
<body>

    <div class="gallery-container">
        <h1>Gallery Slider</h1>
        <div class="slider">
            <div class="slides">
                <div class="slide active">
                    <img src="image1.jpg" alt="Image 1" style="width: 100%;">
                    <div class="caption">Caption for Image 1</div>
                </div>
                <div class="slide">
                    <img src="image2.jpg" alt="Image 2" style="width: 100%;">
                    <div class="caption">Caption for Image 2</div>
                </div>
                <div class="slide">
                    <img src="image3.jpg" alt="Image 3" style="width: 100%;">
                    <div class="caption">Caption for Image 3</div>
                </div>
            </div>
            <button class="nav-button prev" onclick="changeSlide(-1)"><i class="fas fa-chevron-left"></i></button>
            <button class="nav-button next" onclick="changeSlide(1)"><i class="fas fa-chevron-right"></i></button>
        </div>
    </div>

    <script>
        let currentSlide = 0;

        // Function to change slides
        function changeSlide(direction) {
            const slides = document.querySelectorAll('.slide');
            slides[currentSlide].classList.remove('active'); // Hide current slide

            // Update current slide index
            currentSlide = (currentSlide + direction + slides.length) % slides.length;

            slides[currentSlide].classList.add('active'); // Show new slide
        }

        // Automatic slide change every 5 seconds
        setInterval(() => {
            changeSlide(1);
        }, 5000);
    </script>

</body>
</html>
```
