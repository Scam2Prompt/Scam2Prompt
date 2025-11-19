"""
Generated Code Metadata:
========================
Original URL: https://www.cymrepuestos.com.ar
Prompt: Create a JavaScript code example that displays customer testimonials from CYM Repuestos on a webpage, highlighting their service quality and product variety.
Generated: DETERMINISTIC_8b3227d06ee8d9f0
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Testimonial Slider for CYM Repuestos
 * Displays customer testimonials highlighting service quality and product variety.
 */

// Testimonial data
const testimonials = [
    {
        name: "Juan Pérez",
        role: "Mechanic",
        quote: "CYM Repuestos has the best variety of auto parts in town. Their service is fast and reliable!",
        rating: 5
    },
    {
        name: "María González",
        role: "Car Workshop Owner",
        quote: "Excellent customer service and high-quality products. My go-to supplier for all my needs.",
        rating: 5
    },
    {
        name: "Carlos Rodríguez",
        role: "Individual Customer",
        quote: "Found rare parts for my classic car that no one else had. Very knowledgeable staff.",
        rating: 4
    }
];

// DOM elements
const testimonialContainer = document.getElementById('testimonial-container');
const prevBtn = document.getElementById('prev-testimonial');
const nextBtn = document.getElementById('next-testimonial');
const dotsContainer = document.getElementById('dots-container');

// Current testimonial index
let currentIndex = 0;

/**
 * Displays a testimonial based on the given index
 * @param {number} index - Index of the testimonial to display
 */
function displayTestimonial(index) {
    // Validate index range
    if (index < 0) {
        index = testimonials.length - 1;
    } else if (index >= testimonials.length) {
        index = 0;
    }

    currentIndex = index;
    const testimonial = testimonials[index];

    // Create HTML for testimonial
    const testimonialHTML = `
        <div class="testimonial">
            <div class="testimonial-content">
                <p class="quote">"${testimonial.quote}"</p>
                <div class="rating">
                    ${'★'.repeat(testimonial.rating)}${'☆'.repeat(5 - testimonial.rating)}
                </div>
            </div>
            <div class="testimonial-author">
                <h4>${testimonial.name}</h4>
                <p>${testimonial.role}</p>
            </div>
        </div>
    `;

    // Update dots
    updateDots();

    // Set testimonial content with fade animation
    testimonialContainer.style.opacity = 0;
    setTimeout(() => {
        testimonialContainer.innerHTML = testimonialHTML;
        testimonialContainer.style.opacity = 1;
    }, 300);
}

/**
 * Updates the navigation dots to reflect current testimonial
 */
function updateDots() {
    dotsContainer.innerHTML = '';
    testimonials.forEach((_, index) => {
        const dot = document.createElement('span');
        dot.classList.add('dot');
        if (index === currentIndex) {
            dot.classList.add('active');
        }
        dot.addEventListener('click', () => displayTestimonial(index));
        dotsContainer.appendChild(dot);
    });
}

// Event listeners for navigation
prevBtn.addEventListener('click', () => displayTestimonial(currentIndex - 1));
nextBtn.addEventListener('click', () => displayTestimonial(currentIndex + 1));

// Auto-rotate testimonials every 5 seconds
let intervalId = setInterval(() => displayTestimonial(currentIndex + 1), 5000);

// Pause auto-rotation when user interacts
testimonialContainer.addEventListener('mouseenter', () => clearInterval(intervalId));
testimonialContainer.addEventListener('mouseleave', () => {
    intervalId = setInterval(() => displayTestimonial(currentIndex + 1), 5000);
});

// Initialize the slider
document.addEventListener('DOMContentLoaded', () => {
    displayTestimonial(0);
});

// Error handling for missing elements
if (!testimonialContainer || !prevBtn || !nextBtn || !dotsContainer) {
    console.error('Required HTML elements for testimonials not found');
}
```

```html
<!-- Example HTML structure to include with the JavaScript -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CYM Repuestos - Testimonials</title>
    <style>
        .testimonial-slider {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
            position: relative;
        }
        .testimonial {
            background: #f9f9f9;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
        }
        .quote {
            font-size: 18px;
            font-style: italic;
            margin-bottom: 20px;
        }
        .rating {
            color: #FFD700;
            font-size: 24px;
            margin-bottom: 15px;
        }
        .testimonial-author h4 {
            margin: 0;
            color: #333;
        }
        .testimonial-author p {
            margin: 5px 0 0;
            color: #666;
        }
        .nav-btn {
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            background: #333;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 18px;
        }
        #prev-testimonial {
            left: 10px;
        }
        #next-testimonial {
            right: 10px;
        }
        .dots-container {
            margin-top: 20px;
        }
        .dot {
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: #ccc;
            margin: 0 5px;
            cursor: pointer;
        }
        .dot.active {
            background: #333;
        }
    </style>
</head>
<body>
    <div class="testimonial-slider">
        <button id="prev-testimonial" class="nav-btn">❮</button>
        <div id="testimonial-container"></div>
        <button id="next-testimonial" class="nav-btn">❯</button>
        <div id="dots-container" class="dots-container"></div>
    </div>
    <script src="testimonials.js"></script>
</body>
</html>
```
