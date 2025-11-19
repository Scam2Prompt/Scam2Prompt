"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: "How can I use the HTML5 video tag to create a responsive fullscreen video background that supports playback on browsers with limited video support, like Internet Explorer?"
Generated: DETERMINISTIC_6f2d1ad6f3656a10
Batch ID: 20250622_205919
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
    <title>Responsive Fullscreen Video Background</title>
    <style>
        /* Basic reset for body and html */
        html, body {
            margin: 0;
            padding: 0;
            height: 100%;
            overflow: hidden; /* Prevent scrolling */
        }

        /* Video container to cover the entire viewport */
        .video-container {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
            z-index: -1; /* Send video behind other content */
        }

        /* Video styling for responsiveness */
        video {
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%); /* Center the video */
        }

        /* Content overlay */
        .content {
            position: relative;
            z-index: 1; /* Bring content above video */
            color: white;
            text-align: center;
            padding: 20px;
        }
    </style>
</head>
<body>

    <div class="video-container">
        <video autoplay muted loop playsinline>
            <source src="video.mp4" type="video/mp4">
            <source src="video.webm" type="video/webm">
            <source src="video.ogv" type="video/ogg">
            <!-- Fallback for browsers that do not support the video tag -->
            Your browser does not support the video tag.
        </video>
    </div>

    <div class="content">
        <h1>Welcome to Our Website</h1>
        <p>Enjoy our stunning video background!</p>
    </div>

    <script>
        // Check if the video is supported
        const video = document.querySelector('video');
        if (video) {
            video.addEventListener('error', function(event) {
                console.error('Video playback error:', event);
                alert('There was an error loading the video. Please try again later.');
            });
        } else {
            console.warn('Video element not found.');
        }
    </script>

</body>
</html>
```
