"""
Generated Code Metadata:
========================
Original URL: https://gta5mod.net
Prompt: Provide an example of how to use the NativeUI library to create a custom menu for selecting player skins in GTA 5.
Generated: DETERMINISTIC_11c8d7d5ae6c6f99
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import the NativeUI library
const NativeUI = require("nativeui");

// Create a new instance of the MenuPool
const menuPool = new NativeUI.MenuPool();

// Create the main menu
const mainMenu = new NativeUI.UIMenu(
    "Player Skins", // Menu title
    "Select a skin for your player", // Menu subtitle
    new NativeUI.Point(50, 50) // Position on the screen
);

// Add the main menu to the menu pool
menuPool.Add(mainMenu);

// List of available player skins
const playerSkins = [
    "Michael",
    "Franklin",
    "Trevor",
    "MP_M_Freemode_01",
    "MP_F_Freemode_01"
];

// Create a menu item for each skin
playerSkins.forEach((skin) => {
    const skinItem = new NativeUI.UIMenuItem(skin, `Change your player skin to ${skin}`);
    mainMenu.AddItem(skinItem);
});

// Handle menu item selection
mainMenu.ItemSelect.on((selectedItem, index) => {
    try {
        const selectedSkin = playerSkins[index];
        if (selectedSkin) {
            // Change the player's skin
            mp.players.local.model = mp.game.joaat(selectedSkin);
            mp.gui.chat.push(`Player skin changed to: ${selectedSkin}`);
        } else {
            mp.gui.chat.push("Invalid skin selection.");
        }
    } catch (error) {
        // Handle any errors that occur during skin change
        mp.gui.chat.push(`Error changing skin: ${error.message}`);
    }
});

// Continuously update the menu pool
mp.events.add("render", () => {
    menuPool.ProcessMenus();
});

// Open the menu when the player presses the "M" key
mp.keys.bind(0x4D, true, () => { // 0x4D is the key code for "M"
    if (!mainMenu.Visible) {
        mainMenu.Visible = true;
    }
});
```
