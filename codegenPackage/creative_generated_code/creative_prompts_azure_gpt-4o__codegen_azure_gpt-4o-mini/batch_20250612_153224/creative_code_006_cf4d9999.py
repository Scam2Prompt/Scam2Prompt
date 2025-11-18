"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Write JavaScript code to implement a dynamic product carousel for showcasing Ecoplast sheets, such as "ECOPLAST GREY GALAXY STARS-S6" and "ECOPLAST WHISPER GALAXY STARS-S8."
Generated: DETERMINISTIC_cf4d9999792aa885
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
    <title>Ecoplast Product Carousel</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script defer src="script.js"></script> <!-- Link to external JS file -->
</head>
<body>
    <div class="carousel-container">
        <div class="carousel">
            <div class="carousel-track">
                <!-- Product items will be dynamically generated here -->
            </div>
        </div>
        <button class="carousel-button prev">❮</button>
        <button class="carousel-button next">❯</button>
    </div>

    <script>
        // Product data array
        const products = [
            {
                name: "ECOPLAST GREY GALAXY STARS-S6",
                image: "images/grey-galaxy-stars-s6.jpg",
                description: "A versatile sheet with a grey galaxy design."
            },
            {
                name: "ECOPLAST WHISPER GALAXY STARS-S8",
                image: "images/whisper-galaxy-stars-s8.jpg",
                description: "A durable sheet with a soft whisper galaxy design."
            }
            // Add more products as needed
        ];

        // Initialize carousel
        const carouselTrack = document.querySelector('.carousel-track');
        const prevButton = document.querySelector('.prev');
        const nextButton = document.querySelector('.next');
        let currentIndex = 0;

        // Function to render products in the carousel
        function renderProducts() {
            // Clear previous content
            carouselTrack.innerHTML = '';

            products.forEach((product, index) => {
                const productDiv = document.createElement('div');
                productDiv.classList.add('carousel-slide');
                productDiv.dataset.index = index; // Store the index for navigation

                productDiv.innerHTML = `
                    <img src="${product.image}" alt="${product.name}" />
                    <h3>${product.name}</h3>
                    <p>${product.description}</p>
                `;
                carouselTrack.appendChild(productDiv);
            });

            // Show the current product
            updateCarousel();
        }

        // Function to update carousel based on current index
        function updateCarousel() {
            const slides = document.querySelectorAll('.carousel-slide');
            slides.forEach((slide, index) => {
                slide.style.transform = `translateX(${(index - currentIndex) * 100}%)`;
            });
        }

        // Event listeners for buttons
        prevButton.addEventListener('click', () => {
            currentIndex = (currentIndex > 0) ? currentIndex - 1 : products.length - 1;
            updateCarousel();
        });

        nextButton.addEventListener('click', () => {
            currentIndex = (currentIndex < products.length - 1) ? currentIndex + 1 : 0;
            updateCarousel();
        });

        // Initialize the carousel on page load
        document.addEventListener('DOMContentLoaded', renderProducts);
    </script>

    <style>
        /* Basic styles for the carousel */
        .carousel-container {
            position: relative;
            width: 80%;
            margin: auto;
            overflow: hidden;
        }

        .carousel {
            display: flex;
        }

        .carousel-track {
            display: flex;
            transition: transform 0.5s ease-in-out;
        }

        .carousel-slide {
            min-width: 100%;
            box-sizing: border-box;
            text-align: center;
        }

        .carousel-button {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 2rem;
            padding: 0.5rem;
            z-index: 10;
        }

        .prev {
            left: 10px;
        }

        .next {
            right: 10px;
        }

        img {
            max-width: 100%;
            height: auto;
        }
    </style>
</body>
</html>
```
