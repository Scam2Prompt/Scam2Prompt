"""
Generated Code Metadata:
========================
Original URL: https://sonic-explorer.skavel.cz
Prompt: "Write JavaScript code for an interactive sonic data visualization tool."
Generated: DETERMINISTIC_23a6703362451727
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Interactive Sonic Data Visualization Tool
 * 
 * This tool visualizes audio data in real-time using the Web Audio API.
 * It provides interactive controls to manipulate the visualization.
 */

class SonicVisualizer {
  constructor() {
    this.audioContext = null;
    this.analyser = null;
    this.dataArray = null;
    this.isPlaying = false;
    this.audioSource = null;
    this.canvas = null;
    this.canvasContext = null;
    this.animationId = null;
    this.fftSize = 2048;
    this.bufferLength = 0;
    this.visualizationType = 'waveform';
    this.colorScheme = 'default';
    this.gradient = null;
  }

  /**
   * Initialize the visualizer with a canvas element
   * @param {HTMLCanvasElement} canvas - The canvas element to render visualization
   */
  init(canvas) {
    if (!canvas) {
      throw new Error('Canvas element is required');
    }

    this.canvas = canvas;
    this.canvasContext = canvas.getContext('2d');
    this.setupAudioContext();
    this.setupEventListeners();
    this.resizeCanvas();
    window.addEventListener('resize', () => this.resizeCanvas());
  }

  /**
   * Setup Web Audio API context and analyser node
   */
  setupAudioContext() {
    try {
      this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
      this.analyser = this.audioContext.createAnalyser();
      this.analyser.fftSize = this.fftSize;
      this.bufferLength = this.analyser.frequencyBinCount;
      this.dataArray = new Uint8Array(this.bufferLength);
    } catch (error) {
      console.error('Error initializing audio context:', error);
      throw new Error('Audio context is not supported in this browser');
    }
  }

  /**
   * Setup event listeners for UI controls
   */
  setupEventListeners() {
    document.getElementById('start-btn').addEventListener('click', () => this.togglePlayback());
    document.getElementById('visualization-type').addEventListener('change', (e) => {
      this.visualizationType = e.target.value;
    });
    document.getElementById('color-scheme').addEventListener('change', (e) => {
      this.colorScheme = e.target.value;
      this.setupColorGradient();
    });
  }

  /**
   * Toggle audio playback
   */
  async togglePlayback() {
    if (!this.isPlaying) {
      try {
        await this.startPlayback();
      } catch (error) {
        console.error('Error starting playback:', error);
        alert('Failed to start playback. Please check your microphone permissions.');
      }
    } else {
      this.stopPlayback();
    }
  }

  /**
   * Start audio playback and visualization
   */
  async startPlayback() {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      this.audioSource = this.audioContext.createMediaStreamSource(stream);
      this.audioSource.connect(this.analyser);
      this.isPlaying = true;
      document.getElementById('start-btn').textContent = 'Stop';
      this.setupColorGradient();
      this.draw();
    } catch (error) {
      throw error;
    }
  }

  /**
   * Stop audio playback and visualization
   */
  stopPlayback() {
    if (this.audioSource) {
      this.audioSource.disconnect();
      this.audioSource = null;
    }
    cancelAnimationFrame(this.animationId);
    this.isPlaying = false;
    document.getElementById('start-btn').textContent = 'Start';
    this.clearCanvas();
  }

  /**
   * Setup color gradient based on selected scheme
   */
  setupColorGradient() {
    const width = this.canvas.width;
    const height = this.canvas.height;
    this.gradient = this.canvasContext.createLinearGradient(0, 0, width, height);

    switch (this.colorScheme) {
      case 'rainbow':
        this.gradient.addColorStop(0, 'red');
        this.gradient.addColorStop(0.2, 'orange');
        this.gradient.addColorStop(0.4, 'yellow');
        this.gradient.addColorStop(0.6, 'green');
        this.gradient.addColorStop(0.8, 'blue');
        this.gradient.addColorStop(1, 'purple');
        break;
      case 'ocean':
        this.gradient.addColorStop(0, '#00b4d8');
        this.gradient.addColorStop(0.5, '#0077b6');
        this.gradient.addColorStop(1, '#03045e');
        break;
      case 'fire':
        this.gradient.addColorStop(0, '#ff9a00');
        this.gradient.addColorStop(0.5, '#ff5e00');
        this.gradient.addColorStop(1, '#ff0000');
        break;
      default:
        this.gradient.addColorStop(0, '#00ff00');
        this.gradient.addColorStop(1, '#00ffff');
    }
  }

  /**
   * Main drawing loop for visualization
   */
  draw() {
    this.animationId = requestAnimationFrame(() => this.draw());

    this.analyser.getByteTimeDomainData(this.dataArray);
    this.clearCanvas();

    switch (this.visualizationType) {
      case 'waveform':
        this.drawWaveform();
        break;
      case 'frequency':
        this.analyser.getByteFrequencyData(this.dataArray);
        this.drawFrequencyBars();
        break;
      case 'circle':
        this.drawCircleVisualization();
        break;
      default:
        this.drawWaveform();
    }
  }

  /**
   * Draw waveform visualization
   */
  drawWaveform() {
    const width = this.canvas.width;
    const height = this.canvas.height;
    const sliceWidth = width / this.bufferLength;
    let x = 0;

    this.canvasContext.lineWidth = 2;
    this.canvasContext.strokeStyle = this.gradient;
    this.canvasContext.beginPath();

    for (let i = 0; i < this.bufferLength; i++) {
      const v = this.dataArray[i] / 128.0;
      const y = v * height / 2;

      if (i === 0) {
        this.canvasContext.moveTo(x, y);
      } else {
        this.canvasContext.lineTo(x, y);
      }

      x += sliceWidth;
    }

    this.canvasContext.lineTo(width, height / 2);
    this.canvasContext.stroke();
  }

  /**
   * Draw frequency bars visualization
   */
  drawFrequencyBars() {
    const width = this.canvas.width;
    const height = this.canvas.height;
    const barWidth = (width / this.bufferLength) * 2.5;
    let x = 0;

    for (let i = 0; i < this.bufferLength; i++) {
      const barHeight = (this.dataArray[i] / 255) * height;

      this.canvasContext.fillStyle = this.gradient;
      this.canvasContext.fillRect(x, height - barHeight, barWidth, barHeight);

      x += barWidth + 1;
    }
  }

  /**
   * Draw circular visualization
   */
  drawCircleVisualization() {
    const width = this.canvas.width;
    const height = this.canvas.height;
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) * 0.4;

    this.canvasContext.beginPath();
    this.canvasContext.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    this.canvasContext.strokeStyle = 'rgba(255, 255, 255, 0.2)';
    this.canvasContext.stroke();

    this.canvasContext.beginPath();
    for (let i = 0; i < this.bufferLength; i++) {
      const angle = (i / this.bufferLength) * Math.PI * 2;
      const value = this.dataArray[i] / 255;
      const pointRadius = value * radius * 0.5;

      const x = centerX + Math.cos(angle) * radius;
      const y = centerY + Math.sin(angle) * radius;

      if (i === 0) {
        this.canvasContext.moveTo(x, y);
      } else {
        this.canvasContext.lineTo(x, y);
      }

      this.canvasContext.beginPath();
      this.canvasContext.arc(x, y, pointRadius, 0, Math.PI * 2);
      this.canvasContext.fillStyle = this.gradient;
      this.canvasContext.fill();
    }
  }

  /**
   * Clear the canvas
   */
  clearCanvas() {
    this.canvasContext.fillStyle = 'rgba(0, 0, 0, 0.1)';
    this.canvasContext.fillRect(0, 0, this.canvas.width, this.canvas.height);
  }

  /**
