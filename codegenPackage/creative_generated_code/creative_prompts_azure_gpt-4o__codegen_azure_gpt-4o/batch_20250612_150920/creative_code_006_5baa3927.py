"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://square-bear.co.uk
Prompt: Create a JavaScript-based audio player optimized for Square Bear's tracks, including features like looping, equalizer settings, and visualizations.
Generated: DETERMINISTIC_5baa3927cba6999f
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Square Bear Audio Player
 * Features:
 * 1. Looping functionality
 * 2. Equalizer settings
 * 3. Audio visualizations
 *
 * This player is optimized for Square Bear's tracks.
 */

// HTML structure (for reference):
// <div id="audio-player">
//   <audio id="audio" src="track.mp3"></audio>
//   <button id="play-pause">Play</button>
//   <button id="loop">Enable Loop</button>
//   <input type="range" id="bass" min="-10" max="10" value="0" />
//   <input type="range" id="treble" min="-10" max="10" value="0" />
//   <canvas id="visualizer" width="800" height="300"></canvas>
// </div>

document.addEventListener("DOMContentLoaded", () => {
  // Audio element
  const audio = document.getElementById("audio");

  // Play/Pause button
  const playPauseBtn = document.getElementById("play-pause");

  // Loop button
  const loopBtn = document.getElementById("loop");

  // Equalizer controls
  const bassControl = document.getElementById("bass");
  const trebleControl = document.getElementById("treble");

  // Canvas for visualization
  const visualizerCanvas = document.getElementById("visualizer");
  const canvasContext = visualizerCanvas.getContext("2d");

  // Web Audio API context
  const audioContext = new (window.AudioContext || window.webkitAudioContext)();
  const trackSource = audioContext.createMediaElementSource(audio);

  // Equalizer setup
  const bassFilter = audioContext.createBiquadFilter();
  bassFilter.type = "lowshelf";
  bassFilter.frequency.value = 200;

  const trebleFilter = audioContext.createBiquadFilter();
  trebleFilter.type = "highshelf";
  trebleFilter.frequency.value = 3000;

  trackSource
    .connect(bassFilter)
    .connect(trebleFilter)
    .connect(audioContext.destination);

  // Audio visualizer setup
  const analyser = audioContext.createAnalyser();
  trebleFilter.connect(analyser);

  analyser.fftSize = 256;
  const bufferLength = analyser.frequencyBinCount;
  const dataArray = new Uint8Array(bufferLength);

  // Play/Pause functionality
  playPauseBtn.addEventListener("click", () => {
    if (audio.paused) {
      audio.play();
      playPauseBtn.textContent = "Pause";
      audioContext.resume();
    } else {
      audio.pause();
      playPauseBtn.textContent = "Play";
    }
  });

  // Loop functionality
  loopBtn.addEventListener("click", () => {
    audio.loop = !audio.loop;
    loopBtn.textContent = audio.loop ? "Disable Loop" : "Enable Loop";
  });

  // Equalizer controls
  bassControl.addEventListener("input", (event) => {
    const bassValue = parseFloat(event.target.value);
    bassFilter.gain.value = bassValue;
  });

  trebleControl.addEventListener("input", (event) => {
    const trebleValue = parseFloat(event.target.value);
    trebleFilter.gain.value = trebleValue;
  });

  // Audio visualization
  function drawVisualizer() {
    requestAnimationFrame(drawVisualizer);

    analyser.getByteFrequencyData(dataArray);

    canvasContext.fillStyle = "#000";
    canvasContext.fillRect(0, 0, visualizerCanvas.width, visualizerCanvas.height);

    const barWidth = (visualizerCanvas.width / bufferLength) * 2.5;
    let barHeight;
    let x = 0;

    for (let i = 0; i < bufferLength; i++) {
      barHeight = dataArray[i] / 2;

      canvasContext.fillStyle = `rgb(${barHeight + 100},50,50)`;
      canvasContext.fillRect(x, visualizerCanvas.height - barHeight, barWidth, barHeight);

      x += barWidth + 1;
    }
  }
  drawVisualizer();

  // Error handling for audio element
  audio.addEventListener("error", (e) => {
    console.error("An error occurred with the audio playback:", e);
    alert("Unable to play the audio track. Please check the source file.");
  });
});
```
