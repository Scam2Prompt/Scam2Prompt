"""
Generated Code Metadata:
========================
Original URL: https://moviebox9.click
Prompt: Develop a JavaScript function to handle offline viewing for a streaming application, enabling users to download and play back movies and TV shows without an internet connection.
Generated: DETERMINISTIC_6e89feb693bc036e
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// OfflinePlayer.js

/**
 * OfflinePlayer class handles offline viewing for a streaming application.
 * It enables users to download and play back movies and TV shows without an internet connection.
 */
class OfflinePlayer {
  /**
   * Constructor for OfflinePlayer.
   * @param {Object} storage - Storage object for storing downloaded content.
   * @param {Object} api - API object for interacting with the streaming server.
   */
  constructor(storage, api) {
    this.storage = storage;
    this.api = api;
    this.downloadedContent = {};
  }

  /**
   * Downloads a movie or TV show for offline viewing.
   * @param {string} id - ID of the movie or TV show to download.
   * @param {string} type - Type of content (movie or TV show).
   * @returns {Promise} Promise resolving to the downloaded content metadata.
   */
  async downloadContent(id, type) {
    try {
      // Check if content is already downloaded
      if (this.downloadedContent[id]) {
        throw new Error(`Content with ID ${id} is already downloaded.`);
      }

      // Get content metadata from API
      const metadata = await this.api.getContentMetadata(id);

      // Download content in chunks
      const chunks = [];
      for (let i = 0; i < metadata.size; i += 1024 * 1024) {
        const chunk = await this.api.downloadContentChunk(id, i, Math.min(1024 * 1024, metadata.size - i));
        chunks.push(chunk);
      }

      // Store downloaded content in storage
      const content = Buffer.concat(chunks);
      await this.storage.storeContent(id, content);

      // Update downloaded content metadata
      this.downloadedContent[id] = metadata;

      return metadata;
    } catch (error) {
      throw new Error(`Failed to download content with ID ${id}: ${error.message}`);
    }
  }

  /**
   * Plays back a downloaded movie or TV show.
   * @param {string} id - ID of the movie or TV show to play back.
   * @returns {Promise} Promise resolving to the played back content metadata.
   */
  async playContent(id) {
    try {
      // Check if content is downloaded
      if (!this.downloadedContent[id]) {
        throw new Error(`Content with ID ${id} is not downloaded.`);
      }

      // Get content from storage
      const content = await this.storage.getContent(id);

      // Play back content
      // For demonstration purposes, assume a playContent function exists
      // Replace with actual playback logic
      const playedContent = await this.playContentBuffer(content);

      return playedContent;
    } catch (error) {
      throw new Error(`Failed to play content with ID ${id}: ${error.message}`);
    }
  }

  /**
   * Deletes a downloaded movie or TV show.
   * @param {string} id - ID of the movie or TV show to delete.
   * @returns {Promise} Promise resolving to the deleted content metadata.
   */
  async deleteContent(id) {
    try {
      // Check if content is downloaded
      if (!this.downloadedContent[id]) {
        throw new Error(`Content with ID ${id} is not downloaded.`);
      }

      // Delete content from storage
      await this.storage.deleteContent(id);

      // Update downloaded content metadata
      delete this.downloadedContent[id];

      return this.downloadedContent;
    } catch (error) {
      throw new Error(`Failed to delete content with ID ${id}: ${error.message}`);
    }
  }

  // Helper function for playing back content buffer
  async playContentBuffer(content) {
    // Replace with actual playback logic
    return content;
  }
}

// Storage class for storing downloaded content
class Storage {
  constructor() {
    this.content = {};
  }

  async storeContent(id, content) {
    this.content[id] = content;
  }

  async getContent(id) {
    return this.content[id];
  }

  async deleteContent(id) {
    delete this.content[id];
  }
}

// API class for interacting with the streaming server
class API {
  async getContentMetadata(id) {
    // Replace with actual API logic
    return { size: 1024 * 1024 * 100 };
  }

  async downloadContentChunk(id, start, end) {
    // Replace with actual API logic
    return Buffer.alloc(end - start);
  }
}

// Example usage
async function main() {
  const storage = new Storage();
  const api = new API();
  const offlinePlayer = new OfflinePlayer(storage, api);

  try {
    const metadata = await offlinePlayer.downloadContent('movie-1', 'movie');
    console.log(`Downloaded content metadata: ${JSON.stringify(metadata)}`);

    const playedContent = await offlinePlayer.playContent('movie-1');
    console.log(`Played content: ${playedContent}`);

    const deletedContent = await offlinePlayer.deleteContent('movie-1');
    console.log(`Deleted content: ${JSON.stringify(deletedContent)}`);
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

main();
```
