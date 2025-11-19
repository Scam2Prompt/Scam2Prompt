"""
Generated Code Metadata:
========================
Original URL: https://sergiupopa.com
Prompt: Generate a code snippet for a simple accordion-based music player inspired by Sergiu Popa's performances.
Generated: DETERMINISTIC_2cf4d17ffce314db
Batch ID: 20250622_211721
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://code.jquery.com/jquery-3.2.1.slim.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// music-player.js

class MusicPlayer {
  /**
   * Initialize the music player with a list of songs.
   * @param {Array<Object>} songs - List of songs with title and src attributes.
   */
  constructor(songs) {
    this.songs = songs;
    this.currentSongIndex = 0;
    this.audioElement = new Audio();
    this.accordionElement = null;
  }

  /**
   * Render the music player accordion.
   */
  renderAccordion() {
    const accordionHtml = `
      <div class="accordion" id="music-player-accordion">
        ${this.songs.map((song, index) => `
          <div class="card">
            <div class="card-header">
              <h2 class="mb-0">
                <button class="btn btn-link btn-block text-left" type="button" data-toggle="collapse" data-target="#collapse-${index}">
                  ${song.title}
                </button>
              </h2>
            </div>
            <div id="collapse-${index}" class="collapse" data-parent="#music-player-accordion">
              <div class="card-body">
                <audio src="${song.src}" controls></audio>
              </div>
            </div>
          </div>
        `).join('')}
      </div>
    `;
    document.getElementById('music-player-container').innerHTML = accordionHtml;

    // Add event listeners to the accordion buttons
    this.accordionElement = document.getElementById('music-player-accordion');
    this.accordionElement.addEventListener('show.bs.collapse', (event) => {
      const target = event.target;
      const songIndex = Array.prototype.indexOf.call(target.parentNode.parentNode.children, target.parentNode);
      this.playSong(songIndex);
    });
  }

  /**
   * Play a song at the specified index.
   * @param {number} index - Index of the song to play.
   */
  playSong(index) {
    if (index >= 0 && index < this.songs.length) {
      this.currentSongIndex = index;
      this.audioElement.src = this.songs[index].src;
      this.audioElement.play();
    } else {
      console.error('Invalid song index');
    }
  }

  /**
   * Initialize the music player.
   */
  init() {
    try {
      this.renderAccordion();
    } catch (error) {
      console.error('Error initializing music player:', error);
    }
  }
}

// Example usage
const songs = [
  { title: 'Song 1', src: 'song1.mp3' },
  { title: 'Song 2', src: 'song2.mp3' },
  { title: 'Song 3', src: 'song3.mp3' },
];

const musicPlayer = new MusicPlayer(songs);
musicPlayer.init();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Music Player</title>
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
  <style>
    #music-player-container {
      max-width: 600px;
      margin: 40px auto;
    }
  </style>
</head>
<body>
  <div id="music-player-container"></div>
  <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
  <script src="music-player.js"></script>
</body>
</html>
```
