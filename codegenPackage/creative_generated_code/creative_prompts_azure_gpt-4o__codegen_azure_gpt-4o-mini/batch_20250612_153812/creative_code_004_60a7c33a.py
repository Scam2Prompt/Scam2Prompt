"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Create a feature that allows users to view the unique skills and props of Cheems characters (e.g., Samurai Cheems' sword and dash skill) in a web interface. Use HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_60a7c33adb44bfe3
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cheems Character Skills</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Cheems Character Skills</h1>
    </header>
    <main>
        <div id="character-list">
            <button onclick="showCharacter('samurai')">Samurai Cheems</button>
            <button onclick="showCharacter('ninja')">Ninja Cheems</button>
            <button onclick="showCharacter('wizard')">Wizard Cheems</button>
        </div>
        <div id="character-details" class="hidden">
            <h2 id="character-name"></h2>
            <ul id="skills-list"></ul>
            <button onclick="hideCharacter()">Back</button>
        </div>
    </main>
    <footer>
        <p>&copy; 2023 Cheems Fan Club</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    color: #333;
}

header {
    background: #4caf50;
    color: white;
    padding: 20px;
    text-align: center;
}

main {
    padding: 20px;
}

button {
    margin: 5px;
    padding: 10px;
    background-color: #4caf50;
    color: white;
    border: none;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #45a049;
}

.hidden {
    display: none;
}
```

```javascript
// script.js

// Character data storing unique skills and props
const characters = {
    samurai: {
        name: "Samurai Cheems",
        skills: ["Sword Mastery", "Dash"],
    },
    ninja: {
        name: "Ninja Cheems",
        skills: ["Stealth", "Shadow Clone Technique"],
    },
    wizard: {
        name: "Wizard Cheems",
        skills: ["Spell Casting", "Potion Brewing"],
    },
};

/**
 * Displays the selected character's skills.
 * @param {string} characterKey - The key corresponding to the character.
 */
function showCharacter(characterKey) {
    const character = characters[characterKey];

    if (!character) {
        console.error('Character not found:', characterKey);
        return;
    }

    document.getElementById('character-name').textContent = character.name;
    const skillsList = document.getElementById('skills-list');
    skillsList.innerHTML = '';

    character.skills.forEach(skill => {
        const li = document.createElement('li');
        li.textContent = skill;
        skillsList.appendChild(li);
    });

    document.getElementById('character-details').classList.remove('hidden');
}

/**
 * Hides the character details view and resets the fields.
 */
function hideCharacter() {
    document.getElementById('character-details').classList.add('hidden');
    document.getElementById('character-name').textContent = '';
    document.getElementById('skills-list').innerHTML = '';
}
```
