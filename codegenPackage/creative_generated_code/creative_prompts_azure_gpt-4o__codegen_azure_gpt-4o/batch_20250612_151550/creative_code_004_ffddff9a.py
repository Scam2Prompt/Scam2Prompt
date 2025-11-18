"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Write JavaScript code to integrate a workshop customization feature for HV-MTL Forge, allowing users to preview their upgrades in real-time.
Generated: DETERMINISTIC_ffddff9a99733925
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * HV-MTL Forge Workshop Customization Feature
 * Allows users to preview their upgrades in real-time.
 */

// Ensure the DOM is fully loaded before running the script
document.addEventListener('DOMContentLoaded', () => {
    // Select DOM elements
    const upgradeOptions = document.querySelectorAll('.upgrade-option'); // Buttons or UI elements for upgrades
    const previewArea = document.getElementById('preview-area'); // Area to show the real-time preview
    const applyButton = document.getElementById('apply-upgrades'); // Button to apply upgrades
    const errorMessage = document.getElementById('error-message'); // Area to display error messages

    // State to hold current upgrades
    const currentUpgrades = {};

    /**
     * Handles real-time preview updates.
     * @param {Event} event - The event triggered by user interaction.
     */
    const handlePreviewUpdate = (event) => {
        try {
            const upgradeType = event.target.dataset.upgradeType; // Retrieve the type of upgrade (e.g., "color", "shape")
            const upgradeValue = event.target.value; // Retrieve the selected upgrade value

            if (!upgradeType || !upgradeValue) {
                throw new Error('Invalid upgrade option selected.');
            }

            // Update the preview area with the new upgrade
            currentUpgrades[upgradeType] = upgradeValue;
            updatePreviewArea();
        } catch (error) {
            // Display error message to the user
            errorMessage.textContent = error.message;
        }
    };

    /**
     * Updates the preview area based on current upgrades.
     */
    const updatePreviewArea = () => {
        // Clear any existing error messages
        errorMessage.textContent = '';

        // Simulate applying upgrades to the preview area
        Object.keys(currentUpgrades).forEach((upgradeType) => {
            const upgradeValue = currentUpgrades[upgradeType];
            
            // Example logic: Update preview area dynamically based on upgrades
            previewArea.style[upgradeType] = upgradeValue;
        });
    };

    /**
     * Applies upgrades and finalizes customization.
     */
    const applyUpgrades = () => {
        try {
            // Ensure there are upgrades to apply
            if (Object.keys(currentUpgrades).length === 0) {
                throw new Error('No upgrades selected to apply.');
            }

            // Simulate saving upgrades (e.g., sending data to server via API)
            console.log('Applying upgrades:', currentUpgrades);

            // Clear preview and reset state
            previewArea.style = ''; // Clear inline styles
            currentUpgrades = {}; // Reset upgrades
            errorMessage.textContent = 'Upgrades applied successfully!';
        } catch (error) {
            // Display error message to the user
            errorMessage.textContent = error.message;
        }
    };

    // Attach event listeners to upgrade options
    upgradeOptions.forEach((option) => {
        option.addEventListener('change', handlePreviewUpdate); // Listen for changes to upgrade options
    });

    // Attach event listener to apply button
    applyButton.addEventListener('click', applyUpgrades); // Listen for button click to apply upgrades
});
```
