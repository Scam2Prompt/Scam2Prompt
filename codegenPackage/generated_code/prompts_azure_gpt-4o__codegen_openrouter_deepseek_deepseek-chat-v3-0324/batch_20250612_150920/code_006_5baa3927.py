"""
Generated Code Metadata:
========================
Original URL: https://square-bear.co.uk
Prompt: Create a JavaScript-based audio player optimized for Square Bear's tracks, including features like looping, equalizer settings, and visualizations.
Generated: DETERMINISTIC_5baa3927cba6999f
Batch ID: 20250612_150920
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Square Bear Audio Player
 * A feature-rich audio player with looping, equalizer, and visualizations.
 */

class SquareBearAudioPlayer {
  constructor(options = {}) {
    // Default configuration
    this.config = {
      audioElementId: 'audio-player',
      canvasId: 'audio-visualizer',
      equalizerBands: 10,
      maxFrequency: 20000,
      ...options
    };

    // Audio context setup
    this.audioContext = null;
    this.analyser = null;
    this.source = null;
    this.gainNode = null;
    this.eqNodes = [];
    this.isPlaying = false;
    this.currentTrack = null;
    this.loop = false;
    this.volume = 1.0;

    // Initialize player
    this.initAudioContext();
    this.initDOMElements();
    this.initEventListeners();
    this.initEqualizer();
  }

  // Initialize Web Audio API context
  initAudioContext() {
    try {
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
      this.analyser = this.audioContext.createAnalyser();
      this.analyser.fftSize = 2048;
      this.gainNode = this.audioContext.createGain();
      this.gainNode.gain.value = this.volume;
    } catch (error) {
      console.error('Web Audio API is not supported in this browser', error);
    }
  }

  // Initialize DOM elements
  initDOMElements() {
    this.audioElement = document.getElementById(this.config.audioElementId);
    this.canvas = document.getElementById(this.config.canvasId);
    this.canvasContext = this.canvas.getContext('2d');

    if (!this.audioElement) {
      console.error('Audio element not found');
      return;
    }

    if (!this.canvas) {
      console.warn('Visualizer canvas not found, visualization disabled');
    }
  }

  // Initialize event listeners
  initEventListeners() {
    if (this.audioElement) {
      this.audioElement.addEventListener('play', () => this.handlePlay());
      this.audioElement.addEventListener('pause', () => this.handlePause());
      this.audioElement.addEventListener('ended', () => this.handleTrackEnd());
      this.audioElement.addEventListener('timeupdate', () => this.updateProgress());
    }
  }

  // Initialize equalizer
  initEqualizer() {
    if (!this.audioContext) return;

    // Create EQ bands
    for (let i = 0; i < this.config.equalizerBands; i++) {
      const eqNode = this.audioContext.createBiquadFilter();
      eqNode.type = 'peaking';
      eqNode.frequency.value = this.calculateBandFrequency(i);
      eqNode.Q.value = 1.0;
      eqNode.gain.value = 0;
      this.eqNodes.push(eqNode);
    }

    // Connect EQ nodes in series
    this.connectAudioNodes();
  }

  // Calculate frequency for each EQ band
  calculateBandFrequency(bandIndex) {
    const minFrequency = 20;
    const maxFrequency = this.config.maxFrequency;
    return minFrequency * Math.pow(maxFrequency / minFrequency, bandIndex / (this.config.equalizerBands - 1));
  }

  // Connect all audio nodes
  connectAudioNodes() {
    if (!this.audioContext || !this.source) return;

    // Disconnect existing connections
    if (this.source) {
      this.source.disconnect();
    }

    // Create new connection chain
    this.source = this.audioContext.createMediaElementSource(this.audioElement);
    let lastNode = this.source;

    // Connect EQ nodes
    this.eqNodes.forEach(node => {
      lastNode.connect(node);
      lastNode = node;
    });

    // Connect to analyser and gain node
    lastNode.connect(this.analyser);
    this.analyser.connect(this.gainNode);
    this.gainNode.connect(this.audioContext.destination);
  }

  // Load a new track
  loadTrack(trackUrl) {
    if (!this.audioElement) return;

    this.currentTrack = trackUrl;
    this.audioElement.src = trackUrl;
    this.audioElement.load();

    // Reconnect audio nodes when new source is available
    this.audioElement.addEventListener('canplay', () => {
      this.connectAudioNodes();
    }, { once: true });
  }

  // Play/pause toggle
  togglePlay() {
    if (!this.audioElement) return;

    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  // Play track
  play() {
    if (!this.audioElement) return;

    if (this.audioContext.state === 'suspended') {
      this.audioContext.resume();
    }

    this.audioElement.play()
      .then(() => {
        this.isPlaying = true;
        this.startVisualization();
      })
      .catch(error => {
        console.error('Playback failed:', error);
      });
  }

  // Pause track
  pause() {
    if (!this.audioElement) return;

    this.audioElement.pause();
    this.isPlaying = false;
    this.stopVisualization();
  }

  // Stop track
  stop() {
    if (!this.audioElement) return;

    this.audioElement.pause();
    this.audioElement.currentTime = 0;
    this.isPlaying = false;
    this.stopVisualization();
  }

  // Handle play event
  handlePlay() {
    this.isPlaying = true;
    this.startVisualization();
  }

  // Handle pause event
  handlePause() {
    this.isPlaying = false;
    this.stopVisualization();
  }

  // Handle track end
  handleTrackEnd() {
    this.isPlaying = false;
    this.stopVisualization();

    if (this.loop) {
      this.audioElement.currentTime = 0;
      this.play();
    }
  }

  // Toggle loop
  toggleLoop() {
    this.loop = !this.loop;
    return this.loop;
  }

  // Set volume (0.0 to 1.0)
  setVolume(volume) {
    if (volume < 0) volume = 0;
    if (volume > 1) volume = 1;

    this.volume = volume;
    if (this.gainNode) {
      this.gainNode.gain.value = volume;
    }
  }

  // Set equalizer band gain
  setBandGain(bandIndex, gain) {
    if (bandIndex < 0 || bandIndex >= this.eqNodes.length) return;
    this.eqNodes[bandIndex].gain.value = gain;
  }

  // Update progress display
  updateProgress() {
    // Implement progress bar update logic here
  }

  // Start visualization
  startVisualization() {
    if (!this.canvas || !this.analyser) return;

    this.visualizationActive = true;
    this.drawVisualization();
  }

  // Stop visualization
  stopVisualization() {
    this.visualizationActive = false;
  }

  // Draw visualization
  drawVisualization() {
    if (!this.visualizationActive || !this.canvas || !this.analyser) return;

    requestAnimationFrame(() => this.drawVisualization());

    const width = this.canvas.width;
    const height = this.canvas.height;
    this.canvasContext.clearRect(0, 0, width, height);

    // Frequency data visualization
    const bufferLength = this.analyser.frequencyBinCount;
    const dataArray = new Uint8Array(bufferLength);
    this.analyser.getByteFrequencyData(dataArray);

    const barWidth = (width / bufferLength) * 2.5;
    let x = 0;

    for (let i = 0; i < bufferLength; i++) {
      const barHeight = (dataArray[i] / 255) * height;

      this.canvasContext.fillStyle = `rgb(${Math.floor(barHeight * 2)}, 50, 150)`;
      this.canvasContext.fillRect(x, height - barHeight, barWidth, barHeight);

      x += barWidth + 1;
    }
  }
}

// Example usage:
// const player = new SquareBearAudioPlayer({
//   audioElementId: 'my-audio',
//   canvasId: 'my-visualizer'
// });
// player.loadTrack('path/to/track.mp3');
// player.play();
```
