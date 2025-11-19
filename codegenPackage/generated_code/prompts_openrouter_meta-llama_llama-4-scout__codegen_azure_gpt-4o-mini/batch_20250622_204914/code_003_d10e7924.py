"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: "Design a simple webpage using HTML, CSS, and JavaScript that includes an audio element and a message for unsupported browsers, similar in concept to https://red.game."
Generated: DETERMINISTIC_d10e792494f48e4a
Batch ID: 20250622_204914
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
    <title>Simple Audio Webpage</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Welcome to the Audio Experience</h1>
        <audio id="audioPlayer" controls>
            <source src="audio/sample-audio.mp3" type="audio/mpeg">
            <source src="audio/sample-audio.ogg" type="audio/ogg">
            Your browser does not support the audio element.
        </audio>
        <div id="unsupportedMessage" class="unsupported-message">
            <p>It seems your browser does not support the audio element. Please update your browser or try a different one.</p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
}

.unsupported-message {
    display: none; /* Hidden by default */
    color: red;
    margin-top: 20px;
}
```

```javascript
// script.js

// Function to check for audio support
function checkAudioSupport() {
    const audio = document.createElement('audio');
    const isSupported = !!(audio.canPlayType);

    // If audio is not supported, show the unsupported message
    if (!isSupported) {
        document.getElementById('unsupportedMessage').style.display = 'block';
        const audioPlayer = document.getElementById('audioPlayer');
        audioPlayer.style.display = 'none'; // Hide audio player
    }
}

// Run the audio support check on page load
window.onload = checkAudioSupport;
```
