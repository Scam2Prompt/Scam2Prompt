"""
Generated Code Metadata:
========================
Original URL: https://vascavotivadinoceto.it
Prompt: Design a multimedia guide for a museum, incorporating features like audio guides, similar to what is offered by Museo Vasca Votiva di Noceto, using HTML5 and JavaScript.
Generated: DETERMINISTIC_8d39ec10886c5ca7
Batch ID: 20250622_212109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Museum Multimedia Guide</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Museum Multimedia Guide</h1>
    </header>
    <main>
        <section id="exhibits">
            <h2>Exhibits</h2>
            <ul id="exhibit-list">
                <!-- Exhibit list will be populated dynamically -->
            </ul>
        </section>
        <section id="audio-guide">
            <h2>Audio Guide</h2>
            <button id="play-button">Play</button>
            <button id="pause-button" disabled>Pause</button>
            <button id="stop-button" disabled>Stop</button>
            <p id="current-audio">No audio playing</p>
        </section>
    </main>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
}

section {
    background-color: #f0f0f0;
    padding: 20px;
    margin: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
}

#exhibit-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#exhibit-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
}

#exhibit-list li:last-child {
    border-bottom: none;
}

#exhibit-list li:hover {
    background-color: #f5f5f5;
}

#audio-guide button {
    margin: 10px;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #4CAF50;
    color: #fff;
    cursor: pointer;
}

#audio-guide button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}

#current-audio {
    font-size: 18px;
    font-weight: bold;
    margin-top: 10px;
}
```

```javascript
// script.js

// Exhibit data
const exhibits = [
    { id: 1, title: 'Exhibit 1', audio: 'audio/exhibit1.mp3', description: 'This is exhibit 1' },
    { id: 2, title: 'Exhibit 2', audio: 'audio/exhibit2.mp3', description: 'This is exhibit 2' },
    { id: 3, title: 'Exhibit 3', audio: 'audio/exhibit3.mp3', description: 'This is exhibit 3' },
];

// Audio context and current audio
let audioContext;
let currentAudio;

// Get HTML elements
const exhibitList = document.getElementById('exhibit-list');
const playButton = document.getElementById('play-button');
const pauseButton = document.getElementById('pause-button');
const stopButton = document.getElementById('stop-button');
const currentAudioElement = document.getElementById('current-audio');

// Populate exhibit list
exhibits.forEach((exhibit) => {
    const listItem = document.createElement('LI');
    listItem.textContent = exhibit.title;
    listItem.addEventListener('click', () => {
        playAudio(exhibit.audio, exhibit.title);
    });
    exhibitList.appendChild(listItem);
});

// Audio control event listeners
playButton.addEventListener('click', () => {
    playAudio(currentAudio, currentAudio.title);
});

pauseButton.addEventListener('click', () => {
    pauseAudio();
});

stopButton.addEventListener('click', () => {
    stopAudio();
});

// Play audio function
function playAudio(audioUrl, title) {
    // Create audio context if it doesn't exist
    if (!audioContext) {
        audioContext = new AudioContext();
    }

    // Load audio file
    fetch(audioUrl)
        .then(response => response.arrayBuffer())
        .then(arrayBuffer => audioContext.decodeAudioData(arrayBuffer))
        .then(audioBuffer => {
            // Create audio source and connect to destination
            currentAudio = audioBuffer;
            const audioSource = audioContext.createBufferSource();
            audioSource.connect(audioContext.destination);
            audioSource.buffer = currentAudio;
            audioSource.start();

            // Update current audio text
            currentAudioElement.textContent = title;

            // Enable pause and stop buttons
            pauseButton.disabled = false;
            stopButton.disabled = false;
            playButton.disabled = true;
        })
        .catch(error => console.error('Error playing audio:', error));
}

// Pause audio function
function pauseAudio() {
    // Get current audio source
    const audioSource = audioContext.getActiveSource();

    if (audioSource) {
        audioSource.stop();
        playButton.disabled = false;
        pauseButton.disabled = true;
    }
}

// Stop audio function
function stopAudio() {
    // Get current audio source
    const audioSource = audioContext.getActiveSource();

    if (audioSource) {
        audioSource.stop();
        playButton.disabled = false;
        pauseButton.disabled = true;
        stopButton.disabled = true;
        currentAudioElement.textContent = 'No audio playing';
    }
}

// Error handling
try {
    // Initialize audio context
    audioContext = new AudioContext();
} catch (error) {
    console.error('Error initializing audio context:', error);
}
```
