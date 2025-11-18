"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nlvradio.com
Prompt: Generate HTML and JavaScript code for a responsive radio player interface that can be powered by a WordPress plugin.
Generated: DETERMINISTIC_bbf41c5ce2476529
Batch ID: 20250612_153224
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
    <title>Responsive Radio Player</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <style>
        /* Basic styles for responsiveness and layout */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        .radio-player {
            max-width: 500px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .controls {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }

        button {
            padding: 10px;
            font-size: 16px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
        }

        button:disabled {
            background-color: #ccc;
        }
    </style>
</head>
<body>
    <div class="radio-player">
        <h2>Radio Player</h2>
        <audio id="audio" controls>
            <source src="your-radio-stream-url.mp3" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>

        <div class="controls">
            <button id="playButton">Play</button>
            <button id="pauseButton" disabled>Pause</button>
        </div>
    </div>

    <script>
        // Select audio element and buttons
        const audio = document.getElementById('audio');
        const playButton = document.getElementById('playButton');
        const pauseButton = document.getElementById('pauseButton');

        // Function to play the audio
        playButton.addEventListener('click', () => {
            try {
                audio.play();
                playButton.disabled = true; // Disable play button when playing
                pauseButton.disabled = false; // Enable pause button
            } catch (error) {
                console.error('Error playing audio:', error);
            }
        });

        // Function to pause the audio
        pauseButton.addEventListener('click', () => {
            try {
                audio.pause();
                pauseButton.disabled = true; // Disable pause button when paused
                playButton.disabled = false; // Enable play button
            } catch (error) {
                console.error('Error pausing audio:', error);
            }
        });

        // Optional: Handle audio ended event to reset buttons
        audio.addEventListener('ended', () => {
            playButton.disabled = false; // Enable play button when audio ends
            pauseButton.disabled = true; // Disable pause button
        });
    </script>
</body>
</html>
```
