"""
Generated Code Metadata:
========================
Original URL: https://co-djs.com
Prompt: Create a JavaScript code example that enables guests to send song requests to a DJ booth via a mobile-friendly web app, similar to the online request system mentioned on the site.
Generated: DETERMINISTIC_52db35dbd7901429
Batch ID: 20250612_155332
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// songRequest.js

/**
 * Song Request System
 * 
 * Enables guests to send song requests to a DJ booth via a mobile-friendly web app.
 */

// Define the SongRequest class
class SongRequest {
  /**
   * Constructor
   * @param {string} name - Guest's name
   * @param {string} songTitle - Song title
   * @param {string} songArtist - Song artist
   */
  constructor(name, songTitle, songArtist) {
    this.name = name;
    this.songTitle = songTitle;
    this.songArtist = songArtist;
  }
}

// Define the DJBooth class
class DJBooth {
  /**
   * Constructor
   */
  constructor() {
    this.songRequests = [];
  }

  /**
   * Add a song request
   * @param {SongRequest} songRequest - Song request to add
   */
  addSongRequest(songRequest) {
    this.songRequests.push(songRequest);
  }

  /**
   * Get all song requests
   * @returns {SongRequest[]} Array of song requests
   */
  getSongRequests() {
    return this.songRequests;
  }
}

// Define the SongRequestForm class
class SongRequestForm {
  /**
   * Constructor
   * @param {DJBooth} djBooth - DJ booth instance
   */
  constructor(djBooth) {
    this.djBooth = djBooth;
    this.form = document.getElementById('song-request-form');
    this.nameInput = document.getElementById('name');
    this.songTitleInput = document.getElementById('song-title');
    this.songArtistInput = document.getElementById('song-artist');
    this.submitButton = document.getElementById('submit');

    // Add event listener to form submission
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
  }

  /**
   * Handle form submission
   * @param {Event} e - Form submission event
   */
  handleSubmit(e) {
    e.preventDefault();

    // Get input values
    const name = this.nameInput.value.trim();
    const songTitle = this.songTitleInput.value.trim();
    const songArtist = this.songArtistInput.value.trim();

    // Validate input values
    if (name === '' || songTitle === '' || songArtist === '') {
      alert('Please fill out all fields.');
      return;
    }

    // Create a new song request
    const songRequest = new SongRequest(name, songTitle, songArtist);

    // Add song request to DJ booth
    this.djBooth.addSongRequest(songRequest);

    // Clear input fields
    this.nameInput.value = '';
    this.songTitleInput.value = '';
    this.songArtistInput.value = '';

    // Display success message
    alert('Song request sent successfully!');
  }
}

// Initialize DJ booth and song request form
const djBooth = new DJBooth();
const songRequestForm = new SongRequestForm(djBooth);

// Display song requests
const songRequestsElement = document.getElementById('song-requests');

function displaySongRequests() {
  const songRequests = djBooth.getSongRequests();
  const songRequestsHtml = songRequests.map((songRequest, index) => {
    return `
      <li>
        <strong>${songRequest.name}</strong> - ${songRequest.songTitle} by ${songRequest.songArtist}
      </li>
    `;
  }).join('');
  songRequestsElement.innerHTML = `<ul>${songRequestsHtml}</ul>`;
}

// Update song requests display every 5 seconds
setInterval(displaySongRequests, 5000);

// Initial display of song requests
displaySongRequests();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Song Request System</title>
  <style>
    /* Add some basic styling */
    body {
      font-family: Arial, sans-serif;
    }
    #song-request-form {
      width: 50%;
      margin: 40px auto;
    }
    #song-requests {
      width: 50%;
      margin: 40px auto;
    }
  </style>
</head>
<body>
  <h1>Song Request System</h1>
  <form id="song-request-form">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name"><br><br>
    <label for="song-title">Song Title:</label>
    <input type="text" id="song-title" name="song-title"><br><br>
    <label for="song-artist">Song Artist:</label>
    <input type="text" id="song-artist" name="song-artist"><br><br>
    <input type="submit" id="submit" value="Submit">
  </form>
  <div id="song-requests"></div>

  <script src="songRequest.js"></script>
</body>
</html>
```
