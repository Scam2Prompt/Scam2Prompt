"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wavecall.io
Prompt: Write a code snippet to integrate WaveCall's live transcription feature into a web application.
Generated: DETERMINISTIC_0785b101ee1c808e
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Integration of WaveCall's live transcription feature into a web application.
 * This script assumes the usage of WaveCall API and WebSocket for real-time transcription.
 */

// Replace with your WaveCall API key and endpoint URL
const WAVE_CALL_API_KEY = 'your-api-key-here';
const WAVE_CALL_TRANSCRIPTION_ENDPOINT = 'wss://api.wavecall.com/transcription';

// DOM elements for displaying transcription
const transcriptionDisplay = document.getElementById('transcription');
const startButton = document.getElementById('startTranscription');
const stopButton = document.getElementById('stopTranscription');

// WebSocket variable to maintain connection
let waveCallSocket;

/**
 * Starts the live transcription by connecting to the WaveCall WebSocket.
 */
function startTranscription() {
  try {
    // Initialize WebSocket connection to WaveCall
    waveCallSocket = new WebSocket(WAVE_CALL_TRANSCRIPTION_ENDPOINT);

    // Attach event listeners
    waveCallSocket.onopen = () => {
      console.log('WebSocket connected. Starting transcription...');
      // Send authentication or configuration if required by WaveCall API
      waveCallSocket.send(
        JSON.stringify({
          type: 'start',
          apiKey: WAVE_CALL_API_KEY,
        })
      );
    };

    waveCallSocket.onmessage = (event) => {
      // Parse and display real-time transcription data
      const data = JSON.parse(event.data);
      if (data.transcription) {
        transcriptionDisplay.textContent += `${data.transcription}\n`;
      }
    };

    waveCallSocket.onerror = (error) => {
      console.error('WebSocket error:', error);
      alert('An error occurred while connecting to WaveCall.');
    };

    waveCallSocket.onclose = () => {
      console.log('WebSocket connection closed.');
    };

    // Disable the "Start" button and enable the "Stop" button
    startButton.disabled = true;
    stopButton.disabled = false;
  } catch (error) {
    console.error('Error starting transcription:', error);
    alert('Failed to start transcription. Please try again.');
  }
}

/**
 * Stops the live transcription by closing the WebSocket connection.
 */
function stopTranscription() {
  try {
    if (waveCallSocket) {
      waveCallSocket.close(); // Close the WebSocket connection
      transcriptionDisplay.textContent += '\n[Transcription stopped]\n';
    }

    // Reset button states
    startButton.disabled = false;
    stopButton.disabled = true;
  } catch (error) {
    console.error('Error stopping transcription:', error);
    alert('Failed to stop transcription. Please try again.');
  }
}

// Attach event listeners to buttons
startButton.addEventListener('click', startTranscription);
stopButton.addEventListener('click', stopTranscription);

// Ensure the "Stop" button is initially disabled
stopButton.disabled = true;
```

Make sure to adapt the code to your web application's specific requirements and replace placeholders, such as the API key and endpoint URL, with actual values from WaveCall.
