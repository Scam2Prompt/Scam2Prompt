"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code for a scroll progress indicator that works seamlessly in Webflow without jank.
Generated: DETERMINISTIC_7131b7049ec0c224
Batch ID: 20250612_161125
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
    <title>Scroll Progress Indicator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            height: 200vh; /* Extend height for scroll */
        }

        #progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: #e0e0e0;
            z-index: 1000;
        }

        #progress-bar {
            height: 100%;
            background: #3b82f6; /* Blue color */
            width: 0%; /* Initial width */
            transition: width 0.2s ease; /* Smooth transition */
        }
    </style>
</head>
<body>

    <!-- Progress Indicator Container -->
    <div id="progress-container">
        <div id="progress-bar"></div>
    </div>

    <script>
        // Function to update the scroll progress
        function updateScrollProgress() {
            // Get the total height of the document
            const scrollableHeight = document.body.scrollHeight - window.innerHeight;
            // Get the current scroll position
            const scrollPosition = window.scrollY;

            // Calculate the scroll percentage
            const scrollPercentage = (scrollPosition / scrollableHeight) * 100;

            // Update the width of the progress bar
            document.getElementById('progress-bar').style.width = scrollPercentage + '%';
        }

        // Event listener for scroll event
        window.addEventListener('scroll', updateScrollProgress);

        // Error handling: Check if scroll event is supported
        if (!('scroll' in window)) {
            console.error('Scroll event is not supported in this browser.');
        }

        // Initialize progress bar on page load
        window.onload = () => {
            updateScrollProgress(); // Set initial value
        };
    </script>

</body>
</html>
```
