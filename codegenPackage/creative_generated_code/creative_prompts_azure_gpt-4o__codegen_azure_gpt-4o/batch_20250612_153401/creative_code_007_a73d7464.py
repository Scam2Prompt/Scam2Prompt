"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publicsale-mocaverse.pages.dev
Prompt: Create a JavaScript function to simulate the portal conduit described in Mocaverse, allowing users to explore the realms and tribes interactively.
Generated: DETERMINISTIC_a73d7464bfb6ee3a
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Simulates a portal conduit for exploring realms and tribes interactively.
 * 
 * This function allows users to choose a realm and tribe, providing a dynamic
 * and interactive way to explore Mocaverse's realms and tribes.
 * 
 * Usage:
 * - Call the `explorePortalConduit()` function.
 * - Follow the prompts to select a realm and tribe.
 */

// Define the realms and tribes data
const mocaverseData = {
    realms: [
        { id: 1, name: "Realm of Wisdom", tribes: ["Explorers", "Innovators", "Strategists"] },
        { id: 2, name: "Realm of Courage", tribes: ["Warriors", "Defenders", "Adventurers"] },
        { id: 3, name: "Realm of Harmony", tribes: ["Peacemakers", "Collaborators", "Unifiers"] }
    ]
};

/**
 * Validates user input and ensures it is a number within the given range.
 * @param {string} input - The user input.
 * @param {number} min - The minimum valid value.
 * @param {number} max - The maximum valid value.
 * @returns {number|null} - The valid number or null if validation fails.
 */
function validateInput(input, min, max) {
    const parsedInput = parseInt(input, 10);
    if (isNaN(parsedInput) || parsedInput < min || parsedInput > max) {
        console.error("Invalid input. Please enter a number within the valid range.");
        return null;
    }
    return parsedInput;
}

/**
 * Prompts the user to explore a realm and tribe interactively.
 */
async function explorePortalConduit() {
    try {
        // Display available realms
        console.log("Welcome to the Mocaverse Portal Conduit!");
        console.log("Available Realms:");
        mocaverseData.realms.forEach(realm => {
            console.log(`${realm.id}. ${realm.name}`);
        });

        // Prompt user to select a realm
        const realmInput = prompt("Enter the number of the realm you'd like to explore:");
        const realmChoice = validateInput(realmInput, 1, mocaverseData.realms.length);
        if (realmChoice === null) return;

        const selectedRealm = mocaverseData.realms.find(realm => realm.id === realmChoice);
        console.log(`You selected: ${selectedRealm.name}`);

        // Display tribes within the selected realm
        console.log("Available Tribes within this realm:");
        selectedRealm.tribes.forEach((tribe, index) => {
            console.log(`${index + 1}. ${tribe}`);
        });

        // Prompt user to select a tribe
        const tribeInput = prompt("Enter the number of the tribe you'd like to explore:");
        const tribeChoice = validateInput(tribeInput, 1, selectedRealm.tribes.length);
        if (tribeChoice === null) return;

        const selectedTribe = selectedRealm.tribes[tribeChoice - 1];
        console.log(`You selected the tribe: ${selectedTribe}`);

        // Display final selection
        console.log(`Congratulations! You are now exploring the "${selectedTribe}" tribe in the "${selectedRealm.name}" realm.`);
    } catch (error) {
        console.error("An error occurred while exploring the portal conduit:", error.message);
    }
}

// Call the function to begin exploration
explorePortalConduit();
```

This code assumes the use of a browser environment where `prompt()` is available. For environments without `prompt()`, you can replace it with a custom UI or input mechanism.
