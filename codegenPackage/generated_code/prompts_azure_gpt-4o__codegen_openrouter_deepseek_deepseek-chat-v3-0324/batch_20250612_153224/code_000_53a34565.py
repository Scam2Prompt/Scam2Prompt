"""
Generated Code Metadata:
========================
Original URL: https://nlvradio.com
Prompt: Write JavaScript code to integrate a WordPress radio player plugin into a website, ensuring compatibility with HTML5 audio streaming.
Generated: DETERMINISTIC_53a3456556aa4389
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * WordPress Radio Player Integration
 * 
 * This script integrates a WordPress radio player plugin with HTML5 audio streaming.
 * It handles player initialization, playback controls, and error handling.
 */

(function($) {
    'use strict';

    // Configuration
    const config = {
        playerContainer: '.radio-player-container',
        playButton: '.radio-play-button',
        pauseButton: '.radio-pause-button',
        volumeControl: '.radio-volume-control',
        stationInfo: '.radio-station-info',
        streamUrl: '', // Will be populated from WordPress
        defaultVolume: 0.7
    };

    // Initialize the radio player
    class RadioPlayer {
        constructor(config) {
            this.config = config;
            this.audio = new Audio();
            this.isPlaying = false;
            this.volume = config.defaultVolume;
            this.init();
        }

        // Initialize player and event listeners
        init() {
            // Get stream URL from WordPress data attribute
            this.config.streamUrl = $(this.config.playerContainer).data('stream-url');
            
            if (!this.config.streamUrl) {
                console.error('Stream URL not provided');
                return;
            }

            this.audio.src = this.config.streamUrl;
            this.audio.volume = this.volume;
            this.audio.preload = 'none';

            // Set up event listeners
            this.setupEventListeners();
        }

        // Set up all event listeners
        setupEventListeners() {
            // Play button
            $(this.config.playButton).on('click', (e) => {
                e.preventDefault();
                this.play();
            });

            // Pause button
            $(this.config.pauseButton).on('click', (e) => {
                e.preventDefault();
                this.pause();
            });

            // Volume control
            $(this.config.volumeControl).on('input', (e) => {
                this.setVolume(parseFloat(e.target.value));
            });

            // Audio events
            this.audio.addEventListener('playing', () => {
                this.isPlaying = true;
                this.updateUI();
            });

            this.audio.addEventListener('pause', () => {
                this.isPlaying = false;
                this.updateUI();
            });

            this.audio.addEventListener('error', (e) => {
                console.error('Audio error:', e);
                this.handleError();
            });

            this.audio.addEventListener('stalled', () => {
                console.warn('Stream stalled, attempting to reconnect...');
                this.reconnect();
            });
        }

        // Play the stream
        play() {
            if (!this.isPlaying) {
                this.audio.play()
                    .catch(error => {
                        console.error('Playback failed:', error);
                        this.handleError();
                    });
            }
        }

        // Pause the stream
        pause() {
            if (this.isPlaying) {
                this.audio.pause();
            }
        }

        // Set volume (0-1)
        setVolume(volume) {
            this.volume = volume;
            this.audio.volume = volume;
        }

        // Update UI elements based on player state
        updateUI() {
            if (this.isPlaying) {
                $(this.config.playButton).hide();
                $(this.config.pauseButton).show();
            } else {
                $(this.config.playButton).show();
                $(this.config.pauseButton).hide();
            }
        }

        // Handle errors
        handleError() {
            this.isPlaying = false;
            this.updateUI();
            $(this.config.stationInfo).text('Error: Unable to play stream');
        }

        // Attempt to reconnect
        reconnect() {
            this.pause();
            setTimeout(() => {
                this.audio.src = this.config.streamUrl;
                this.play();
            }, 3000);
        }
    }

    // Initialize when DOM is ready
    $(document).ready(function() {
        const player = new RadioPlayer(config);
        
        // Make player instance available globally if needed
        window.radioPlayer = player;
    });

})(jQuery);
```
