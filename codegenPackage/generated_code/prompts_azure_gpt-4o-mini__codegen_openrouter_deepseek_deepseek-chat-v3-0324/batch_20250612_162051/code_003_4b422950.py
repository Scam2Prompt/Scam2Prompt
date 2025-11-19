"""
Generated Code Metadata:
========================
Original URL: https://www.somosfortic.es
Prompt: Develop a JavaScript function that dynamically displays the different design options (rustic, minimalist, garden) for Fortic's concrete beams on a webpage.
Generated: DETERMINISTIC_4b4229500fe72ad5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Displays different design options for Fortic's concrete beams on a webpage.
 * @param {string} designType - The type of design to display ('rustic', 'minimalist', 'garden').
 * @param {HTMLElement} container - The DOM element where the design options will be rendered.
 */
function displayDesignOptions(designType, container) {
    // Validate input parameters
    if (!container || !(container instanceof HTMLElement)) {
        console.error('Invalid container element provided.');
        return;
    }

    const validDesignTypes = ['rustic', 'minimalist', 'garden'];
    if (!validDesignTypes.includes(designType)) {
        console.error(`Invalid design type: ${designType}. Must be one of: ${validDesignTypes.join(', ')}`);
        return;
    }

    // Clear previous content
    container.innerHTML = '';

    try {
        // Design data (could be fetched from an API in a real-world scenario)
        const designs = {
            rustic: {
                title: 'Rustic Design',
                description: 'Features a textured, aged appearance perfect for traditional settings.',
                imageUrl: 'images/rustic-beam.jpg'
            },
            minimalist: {
                title: 'Minimalist Design',
                description: 'Clean lines and smooth surfaces for modern architectural projects.',
                imageUrl: 'images/minimalist-beam.jpg'
            },
            garden: {
                title: 'Garden Design',
                description: 'Decorative patterns and natural finishes ideal for outdoor spaces.',
                imageUrl: 'images/garden-beam.jpg'
            }
        };

        const design = designs[designType];

        // Create and append HTML elements
        const designElement = document.createElement('div');
        designElement.className = 'design-option';

        const titleElement = document.createElement('h2');
        titleElement.textContent = design.title;
        designElement.appendChild(titleElement);

        const imageElement = document.createElement('img');
        imageElement.src = design.imageUrl;
        imageElement.alt = `${design.title} concrete beam`;
        imageElement.className = 'design-image';
        designElement.appendChild(imageElement);

        const descriptionElement = document.createElement('p');
        descriptionElement.textContent = design.description;
        descriptionElement.className = 'design-description';
        designElement.appendChild(descriptionElement);

        container.appendChild(designElement);
    } catch (error) {
        console.error('Error rendering design options:', error);
        container.innerHTML = '<p class="error">Failed to load design options. Please try again later.</p>';
    }
}

// Example usage when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const designContainer = document.getElementById('design-container');
    if (designContainer) {
        // Default to rustic design on page load
        displayDesignOptions('rustic', designContainer);

        // Add event listeners for design selection buttons
        document.querySelectorAll('.design-selector').forEach(button => {
            button.addEventListener('click', function() {
                const designType = this.getAttribute('data-design-type');
                displayDesignOptions(designType, designContainer);
            });
        });
    }
});
```
