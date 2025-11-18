"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://naikreatif.com
Prompt: Write JavaScript code to implement a carousel showcasing project highlights, such as those featured by Naikreatif for their clients.
Generated: DETERMINISTIC_141beb1ffc836690
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
    <title>Project Highlights Carousel</title>
    <link rel="stylesheet" href="styles.css"> <!-- Assuming a separate CSS file -->
    <script defer src="carousel.js"></script> <!-- External JavaScript file -->
    <style>
        /* Basic styles for the carousel */
        .carousel {
            position: relative;
            width: 80%;
            margin: auto;
            overflow: hidden;
            border: 2px solid #ddd;
            border-radius: 10px;
        }
        .carousel-inner {
            display: flex;
            transition: transform 0.5s ease;
        }
        .carousel-item {
            min-width: 100%;
            box-sizing: border-box;
        }
        .carousel img {
            width: 100%;
            border-radius: 10px;
        }
        .carousel-control {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            cursor: pointer;
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            border-radius: 5px;
            padding: 10px;
        }
        .carousel-control.prev {
            left: 10px;
        }
        .carousel-control.next {
            right: 10px;
        }
        .carousel-indicators {
            text-align: center;
            margin-top: 10px;
        }
        .carousel-indicators button {
            background-color: #ddd;
            border: none;
            border-radius: 50%;
            width: 10px;
            height: 10px;
            margin: 0 5px;
            cursor: pointer;
        }
        .carousel-indicators button.active {
            background-color: #333;
        }
    </style>
</head>
<body>

<div class="carousel" id="projectCarousel">
    <div class="carousel-inner">
        <div class="carousel-item active">
            <img src="project1.jpg" alt="Project 1">
            <p>Project Highlight 1: Description of project 1.</p>
        </div>
        <div class="carousel-item">
            <img src="project2.jpg" alt="Project 2">
            <p>Project Highlight 2: Description of project 2.</p>
        </div>
        <div class="carousel-item">
            <img src="project3.jpg" alt="Project 3">
            <p>Project Highlight 3: Description of project 3.</p>
        </div>
        <!-- Additional project items can be added here -->
    </div>
    <button class="carousel-control prev" id="prevBtn">&#10094;</button>
    <button class="carousel-control next" id="nextBtn">&#10095;</button>
</div>

<div class="carousel-indicators" id="indicators"></div>

<script>
    // Carousel functionality
    document.addEventListener('DOMContentLoaded', () => {
        const carousel = document.getElementById('projectCarousel');
        const carouselInner = carousel.querySelector('.carousel-inner');
        const items = carouselInner.querySelectorAll('.carousel-item');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        const indicatorsContainer = document.getElementById('indicators');
        
        let currentIndex = 0;

        // Function to update carousel display 
        const updateCarousel = () => {
            // Reset the transform property to show the current item
            const offset = -currentIndex * 100;
            carouselInner.style.transform = `translateX(${offset}%)`;
            updateIndicators();
        };

        // Function to create carousel indicators
        const updateIndicators = () => {
            indicatorsContainer.innerHTML = '';
            items.forEach((item, index) => {
                const button = document.createElement('button');
                button.className = index === currentIndex ? 'active' : '';
                button.addEventListener('click', () => {
                    currentIndex = index;
                    updateCarousel();
                });
                indicatorsContainer.appendChild(button);
            });
        };

        // Event listener for previous button
        prevBtn.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : items.length - 1;
            updateCarousel();
        });

        // Event listener for next button
        nextBtn.addEventListener('click', () => {
            currentIndex = (currentIndex < items.length - 1) ? currentIndex + 1 : 0;
            updateCarousel();
        });

        // Initialize carousel on page load
        updateCarousel();
    });
</script>

</body>
</html>
```
