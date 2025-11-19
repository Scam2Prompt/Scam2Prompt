"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Write code to implement a radial scroll progress indicator in Webflow, ensuring smooth performance without jank, as described on the Scroll Progress Indicator webpage.
Generated: DETERMINISTIC_4499097973a49bb2
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
            height: 200vh; /* Extend body height for scrolling */
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0;
        }

        .progress-container {
            position: relative;
            width: 150px;
            height: 150px;
            border-radius: 50%;
            overflow: hidden;
        }

        .progress-circle {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            clip-path: inset(0 0 0 0);
            background: conic-gradient(#4caf50 var(--progress), #e0e0e0 var(--progress));
            transition: background 0.1s linear; /* Smooth transition */
        }
    </style>
</head>
<body>

<div class="progress-container">
    <div class="progress-circle" id="progressCircle"></div>
</div>

<script>
    // Function to update the radial progress indicator based on scroll position
    function updateScrollProgress() {
        try {
            // Get the total scrollable height
            const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
            // Get the current scroll position
            const scrollPosition = window.scrollY;
            // Calculate the scroll progress as a percentage
            const progressPercentage = (scrollPosition / totalHeight) * 100;

            // Update the CSS variable for the conic gradient
            document.getElementById('progressCircle').style.setProperty('--progress', `${progressPercentage}deg`);
        } catch (error) {
            console.error('Error updating scroll progress:', error);
        }
    }

    // Event listener for scroll events
    window.addEventListener('scroll', updateScrollProgress);

    // Initial call to set progress on page load
    updateScrollProgress();
</script>

</body>
</html>
```
