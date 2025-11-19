"""
Generated Code Metadata:
========================
Original URL: https://topgraininteriors.com
Prompt: Write code to implement a testimonial slider for a custom cabinetry website, showcasing customer reviews about services like "Bathroom Design & Remodeling" and "Home Office Built-ins."
Generated: DETERMINISTIC_9d86d996827dcf76
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Cabinetry Testimonials</title>
    <style>
        /* Base styles */
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }

        .testimonial-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 40px 20px;
            text-align: center;
        }

        .testimonial-title {
            font-size: 2.5rem;
            margin-bottom: 40px;
            color: #2c3e50;
        }

        .testimonial-slider {
            position: relative;
            overflow: hidden;
            padding: 20px 0;
        }

        .testimonial-slide {
            display: none;
            padding: 30px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
            max-width: 800px;
            margin: 0 auto;
        }

        .testimonial-slide.active {
            display: block;
            animation: fadeIn 0.5s ease;
        }

        .testimonial-content {
            font-size: 1.1rem;
            font-style: italic;
            margin-bottom: 20px;
            color: #555;
        }

        .testimonial-author {
            font-weight: bold;
            font-size: 1.2rem;
            color: #2c3e50;
        }

        .testimonial-service {
            display: block;
            font-size: 0.9rem;
            color: #7f8c8d;
            margin-top: 5px;
        }

        .slider-nav {
            margin-top: 30px;
        }

        .slider-dots {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 0;
        }

        .slider-dots li {
            margin: 0 5px;
        }

        .slider-dots button {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            border: none;
            background: #bdc3c7;
            cursor: pointer;
            padding: 0;
            text-indent: -9999px;
            transition: background 0.3s ease;
        }

        .slider-dots button.active {
            background: #2c3e50;
        }

        .slider-arrows {
            display: flex;
            justify-content: center;
            margin-top: 20px;
        }

        .slider-arrow {
            background: none;
            border: none;
            font-size: 2rem;
            cursor: pointer;
            color: #2c3e50;
            margin: 0 15px;
            transition: color 0.3s ease;
        }

        .slider-arrow:hover {
            color: #3498db;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Responsive styles */
        @media (max-width: 768px) {
            .testimonial-title {
                font-size: 2rem;
            }

            .testimonial-content {
                font-size: 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="testimonial-container">
        <h2 class="testimonial-title">Customer Testimonials</h2>
        
        <div class="testimonial-slider">
            <!-- Slide 1 -->
            <div class="testimonial-slide active">
                <p class="testimonial-content">
                    "The team transformed our outdated bathroom into a luxurious spa-like retreat. Their attention to detail and craftsmanship is unmatched."
                </p>
                <span class="testimonial-author">Sarah Johnson</span>
                <span class="testimonial-service">Bathroom Design & Remodeling</span>
            </div>
            
            <!-- Slide 2 -->
            <div class="testimonial-slide">
                <p class="testimonial-content">
                    "Our home office built-ins are not only beautiful but incredibly functional. They maximized our space while maintaining a clean, modern look."
                </p>
                <span class="testimonial-author">Michael Chen</span>
                <span class="testimonial-service">Home Office Built-ins</span>
            </div>
            
            <!-- Slide 3 -->
            <div class="testimonial-slide">
                <p class="testimonial-content">
                    "From design to installation, the process was seamless. The custom cabinetry in our kitchen has completely changed how we use the space."
                </p>
                <span class="testimonial-author">Emily Rodriguez</span>
                <span class="testimonial-service">Kitchen Cabinetry</span>
            </div>
        </div>
        
        <div class="slider-nav">
            <ul class="slider-dots">
                <li><button class="active" data-index="0">1</button></li>
                <li><button data-index="1">2</button></li>
                <li><button data-index="2">3</button></li>
            </ul>
            
            <div class="slider-arrows">
                <button class="slider-arrow prev">&#10094;</button>
                <button class="slider-arrow next">&#10095;</button>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const slides = document.querySelectorAll('.testimonial-slide');
            const dots = document.querySelectorAll('.slider-dots button');
            const prevBtn = document.querySelector('.prev');
            const nextBtn = document.querySelector('.next');
            let currentIndex = 0;
            let slideInterval;
            const slideDuration = 5000; // 5 seconds
            
            // Initialize slider
            function initSlider() {
                if (slides.length === 0) {
                    console.error('No slides found');
                    return;
                }
                
                showSlide(currentIndex);
                startSlideShow();
                
                // Event listeners
                prevBtn.addEventListener('click', prevSlide);
                nextBtn.addEventListener('click', nextSlide);
                
                dots.forEach(dot => {
                    dot.addEventListener('click', function() {
                        const index = parseInt(this.getAttribute('data-index'));
                        goToSlide(index);
                    });
                });
            }
            
            // Show slide at given index
            function showSlide(index) {
                if (index < 0 || index >= slides.length) {
                    console.error('Invalid slide index');
                    return;
                }
                
                // Hide all slides
                slides.forEach(slide => {
                    slide.classList.remove('active');
                });
                
                // Remove active class from all dots
                dots.forEach(dot => {
                    dot.classList.remove('active');
                });
                
                // Show current slide and activate corresponding dot
                slides[index].classList.add('active');
                dots[index].classList.add('active');
                currentIndex = index;
            }
            
            // Go to next slide
            function nextSlide() {
                resetSlideShow();
                const newIndex = (currentIndex + 1) % slides.length;
                showSlide(newIndex);
            }
            
            // Go to previous slide
            function prevSlide() {
                resetSlideShow();
                const newIndex = (currentIndex - 1 + slides.length) % slides.length;
                showSlide(newIndex);
            }
            
            // Go to specific slide
            function goToSlide(index) {
                resetSlideShow();
                showSlide(index);
            }
            
            // Start automatic slideshow
            function startSlideShow() {
                slideInterval = setInterval(nextSlide, slideDuration);
            }
            
            // Reset slideshow timer
            function resetSlideShow() {
                clearInterval(slideInterval);
                startSlideShow();
            }
            
            // Initialize the slider
            initSlider();
            
            // Pause on hover
            const slider = document.querySelector('.testimonial-slider');
            if (slider) {
                slider.addEventListener('mouseenter', () => {
                    clearInterval(slideInterval);
                });
                
                slider.addEventListener('mouseleave', () => {
                    startSlideShow();
                });
            }
        });
    </script>
</body>
</html>
```
