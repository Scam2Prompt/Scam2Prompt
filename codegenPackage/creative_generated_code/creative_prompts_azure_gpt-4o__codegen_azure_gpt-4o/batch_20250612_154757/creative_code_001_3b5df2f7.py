"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Generate SVG code for a radial scroll progress indicator that updates dynamically based on the scroll position, as outlined on the Scroll Progress Indicator website.
Generated: DETERMINISTIC_3b5df2f798955c84
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
        /* Center the radial progress indicator */
        body {
            margin: 0;
            overflow-y: scroll; /* Ensure scrollable content */
            height: 200vh; /* Simulate a tall page for scrolling */
            display: flex;
            justify-content: center;
            align-items: center;
        }

        svg {
            width: 100px;
            height: 100px;
        }

        .progress-circle {
            transform: rotate(-90deg); /* Rotate to start progress at the top */
            transform-origin: center;
        }
    </style>
</head>
<body>
    <!-- SVG for radial progress indicator -->
    <svg viewBox="0 0 100 100">
        <!-- Background circle -->
        <circle cx="50" cy="50" r="45" stroke="#e6e6e6" stroke-width="5" fill="none"></circle>
        <!-- Progress circle -->
        <circle
            class="progress-circle"
            cx="50"
            cy="50"
            r="45"
            stroke="#3498db"
            stroke-width="5"
            fill="none"
            stroke-dasharray="283" <!-- Circumference = 2 * pi * radius -->
            stroke-dashoffset="283" <!-- Start fully hidden -->
        ></circle>
    </svg>

    <script>
        // Function to calculate scroll progress
        function updateProgress() {
            try {
                const progressCircle = document.querySelector('.progress-circle');
                const scrollTop = window.scrollY; // Scrolled distance from the top
                const docHeight = document.documentElement.scrollHeight; // Total document height
                const windowHeight = window.innerHeight; // Viewport height

                // Calculate scroll percentage (always between 0 and 1)
                const scrollPercentage = scrollTop / (docHeight - windowHeight);

                // Map the scroll percentage to the circle's circumference
                const circumference = 2 * Math.PI * 45; // Radius = 45
                const offset = circumference * (1 - scrollPercentage);

                // Update the stroke-dashoffset to reflect the scroll progress
                progressCircle.style.strokeDashoffset = offset;
            } catch (error) {
                console.error("Error updating scroll progress:", error);
            }
        }

        // Attach scroll event listener to update progress
        window.addEventListener('scroll', updateProgress);

        // Initial update to set progress correctly on page load
        updateProgress();
    </script>
</body>
</html>
```
