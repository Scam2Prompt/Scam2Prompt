"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://topgraininteriors.com
Prompt: Write code to implement a testimonial slider for a custom cabinetry website, showcasing customer reviews about services like "Bathroom Design & Remodeling" and "Home Office Built-ins."
Generated: DETERMINISTIC_9d86d996827dcf76
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
            <p>"The bathroom design and remodeling exceeded my expectations! The team was professional and attentive."</p>
            <p class="customer-name">- Sarah J.</p>
        </div>
        <div class="testimonial" id="testimonial-2">
            <p>"My home office built-ins are both functional and beautiful! Highly recommend their services."</p>
            <p class="customer-name">- Mark L.</p>
        </div>
        <div class="testimonial" id="testimonial-3">
            <p>"Excellent craftsmanship and customer service during our cabinetry project. Will definitely hire again!"</p>
            <p class="customer-name">- Emily R.</p>
        </div>
        <button class="prev" onclick="changeTestimonial(-1)">&#10094;</button>
        <button class="next" onclick="changeTestimonial(1)">&#10095;</button>
    </div>

    <script>
        // Current testimonial index
        let currentIndex = 0;

        // Function to change the testimonial displayed
        function changeTestimonial(direction) {
            const testimonials = document.querySelectorAll('.testimonial');
            const totalTestimonials = testimonials.length;

            // Hide the current testimonial
            testimonials[currentIndex].style.display = 'none';

            // Update the index based on the direction
            currentIndex = (currentIndex + direction + totalTestimonials) % totalTestimonials;

            // Show the new current testimonial
            testimonials[currentIndex].style.display = 'block';
        }

        // Initialize the slider by displaying the first testimonial
        function initSlider() {
            const testimonials = document.querySelectorAll('.testimonial');
            // Hide all testimonials except the first one
            testimonials.forEach((testimonial, index) => {
                testimonial.style.display = index === 0 ? 'block' : 'none';
            });
        }

        // Run the initialization function on page load
        window.onload = initSlider;
    </script>

    <style>
        /* Basic styles for the testimonial slider */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
        }

        .testimonial-slider {
            width: 60%;
            margin: 50px auto;
            border: 1px solid #ccc;
            border-radius: 10px;
            overflow: hidden;
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: relative;
            padding: 20px;
        }

        .testimonial {
            display: none; /* Hidden by default */
        }

        .customer-name {
            font-weight: bold;
            text-align: right;
        }

        button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
        }

        .prev {
            left: 10px;
        }

        .next {
            right: 10px;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</body>

</html>
```
