"""
Generated Code Metadata:
========================
Original URL: https://www.dexodoor.com
Prompt: Create a JavaScript function that dynamically displays different UPVC window styles based on user selection, as seen in the DEXODOOR product offerings.
Generated: DETERMINISTIC_d2cac291411f6085
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * UPVC Window Style Selector
 * Dynamically displays different UPVC window styles based on user selection
 * 
 * @param {string} selectedStyle - The selected window style from the dropdown
 */
function displayWindowStyle(selectedStyle) {
    try {
        // Validate input
        if (!selectedStyle) {
            throw new Error('No window style selected');
        }

        // Get DOM elements
        const styleContainer = document.getElementById('window-style-container');
        const styleDescription = document.getElementById('style-description');
        const styleImage = document.getElementById('style-image');
        
        if (!styleContainer || !styleDescription || !styleImage) {
            throw new Error('Required DOM elements not found');
        }

        // Clear previous content
        styleContainer.innerHTML = '';
        styleDescription.textContent = '';
        styleImage.src = '';
        styleImage.alt = '';

        // Define available window styles with their properties
        const windowStyles = {
            'casement': {
                name: 'Casement Window',
                description: 'A versatile window hinged at the side that opens outward with a handle.',
                imageUrl: 'images/casement-window.jpg'
            },
            'tilt-and-turn': {
                name: 'Tilt & Turn Window',
                description: 'Multi-functional window that can tilt inwards from the top or fully open like a door.',
                imageUrl: 'images/tilt-turn-window.jpg'
            },
            'sliding': {
                name: 'Sliding Window',
                description: 'Horizontal sliding windows that are space-saving and easy to operate.',
                imageUrl: 'images/sliding-window.jpg'
            },
            'fixed': {
                name: 'Fixed Window',
                description: 'Non-operable windows designed for maximum light and unobstructed views.',
                imageUrl: 'images/fixed-window.jpg'
            },
            'bay': {
                name: 'Bay Window',
                description: 'Projecting windows that create additional space and panoramic views.',
                imageUrl: 'images/bay-window.jpg'
            }
        };

        // Get selected style details
        const selectedStyleDetails = windowStyles[selectedStyle];
        if (!selectedStyleDetails) {
            throw new Error('Invalid window style selected');
        }

        // Create and display the selected style
        const styleTitle = document.createElement('h3');
        styleTitle.textContent = selectedStyleDetails.name;
        styleContainer.appendChild(styleTitle);

        styleDescription.textContent = selectedStyleDetails.description;
        styleImage.src = selectedStyleDetails.imageUrl;
        styleImage.alt = `${selectedStyleDetails.name} illustration`;

        // Add loading and error handling for the image
        styleImage.onload = () => {
            styleImage.style.display = 'block';
        };
        styleImage.onerror = () => {
            styleImage.style.display = 'none';
            console.error(`Failed to load image: ${selectedStyleDetails.imageUrl}`);
        };

    } catch (error) {
        console.error('Error displaying window style:', error.message);
        const errorContainer = document.getElementById('window-style-container') || document.body;
        errorContainer.innerHTML = `<p class="error">Error: ${error.message}. Please try again.</p>`;
    }
}

// Event listener for dropdown change
document.addEventListener('DOMContentLoaded', () => {
    const styleSelector = document.getElementById('window-style-selector');
    if (styleSelector) {
        styleSelector.addEventListener('change', (event) => {
            displayWindowStyle(event.target.value);
        });
        
        // Initialize with first option if available
        if (styleSelector.options.length > 0) {
            displayWindowStyle(styleSelector.options[styleSelector.selectedIndex].value);
        }
    }
});
```
