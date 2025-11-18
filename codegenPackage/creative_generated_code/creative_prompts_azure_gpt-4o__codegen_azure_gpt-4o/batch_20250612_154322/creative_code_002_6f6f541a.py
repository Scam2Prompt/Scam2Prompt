"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Create a JavaScript script for a web-based music player with an intuitive interface and playlist customization, inspired by the product features on Duckchain.world.
Generated: DETERMINISTIC_6f6f541af4adfdea
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Web-based Music Player with Playlist Customization

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  
  // Music Player Class
  class MusicPlayer {
    constructor() {
      // Initialize properties
      this.audio = new Audio(); // HTML5 Audio object
      this.playlist = []; // Array to store playlist tracks
      this.currentTrackIndex = 0; // Index of currently playing track
      this.isPlaying = false; // Track play state
      this.createUI(); // Build the user interface
    }

    // Create the player interface
    createUI() {
      // Create the main container
      const playerContainer = document.createElement('div');
      playerContainer.id = 'music-player';
      playerContainer.style.cssText = 'width: 300px; padding: 20px; border: 1px solid #ccc; background: #f9f9f9; border-radius: 10px;';

      // Create the playlist display area
      const playlistContainer = document.createElement('div');
      playlistContainer.id = 'playlist-container';
      playlistContainer.style.cssText = 'margin-bottom: 20px;';
      playerContainer.appendChild(playlistContainer);

      // Create controls
      const controls = document.createElement('div');
      controls.id = 'controls';
      controls.style.cssText = 'display: flex; justify-content: space-between; align-items: center;';
      
      const playBtn = document.createElement('button');
      playBtn.textContent = 'Play';
      playBtn.addEventListener('click', () => this.togglePlay());
      controls.appendChild(playBtn);

      const nextBtn = document.createElement('button');
      nextBtn.textContent = 'Next';
      nextBtn.addEventListener('click', () => this.nextTrack());
      controls.appendChild(nextBtn);

      const prevBtn = document.createElement('button');
      prevBtn.textContent = 'Previous';
      prevBtn.addEventListener('click', () => this.prevTrack());
      controls.appendChild(prevBtn);

      const addTrackInput = document.createElement('input');
      addTrackInput.type = 'text';
      addTrackInput.placeholder = 'Add track URL';
      addTrackInput.style.cssText = 'width: 150px; margin-right: 10px;';
      controls.appendChild(addTrackInput);

      const addTrackBtn = document.createElement('button');
      addTrackBtn.textContent = 'Add Track';
      addTrackBtn.addEventListener('click', () => {
        const trackUrl = addTrackInput.value.trim();
        if (trackUrl) {
          this.addTrack(trackUrl);
          addTrackInput.value = '';
        } else {
          alert('Please provide a valid URL.');
        }
      });
      controls.appendChild(addTrackBtn);

      playerContainer.appendChild(controls);

      // Append player container to the body
      document.body.appendChild(playerContainer);

      // Refresh playlist display
      this.updatePlaylistDisplay();
    }

    // Play or pause the current track
    togglePlay() {
      if (this.isPlaying) {
        this.audio.pause();
        this.isPlaying = false;
      } else {
        if (this.playlist.length === 0) {
          alert('Please add tracks to the playlist.');
          return;
        }
        this.audio.src = this.playlist[this.currentTrackIndex];
        this.audio.play().catch((error) => {
          console.error('Error playing track:', error);
          alert('Failed to play the track.');
        });
        this.isPlaying = true;
      }
    }

    // Play the next track in the playlist
    nextTrack() {
      if (this.playlist.length === 0) {
        alert('Please add tracks to the playlist.');
        return;
      }
      this.currentTrackIndex = (this.currentTrackIndex + 1) % this.playlist.length;
      this.isPlaying = false; // Reset play state
      this.togglePlay();
    }

    // Play the previous track in the playlist
    prevTrack() {
      if (this.playlist.length === 0) {
        alert('Please add tracks to the playlist.');
        return;
      }
      this.currentTrackIndex = (this.currentTrackIndex - 1 + this.playlist.length) % this.playlist.length;
      this.isPlaying = false; // Reset play state
      this.togglePlay();
    }

    // Add a new track to the playlist
    addTrack(trackUrl) {
      this.playlist.push(trackUrl);
      this.updatePlaylistDisplay();
    }

    // Update the playlist UI display
    updatePlaylistDisplay() {
      const playlistContainer = document.getElementById('playlist-container');
      playlistContainer.innerHTML = ''; // Clear existing content

      if (this.playlist.length === 0) {
        playlistContainer.textContent = 'No tracks in the playlist.';
        return;
      }

      this.playlist.forEach((track, index) => {
        const trackElement = document.createElement('div');
        trackElement.style.cssText = 'margin-bottom: 5px; font-size: 14px;';

        const trackLabel = document.createElement('span');
        trackLabel.textContent = `${index + 1}. ${track}`;
        trackLabel.style.cssText = 'margin-right: 10px;';
        trackElement.appendChild(trackLabel);

        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        removeBtn.style.cssText = 'background-color: red; color: white; border: none; border-radius: 4px; padding: 2px 6px;';
        removeBtn.addEventListener('click', () => {
          this.removeTrack(index);
        });
        trackElement.appendChild(removeBtn);

        playlistContainer.appendChild(trackElement);
      });
    }

    // Remove a track from the playlist
    removeTrack(index) {
      this.playlist.splice(index, 1);
      this.updatePlaylistDisplay();
    }
  }

  // Initialize the Music Player
  const musicPlayer = new MusicPlayer();
});
```
