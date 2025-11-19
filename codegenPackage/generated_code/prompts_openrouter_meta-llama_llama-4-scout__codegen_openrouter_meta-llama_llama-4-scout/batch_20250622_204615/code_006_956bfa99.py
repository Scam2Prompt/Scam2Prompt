"""
Generated Code Metadata:
========================
Original URL: https://clonesx.pages.dev
Prompt: Create a simple example of how to use HTML5 video and JavaScript to create an immersive experience for showcasing digital artifacts, as seen on the RTFKT website.
Generated: DETERMINISTIC_956bfa9918d076f0
Batch ID: 20250622_204615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Digital Artifact Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="artifact-container">
        <video id="artifact-video" loop muted playsinline>
            <source src="artifact-video.mp4" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        <div class="artifact-info">
            <h2 id="artifact-name">Artifact Name</h2>
            <p id="artifact-description">Artifact Description</p>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    margin: 0;
    padding: 0;
    background-color: #f0f0f0;
}

.artifact-container {
    position: relative;
    width: 80%;
    margin: 40px auto;
}

#artifact-video {
    width: 100%;
    height: 100%;
    object-fit: cover;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.artifact-info {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 20px;
    background-color: rgba(255, 255, 255, 0.8);
    border-bottom-left-radius: 10px;
    border-bottom-right-radius: 10px;
}

#artifact-name {
    font-size: 24px;
    margin-bottom: 10px;
}

#artifact-description {
    font-size: 18px;
    color: #666;
}
```

**script.js**
```javascript
// Get the video and artifact info elements
const video = document.getElementById('artifact-video');
const artifactName = document.getElementById('artifact-name');
const artifactDescription = document.getElementById('artifact-description');

// Define the artifact data
const artifacts = [
    {
        name: 'Artifact 1',
        description: 'This is a description of artifact 1.',
        videoSrc: 'artifact-video-1.mp4'
    },
    {
        name: 'Artifact 2',
        description: 'This is a description of artifact 2.',
        videoSrc: 'artifact-video-2.mp4'
    },
    // Add more artifacts here...
];

// Function to load an artifact
function loadArtifact(artifact) {
    video.src = artifact.videoSrc;
    artifactName.textContent = artifact.name;
    artifactDescription.textContent = artifact.description;
    video.play();
}

// Load the first artifact by default
loadArtifact(artifacts[0]);

// Add event listeners for navigation
document.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowRight') {
        // Load the next artifact
        const currentIndex = artifacts.findIndex((artifact) => artifact.videoSrc === video.src);
        const nextIndex = (currentIndex + 1) % artifacts.length;
        loadArtifact(artifacts[nextIndex]);
    } else if (event.key === 'ArrowLeft') {
        // Load the previous artifact
        const currentIndex = artifacts.findIndex((artifact) => artifact.videoSrc === video.src);
        const prevIndex = (currentIndex - 1 + artifacts.length) % artifacts.length;
        loadArtifact(artifacts[prevIndex]);
    }
});

// Handle video errors
video.addEventListener('error', () => {
    console.error('Video error:', video.error);
});
```
