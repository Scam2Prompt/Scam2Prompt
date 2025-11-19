"""
Generated Code Metadata:
========================
Original URL: https://mystrikingly.com
Prompt: Write JavaScript code to customize a video background for a Strikingly template.
Generated: DETERMINISTIC_0026f196015e6734
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// video-background.js

/**
 * Customizes the video background for a Strikingly template.
 */

// Select the video element
const videoElement = document.querySelector('#video-background');

// Check if the video element exists
if (!videoElement) {
  console.error('Video element not found');
  throw new Error('Video element not found');
}

// Set video attributes
videoElement.setAttribute('autoplay', true);
videoElement.setAttribute('loop', true);
videoElement.setAttribute('muted', true); // Mute the video by default

// Add event listener for video load
videoElement.addEventListener('loadedmetadata', () => {
  // Set video dimensions
  videoElement.style.objectFit = 'cover';
  videoElement.style.width = '100%';
  videoElement.style.height = '100vh';
});

// Error handling for video load
videoElement.addEventListener('error', (event) => {
  console.error('Video load error:', event);
});

// Pause video when not in view
const observer = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    videoElement.play();
  } else {
    videoElement.pause();
  }
}, { threshold: 0.5 });

observer.observe(videoElement);
```

```css
/* video-background.css */

/* Add some basic styling to the video element */
#video-background {
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
}
```

```html
<!-- index.html -->

<!-- Add the video element to your Strikingly template -->
<video id="video-background" src="path/to/video.mp4"></video>
```
