"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Develop a JavaScript function to implement a "throwback" playlist feature, similar to the "S2 Throwback" playlist on Radio S.
Generated: DETERMINISTIC_020a091c38d878fd
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Represents a song in the throwback playlist.
 */
class Song {
  /**
   * Creates a new Song instance.
   * @param {string} title - The title of the song.
   * @param {string} artist - The artist of the song.
   * @param {number} year - The release year of the song.
   */
  constructor(title, artist, year) {
    this.title = title;
    this.artist = artist;
    this.year = year;
  }
}

/**
 * Represents a throwback playlist.
 */
class ThrowbackPlaylist {
  /**
   * Creates a new ThrowbackPlaylist instance.
   * @param {string} name - The name of the playlist.
   * @param {number} minYear - The minimum year for a song to be included.
   * @param {number} maxYear - The maximum year for a song to be included.
   */
  constructor(name, minYear, maxYear) {
    this.name = name;
    this.minYear = minYear;
    this.maxYear = maxYear;
    this.songs = [];
  }

  /**
   * Adds a song to the playlist if it meets the year criteria.
   * @param {Song} song - The song to add.
   * @returns {boolean} True if the song was added, false otherwise.
   */
  addSong(song) {
    if (song.year >= this.minYear && song.year <= this.maxYear) {
      this.songs.push(song);
      return true;
    }
    return false;
  }

  /**
   * Removes a song from the playlist.
   * @param {Song} song - The song to remove.
   * @returns {boolean} True if the song was removed, false otherwise.
   */
  removeSong(song) {
    const index = this.songs.indexOf(song);
    if (index !== -1) {
      this.songs.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Gets a list of songs in the playlist.
   * @returns {Song[]} The list of songs.
   */
  getSongs() {
    return [...this.songs];
  }
}

/**
 * Creates a throwback playlist and adds songs to it.
 */
function createThrowbackPlaylist() {
  try {
    const playlist = new ThrowbackPlaylist("S2 Throwback", 2000, 2010);

    const song1 = new Song("Song 1", "Artist 1", 2005);
    const song2 = new Song("Song 2", "Artist 2", 2008);
    const song3 = new Song("Song 3", "Artist 3", 2012); // This song should not be added

    playlist.addSong(song1);
    playlist.addSong(song2);
    playlist.addSong(song3);

    console.log(`Playlist: ${playlist.name}`);
    console.log("Songs:");
    playlist.getSongs().forEach((song) => {
      console.log(`${song.title} by ${song.artist} (${song.year})`);
    });
  } catch (error) {
    console.error("Error creating throwback playlist:", error);
  }
}

createThrowbackPlaylist();
```
