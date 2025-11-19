"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Write HTML and CSS code to design a user interface for a digital radio platform, inspired by Radio S's layout, featuring sections for "Radio Uživo," "Muzički Mix," and "Podcast."
Generated: DETERMINISTIC_cffd9a162572566e
Batch ID: 20250612_150234
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
    <title>Digital Radio Platform</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#radio-uzivo">Radio Uživo</a></li>
                <li><a href="#muzicki-mix">Muzički Mix</a></li>
                <li><a href="#podcast">Podcast</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="radio-uzivo">
            <h2>Radio Uživo</h2>
            <div class="radio-uzivo-content">
                <div class="radio-stream">
                    <audio controls>
                        <source src="radio_stream.mp3" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                </div>
                <div class="radio-info">
                    <p>Currently playing: <span id="current-song">Unknown</span></p>
                    <p>DJ: <span id="current-dj">Unknown</span></p>
                </div>
            </div>
        </section>
        <section id="muzicki-mix">
            <h2>Muzički Mix</h2>
            <div class="muzicki-mix-content">
                <div class="playlist">
                    <ul id="playlist">
                        <!-- Playlist items will be generated dynamically -->
                    </ul>
                </div>
                <div class="player">
                    <audio controls id="muzicki-mix-player">
                        <source src="" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </div>
        </section>
        <section id="podcast">
            <h2>Podcast</h2>
            <div class="podcast-content">
                <div class="podcast-list">
                    <ul id="podcast-list">
                        <!-- Podcast items will be generated dynamically -->
                    </ul>
                </div>
                <div class="player">
                    <audio controls id="podcast-player">
                        <source src="" type="audio/mp3">
                        Your browser does not support the audio element.
                    </audio>
                </div>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

#radio-uzivo {
    background-image: linear-gradient(to bottom, #333, #555);
    color: #fff;
}

.radio-uzivo-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.radio-stream {
    margin-bottom: 20px;
}

.radio-info {
    font-size: 18px;
}

#muzicki-mix {
    background-color: #fff;
}

.muzicki-mix-content {
    display: flex;
    flex-direction: row;
}

.playlist {
    width: 30%;
    margin-right: 20px;
}

#playlist {
    list-style: none;
    padding: 0;
    margin: 0;
}

#playlist li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
    cursor: pointer;
}

#playlist li:hover {
    background-color: #f0f0f0;
}

.player {
    width: 70%;
}

#muzicki-mix-player, #podcast-player {
    width: 100%;
}

#podcast {
    background-color: #f7f7f7;
}

.podcast-content {
    display: flex;
    flex-direction: row;
}

.podcast-list {
    width: 30%;
    margin-right: 20px;
}

#podcast-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#podcast-list li {
    padding: 10px;
    border-bottom: 1px solid #ccc;
    cursor: pointer;
}

#podcast-list li:hover {
    background-color: #f0f0f0;
}
```

**script.js**
```javascript
// Generate playlist items dynamically
const playlist = [
    { title: 'Song 1', artist: 'Artist 1', src: 'song1.mp3' },
    { title: 'Song 2', artist: 'Artist 2', src: 'song2.mp3' },
    { title: 'Song 3', artist: 'Artist 3', src: 'song3.mp3' },
];

const playlistElement = document.getElementById('playlist');
playlist.forEach((song) => {
    const li = document.createElement('li');
    li.textContent = `${song.title} by ${song.artist}`;
    li.addEventListener('click', () => {
        const player = document.getElementById('muzicki-mix-player');
        player.src = song.src;
        player.play();
    });
    playlistElement.appendChild(li);
});

// Generate podcast items dynamically
const podcastList = [
    { title: 'Podcast 1', src: 'podcast1.mp3' },
    { title: 'Podcast 2', src: 'podcast2.mp3' },
    { title: 'Podcast 3', src: 'podcast3.mp3' },
];

const podcastListElement = document.getElementById('podcast-list');
podcastList.forEach((podcast) => {
    const li = document.createElement('li');
    li.textContent = podcast.title;
    li.addEventListener('click', () => {
        const player = document.getElementById('podcast-player');
        player.src = podcast.src;
        player.play();
    });
    podcastListElement.appendChild(li);
});

// Update current song and DJ info
const currentSongElement = document.getElementById('current-song');
const currentDjElement = document.getElementById('current-dj');

// Simulate updating current song and DJ info
setInterval(() => {
    currentSongElement.textContent = 'New Song';
    currentDjElement.textContent = 'New DJ';
}, 10000);
```
