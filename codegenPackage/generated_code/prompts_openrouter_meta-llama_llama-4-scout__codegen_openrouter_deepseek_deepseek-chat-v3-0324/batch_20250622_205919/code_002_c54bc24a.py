"""
Generated Code Metadata:
========================
Original URL: https://laguarda.com.ec
Prompt: "Generate CSS for a responsive fullscreen video container that adjusts to different screen sizes and devices, ensuring a seamless video playback experience."
Generated: DETERMINISTIC_c54bc24a8572ac3f
Batch ID: 20250622_205919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Base styles for the video container */
.video-container {
    position: relative;
    width: 100%;
    height: 100vh; /* Full viewport height */
    overflow: hidden;
    background-color: #000; /* Fallback background */
}

/* Video element styles */
.video-container video {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    min-width: 100%;
    min-height: 100%;
    width: auto;
    height: auto;
    
    /* Maintain aspect ratio */
    object-fit: cover;
}

/* Responsive adjustments for different aspect ratios */
@media (aspect-ratio: 16/9) {
    .video-container video {
        width: 100%;
        height: auto;
    }
}

@media (aspect-ratio: 4/3) {
    .video-container video {
        width: auto;
        height: 100%;
    }
}

/* Mobile device adjustments */
@media (max-width: 768px) {
    .video-container {
        height: 80vh; /* Adjust height for mobile */
    }
    
    .video-container video {
        /* Optional: Different video source or settings for mobile */
    }
}

/* Tablet device adjustments */
@media (min-width: 769px) and (max-width: 1024px) {
    .video-container {
        height: 90vh; /* Adjust height for tablets */
    }
}

/* Accessibility: Add focus styles for keyboard navigation */
.video-container video:focus {
    outline: 2px solid #4a90e2;
    outline-offset: 2px;
}

/* Fallback for browsers that don't support object-fit */
@supports not (object-fit: cover) {
    .video-container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .video-container video {
        position: static;
        transform: none;
        max-width: 100%;
        max-height: 100%;
    }
}
```
