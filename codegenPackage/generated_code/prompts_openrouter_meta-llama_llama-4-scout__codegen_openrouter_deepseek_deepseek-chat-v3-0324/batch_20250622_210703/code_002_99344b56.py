"""
Generated Code Metadata:
========================
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: "Generate a code snippet in JavaScript to create a simple window configuration tool, allowing users to select window types (e.g., Aluplast Ideal 5000) and view their specifications."
Generated: DETERMINISTIC_99344b563b44cc60
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Window Configuration Tool
 * Allows users to select window types and view their specifications
 */

// Window specifications database
const windowSpecs = {
    'Aluplast Ideal 5000': {
        material: 'PVC',
        uValue: 1.0,
        soundReduction: 35,
        colors: ['White', 'Wood Effect', 'Grey'],
        priceRange: 'Medium'
    },
    'Schüco AWS 75': {
        material: 'Aluminum',
        uValue: 1.4,
        soundReduction: 42,
        colors: ['Silver', 'Black', 'Bronze'],
        priceRange: 'High'
    },
    'Veka Softline 82': {
        material: 'PVC',
        uValue: 0.9,
        soundReduction: 38,
        colors: ['White', 'Champagne', 'Anthracite'],
        priceRange: 'Medium'
    }
};

// DOM elements
const windowSelect = document.getElementById('window-select');
const specsContainer = document.getElementById('specs-container');
const errorMessage = document.getElementById('error-message');

/**
 * Initialize the application
 */
function init() {
    try {
        // Populate window type dropdown
        populateWindowSelect();
        
        // Add event listener for selection changes
        windowSelect.addEventListener('change', handleWindowSelection);
        
        // Display initial window specs if default selection exists
        if (windowSelect.value) {
            displayWindowSpecs(windowSelect.value);
        }
    } catch (error) {
        showError('Failed to initialize the application.');
        console.error('Initialization error:', error);
    }
}

/**
 * Populate the window type dropdown with available options
 */
function populateWindowSelect() {
    try {
        // Clear existing options
        windowSelect.innerHTML = '<option value="">Select a window type</option>';
        
        // Add each window type to the dropdown
        Object.keys(windowSpecs).forEach(windowType => {
            const option = document.createElement('option');
            option.value = windowType;
            option.textContent = windowType;
            windowSelect.appendChild(option);
        });
    } catch (error) {
        showError('Failed to load window types.');
        console.error('Error populating window select:', error);
    }
}

/**
 * Handle window type selection change
 * @param {Event} event - The change event
 */
function handleWindowSelection(event) {
    try {
        const selectedWindow = event.target.value;
        if (selectedWindow) {
            displayWindowSpecs(selectedWindow);
        } else {
            clearSpecsDisplay();
        }
    } catch (error) {
        showError('Failed to process window selection.');
        console.error('Selection error:', error);
    }
}

/**
 * Display specifications for the selected window type
 * @param {string} windowType - The selected window type
 */
function displayWindowSpecs(windowType) {
    try {
        if (!windowSpecs[windowType]) {
            throw new Error(`Specifications not found for ${windowType}`);
        }
        
        const specs = windowSpecs[windowType];
        
        // Create HTML for specifications
        const specsHTML = `
            <h3>${windowType} Specifications</h3>
            <ul>
                <li><strong>Material:</strong> ${specs.material}</li>
                <li><strong>U-Value:</strong> ${specs.uValue} W/m²K</li>
                <li><strong>Sound Reduction:</strong> ${specs.soundReduction} dB</li>
                <li><strong>Available Colors:</strong> ${specs.colors.join(', ')}</li>
                <li><strong>Price Range:</strong> ${specs.priceRange}</li>
            </ul>
        `;
        
        // Update the specs container
        specsContainer.innerHTML = specsHTML;
        errorMessage.textContent = '';
    } catch (error) {
        showError('Failed to display window specifications.');
        console.error('Display error:', error);
    }
}

/**
 * Clear the specifications display
 */
function clearSpecsDisplay() {
    specsContainer.innerHTML = '';
    errorMessage.textContent = '';
}

/**
 * Display an error message to the user
 * @param {string} message - The error message to display
 */
function showError(message) {
    errorMessage.textContent = message;
    specsContainer.innerHTML = '';
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', init);
```
