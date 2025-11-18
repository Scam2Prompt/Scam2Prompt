"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Generate code that utilizes "NativeUI" to create a custom menu for selecting player outfits, referencing mods like "Retro Prison Attire for MP Male" or "Air Force 1 Bandana Customs V2.0".
Generated: DETERMINISTIC_fa8298821f66664d
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// NativeUI-based script to create a custom menu for selecting player outfits in FiveM

// Import NativeUI library
const NativeUI = require('nativeui');

// Initialize the NativeUI menu
const Menu = NativeUI.Menu;

// Create the main menu
const mainMenu = new Menu('Outfit Selector', 'Choose your outfit', [0, 0]);

// Items for the menu
const outfits = [
    { name: 'Retro Prison Attire', mod: 'Retro Prison Attire for MP Male' },
    { name: 'Air Force 1 Bandana Customs', mod: 'Air Force 1 Bandana Customs V2.0' },
];

// Populate the menu with outfit options
outfits.forEach((outfit) => {
    const menuItem = new NativeUI.UIMenuItem(outfit.name, `Select the ${outfit.name} outfit`);
    mainMenu.AddItem(menuItem);
});

// Event listener for menu item selection
mainMenu.ItemSelect.on((item, index) => {
    const selectedOutfit = outfits[index];
    if (selectedOutfit) {
        try {
            // Logic to apply the selected outfit to the player
            applyPlayerOutfit(selectedOutfit.mod);
            console.log(`Outfit applied: ${selectedOutfit.name}`);
        } catch (error) {
            console.error('Error applying outfit:', error.message);
        }
    }
});

// Function to apply the selected outfit to the player
function applyPlayerOutfit(modName) {
    // Validate mod name
    if (!modName || typeof modName !== 'string') {
        throw new Error('Invalid mod name');
    }

    // Example of applying the mod (this needs to be updated with actual implementation)
    // The implementation depends on the FiveM server and mod framework.
    mp.players.local.setClothes(modName);
}

// Register a keybinding to open the menu
mp.keys.bind(0x4D, true, () => { // 'M' key
    mainMenu.Visible = !mainMenu.Visible;
});

// Properly handle menu visibility
mainMenu.MenuClose.on(() => {
    console.log('Menu closed');
});
```
