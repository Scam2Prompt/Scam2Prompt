"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Design a Webflow scroll progress indicator that displays 100% completion with an SVG and a "Back to Top" button.
Generated: DETERMINISTIC_135f954b802c8dd7
Batch ID: 20250622_212208
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
    <title>Scroll Progress Indicator</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            min-height: 200vh; /* For demonstration */
        }

        /* Progress indicator container */
        .progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: #f0f0f0;
            z-index: 1000;
        }

        /* Progress bar */
        .progress-bar {
            height: 100%;
            background: linear-gradient(90deg, #ff5e62, #ff9966);
            width: 0%;
            transition: width 0.1s ease;
        }

        /* Back to top button */
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, #ff5e62, #ff9966);
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            z-index: 999;
        }

        .back-to-top.show {
            opacity: 1;
            visibility: visible;
        }

        .back-to-top svg {
            width: 24px;
            height: 24px;
            fill: white;
        }

        /* Content for demonstration */
        .content {
            padding: 50px;
            max-width: 800px;
            margin: 0 auto;
        }

        .content h1 {
            margin-bottom: 20px;
        }

        .content p {
            margin-bottom: 20px;
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <!-- Progress indicator -->
    <div class="progress-container">
        <div class="progress-bar" id="progressBar"></div>
    </div>

    <!-- Back to top button -->
    <div class="back-to-top" id="backToTop">
        <svg viewBox="0 0 24 24">
            <path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"/>
        </svg>
    </div>

    <!-- Demo content -->
    <div class="content">
        <h1>Scroll Progress Indicator</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio.</p>
        <p>Proin at quam et erat tempor pellentesque. Praesent consequat velit in nisl blandit ultrices. Vivamus sed leo eu metus scelerisque vehicula. Sed quis tortor purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras pharetra, quam et pretium volutpat, eros ipsum rhoncus sem, in malesuada elit libero quis mi. Donec interdum, nisl in tincidunt congue, nibh leo ultrices metus, vitae aliquet nibh metus sed magna.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio.</p>
        <p>Proin at quam et erat tempor pellentesque. Praesent consequat velit in nisl blandit ultrices. Vivamus sed leo eu metus scelerisque vehicula. Sed quis tortor purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras pharetra, quam et pretium volutpat, eros ipsum rhoncus sem, in malesuada elit libero quis mi. Donec interdum, nisl in tincidunt congue, nibh leo ultrices metus, vitae aliquet nibh metus sed magna.</p>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor. Ut in nulla enim. Phasellus molestie magna non est bibendum non venenatis nisl tempor. Suspendisse dictum feugiat nisl ut dapibus. Mauris iaculis porttitor posuere. Praesent id metus massa, ut blandit odio.</p>
        <p>Proin at quam et erat tempor pellentesque. Praesent consequat velit in nisl blandit ultrices. Vivamus sed leo eu metus scelerisque vehicula. Sed quis tortor purus. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Cras pharetra, quam et pretium volutpat, eros ipsum rhoncus sem, in malesuada elit libero quis mi. Donec interdum, nisl in tincidunt congue, nibh leo ultrices metus, vitae aliquet nibh metus sed magna.</p>
    </div>

    <script>
        // Wait for DOM to be fully loaded
        document.addEventListener('DOMContentLoaded', function() {
            const progressBar = document.getElementById('progressBar');
            const backToTopButton = document.getElementById('backToTop');

            // Update progress bar on scroll
            window.addEventListener('scroll', function() {
                const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
                const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                const scrollProgress = (scrollTop / scrollHeight) * 100;
                
                // Update progress bar width
                progressBar.style.width = scrollProgress + '%';

                // Show/hide back to top button
                if (scrollProgress > 20) {
                    backToTopButton.classList.add('show');
                } else {
                    backToTopButton.classList.remove('show');
                }
            });

            // Smooth scroll to top when button is clicked
            backToTopButton.addEventListener('click', function() {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });
        });
    </script>
</body>
</html>
```
