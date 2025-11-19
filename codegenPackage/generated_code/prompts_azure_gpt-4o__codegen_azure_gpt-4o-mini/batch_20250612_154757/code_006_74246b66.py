"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write a Webflow-specific tutorial for adding a radial scroll progress indicator with dynamic updates and "Back to Top" functionality, as featured on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_74246b66e5627c7f
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
    <title>Radial Scroll Progress Indicator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 200vh; /* For demonstration, make the page tall */
            background: linear-gradient(to bottom, #f0f0f0, #ccc);
        }

        #progress-container {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            background: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        #progress {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: conic-gradient(#4caf50 0%, #4caf50 var(--progress), #e0e0e0 var(--progress), #e0e0e0 100%);
            transition: background 0.3s ease;
        }

        #back-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: none; /* Hidden by default */
            padding: 10px 15px;
            background: #4caf50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
        }

        #back-to-top:hover {
            background: #45a049;
        }
    </style>
</head>
<body>

    <div id="progress-container">
        <div id="progress"></div>
    </div>
    <button id="back-to-top">Back to Top</button>

    <script>
        // Function to update the radial progress indicator based on scroll position
        function updateScrollProgress() {
            const scrollTop = window.scrollY; // Current scroll position
            const documentHeight = document.documentElement.scrollHeight; // Total height of the document
            const windowHeight = window.innerHeight; // Height of the viewport
            const scrollableHeight = documentHeight - windowHeight; // Total scrollable height

            // Calculate the scroll percentage
            const scrollPercentage = (scrollTop / scrollableHeight) * 100;

            // Update the CSS variable for the conic gradient
            document.getElementById('progress').style.setProperty('--progress', `${scrollPercentage}deg`);

            // Show or hide the "Back to Top" button based on scroll position
            const backToTopButton = document.getElementById('back-to-top');
            if (scrollTop > 200) {
                backToTopButton.style.display = 'block'; // Show button
            } else {
                backToTopButton.style.display = 'none'; // Hide button
            }
        }

        // Function to scroll back to the top of the page
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Smooth scroll effect
            });
        }

        // Event listeners for scroll and button click
        window.addEventListener('scroll', updateScrollProgress);
        document.getElementById('back-to-top').addEventListener('click', scrollToTop);

        // Initial call to set progress on page load
        updateScrollProgress();
    </script>
</body>
</html>
```
