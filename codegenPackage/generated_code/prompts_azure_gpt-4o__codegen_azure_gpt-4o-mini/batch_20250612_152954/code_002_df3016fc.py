"""
Generated Code Metadata:
========================
Original URL: https://sonic-explorer.skavel.cz
Prompt: Create a web application using JavaScript that leverages Sonic Explorer's features for real-time audio visualization.
Generated: DETERMINISTIC_df3016fcbc4ad47b
Batch ID: 20250612_152954
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
    <title>Real-Time Audio Visualization</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #282c34;
            color: white;
            font-family: Arial, sans-serif;
        }
        canvas {
            border: 1px solid white;
        }
    </style>
</head>
<body>
    <canvas id="audioCanvas" width="800" height="400"></canvas>
    <script>
        // Get the canvas element and its context
        const canvas = document.getElementById('audioCanvas');
        const ctx = canvas.getContext('2d');

        // Initialize audio context and analyser
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const analyser = audioContext.createAnalyser();
        analyser.fftSize = 2048; // Set the FFT size for frequency data

        // Create a buffer for the audio data
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        // Function to visualize audio data
        function visualize() {
            requestAnimationFrame(visualize); // Call visualize again for the next frame

            // Get the frequency data
            analyser.getByteFrequencyData(dataArray);

            // Clear the canvas
            ctx.fillStyle = 'rgba(40, 44, 52, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Draw the frequency bars
            const barWidth = (canvas.width / bufferLength) * 2.5; // Width of each bar
            let barHeight;
            let x = 0;

            for (let i = 0; i < bufferLength; i++) {
                barHeight = dataArray[i] / 2; // Scale the bar height
                ctx.fillStyle = `rgb(${barHeight + 100}, 50, 50)`; // Color based on height
                ctx.fillRect(x, canvas.height - barHeight, barWidth, barHeight);
                x += barWidth + 1; // Move to the next bar position
            }
        }

        // Function to start audio visualization
        function startVisualization(stream) {
            const source = audioContext.createMediaStreamSource(stream);
            source.connect(analyser); // Connect the source to the analyser
            visualize(); // Start visualizing
        }

        // Function to handle errors
        function handleError(error) {
            console.error('Error accessing audio stream:', error);
            alert('Could not access audio stream. Please check your microphone permissions.');
        }

        // Request audio stream from the user's microphone
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(startVisualization)
            .catch(handleError);
    </script>
</body>
</html>
```
