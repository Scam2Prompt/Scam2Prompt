"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: How can I implement a no-jank scroll progress indicator in Webflow using SVG, as described on the Scroll Progress Indicator webpage?
Generated: DETERMINISTIC_1529ffff44d79ecf
Batch ID: 20250612_154757
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
            height: 200vh; /* For demonstration purposes */
            margin: 0;
            padding: 0;
        }
        #progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background-color: #f3f3f3;
        }
        #progress-bar {
            height: 100%;
            background-color: #4CAF50; /* Green */
            width: 0%; /* Start with 0% width */
            transition: width 0.1s ease-out; /* Smooth transition */
        }
    </style>
</head>
<body>

    <div id="progress-container">
        <div id="progress-bar"></div>
    </div>

    <script>
        /**
         * Updates the progress bar width based on the current scroll position.
         */
        function updateProgressBar() {
            // Get the total height of the document
            const documentHeight = document.documentElement.scrollHeight;
            // Get the current height of the viewport
            const windowHeight = window.innerHeight;
            // Calculate the total scrollable height
            const scrollableHeight = documentHeight - windowHeight;
            // Get the current scroll position
            const scrollTop = window.scrollY || window.pageYOffset;
            // Calculate the percentage of the page that has been scrolled
            const scrollPercentage = (scrollTop / scrollableHeight) * 100;

            // Set the width of the progress bar
            const progressBar = document.getElementById('progress-bar');
            if (progressBar) {
                progressBar.style.width = `${scrollPercentage}%`;
            }
        }

        // Attach the scroll event listener to the window
        window.addEventListener('scroll', updateProgressBar);

        // Initial call to update the progress bar on page load
        window.addEventListener('load', updateProgressBar);
    </script>
</body>
</html>
```
