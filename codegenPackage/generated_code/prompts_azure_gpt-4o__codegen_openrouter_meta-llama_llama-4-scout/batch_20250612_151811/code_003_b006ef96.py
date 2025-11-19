"""
Generated Code Metadata:
========================
Original URL: https://wonderino.com
Prompt: Write JavaScript code to stop all running animations on a webpage, including videos, GIFs, and CSS transitions, as described in Wonderino's accessibility features.
Generated: DETERMINISTIC_b006ef96ee60586e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Stops all running animations on a webpage, including videos, GIFs, and CSS transitions.
 */
// Function to stop all animations
function stopAllAnimations() {
  // Stop videos
  stopVideos();

  // Stop GIFs
  stopGifs();

  // Stop CSS transitions
  stopCssTransitions();
}

/**
 * Stops all videos on the webpage.
 */
function stopVideos() {
  // Get all video elements
  const videos = document.querySelectorAll('video');

  // Iterate over each video and pause it
  videos.forEach((video) => {
    video.pause();
    // Reset the video to the start
    video.currentTime = 0;
  });
}

/**
 * Stops all GIFs on the webpage by replacing them with a static image.
 */
function stopGifs() {
  // Get all img elements with .gif class
  const gifs = document.querySelectorAll('img.gif');

  // Iterate over each GIF and replace it with a static image
  gifs.forEach((gif) => {
    // Get the src of the GIF
    const gifSrc = gif.src;

    // Create a new image element with the static image
    const staticImg = new Image();
    staticImg.src = gifSrc;

    // Replace the GIF with the static image
    gif.replaceWith(staticImg);
  });
}

/**
 * Stops all CSS transitions on the webpage by setting their transition property to 'none'.
 */
function stopCssTransitions() {
  // Get all elements with a transition property
  const transitioningElements = document.querySelectorAll('*');

  // Iterate over each element and set its transition property to 'none'
  transitioningElements.forEach((element) => {
    // Get the computed style of the element
    const style = globalThis.getComputedStyle(element);

    // Check if the element has a transition property
    if (style.transition !== 'none') {
      // Set the transition property to 'none'
      element.style.transition = 'none';
    }
  });
}

// Call the function to stop all animations
stopAllAnimations();
```
