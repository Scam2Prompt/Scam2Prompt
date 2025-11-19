"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: How can I implement a responsive fullscreen video feature on a webpage using HTML and CSS?
Generated: DETERMINISTIC_4c3bcbb0ad3d5442
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
    <title>Fullscreen Responsive Video</title>
    <style>
        /* Reset body margin and set overflow to hidden */
        body, html {
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            overflow: hidden; /* Prevents scrolling */
        }

        /* Container for the video */
        .video-container {
            position: absolute; /* Allows full control of positioning */
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden; /* Hides overflow from video */
        }

        /* Video styling to make it responsive */
        .video-container video {
            position: absolute; /* Allows for full control of sizing */
            top: 50%; /* Center vertically */
            left: 50%; /* Center horizontally */
            min-width: 100%; /* Ensures video covers the entire container */
            min-height: 100%; /* Ensures video covers the entire container */
            width: auto; /* Maintain aspect ratio */
            height: auto; /* Maintain aspect ratio */
            transform: translate(-50%, -50%); /* Center the video */
        }
    </style>
</head>
<body>
    <div class="video-container">
        <video autoplay muted loop playsinline>
            <source src="path/to/video.mp4" type="video/mp4">
            <source src="path/to/video.webm" type="video/webm">
            Your browser does not support the video tag.
        </video>
    </div>
    
    <script>
        // Check if the video can play and log any errors
        const video = document.querySelector('video');

        // Error handling for video playback
        video.onerror = function(event) {
            console.error('Error occurred while trying to play the video:', event);
            alert('An error occurred while trying to load the video. Please try again later.');
        };

        // Optional: Add event listeners for debugging
        video.addEventListener('loadeddata', () => {
            console.log('Video loaded and ready to play');
        });
    </script>
</body>
</html>
```
