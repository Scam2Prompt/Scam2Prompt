"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: Can you provide a code snippet for creating a fullscreen video background that adjusts to various screen sizes?
Generated: DETERMINISTIC_c738e0fcbdbff5fe
Batch ID: 20250612_161039
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
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            overflow: hidden;
            font-family: Arial, sans-serif;
        }

        #video-background {
            position: fixed;
            right: 0;
            bottom: 0;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -1;
            background-size: cover;
        }

        .content {
            position: relative;
            z-index: 1;
            color: white;
            text-align: center;
            padding: 20px;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
    </style>
</head>
<body>
    <video id="video-background" autoplay muted loop>
        <source src="your-video.mp4" type="video/mp4">
        <!-- Fallback for browsers that don't support video -->
        Your browser does not support the video tag.
    </video>

    <div class="content">
        <h1>Your Content Here</h1>
        <p>This text will appear over the video background.</p>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const video = document.getElementById('video-background');
            
            // Adjust video size when window is resized
            function resizeVideo() {
                const windowWidth = window.innerWidth;
                const windowHeight = window.innerHeight;
                const windowRatio = windowWidth / windowHeight;
                const videoRatio = video.videoWidth / video.videoHeight;

                if (windowRatio < videoRatio) {
                    video.style.width = 'auto';
                    video.style.height = '100%';
                } else {
                    video.style.width = '100%';
                    video.style.height = 'auto';
                }
            }

            // Initial resize
            resizeVideo();

            // Add event listener for window resize
            window.addEventListener('resize', resizeVideo);

            // Handle video loading errors
            video.addEventListener('error', function() {
                console.error('Error loading video:', video.error);
                // Fallback to background image if video fails to load
                video.style.display = 'none';
                document.body.style.backgroundImage = 'url(fallback-image.jpg)';
                document.body.style.backgroundSize = 'cover';
                document.body.style.backgroundPosition = 'center';
            });

            // Ensure video plays when autoplay is blocked (mobile devices)
            video.addEventListener('loadedmetadata', function() {
                const playPromise = video.play();
                
                if (playPromise !== undefined) {
                    playPromise.catch(error => {
                        console.log('Autoplay prevented:', error);
                        video.muted = true;
                        video.play();
                    });
                }
            });
        });
    </script>
</body>
</html>
```
