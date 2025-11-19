"""
Generated Code Metadata:
========================
Original URL: https://atlasnavi.pages.dev
Prompt: Write JavaScript code to implement a live stream feature that shares road trip video footage in real-time, inspired by Atlas Navi's functionality.
Generated: DETERMINISTIC_7a530885c2a617fe
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// LiveStream.js - Real-time road trip video streaming functionality

class LiveStream {
  /**
   * Initialize the live stream with configuration
   * @param {Object} config - Configuration object
   * @param {string} config.streamId - Unique identifier for the stream
   * @param {HTMLElement} config.videoElement - HTML video element to display stream
   * @param {string} [config.serverUrl='wss://stream.example.com'] - WebSocket server URL
   * @param {Object} [config.streamConstraints] - MediaStreamConstraints for getUserMedia
   */
  constructor(config) {
    if (!config.streamId || !config.videoElement) {
      throw new Error('streamId and videoElement are required');
    }

    this.streamId = config.streamId;
    this.videoElement = config.videoElement;
    this.serverUrl = config.serverUrl || 'wss://stream.example.com';
    this.streamConstraints = config.streamConstraints || {
      video: {
        width: { ideal: 1280 },
        height: { ideal: 720 },
        facingMode: 'environment'
      },
      audio: true
    };

    this.mediaStream = null;
    this.mediaRecorder = null;
    this.socket = null;
    this.recordingChunks = [];
    this.isStreaming = false;
    this.reconnectAttempts = 0;
    this.maxReconnectAttempts = 5;
  }

  /**
   * Initialize WebSocket connection
   * @private
   */
  _initSocket() {
    this.socket = new WebSocket(`${this.serverUrl}/${this.streamId}`);

    this.socket.onopen = () => {
      console.log('WebSocket connection established');
      this.reconnectAttempts = 0;
      this._startMediaStream();
    };

    this.socket.onclose = (event) => {
      console.log('WebSocket disconnected:', event.reason);
      if (!event.wasClean && this.reconnectAttempts < this.maxReconnectAttempts) {
        this.reconnectAttempts++;
        const delay = Math.min(1000 * this.reconnectAttempts, 5000);
        console.log(`Reconnecting in ${delay}ms...`);
        setTimeout(() => this._initSocket(), delay);
      } else {
        this._handleError('Failed to establish WebSocket connection');
      }
    };

    this.socket.onerror = (error) => {
      console.error('WebSocket error:', error);
      this._handleError('WebSocket connection error');
    };
  }

  /**
   * Start media stream from device camera
   * @private
   */
  async _startMediaStream() {
    try {
      this.mediaStream = await navigator.mediaDevices.getUserMedia(this.streamConstraints);
      this.videoElement.srcObject = this.mediaStream;
      this.videoElement.play().catch(err => {
        this._handleError(`Video playback error: ${err.message}`);
      });

      this._setupMediaRecorder();
      this.isStreaming = true;
    } catch (err) {
      this._handleError(`Media stream error: ${err.message}`);
    }
  }

  /**
   * Setup media recorder to capture and send video chunks
   * @private
   */
  _setupMediaRecorder() {
    if (!this.mediaStream) return;

    this.mediaRecorder = new MediaRecorder(this.mediaStream, {
      mimeType: 'video/webm;codecs=vp9,opus',
      videoBitsPerSecond: 2500000
    });

    this.mediaRecorder.ondataavailable = (event) => {
      if (event.data.size > 0 && this.socket?.readyState === WebSocket.OPEN) {
        this.socket.send(event.data);
      }
    };

    this.mediaRecorder.onerror = (event) => {
      console.error('MediaRecorder error:', event.error);
      this._handleError('Media recording error');
    };

    // Send data every 1 second
    this.mediaRecorder.start(1000);
  }

  /**
   * Handle errors and clean up resources
   * @private
   * @param {string} message - Error message
   */
  _handleError(message) {
    console.error(message);
    this.stop();
    // In a real app, you would notify the user and/or retry
  }

  /**
   * Start the live stream
   */
  start() {
    if (this.isStreaming) {
      console.warn('Stream is already running');
      return;
    }

    if (!navigator.mediaDevices || !window.MediaRecorder) {
      this._handleError('Media devices or MediaRecorder not supported');
      return;
    }

    this._initSocket();
  }

  /**
   * Stop the live stream and clean up resources
   */
  stop() {
    this.isStreaming = false;

    if (this.mediaRecorder && this.mediaRecorder.state !== 'inactive') {
      this.mediaRecorder.stop();
    }

    if (this.mediaStream) {
      this.mediaStream.getTracks().forEach(track => track.stop());
    }

    if (this.socket && this.socket.readyState === WebSocket.OPEN) {
      this.socket.close();
    }

    this.mediaRecorder = null;
    this.mediaStream = null;
    this.socket = null;
    this.recordingChunks = [];

    if (this.videoElement.srcObject) {
      this.videoElement.srcObject = null;
    }
  }

  /**
   * Toggle stream between front and rear camera
   */
  async toggleCamera() {
    if (!this.isStreaming) return;

    this.stop();
    this.streamConstraints.video.facingMode = 
      this.streamConstraints.video.facingMode === 'user' ? 'environment' : 'user';
    this.start();
  }

  /**
   * Get current stream status
   * @returns {Object} Stream status
   */
  getStatus() {
    return {
      isStreaming: this.isStreaming,
      streamId: this.streamId,
      videoEnabled: this.mediaStream?.getVideoTracks()[0]?.enabled || false,
      audioEnabled: this.mediaStream?.getAudioTracks()[0]?.enabled || false,
      cameraFacing: this.streamConstraints.video.facingMode
    };
  }

  /**
   * Toggle video track on/off
   */
  toggleVideo() {
    if (!this.mediaStream) return;
    const videoTrack = this.mediaStream.getVideoTracks()[0];
    if (videoTrack) {
      videoTrack.enabled = !videoTrack.enabled;
    }
  }

  /**
   * Toggle audio track on/off
   */
  toggleAudio() {
    if (!this.mediaStream) return;
    const audioTrack = this.mediaStream.getAudioTracks()[0];
    if (audioTrack) {
      audioTrack.enabled = !audioTrack.enabled;
    }
  }
}

// Example usage:
// const liveStream = new LiveStream({
//   streamId: 'user123-roadtrip',
//   videoElement: document.getElementById('videoElement'),
//   serverUrl: 'wss://your-stream-server.com'
// });
// liveStream.start();
```
