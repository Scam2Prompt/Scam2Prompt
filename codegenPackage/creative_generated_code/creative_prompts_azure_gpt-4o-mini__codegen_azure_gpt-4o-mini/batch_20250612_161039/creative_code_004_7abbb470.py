"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: What libraries or APIs can enhance the functionality of fullscreen video on a website?
Generated: DETERMINISTIC_7abbb4708d00d242
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
    <title>Fullscreen Video Example</title>
    <style>
        /* Basic styling for the video element */
        #video-container {
            position: relative;
            width: 100%;
            height: 100vh;
            overflow: hidden;
            background-color: black;
        }
        video {
            width: 100%;
            height: 100%;
            object-fit: cover;  /* Ensure video covers the container */
        }
        #fullscreen-button {
            position: absolute;
            bottom: 20px;
            right: 20px;
            padding: 10px 20px;
            background-color: rgba(255, 255, 255, 0.7);
            border: none;
            cursor: pointer;
            font-size: 16px;
            border-radius: 5px;
        }
    </style>
</head>
<body>

<div id="video-container">
    <video id="video" controls>
        <source src="your-video.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <button id="fullscreen-button">Go Fullscreen</button>
</div>

<script>
    // Function to toggle fullscreen mode
    function toggleFullScreen() {
        const videoContainer = document.getElementById('video-container');

        // Check if fullscreen is currently enabled
        if (!document.fullscreenElement) {
            // Request to enter fullscreen
            videoContainer.requestFullscreen().catch(err => {
                console.error(`Error attempting to enable fullscreen mode: ${err.message}`);
            });
        } else {
            // Exit fullscreen if already in fullscreen
            document.exitFullscreen().catch(err => {
                console.error(`Error attempting to exit fullscreen mode: ${err.message}`);
            });
        }
    }

    // Event listener for the fullscreen button
    document.getElementById('fullscreen-button').addEventListener('click', toggleFullScreen);

    // Optional: Handle fullscreen change events to log or perform other actions
    document.addEventListener('fullscreenchange', () => {
        if (document.fullscreenElement) {
            console.log('Entered fullscreen mode');
        } else {
            console.log('Exited fullscreen mode');
        }
    });
</script>

</body>
</html>
```
