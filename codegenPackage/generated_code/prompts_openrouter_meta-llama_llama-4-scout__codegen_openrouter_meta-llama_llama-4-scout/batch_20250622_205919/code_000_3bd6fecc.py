"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: "Write HTML5 code for a responsive fullscreen video background that works on most browsers, including older versions that don't support modern video playback."
Generated: DETERMINISTIC_3bd6fecc56cfdd3f
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
    <title>Fullscreen Video Background</title>
    <style>
        /* Make the video background fullscreen */
        .video-background {
            position: relative;
            width: 100%;
            height: 100vh;
            background-size: cover;
            background-position: center;
        }
        
        /* Style the video element */
        .video-background video {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            object-position: center;
        }
        
        /* Add a fallback background image for older browsers */
        .video-background.no-video {
            background-image: url('fallback-image.jpg');
            background-size: cover;
            background-position: center;
        }
    </style>
</head>
<body>
    <div class="video-background">
        <video autoplay loop muted playsinline>
            <source src="video.mp4" type="video/mp4">
            <source src="video.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
    </div>

    <script>
        // Check if the browser supports video playback
        const video = document.querySelector('video');
        if (!video.canPlayType('video/mp4') && !video.canPlayType('video/webm')) {
            // If not, add a fallback class to display a background image
            document.querySelector('.video-background').classList.add('no-video');
        }
    </script>
</body>
</html>
```
