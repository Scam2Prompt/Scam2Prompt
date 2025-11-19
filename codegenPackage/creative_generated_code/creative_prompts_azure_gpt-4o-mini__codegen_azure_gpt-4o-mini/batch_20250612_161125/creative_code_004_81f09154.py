"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: How do I customize a radial scroll progress indicator in Webflow for better user experience?
Generated: DETERMINISTIC_81f0915426eb665f
Batch ID: 20250612_161125
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
        /* Styles for the radial progress indicator */
        #progress-container {
            position: relative;
            width: 200px;
            height: 200px;
            border-radius: 50%;
            overflow: hidden;
            margin: 0 auto;
        }

        #progress-circle {
            position: absolute;
            width: 100%;
            height: 100%;
            border-radius: 50%;
            background: conic-gradient(#4caf50 var(--progress), #e0e0e0 var(--progress));
            transition: background 0.3s ease;
        }

        #scroll-message {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 1.5em;
            text-align: center;
            color: #333;
        }
    </style>
</head>
<body>

    <div id="progress-container">
        <div id="progress-circle" style="--progress: 0%;"></div>
        <div id="scroll-message">Scroll to Progress</div>
    </div>

    <script>
        // Function to update radial progress based on scroll
        const updateProgress = () => {
            // Get scroll position and total scrollable height
            const scrollTop = window.scrollY;
            const documentHeight = document.documentElement.scrollHeight - window.innerHeight;

            // Calculate progress percentage
            const progress = (scrollTop / documentHeight) * 100;

            // Update CSS variable for conic-gradient background
            document.getElementById('progress-circle').style.setProperty('--progress', `${progress}%`);

            // Error handling for bounds
            if (progress < 0 || progress > 100) {
                console.error("Progress value out of bounds:", progress);
            }
        };

        // Event listener for scroll event
        window.addEventListener('scroll', updateProgress);

        // Initial call to set progress on page load
        updateProgress();
    </script>

</body>
</html>
```
