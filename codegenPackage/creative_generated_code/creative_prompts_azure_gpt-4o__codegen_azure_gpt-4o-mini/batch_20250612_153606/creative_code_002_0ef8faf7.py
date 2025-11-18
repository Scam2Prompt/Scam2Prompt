"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneymintpinnacles.firebaseapp.com
Prompt: Generate a script to validate browser support for HTML5 video formats (mp4 and webm) and provide fallback options, inspired by the Disney Pinnacle webpage.
Generated: DETERMINISTIC_0ef8faf7e080edd3
Batch ID: 20250612_153606
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
    <title>HTML5 Video Support Check</title>
    <style>
        /* Basic styling for the video container */
        .video-container {
            text-align: center;
            margin: 20px;
        }
        .fallback-message {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>

<div class="video-container">
    <h1>HTML5 Video Support Check</h1>
    <video id="videoPlayer" controls>
        <!-- MP4 source -->
        <source src="video/sample.mp4" type="video/mp4">
        <!-- WebM source -->
        <source src="video/sample.webm" type="video/webm">
        <!-- Fallback message for unsupported browsers -->
        Your browser does not support HTML5 video.
    </video>
    <p class="fallback-message" id="fallbackMessage" style="display: none;"></p>
</div>

<script>
    // Function to check for HTML5 video support
    function checkVideoSupport() {
        const video = document.createElement('video');
        const mp4Supported = !!video.canPlayType('video/mp4; codecs="avc1.42E01E, mp4a.40.2"');
        const webmSupported = !!video.canPlayType('video/webm; codecs="vp8, vorbis"');

        // Prepare fallback message based on support
        const fallbackMessageElement = document.getElementById('fallbackMessage');
        
        if (!mp4Supported && !webmSupported) {
            // If neither format is supported, show fallback message
            fallbackMessageElement.textContent = 'Your browser does not support HTML5 video. Please update your browser or use a different one.';
            fallbackMessageElement.style.display = 'block';
        } else {
            // If at least one format is supported, hide the fallback message
            fallbackMessageElement.style.display = 'none';
        }
    }

    // Execute the video support check on page load
    window.onload = checkVideoSupport;
</script>

</body>
</html>
```
