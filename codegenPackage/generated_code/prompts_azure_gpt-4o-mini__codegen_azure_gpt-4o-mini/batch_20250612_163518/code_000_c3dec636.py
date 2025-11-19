"""
Generated Code Metadata:
========================
Original URL: https://moontropica.pages.dev
Prompt: How can I implement character customization in a battle arena game like Moon Tropica using JavaScript?
Generated: DETERMINISTIC_c3dec636dcbfd92d
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CharacterCustomization.js

class Character {
    constructor(name, color, weapon) {
        this.name = name; // Character's name
        this.color = color; // Character's color
        this.weapon = weapon; // Character's weapon
    }

    // Method to display character details
    displayCharacter() {
        console.log(`Character Name: ${this.name}`);
        console.log(`Character Color: ${this.color}`);
        console.log(`Character Weapon: ${this.weapon}`);
    }
}

class CharacterCustomization {
    constructor() {
        this.characters = []; // Array to hold created characters
    }

    // Method to create a new character
    createCharacter(name, color, weapon) {
        try {
            // Validate inputs
            if (!name || !color || !weapon) {
                throw new Error("All fields (name, color, weapon) are required.");
            }

            // Create a new character instance
            const newCharacter = new Character(name, color, weapon);
            this.characters.push(newCharacter); // Add character to the array
            console.log(`Character ${name} created successfully.`);
        } catch (error) {
            console.error(`Error creating character: ${error.message}`);
        }
    }

    // Method to list all characters
    listCharacters() {
        if (this.characters.length === 0) {
            console.log("No characters created yet.");
            return;
        }

        console.log("List of Characters:");
        this.characters.forEach((character, index) => {
            console.log(`${index + 1}:`);
            character.displayCharacter();
        });
    }

    // Method to customize an existing character
    customizeCharacter(index, newColor, newWeapon) {
        try {
            // Validate index
            if (index < 0 || index >= this.characters.length) {
                throw new Error("Invalid character index.");
            }

            // Update character properties
            if (newColor) {
                this.characters[index].color = newColor;
            }
            if (newWeapon) {
                this.characters[index].weapon = newWeapon;
            }

            console.log(`Character ${this.characters[index].name} customized successfully.`);
        } catch (error) {
            console.error(`Error customizing character: ${error.message}`);
        }
    }
}

// Example usage
const customization = new CharacterCustomization();
customization.createCharacter("Warrior", "Red", "Sword");
customization.createCharacter("Mage", "Blue", "Staff");
customization.listCharacters();
customization.customizeCharacter(0, "Green", "Axe");
customization.listCharacters();
```
