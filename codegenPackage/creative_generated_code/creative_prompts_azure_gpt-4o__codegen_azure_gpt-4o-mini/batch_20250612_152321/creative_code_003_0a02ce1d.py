"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://laguarda.com.ec
Prompt: Provide a solution to detect browser support for video playback and display an alternative message using JavaScript, as referenced on laguarda.com.ec.
Generated: DETERMINISTIC_0a02ce1d36aa733e
Batch ID: 20250612_152321
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
    <title>Video Support Detection</title>
    <style>
        /* Style for the alternative message */
        .alternative-message {
            display: none;
            color: red;
            font-weight: bold;
        }
    </style>
</head>
<body>

    <video id="myVideo" controls>
        <source src="sample-video.mp4" type="video/mp4">
        <source src="sample-video.webm" type="video/webm">
        Your browser does not support the video tag. 
    </video>
    
    <div id="alternativeMessage" class="alternative-message">
        Your browser does not support video playback. Please consider updating your browser.
    </div>

    <script>
        // Function to check if the browser supports video playback
        function checkVideoSupport() {
            // Get the video element
            const video = document.getElementById('myVideo');
            const altMessage = document.getElementById('alternativeMessage');

            // Check if the video element is supported
            if (video.canPlayType) {
                // Check for MP4 support
                const isMp4Supported = video.canPlayType('video/mp4');
                // Check for WebM support
                const isWebmSupported = video.canPlayType('video/webm');

                // If neither format is supported, show the alternative message
                if (!isMp4Supported && !isWebmSupported) {
                    altMessage.style.display = 'block';
                }
            } else {
                // If the canPlayType method is not available, show the alternative message
                altMessage.style.display = 'block';
            }
        }

        // Execute the video support check when the page loads
        window.onload = function() {
            try {
                checkVideoSupport();
            } catch (error) {
                console.error("Error checking video support: ", error);
            }
        };
    </script>

</body>
</html>
```
