"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code to implement a radial scroll progress indicator in Webflow, ensuring smooth performance without jank, as described on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_4499097973a49bb2
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
    <title>Radial Scroll Progress Indicator</title>
    <style>
        body {
            height: 200vh; /* Make the body tall enough to scroll */
            margin: 0;
            background: linear-gradient(to bottom, #ff7e5f, #feb47b);
            display: flex;
            align-items: center;
            justify-content: center;
        }

        #progress-container {
            position: fixed;
            top: 20px;
            left: 20px;
            width: 100px;
            height: 100px;
            border-radius: 50%;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
        }

        #progress-circle {
            width: 100%;
            height: 100%;
            border-radius: 50%;
            position: relative;
            background: conic-gradient(#4caf50 0%, #4caf50 var(--progress), #e0e0e0 var(--progress), #e0e0e0 100%);
        }
    </style>
</head>
<body>

<div id="progress-container">
    <div id="progress-circle"></div>
</div>

<script>
    // Function to calculate and update the scroll progress
    function updateScrollProgress() {
        // Get the total scrollable height
        const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
        
        // Get the current scroll position
        const scrollTop = window.scrollY;

        // Calculate the scroll progress as a percentage
        const scrollProgress = (scrollTop / scrollableHeight) * 100;

        // Update the CSS variable '--progress' for the conic gradient
        document.getElementById('progress-circle').style.setProperty('--progress', `${scrollProgress}%`);
    }

    // Add event listener for the scroll event
    window.addEventListener('scroll', updateScrollProgress);

    // Initialize the progress indicator on page load
    window.addEventListener('load', updateScrollProgress);
</script>

</body>
</html>
```
