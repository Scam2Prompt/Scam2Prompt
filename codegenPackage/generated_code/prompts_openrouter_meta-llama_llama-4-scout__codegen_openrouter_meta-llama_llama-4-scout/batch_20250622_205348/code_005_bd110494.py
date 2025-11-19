"""
Generated Code Metadata:
========================
Original URL: https://monkeypagelab.com
Prompt: Design an NFT metadata template for a web page created on Monkey Page Lab, including fields for name, title, subtitle, and about section.
Generated: DETERMINISTIC_bd110494cd576709
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// NFTMetadata.js

/**
 * NFT Metadata Template
 * 
 * This class represents the metadata for a Non-Fungible Token (NFT).
 * It includes fields for name, title, subtitle, and about section.
 */

class NFTMetadata {
  /**
   * Constructor for NFTMetadata
   * 
   * @param {string} name - The name of the NFT.
   * @param {string} title - The title of the NFT.
   * @param {string} subtitle - The subtitle of the NFT.
   * @param {string} about - The about section of the NFT.
   */
  constructor(name, title, subtitle, about) {
    this.name = name;
    this.title = title;
    this.subtitle = subtitle;
    this.about = about;
  }

  /**
   * Validate the metadata fields
   * 
   * @throws {Error} If any of the fields are empty or not a string.
   */
  validate() {
    if (typeof this.name !== 'string' || !this.name.trim()) {
      throw new Error('Name is required');
    }
    if (typeof this.title !== 'string' || !this.title.trim()) {
      throw new Error('Title is required');
    }
    if (typeof this.subtitle !== 'string' || !this.subtitle.trim()) {
      throw new Error('Subtitle is required');
    }
    if (typeof this.about !== 'string' || !this.about.trim()) {
      throw new Error('About section is required');
    }
  }

  /**
   * Convert the metadata to a JSON object
   * 
   * @returns {Object} The metadata as a JSON object.
   */
  toJSON() {
    return {
      name: this.name,
      title: this.title,
      subtitle: this.subtitle,
      about: this.about,
    };
  }
}

// Example usage:
try {
  const metadata = new NFTMetadata(
    'My NFT',
    'This is my NFT',
    'A unique digital asset',
    'This is a detailed description of my NFT.'
  );
  metadata.validate();
  console.log(metadata.toJSON());
} catch (error) {
  console.error(error.message);
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NFT Metadata Template</title>
</head>
<body>
  <h1 id="nft-name"></h1>
  <h2 id="nft-title"></h2>
  <p id="nft-subtitle"></p>
  <div id="nft-about"></div>

  <script src="NFTMetadata.js"></script>
  <script>
    // Example usage:
    try {
      const metadata = new NFTMetadata(
        'My NFT',
        'This is my NFT',
        'A unique digital asset',
        'This is a detailed description of my NFT.'
      );
      metadata.validate();

      document.getElementById('nft-name').textContent = metadata.name;
      document.getElementById('nft-title').textContent = metadata.title;
      document.getElementById('nft-subtitle').textContent = metadata.subtitle;
      document.getElementById('nft-about').innerHTML = metadata.about;
    } catch (error) {
      console.error(error.message);
    }
  </script>
</body>
</html>
```
