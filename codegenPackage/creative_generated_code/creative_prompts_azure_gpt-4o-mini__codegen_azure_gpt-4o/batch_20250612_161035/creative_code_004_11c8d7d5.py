"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gta5mod.net
Prompt: Provide an example of how to use the NativeUI library to create a custom menu for selecting player skins in GTA 5.
Generated: DETERMINISTIC_11c8d7d5ae6c6f99
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/// NativeUI Example: Custom Menu for Selecting Player Skins in GTA 5
/// Ensure you have the NativeUI library installed and properly set up in your project.
/// This script uses the NativeUI library to create a menu for selecting player skins.

const NativeUI = require('nativeui'); // Import NativeUI library
const Menu = NativeUI.Menu; // Alias for easier usage
const UIMenuItem = NativeUI.UIMenuItem;

let playerSkinsMenu; // Reference to the main menu

/// List of available player skins (model names)
const playerSkins = [
    "a_f_y_beach_01", 
    "a_m_y_skater_01", 
    "mp_m_freemode_01", 
    "mp_f_freemode_01"
];

/// Function to apply the selected player skin
function applyPlayerSkin(skin) {
    try {
        const playerPed = mp.players.local; // Get the local player
        mp.game.streaming.requestModel(skin); // Request the model
        if (mp.game.streaming.hasModelLoaded(skin)) {
            playerPed.model = mp.game.joaat(skin); // Set the player model
            mp.game.streaming.setModelAsNoLongerNeeded(skin); // Release the model
        } else {
            mp.gui.chat.push(`Failed to load skin: ${skin}`); // Inform failure
        }
    } catch (error) {
        mp.gui.chat.push(`An error occurred: ${error.message}`); // Error handling
    }
}

/// Function to create the player skins menu
function createPlayerSkinsMenu() {
    playerSkinsMenu = new Menu("Player Skins", "Select a skin", [300, 300]); // Create menu

    playerSkins.forEach((skin) => {
        const item = new UIMenuItem(skin, `Set your player skin to ${skin}`);
        playerSkinsMenu.AddItem(item); // Add item to menu
        
        /// Event: Handle item selection
        playerSkinsMenu.ItemSelect.on((selectedItem, index) => {
            if (selectedItem.Text === skin) {
                applyPlayerSkin(skin); // Apply the selected skin
            }
        });
    });

    playerSkinsMenu.Visible = true; // Make the menu visible
}

/// Command to open the menu
mp.events.addCommand("skinsmenu", () => {
    if (!playerSkinsMenu) {
        createPlayerSkinsMenu(); // Create the menu if it doesn't exist
    } else {
        playerSkinsMenu.Visible = !playerSkinsMenu.Visible; // Toggle visibility
    }
});
```
