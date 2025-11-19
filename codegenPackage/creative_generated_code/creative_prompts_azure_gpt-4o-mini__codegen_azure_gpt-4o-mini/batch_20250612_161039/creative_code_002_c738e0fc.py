"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: Can you provide a code snippet for creating a fullscreen video background that adjusts to various screen sizes?
Generated: DETERMINISTIC_c738e0fcbdbff5fe
Batch ID: 20250612_161039
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
    <title>Fullscreen Video Background</title>
    <style>
        /* Basic reset for body and html */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html, body {
            height: 100%;
            overflow: hidden; /* Prevent scrolling */
        }

        /* Container for the video */
        .video-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden; /* Hide overflow to keep the background clean */
        }

        /* Video styling to cover the screen */
        video {
            position: absolute;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            transform: translate(-50%, -50%); /* Center video */
            z-index: -1; /* Send video to the back */
        }

        /* Content overlay */
        .content {
            position: relative;
            z-index: 1; /* Place content above video */
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>

    <div class="video-container">
        <video autoplay muted loop>
            <!-- Fallback for browsers that do not support video -->
            <source src="your-video-file.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>

    <div class="content">
        <h1>Welcome to My Website</h1>
        <p>This is a fullscreen video background example.</p>
    </div>

    <script>
        // Check if video element is supported
        const video = document.querySelector('video');
        if (!video) {
            console.error("Video element not found.");
            alert("Your browser does not support the video element.");
        }
    </script>
</body>
</html>
```
