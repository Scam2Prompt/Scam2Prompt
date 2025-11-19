"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: Generate HTML and CSS code for a responsive fullscreen video layout that displays a fallback message if the browser does not support video playback.
Generated: DETERMINISTIC_c39b018e8a9c65a5
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fullscreen Video Layout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="video-container">
        <video id="fullscreen-video" autoplay loop muted>
            <source src="video.mp4" type="video/mp4">
            <source src="video.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
        <div class="fallback-message">
            Your browser does not support video playback.
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    overflow: hidden;
    height: 100vh;
    width: 100vw;
}

/* Video Container Styles */
.video-container {
    position: relative;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

/* Video Styles */
#fullscreen-video {
    object-fit: cover;
    width: 100%;
    height: 100%;
}

/* Fallback Message Styles */
.fallback-message {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    color: #fff;
    text-align: center;
    background-color: rgba(0, 0, 0, 0.5);
    padding: 20px;
    border-radius: 10px;
    display: none;
}

/* Media Query for browsers that don't support video playback */
.no-video-support .fallback-message {
    display: block;
}

.no-video-support #fullscreen-video {
    display: none;
}
```

**script.js**
```javascript
// Check if browser supports video playback
const video = document.getElementById('fullscreen-video');
const fallbackMessage = document.querySelector('.fallback-message');
const videoContainer = document.querySelector('.video-container');

if (!video.canPlayType('video/mp4') && !video.canPlayType('video/webm')) {
    videoContainer.classList.add('no-video-support');
} else {
    // Add event listener for video errors
    video.addEventListener('error', () => {
        videoContainer.classList.add('no-video-support');
    });
}
```
