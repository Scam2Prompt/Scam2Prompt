"""
Generated Code Metadata:
========================
Original URL: https://todosobreguitarra.com
Prompt: Create a JavaScript code snippet to create a simple guitar tuner with audio and visual feedback.
Generated: DETERMINISTIC_f83db724b24f5205
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Guitar Tuner Application
 * This script provides a simple guitar tuner with audio and visual feedback.
 * It uses the Web Audio API to analyze the frequency of the input sound and
 * displays the closest note with a visual indicator.
 */

// Constants for note frequencies (standard tuning for guitar)
const NOTES = [
  { name: "E2", frequency: 82.41 },
  { name: "A2", frequency: 110.00 },
  { name: "D3", frequency: 146.83 },
  { name: "G3", frequency: 196.00 },
  { name: "B3", frequency: 246.94 },
  { name: "E4", frequency: 329.63 },
];

// HTML Elements for visual feedback
const noteDisplay = document.getElementById("note-display");
const frequencyDisplay = document.getElementById("frequency-display");
const detuneDisplay = document.getElementById("detune-display");

// Web Audio API setup
let audioContext = new (window.AudioContext || window.webkitAudioContext)();
let analyser = audioContext.createAnalyser();
analyser.fftSize = 2048;
let buffer = new Float32Array(analyser.fftSize);

// Start microphone input
async function startTuner() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const source = audioContext.createMediaStreamSource(stream);
    source.connect(analyser);
    updateTuner();
  } catch (error) {
    console.error("Error accessing microphone:", error);
    alert("Unable to access microphone. Please check your permissions.");
  }
}

// Analyze frequency and update visual feedback
function updateTuner() {
  analyser.getFloatTimeDomainData(buffer);
  const frequency = detectFrequency(buffer, audioContext.sampleRate);

  if (frequency) {
    const closestNote = findClosestNote(frequency);
    const detune = calculateDetune(frequency, closestNote.frequency);

    // Update UI
    noteDisplay.textContent = closestNote.name;
    frequencyDisplay.textContent = frequency.toFixed(2) + " Hz";
    detuneDisplay.textContent = detune > 0 ? `+${detune.toFixed(2)} cents` : `${detune.toFixed(2)} cents`;
  }

  requestAnimationFrame(updateTuner);
}

// Detect frequency using autocorrelation
function detectFrequency(buffer, sampleRate) {
  let size = buffer.length;
  let bestOffset = -1;
  let bestCorrelation = 0;
  let rms = 0;

  for (let i = 0; i < size; i++) {
    rms += buffer[i] * buffer[i];
  }
  rms = Math.sqrt(rms / size);
  if (rms < 0.01) return null; // Low signal

  let lastCorrelation = 1;
  for (let offset = 0; offset < size / 2; offset++) {
    let correlation = 0;
    for (let i = 0; i < size / 2; i++) {
      correlation += buffer[i] * buffer[i + offset];
    }
    correlation /= size / 2;

    if (correlation > 0.9 && correlation > lastCorrelation) {
      bestCorrelation = correlation;
      bestOffset = offset;
    }
    lastCorrelation = correlation;
  }

  if (bestCorrelation > 0.01) {
    return sampleRate / bestOffset;
  }
  return null;
}

// Find the closest note to the detected frequency
function findClosestNote(frequency) {
  let closestNote = NOTES[0];
  let minDifference = Math.abs(frequency - closestNote.frequency);

  for (let note of NOTES) {
    let difference = Math.abs(frequency - note.frequency);
    if (difference < minDifference) {
      closestNote = note;
      minDifference = difference;
    }
  }

  return closestNote;
}

// Calculate detune in cents
function calculateDetune(frequency, targetFrequency) {
  return 1200 * Math.log2(frequency / targetFrequency);
}

// Start the tuner when the page loads
window.onload = () => {
  startTuner();
};
```

```html
<!-- HTML for Guitar Tuner -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Guitar Tuner</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 20px;
    }
    #note-display {
      font-size: 2em;
      margin: 10px;
    }
    #frequency-display, #detune-display {
      font-size: 1.5em;
      margin: 5px;
    }
  </style>
</head>
<body>
  <h1>Guitar Tuner</h1>
  <div id="note-display">--</div>
  <div id="frequency-display">-- Hz</div>
  <div id="detune-display">-- cents</div>
  <script src="tuner.js"></script>
</body>
</html>
```
