"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Create a feature that allows users to view the unique skills and props of Cheems characters (e.g., Samurai Cheems' sword and dash skill) in a web interface. Use HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_60a7c33adb44bfe3
Batch ID: 20250612_153812
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
    <title>Cheems Characters</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Cheems Characters</h1>
    <div class="characters-container"></div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
}

.characters-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.character-card {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 200px;
}

.character-card h2 {
    margin-top: 0;
}

.skills-list, .props-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

.skills-list li, .props-list li {
    margin-bottom: 10px;
}

.skill {
    color: #008000;
}

.prop {
    color: #ff69b4;
}
```

**script.js**
```javascript
// Data for Cheems characters
const charactersData = [
    {
        name: "Samurai Cheems",
        skills: [
            { name: "Dash", description: "Increases movement speed" },
            { name: "Sword Slash", description: "Deals damage to enemies" }
        ],
        props: [
            { name: "Sword", description: "A sharp sword for close combat" },
            { name: "Samurai Armor", description: "Protective armor for the samurai" }
        ]
    },
    {
        name: "Mage Cheems",
        skills: [
            { name: "Fireball", description: "Deals damage to enemies" },
            { name: "Healing Spell", description: "Restores health to allies" }
        ],
        props: [
            { name: "Staff", description: "A magical staff for casting spells" },
            { name: "Mage Robes", description: "Robes for the mage" }
        ]
    }
];

// Function to create character card
function createCharacterCard(character) {
    const card = document.createElement("div");
    card.classList.add("character-card");

    const name = document.createElement("h2");
    name.textContent = character.name;
    card.appendChild(name);

    const skillsList = document.createElement("ul");
    skillsList.classList.add("skills-list");
    character.skills.forEach(skill => {
        const skillItem = document.createElement("li");
        skillItem.textContent = `${skill.name} - ${skill.description}`;
        skillItem.classList.add("skill");
        skillsList.appendChild(skillItem);
    });
    card.appendChild(skillsList);

    const propsList = document.createElement("ul");
    propsList.classList.add("props-list");
    character.props.forEach(prop => {
        const propItem = document.createElement("li");
        propItem.textContent = `${prop.name} - ${prop.description}`;
        propItem.classList.add("prop");
        propsList.appendChild(propItem);
    });
    card.appendChild(propsList);

    return card;
}

// Function to render characters
function renderCharacters() {
    try {
        const charactersContainer = document.querySelector(".characters-container");
        charactersContainer.innerHTML = "";

        charactersData.forEach(character => {
            const card = createCharacterCard(character);
            charactersContainer.appendChild(card);
        });
    } catch (error) {
        console.error("Error rendering characters:", error);
    }
}

// Render characters on page load
document.addEventListener("DOMContentLoaded", renderCharacters);
```
