"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: What are the best practices for ensuring video compatibility across different browsers in a responsive design?
Generated: DETERMINISTIC_0e6a69c62d179bab
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
    <title>Responsive Video Compatibility</title>
    <style>
        /* Responsive video container */
        .video-container {
            position: relative;
            width: 100%;
            padding-bottom: 56.25%; /* 16:9 aspect ratio */
            height: 0;
            overflow: hidden;
        }
        .video-container iframe,
        .video-container object,
        .video-container embed {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }
    </style>
</head>
<body>

<!-- Responsive Video Container -->
<div class="video-container">
    <video controls>
        <source src="video.mp4" type="video/mp4">
        <source src="video.webm" type="video/webm">
        <source src="video.ogv" type="video/ogg">
        Your browser does not support the video tag.
    </video>
</div>

<script>
    // Function to check if the video type is supported
    function isVideoSupported(type) {
        const video = document.createElement('video');
        return video.canPlayType(type) !== '';
    }

    // Check for supported video formats
    const formats = [
        { type: 'video/mp4', source: 'video.mp4' },
        { type: 'video/webm', source: 'video.webm' },
        { type: 'video/ogg', source: 'video.ogv' }
    ];

    // Set the video source based on the browser's support
    const videoElement = document.querySelector('video');
    let videoSourceSet = false;

    formats.forEach(format => {
        if (isVideoSupported(format.type) && !videoSourceSet) {
            const sourceElement = document.createElement('source');
            sourceElement.src = format.source;
            sourceElement.type = format.type;
            videoElement.appendChild(sourceElement);
            videoSourceSet = true; // Set the source if supported
        }
    });

    // If no source is set, alert the user
    if (!videoSourceSet) {
        console.error('No supported video formats found.');
        alert('Your browser does not support any of the available video formats.');
    }
</script>

</body>
</html>
```
