"""
Generated Code Metadata:
========================
Original URL: https://quick-battery-few.on-fleek.app
Prompt: Create a simple web interface using HTML and CSS for users to vote for their favorite digital character, inspired by the Xterio Palio event interface.
Generated: DETERMINISTIC_9fcc66a338f68517
Batch ID: 20250622_205030
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/character3.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/character2.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/character1.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
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
    <title>Digital Character Voting</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Digital Character Voting</h1>
    </header>
    <main>
        <section class="characters">
            <!-- Characters will be generated dynamically -->
        </section>
        <section class="vote">
            <h2>Cast Your Vote</h2>
            <form id="vote-form">
                <div class="character-select">
                    <label for="character">Select a Character:</label>
                    <select id="character" name="character"></select>
                </div>
                <button type="submit">Vote</button>
            </form>
            <p id="vote-result"></p>
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
    background-color: #f0f0f0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.characters {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin-bottom: 2em;
}

.character {
    margin: 1em;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 200px;
    text-align: center;
}

.character img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.character h3 {
    margin-top: 0.5em;
}

.vote {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#vote-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.character-select {
    margin-bottom: 1em;
}

#vote-result {
    margin-top: 1em;
    font-weight: bold;
}
```

**script.js**
```javascript
// Define characters data
const characters = [
    { id: 1, name: 'Character 1', image: 'https://example.com/character1.png' },
    { id: 2, name: 'Character 2', image: 'https://example.com/character2.png' },
    { id: 3, name: 'Character 3', image: 'https://example.com/character3.png' },
    // Add more characters here...
];

// Get DOM elements
const charactersSection = document.querySelector('.characters');
const voteForm = document.getElementById('vote-form');
const characterSelect = document.getElementById('character');
const voteResult = document.getElementById('vote-result');

// Generate characters HTML
characters.forEach((character) => {
    const characterHTML = `
        <div class="character">
            <img src="${character.image}" alt="${character.name}">
            <h3>${character.name}</h3>
        </div>
    `;
    charactersSection.insertAdjacentHTML('beforeend', characterHTML);
});

// Populate character select options
characters.forEach((character) => {
    const option = document.createElement('option');
    option.value = character.id;
    option.textContent = character.name;
    characterSelect.appendChild(option);
});

// Handle vote form submission
voteForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const selectedCharacterId = parseInt(characterSelect.value);
    const selectedCharacter = characters.find((character) => character.id === selectedCharacterId);

    if (selectedCharacter) {
        // Simulate voting logic (replace with actual backend API call)
        console.log(`User voted for ${selectedCharacter.name}`);
        voteResult.textContent = `You voted for ${selectedCharacter.name}!`;
    } else {
        console.error('Invalid character selection');
        voteResult.textContent = 'Error: Invalid character selection';
    }
});
```
