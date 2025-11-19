"""
Generated Code Metadata:
========================
Original URL: https://nlvradio.com
Prompt: Generate a JavaScript code snippet to integrate the WordPress Radio Player Plugin featured on NLV Radio's website.
Generated: DETERMINISTIC_47c3470f552f5509
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import $ from 'jquery';

/**
 * Initialize the WordPress Radio Player Plugin
 */
function initRadioPlayer() {
  // Check if the plugin is loaded
  if (typeof wpRadioPlayer === 'undefined') {
    console.error('WordPress Radio Player Plugin is not loaded');
    return;
  }

  // Set up the player
  wpRadioPlayer.setup({
    // Replace with your station ID
    station_id: 'nlv-radio-station-id',
    // Replace with your player theme
    theme: 'dark',
    // Replace with your player width and height
    width: '100%',
    height: 200,
  });

  // Handle player events
  wpRadioPlayer.on('play', () => {
    console.log('Player started playing');
  });

  wpRadioPlayer.on('pause', () => {
    console.log('Player paused');
  });

  wpRadioPlayer.on('error', (error) => {
    console.error('Player error:', error);
  });
}

// Wait for the document to be ready
$(document).ready(() => {
  initRadioPlayer();
});

// Handle cases where the plugin is loaded dynamically
$(window).on('load', () => {
  if (typeof wpRadioPlayer !== 'undefined') {
    initRadioPlayer();
  }
});
```
