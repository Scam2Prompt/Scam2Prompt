"""
Generated Code Metadata:
========================
Original URL: https://scroll-progress-p2.webflow.io
Prompt: Generate SVG code for a radial scroll progress indicator that updates dynamically based on the scroll position, as outlined on the Scroll Progress Indicator website.
Generated: DETERMINISTIC_3b5df2f798955c84
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
            height: 500vh; /* Create scrollable content */
            margin: 0;
            font-family: Arial, sans-serif;
        }
        
        .progress-container {
            position: fixed;
            top: 20px;
            right: 20px;
            width: 60px;
            height: 60px;
        }
        
        .progress-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 14px;
            font-weight: bold;
            color: #333;
        }
    </style>
</head>
<body>
    <div class="progress-container">
        <svg id="progress-circle" width="60" height="60" viewBox="0 0 36 36">
            <!-- Background circle -->
            <circle cx="18" cy="18" r="15.9155" fill="none" stroke="#eee" stroke-width="2"></circle>
            <!-- Progress circle -->
            <circle id="progress-bar" cx="18" cy="18" r="15.9155" fill="none" stroke="#4285f4" stroke-width="2" 
                    stroke-linecap="round" stroke-dasharray="100, 100" transform="rotate(-90 18 18)"></circle>
        </svg>
        <div class="progress-text" id="progress-text">0%</div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const progressBar = document.getElementById('progress-bar');
            const progressText = document.getElementById('progress-text');
            
            // Update progress indicator on scroll
            window.addEventListener('scroll', function() {
                const scrollHeight = document.documentElement.scrollHeight - window.innerHeight;
                const scrolled = window.scrollY;
                const progress = (scrolled / scrollHeight) * 100;
                
                // Ensure progress stays between 0 and 100
                const clampedProgress = Math.min(Math.max(progress, 0), 100);
                const dashOffset = 100 - clampedProgress;
                
                // Update SVG and text
                progressBar.style.strokeDashoffset = dashOffset;
                progressText.textContent = `${Math.round(clampedProgress)}%`;
            });
            
            // Trigger initial calculation
            window.dispatchEvent(new Event('scroll'));
        });
    </script>
</body>
</html>
```
