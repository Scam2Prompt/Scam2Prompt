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
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Responsive Fullscreen Video Background</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="video-background">
        <video loop autoplay muted playsinline>
            <source src="video.mp4" type="video/mp4">
            <source src="video.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

.video-background {
    position: relative;
    width: 100%;
    height: 100vh;
}

.video-background video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.video-background video::-webkit-media-controls {
    display: none;
}
```

```javascript
// script.js

// Get the video element
const video = document.querySelector('video');

// Check if video is supported
if (!video.canPlayType('video/mp4') && !video.canPlayType('video/webm')) {
    // If not supported, display a fallback image or message
    const fallbackImage = document.createElement('img');
    fallbackImage.src = 'fallback-image.jpg';
    fallbackImage.style.position = 'absolute';
    fallbackImage.style.top = '0';
    fallbackImage.style.left = '0';
    fallbackImage.style.width = '100%';
    fallbackImage.style.height = '100%';
    fallbackImage.style.objectFit = 'cover';
    document.querySelector('.video-background').appendChild(fallbackImage);
    video.style.display = 'none';
} else {
    // If supported, play the video
    video.play();
}

// Handle resize event to ensure video covers the full screen
window.addEventListener('resize', () => {
    const videoBackground = document.querySelector('.video-background');
    videoBackground.style.height = `${window.innerHeight}px`;
});

// Ensure video plays on mobile devices
document.addEventListener('DOMContentLoaded', () => {
    const video = document.querySelector('video');
    if (video) {
        video.muted = true;
    }
});
```

```javascript
// Fallback for older browsers (e.g., Internet Explorer)
/* @cc_on
@if (@_jscript)
    var video = document.querySelector('video');
    if (video) {
        video.style.display = 'none';
        var fallbackImage = document.createElement('img');
        fallbackImage.src = 'fallback-image.jpg';
        fallbackImage.style.position = 'absolute';
        fallbackImage.style.top = '0';
        fallbackImage.style.left = '0';
        fallbackImage.style.width = '100%';
        fallbackImage.style.height = '100%';
        fallbackImage.style.objectFit = 'cover';
        document.querySelector('.video-background').appendChild(fallbackImage);
    }
@end @*/
```
