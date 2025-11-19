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
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 200vh; /* For demonstration purposes */
            background: linear-gradient(to bottom, #f0f0f0, #ccc);
        }
        #progress-container {
            position: fixed;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            max-width: 600px;
            text-align: center;
            z-index: 1000;
        }
        #progress-svg {
            width: 100%;
            height: 50px;
        }
        #back-to-top {
            display: none;
            margin-top: 10px;
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #back-to-top:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

    <div id="progress-container">
        <svg id="progress-svg" viewBox="0 0 100 10">
            <rect id="progress-bar" width="0" height="10" fill="#007BFF"></rect>
        </svg>
        <button id="back-to-top">Back to Top</button>
    </div>

    <script>
        // Function to update the scroll progress
        function updateScrollProgress() {
            const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
            const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrollPercent = (scrollTop / scrollHeight) * 100;

            // Update the width of the progress bar
            const progressBar = document.getElementById('progress-bar');
            progressBar.setAttribute('width', scrollPercent);

            // Show or hide the "Back to Top" button based on scroll position
            const backToTopButton = document.getElementById('back-to-top');
            if (scrollPercent > 0) {
                backToTopButton.style.display = 'block';
            } else {
                backToTopButton.style.display = 'none';
            }
        }

        // Function to scroll back to the top smoothly
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Event listeners for scroll and button click
        window.addEventListener('scroll', updateScrollProgress);
        document.getElementById('back-to-top').addEventListener('click', scrollToTop);

        // Initial call to set the progress bar on page load
        updateScrollProgress();
    </script>
</body>
</html>
```
