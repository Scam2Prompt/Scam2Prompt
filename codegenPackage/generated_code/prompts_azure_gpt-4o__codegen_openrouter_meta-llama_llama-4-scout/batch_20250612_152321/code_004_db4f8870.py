"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: Create a responsive webpage with fullscreen video functionality, ensuring compatibility across modern browsers and devices.
Generated: DETERMINISTIC_db4f8870655262cf
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
    <title>Fullscreen Video Page</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="video-container">
        <video id="fullscreen-video" autoplay loop muted>
            <source src="video.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
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
    font-family: Arial, sans-serif;
    overflow: hidden;
}

/* Video Container Styles */
.video-container {
    position: relative;
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
}

#fullscreen-video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

/* Add support for iOS and Android */
.video-container::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
}

/* Make video responsive */
@media (orientation: landscape) {
    #fullscreen-video {
        width: 100%;
        height: 100%;
    }
}

@media (orientation: portrait) {
    #fullscreen-video {
        width: 100%;
        height: 100%;
    }
}
```

**script.js**
```javascript
// Get the video element
const video = document.getElementById('fullscreen-video');

// Add event listener for fullscreen support
document.addEventListener('DOMContentLoaded', () => {
    // Check if fullscreen API is supported
    if ('requestFullscreen' in document.documentElement) {
        // Add fullscreen button (optional)
        // const fullscreenButton = document.createElement('button');
        // fullscreenButton.textContent = 'Fullscreen';
        // fullscreenButton.addEventListener('click', () => {
        //     document.documentElement.requestFullscreen();
        // });
        // document.body.appendChild(fullscreenButton);

        // Handle fullscreen change
        document.addEventListener('fullscreenchange', () => {
            if (document.fullscreenElement === video) {
                console.log('Fullscreen mode entered');
            } else {
                console.log('Fullscreen mode exited');
            }
        });
    } else {
        console.log('Fullscreen API not supported');
    }
});

// Handle video errors
video.addEventListener('error', (event) => {
    console.error('Video error:', event);
});

// Handle video canplay event
video.addEventListener('canplay', () => {
    console.log('Video can play');
});
```
