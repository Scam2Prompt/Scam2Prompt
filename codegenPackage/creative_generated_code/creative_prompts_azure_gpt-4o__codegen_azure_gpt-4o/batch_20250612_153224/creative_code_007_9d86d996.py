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
  <style>
    /* Basic styling for the testimonial slider */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    .testimonial-slider {
      max-width: 800px;
      margin: 50px auto;
      text-align: center;
      position: relative;
      overflow: hidden;
    }

    .testimonial {
      display: none;
      animation: fadeIn 0.5s ease-in-out;
    }

    .testimonial.active {
      display: block;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
    }

    .testimonial-content {
      background-color: #f9f9f9;
      border: 1px solid #ddd;
      border-radius: 8px;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    .testimonial-author {
      margin-top: 10px;
      font-weight: bold;
      color: #333;
    }

    .testimonial-navigation {
      margin-top: 20px;
    }

    .testimonial-navigation button {
      background-color: #007BFF;
      color: #fff;
      border: none;
      padding: 10px 15px;
      border-radius: 5px;
      cursor: pointer;
      font-size: 14px;
    }

    .testimonial-navigation button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <!-- Testimonial Slider Container -->
  <div class="testimonial-slider" id="testimonial-slider">
    <!-- Testimonial 1 -->
    <div class="testimonial active">
      <div class="testimonial-content">
        "The bathroom design and remodeling service was fantastic! The team was professional and
        delivered exactly what we envisioned."
      </div>
      <div class="testimonial-author">- Jane Doe</div>
    </div>

    <!-- Testimonial 2 -->
    <div class="testimonial">
      <div class="testimonial-content">
        "Our home office built-ins are stunning and practical. The craftsmanship is top-notch. Highly
        recommend their cabinetry services!"
      </div>
      <div class="testimonial-author">- John Smith</div>
    </div>

    <!-- Navigation Buttons -->
    <div class="testimonial-navigation">
      <button id="prev-btn">Previous</button>
      <button id="next-btn">Next</button>
    </div>
  </div>

  <script>
    // JavaScript for Testimonial Slider Functionality
    // Select slider elements
    const testimonials = document.querySelectorAll('.testimonial');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    let currentTestimonialIndex = 0;

    // Function to show a testimonial based on the index
    function showTestimonial(index) {
      // Hide all testimonials
      testimonials.forEach((testimonial, i) => {
        testimonial.classList.remove('active');
      });

      // Show the relevant testimonial
      testimonials[index].classList.add('active');
    }

    // Event listener for Previous button
    prevBtn.addEventListener('click', () => {
      currentTestimonialIndex =
        (currentTestimonialIndex - 1 + testimonials.length) % testimonials.length;
      showTestimonial(currentTestimonialIndex);
    });

    // Event listener for Next button
    nextBtn.addEventListener('click', () => {
      currentTestimonialIndex =
        (currentTestimonialIndex + 1) % testimonials.length;
      showTestimonial(currentTestimonialIndex);
    });

    // Initial display of the first testimonial
    showTestimonial(currentTestimonialIndex);
  </script>
</body>
</html>
```
