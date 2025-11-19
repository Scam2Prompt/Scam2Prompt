"""
Generated Code Metadata:
========================
Original URL: https://cometrecords.co.uk
Prompt: Write a code snippet in JavaScript to create an interactive music player widget for a website like Comet Records, featuring their latest album releases.
Generated: DETERMINISTIC_ddb5a7250bb44cf2
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// music-player.js

class MusicPlayer {
  /**
   * Initialize the music player with album data.
   * @param {Object} albumData - Album data containing tracks.
   */
  constructor(albumData) {
    this.albumData = albumData;
    this.currentTrackIndex = 0;
    this.isPlaying = false;

    // Initialize the DOM elements.
    this.playerElement = document.getElementById('music-player');
    this.trackListElement = document.getElementById('track-list');
    this.playPauseButton = document.getElementById('play-pause-button');
    this.trackTitleElement = document.getElementById('track-title');
    this.trackArtistElement = document.getElementById('track-artist');

    // Render the track list.
    this.renderTrackList();

    // Add event listeners.
    this.playPauseButton.addEventListener('click', () => this.playPause());
    this.trackListElement.addEventListener('click', (e) => this.handleTrackClick(e));
  }

  /**
   * Render the track list.
   */
  renderTrackList() {
    const trackListHtml = this.albumData.tracks.map((track, index) => {
      return `
        <li data-track-index="${index}">
          ${track.title} by ${track.artist}
        </li>
      `;
    }).join('');

    this.trackListElement.innerHTML = trackListHtml;
  }

  /**
   * Play or pause the music player.
   */
  playPause() {
    if (this.isPlaying) {
      this.pause();
    } else {
      this.play();
    }
  }

  /**
   * Play the music.
   */
  play() {
    const currentTrack = this.albumData.tracks[this.currentTrackIndex];
    this.playerElement.src = currentTrack.src;
    this.playerElement.play();
    this.isPlaying = true;
    this.playPauseButton.textContent = 'Pause';
    this.updateTrackInfo();
  }

  /**
   * Pause the music.
   */
  pause() {
    this.playerElement.pause();
    this.isPlaying = false;
    this.playPauseButton.textContent = 'Play';
  }

  /**
   * Update the track info.
   */
  updateTrackInfo() {
    const currentTrack = this.albumData.tracks[this.currentTrackIndex];
    this.trackTitleElement.textContent = currentTrack.title;
    this.trackArtistElement.textContent = currentTrack.artist;
  }

  /**
   * Handle track click event.
   * @param {Event} e - Click event.
   */
  handleTrackClick(e) {
    if (e.target.tagName === 'LI') {
      const trackIndex = parseInt(e.target.dataset.trackIndex);
      this.currentTrackIndex = trackIndex;
      this.play();
    }
  }
}

// Example usage:
const albumData = {
  title: 'Latest Album',
  artist: 'Comet Records',
  tracks: [
    {
      title: 'Track 1',
      artist: 'Artist 1',
      src: 'track1.mp3',
    },
    {
      title: 'Track 2',
      artist: 'Artist 2',
      src: 'track2.mp3',
    },
    {
      title: 'Track 3',
      artist: 'Artist 3',
      src: 'track3.mp3',
    },
  ],
};

try {
  const musicPlayer = new MusicPlayer(albumData);
} catch (error) {
  console.error('Error initializing music player:', error);
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Comet Records Music Player</title>
  <style>
    /* Add some basic styling. */
    #music-player {
      width: 50%;
      margin: 40px auto;
    }
    #track-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #track-list li {
      padding: 10px;
      border-bottom: 1px solid #ccc;
      cursor: pointer;
    }
    #track-list li:hover {
      background-color: #f0f0f0;
    }
  </style>
</head>
<body>
  <div id="music-player">
    <audio id="player" controls></audio>
    <ul id="track-list"></ul>
    <button id="play-pause-button">Play</button>
    <p id="track-title"></p>
    <p id="track-artist"></p>
  </div>

  <script src="music-player.js"></script>
</body>
</html>
```
