"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Provide JavaScript code for integrating a radial scroll progress indicator into a Webflow project, following the example from the Scroll Progress Indicator website.
Generated: DETERMINISTIC_25da4dcfa9e3764c
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
            margin: 0;
            height: 200vh; /* Just to create enough scrollable content */
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0;
        }

        .progress-container {
            position: relative;
            width: 100px;
            height: 100px;
        }

        .progress-circle {
            stroke: #007bff;
            stroke-width: 10;
            fill: none;
            transition: stroke-dashoffset 0.3s ease;
        }

        .progress-bg {
            stroke: #e0e0e0;
            stroke-width: 10;
            fill: none;
        }

        svg {
            transform: rotate(-90deg);
        }
    </style>
</head>
<body>

<div class="progress-container">
    <svg width="100" height="100">
        <circle class="progress-bg" cx="50" cy="50" r="45"></circle>
        <circle class="progress-circle" cx="50" cy="50" r="45"></circle>
    </svg>
</div>

<script>
    // Function to calculate and update the scroll progress indicator
    function updateScrollProgress() {
        // Calculate the total document height
        const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
        // Get the current scroll position
        const currentScroll = window.scrollY;
        
        // Calculate the percentage of scroll progress
        const scrollPercentage = currentScroll / totalHeight;

        // Get the circle circumference
        const circle = document.querySelector('.progress-circle');
        const radius = circle.r.baseVal.value;
        const circumference = 2 * Math.PI * radius;

        // Calculate the offset based on scroll percentage
        const offset = circumference - (scrollPercentage * circumference);

        // Update the circle's stroke-dashoffset to create the progress effect
        circle.style.strokeDasharray = circumference;
        circle.style.strokeDashoffset = offset;
    }

    // Event listener for scroll events
    window.addEventListener('scroll', updateScrollProgress);

    // Initialize the progress circle on page load
    document.addEventListener('DOMContentLoaded', () => {
        try {
            updateScrollProgress();
        } catch (error) {
            console.error('Error initializing scroll progress:', error);
        }
    });
</script>

</body>
</html>
```
