"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sonic-explorer.skavel.cz
Prompt: Create a web application using JavaScript that leverages Sonic Explorer's features for real-time audio visualization.
Generated: DETERMINISTIC_df3016fcbc4ad47b
Batch ID: 20250612_152954
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
    <title>Sonic Explorer - Real-time Audio Visualization</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
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
    <canvas id="visualizer" width="800" height="400"></canvas>
    <script>
        // Define canvas and context for rendering audio visualization
        const canvas = document.getElementById('visualizer');
        const ctx = canvas.getContext('2d');

        // Initialize Audio Context
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();

        // Create an AnalyserNode for real-time frequency and time-domain analysis
        const analyser = audioContext.createAnalyser();
        analyser.fftSize = 2048; // Determines the size of the FFT used for analysis

        // Create a data array to hold frequency data
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        // Function to draw the visualization
        function draw() {
            // Request animation frame for smooth rendering
            requestAnimationFrame(draw);
            analyser.getByteFrequencyData(dataArray); // Get frequency data from the analyser
            ctx.fillStyle = 'rgb(40, 44, 52)'; // Background color
            ctx.fillRect(0, 0, canvas.width, canvas.height); // Clear canvas

            const barWidth = (canvas.width / bufferLength) * 2.5; // Width of each bar
            let barHeight;
            let x = 0;

            // Loop through frequency data and draw bars
            for (let i = 0; i < bufferLength; i++) {
                barHeight = dataArray[i]; // Get the height of the bar
                ctx.fillStyle = `rgb(${barHeight + 100}, 50, 50)`; // Dynamic color based on height
                ctx.fillRect(x, canvas.height - barHeight / 2, barWidth, barHeight / 2); // Draw bar
                x += barWidth + 1; // Move to the next bar position
            }
        }

        // Function to start audio stream from user's microphone
        async function startAudio() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                const source = audioContext.createMediaStreamSource(stream); // Create source from microphone
                source.connect(analyser); // Connect source to analyser
                draw(); // Start drawing visualization
            } catch (error) {
                console.error('Error accessing audio input:', error); // Log any errors for debugging
            }
        }

        // Start the audio stream when the page loads
        window.onload = () => {
            if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
                startAudio(); // Call function to start audio
            } else {
                alert('getUserMedia not supported on your browser!'); // Alert user if not supported
            }
        };
    </script>
</body>
</html>
```
