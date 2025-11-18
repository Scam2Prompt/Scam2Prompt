"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metaforce360.com
Prompt: Write code to implement a testimonial slider for a website, using the structure of client reviews showcased on Meta Force 360’s webpage.
Generated: DETERMINISTIC_d173c0dc700e697d
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
    <title>Testimonial Slider</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="testimonial-slider">
        <div class="testimonial" id="testimonial-1">
            <p class="review">"Meta Force 360 has transformed our business!"</p>
            <h3 class="client-name">John Doe</h3>
            <p class="client-role">CEO, Company A</p>
        </div>
        <div class="testimonial" id="testimonial-2">
            <p class="review">"Fantastic service and support!"</p>
            <h3 class="client-name">Jane Smith</h3>
            <p class="client-role">Marketing Director, Company B</p>
        </div>
        <div class="testimonial" id="testimonial-3">
            <p class="review">"Highly recommend Meta Force 360!"</p>
            <h3 class="client-name">Emily Johnson</h3>
            <p class="client-role">Operations Manager, Company C</p>
        </div>
        <button id="prev" class="nav-button">Previous</button>
        <button id="next" class="nav-button">Next</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
}

.testimonial-slider {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    text-align: center;
}

.testimonial {
    display: none; /* Hide testimonials by default */
}

.testimonial.active {
    display: block; /* Show the active testimonial */
}

.nav-button {
    background-color: #007bff;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    margin: 10px;
}

.nav-button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js
// JavaScript for handling the testimonial slider functionality

document.addEventListener('DOMContentLoaded', () => {
    // Select all testimonials and navigation buttons
    const testimonials = document.querySelectorAll('.testimonial');
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');

    let currentIndex = 0;

    // Function to show the current testimonial
    function showTestimonial(index) {
        // Hide all testimonials
        testimonials.forEach(testimonial => testimonial.classList.remove('active'));
        
        // Show the current testimonial
        testimonials[index].classList.add('active');
    }

    // Function to handle showing the next testimonial
    function showNextTestimonial() {
        currentIndex = (currentIndex + 1) % testimonials.length;
        showTestimonial(currentIndex);
    }

    // Function to handle showing the previous testimonial
    function showPrevTestimonial() {
        currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length;
        showTestimonial(currentIndex);
    }

    // Event listeners for navigation buttons
    nextButton.addEventListener('click', showNextTestimonial);
    prevButton.addEventListener('click', showPrevTestimonial);

    // Initialize the slider by showing the first testimonial
    showTestimonial(currentIndex);
});
```

This implementation creates a basic testimonial slider with HTML, CSS, and JavaScript. Each testimonial is shown one at a time, and users can navigate through them using "Previous" and "Next" buttons. The code is structured to be clean, efficient, and easily extendable for future enhancements.
