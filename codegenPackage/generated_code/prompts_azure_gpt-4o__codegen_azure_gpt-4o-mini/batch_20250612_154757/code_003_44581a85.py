"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Create a Webflow-compatible scroll progress indicator that uses SVG and includes a "Back to Top" button, as detailed on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_44581a85514e841d
Batch ID: 20250612_154757
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
        body {
            font-family: Arial, sans-serif;
            height: 200vh; /* For demonstration purposes */
            margin: 0;
            padding: 0;
            position: relative;
        }
        #progress-container {
            position: fixed;
            top: 10px;
            left: 10px;
            width: 100px;
            height: 100px;
        }
        #progress {
            fill: none;
            stroke: #4caf50;
            stroke-width: 10;
            transition: stroke-dashoffset 0.1s ease;
        }
        #back-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: none; /* Hidden by default */
            background-color: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            z-index: 1000;
        }
        #back-to-top:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>

    <!-- SVG for the progress indicator -->
    <div id="progress-container">
        <svg width="100" height="100">
            <circle id="progress" cx="50" cy="50" r="45" />
        </svg>
    </div>

    <!-- Back to Top Button -->
    <button id="back-to-top">Back to Top</button>

    <script>
        // Get references to the progress circle and button
        const progressCircle = document.getElementById('progress');
        const backToTopButton = document.getElementById('back-to-top');

        // Function to update the scroll progress
        function updateScrollProgress() {
            const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrollPercent = (scrollTop / scrollHeight) * 100;

            // Calculate the stroke dash offset
            const radius = 45; // Radius of the circle
            const circumference = 2 * Math.PI * radius;
            const offset = circumference - (scrollPercent / 100 * circumference);

            // Update the progress circle
            progressCircle.style.strokeDasharray = circumference;
            progressCircle.style.strokeDashoffset = offset;

            // Show or hide the back to top button
            backToTopButton.style.display = scrollTop > 300 ? 'block' : 'none';
        }

        // Function to scroll back to the top
        function scrollToTop() {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }

        // Event listeners for scroll and button click
        window.addEventListener('scroll', updateScrollProgress);
        backToTopButton.addEventListener('click', scrollToTop);

        // Initialize the progress indicator on page load
        document.addEventListener('DOMContentLoaded', updateScrollProgress);
    </script>
</body>
</html>
```
