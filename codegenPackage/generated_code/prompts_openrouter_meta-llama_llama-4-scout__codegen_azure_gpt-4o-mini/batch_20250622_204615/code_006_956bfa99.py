"""
Generated Code Metadata:
========================
Original URL: https://clonesx.pages.dev
Prompt: Create a simple example of how to use HTML5 video and JavaScript to create an immersive experience for showcasing digital artifacts, as seen on the RTFKT website.
Generated: DETERMINISTIC_956bfa9918d076f0
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Immersive Video Experience</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #000;
            color: #fff;
            font-family: Arial, sans-serif;
        }
        #video-container {
            position: relative;
            width: 80%;
            max-width: 800px;
        }
        video {
            width: 100%;
            height: auto;
            border: 2px solid #fff;
        }
        .overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #fff;
            background: rgba(0, 0, 0, 0.5);
            opacity: 0;
            transition: opacity 0.5s;
        }
        .overlay.visible {
            opacity: 1;
        }
    </style>
</head>
<body>

<div id="video-container">
    <video id="artifact-video" controls>
        <source src="path/to/your/video.mp4" type="video/mp4">
        Your browser does not support the video tag.
    </video>
    <div class="overlay" id="video-overlay">
        <h2>Digital Artifact Title</h2>
        <p>Description of the digital artifact goes here.</p>
        <button id="close-overlay">Close</button>
    </div>
</div>

<script>
    // Get references to the video and overlay elements
    const video = document.getElementById('artifact-video');
    const overlay = document.getElementById('video-overlay');
    const closeButton = document.getElementById('close-overlay');

    // Function to show the overlay when the video is played
    function showOverlay() {
        overlay.classList.add('visible');
    }

    // Function to hide the overlay when the close button is clicked
    function hideOverlay() {
        overlay.classList.remove('visible');
    }

    // Event listener for when the video is played
    video.addEventListener('play', showOverlay);

    // Event listener for the close button
    closeButton.addEventListener('click', hideOverlay);

    // Error handling for video loading
    video.onerror = function() {
        console.error('Error loading video. Please check the file path and format.');
        alert('An error occurred while loading the video. Please try again later.');
    };
</script>

</body>
</html>
```
