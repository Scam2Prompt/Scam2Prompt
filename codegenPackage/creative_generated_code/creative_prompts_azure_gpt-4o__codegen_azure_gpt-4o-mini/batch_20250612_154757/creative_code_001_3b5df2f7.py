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
        body {
            height: 200vh; /* Make the body taller to allow scrolling */
            margin: 0;
            font-family: Arial, sans-serif;
        }
        #progress-circle {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 100px;
            height: 100px;
        }
    </style>
</head>
<body>
    <svg id="progress-circle" viewBox="0 0 100 100">
        <circle cx="50" cy="50" r="45" stroke="#e6e6e6" stroke-width="10" fill="none" />
        <circle id="progress" cx="50" cy="50" r="45" stroke="#4caf50" stroke-width="10" fill="none" stroke-dasharray="283" stroke-dashoffset="283" />
    </svg>

    <script>
        // Get the SVG circle element for progress
        const progressCircle = document.getElementById('progress');
        
        // Function to update the stroke-dashoffset based on scroll position
        const updateProgress = () => {
            // Calculate scroll percentage
            const scrollTop = window.scrollY;
            const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPercentage = scrollTop / documentHeight;

            // Calculate the offset for the stroke-dasharray
            const offset = 283 - (scrollPercentage * 283);
            
            // Update the stroke-dashoffset to create the progress effect
            progressCircle.style.strokeDashoffset = offset;
        };

        // Add the scroll event listener to update the progress indicator
        window.addEventListener('scroll', updateProgress);

        // Initial call to set the progress indicator on page load
        updateProgress();
    </script>
</body>
</html>
```
