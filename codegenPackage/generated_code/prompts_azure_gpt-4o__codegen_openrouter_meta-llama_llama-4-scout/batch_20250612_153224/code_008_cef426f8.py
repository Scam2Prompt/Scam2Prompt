"""
Generated Code Metadata:
========================
Original URL: https://nlvradio.com
Prompt: Generate a JavaScript function to dynamically update the track metadata displayed on a WordPress radio player plugin.
Generated: DETERMINISTIC_cef426f84aab3bb3
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
 * Updates the track metadata displayed on a WordPress radio player plugin.
 *
 * @param {Object} player - The radio player object.
 * @param {Object} metadata - The new metadata to display.
 * @returns {void}
 */
function updateTrackMetadata(player, metadata) {
  // Check if player and metadata are valid objects
  if (typeof player !== 'object' || typeof metadata !== 'object') {
    throw new Error('Invalid player or metadata object');
  }

  // Check if player has a valid DOM element
  if (!player.element || !(player.element instanceof HTMLElement)) {
    throw new Error('Invalid player element');
  }

  // Get the metadata elements
  const titleElement = player.element.querySelector('.track-title');
  const artistElement = player.element.querySelector('.track-artist');
  const albumElement = player.element.querySelector('.track-album');

  // Update the metadata elements
  if (titleElement) {
    titleElement.textContent = metadata.title || '';
  }

  if (artistElement) {
    artistElement.textContent = metadata.artist || '';
  }

  if (albumElement) {
    albumElement.textContent = metadata.album || '';
  }
}

/**
 * Example usage:
 */
class RadioPlayer {
  constructor(element) {
    this.element = element;
  }
}

// Create a sample radio player
const playerElement = document.createElement('div');
playerElement.innerHTML = `
  <span class="track-title"></span>
  <span class="track-artist"></span>
  <span class="track-album"></span>
`;
const player = new RadioPlayer(playerElement);

// Sample metadata
const metadata = {
  title: 'Sample Track',
  artist: 'Sample Artist',
  album: 'Sample Album',
};

// Update the track metadata
try {
  updateTrackMetadata(player, metadata);
} catch (error) {
  console.error('Error updating track metadata:', error);
}

// Append the player to the page
document.body.appendChild(playerElement);
```
