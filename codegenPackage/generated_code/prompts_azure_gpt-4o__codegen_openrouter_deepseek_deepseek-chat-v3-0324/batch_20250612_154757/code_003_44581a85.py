"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Create a Webflow-compatible scroll progress indicator that uses SVG and includes a "Back to Top" button, as detailed on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_44581a85514e841d
Batch ID: 20250612_154757
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            line-height: 1.6;
            color: #333;
            min-height: 200vh; /* For demonstration */
        }

        /* Scroll progress container */
        .scroll-progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background-color: #f0f0f0;
            z-index: 1000;
        }

        /* Scroll progress bar */
        .scroll-progress-bar {
            height: 100%;
            background-color: #4a6cf7;
            width: 0%;
            transition: width 0.1s ease-out;
        }

        /* Back to top button */
        .back-to-top {
            position: fixed;
            bottom: 30px;
            right: 30px;
            width: 50px;
            height: 50px;
            background-color: #4a6cf7;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
            z-index: 999;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .back-to-top.visible {
            opacity: 1;
            visibility: visible;
        }

        .back-to-top svg {
            width: 20px;
            height: 20px;
            fill: white;
        }

        /* Content styles for demo */
        .content {
            max-width: 800px;
            margin: 0 auto;
            padding: 80px 20px;
        }

        h1, h2 {
            margin-bottom: 20px;
        }

        p {
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <!-- Scroll Progress Indicator -->
    <div class="scroll-progress-container">
        <div class="scroll-progress-bar"></div>
    </div>

    <!-- Back to Top Button -->
    <div class="back-to-top" id="backToTop">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M12 4l-8 8h5v8h6v-8h5z"/>
        </svg>
    </div>

    <!-- Demo Content -->
    <div class="content">
        <h1>Scroll Progress Indicator</h1>
        <p>Scroll down to see the progress indicator and the "Back to Top" button.</p>
        
        <h2>Section 1</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.</p>
        
        <h2>Section 2</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.</p>
        
        <h2>Section 3</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.</p>
        
        <h2>Section 4</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam in dui mauris. Vivamus hendrerit arcu sed erat molestie vehicula. Sed auctor neque eu tellus rhoncus ut eleifend nibh porttitor.</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Get DOM elements
            const progressBar = document.querySelector('.scroll-progress-bar');
            const backToTopButton = document.getElementById('backToTop');
            
            // Check if elements exist
            if (!progressBar || !backToTopButton) {
                console.error('Required elements not found in the DOM');
                return;
            }

            // Calculate scroll progress
            function updateScrollProgress() {
                try {
                    const scrollPosition = window.scrollY;
                    const windowHeight = window.innerHeight;
                    const documentHeight = document.documentElement.scrollHeight;
                    
                    // Calculate scroll percentage
                    const scrollPercentage = (scrollPosition / (documentHeight - windowHeight)) * 100;
                    
                    // Update progress bar width
                    progressBar.style.width = scrollPercentage + '%';
                    
                    // Show/hide back to top button
                    if (scrollPercentage > 20) {
                        backToTopButton.classList.add('visible');
                    } else {
                        backToTopButton.classList.remove('visible');
                    }
                } catch (error) {
                    console.error('Error updating scroll progress:', error);
                }
            }

            // Scroll to top function
            function scrollToTop() {
                try {
                    window.scrollTo({
                        top: 0,
                        behavior: 'smooth'
                    });
                } catch (error) {
                    console.error('Error scrolling to top:', error);
                    // Fallback for browsers that don't support smooth scrolling
                    window.scrollTo(0, 0);
                }
            }

            // Event listeners
            window.addEventListener('scroll', updateScrollProgress);
            backToTopButton.addEventListener('click', scrollToTop);

            // Initialize scroll progress
            updateScrollProgress();
        });
    </script>
</body>
</html>
```
