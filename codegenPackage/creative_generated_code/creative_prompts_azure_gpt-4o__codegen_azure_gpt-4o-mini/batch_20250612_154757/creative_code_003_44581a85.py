"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Create a Webflow-compatible scroll progress indicator that uses SVG and includes a "Back to Top" button, as detailed on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_44581a85514e841d
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
            height: 200vh; /* Make the body tall for scrolling */
            margin: 0;
            padding: 0;
            background: linear-gradient(white, lightgray);
        }

        #scroll-progress {
            position: fixed;
            top: 0;
            left: 0;
            height: 5px;
            background: #4caf50; /* Progress bar color */
            z-index: 9999;
            width: 0%; /* Start at 0% width */
            transition: width 0.1s ease-in-out;
        }

        #back-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: none; /* Hidden by default */
            background: #007BFF; /* Button color */
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            z-index: 9999;
        }

        #back-to-top:hover {
            background: #0056b3; /* Darker on hover */
        }
    </style>
</head>
<body>

<div id="scroll-progress"></div>
<button id="back-to-top">Back to Top</button>

<script>
    // Function to update the scroll progress bar
    function updateScrollProgress() {
        const scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
        const docHeight = document.documentElement.scrollHeight - window.innerHeight;
        const scrollPercent = (scrollTop / docHeight) * 100;

        // Update the width of the scroll progress bar
        document.getElementById('scroll-progress').style.width = scrollPercent + '%';

        // Show or hide the Back to Top button based on scroll position
        const backToTopButton = document.getElementById('back-to-top');
        if (scrollTop > 300) {
            backToTopButton.style.display = 'block'; // Show button
        } else {
            backToTopButton.style.display = 'none'; // Hide button
        }
    }

    // Function to scroll back to the top of the page
    function scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth' // Smooth scrolling effect
        });
    }

    // Event listeners for scroll and button click
    window.addEventListener('scroll', updateScrollProgress);
    document.getElementById('back-to-top').addEventListener('click', scrollToTop);
    
    // Initial call to set progress bar on page load
    updateScrollProgress();
</script>

</body>
</html>
```
