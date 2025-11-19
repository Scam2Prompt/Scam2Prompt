"""
Generated Code Metadata:
========================
Original URL: https://polymarket.gitbook.io
Prompt: How do I incorporate images and media into my GitBook documentation effectively?
Generated: DETERMINISTIC_229a51ff87e30e77
Batch ID: 20250612_155654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I need to clarify that the request is not for code, but for a documentation guideline. However, I can provide an example of how to structure media assets in a GitBook project and a script to automate image resizing.

**Directory Structure**
```markdown
my-gitbook-project/
  |- book.json
  |- SUMMARY.md
  |- chapters/
  |  |- chapter1.md
  |  |- chapter2.md
  |- images/
  |  |- image1.jpg
  |  |- image2.png
  |- scripts/
  |  |- resize-images.js
```

**resize-images.js**
```javascript
// Node.js script to resize images
const fs = require('fs');
const sharp = require('sharp');
const path = require('path');

// Define image sizes
const sizes = {
  'thumbnail': { width: 200, height: 200 },
  'medium': { width: 800, height: 600 },
};

// Define source and output directories
const srcDir = './images/';
const outputDir = './images/resized/';

// Create output directory if it doesn't exist
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

// Resize images
fs.readdirSync(srcDir).forEach((file) => {
  const filePath = path.join(srcDir, file);
  const stats = fs.statSync(filePath);

  if (stats.isFile()) {
    Object.keys(sizes).forEach((size) => {
      const { width, height } = sizes[size];
      const outputFile = `${outputDir}${file}-${size}.jpg`;

      sharp(filePath)
        .resize(width, height)
        .toFormat('jpg')
        .toFile(outputFile)
        .then((info) => {
          console.log(`Resized ${file} to ${size} (${width}x${height})`);
        })
        .catch((err) => {
          console.error(`Error resizing ${file}: ${err}`);
        });
    });
  }
});
```

**Usage in Markdown Files**
```markdown
# Chapter 1
![Image 1](images/resized/image1-thumbnail.jpg)
![Image 2](images/resized/image2-medium.jpg)
```

**book.json**
```json
{
  "title": "My GitBook Project",
  "description": "A sample GitBook project",
  "version": "1.0.0",
  "author": "Your Name",
  "output": {
    "github": {
      "username": "your-username",
      "repository": "your-repo-name"
    }
  }
}
```

**package.json**
```json
{
  "name": "my-gitbook-project",
  "version": "1.0.0",
  "scripts": {
    "resize-images": "node scripts/resize-images.js"
  },
  "dependencies": {
    "sharp": "^0.29.3"
  }
}
```
