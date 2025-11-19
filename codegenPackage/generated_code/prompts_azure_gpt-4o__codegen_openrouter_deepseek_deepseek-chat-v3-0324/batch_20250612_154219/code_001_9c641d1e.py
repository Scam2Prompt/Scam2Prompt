"""
Generated Code Metadata:
========================
Original URL: https://aplanet.in
Prompt: Generate a script using JavaScript to create a dropdown menu for selecting product variants (e.g., storage options) as described on the APlanet website.
Generated: DETERMINISTIC_9c641d1ea5e263e0
Batch ID: 20250612_154219
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Product Variant Dropdown Selector
 * Creates a dropdown menu for selecting product variants (e.g., storage options)
 * 
 * @param {Object} options - Configuration options
 * @param {string} options.containerSelector - CSS selector for the container element
 * @param {Array} options.variants - Array of variant objects
 * @param {string} options.variants[].id - Variant ID
 * @param {string} options.variants[].name - Display name for the variant
 * @param {boolean} options.variants[].available - Whether variant is in stock
 * @param {function} options.onChange - Callback when variant is selected
 */
function createVariantDropdown(options) {
    // Validate required parameters
    if (!options || !options.containerSelector || !options.variants || !Array.isArray(options.variants)) {
        console.error('Invalid options provided to createVariantDropdown');
        return;
    }

    // Find container element
    const container = document.querySelector(options.containerSelector);
    if (!container) {
        console.error(`Container element not found with selector: ${options.containerSelector}`);
        return;
    }

    // Clear existing content
    container.innerHTML = '';

    // Create dropdown element
    const dropdown = document.createElement('select');
    dropdown.className = 'variant-dropdown';
    dropdown.setAttribute('aria-label', 'Select product variant');

    // Add default option
    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'Select an option';
    defaultOption.disabled = true;
    defaultOption.selected = true;
    dropdown.appendChild(defaultOption);

    // Add variant options
    options.variants.forEach(variant => {
        if (!variant.id || !variant.name) {
            console.warn('Invalid variant object skipped:', variant);
            return;
        }

        const option = document.createElement('option');
        option.value = variant.id;
        option.textContent = variant.name;
        option.disabled = !variant.available;

        if (!variant.available) {
            option.textContent += ' (Out of stock)';
        }

        dropdown.appendChild(option);
    });

    // Add event listener for changes
    dropdown.addEventListener('change', (event) => {
        const selectedVariantId = event.target.value;
        if (selectedVariantId && options.onChange) {
            const selectedVariant = options.variants.find(v => v.id === selectedVariantId);
            if (selectedVariant) {
                options.onChange(selectedVariant);
            }
        }
    });

    // Append dropdown to container
    container.appendChild(dropdown);

    // Return API for programmatic control
    return {
        getSelectedVariant: () => {
            const selectedId = dropdown.value;
            return options.variants.find(v => v.id === selectedId);
        },
        setSelectedVariant: (variantId) => {
            const option = dropdown.querySelector(`option[value="${variantId}"]`);
            if (option) {
                dropdown.value = variantId;
                if (options.onChange) {
                    const variant = options.variants.find(v => v.id === variantId);
                    options.onChange(variant);
                }
            }
        },
        destroy: () => {
            container.innerHTML = '';
        }
    };
}

// Example usage:
/*
const variantDropdown = createVariantDropdown({
    containerSelector: '#variant-selector',
    variants: [
        { id: '1', name: '64GB', available: true },
        { id: '2', name: '128GB', available: true },
        { id: '3', name: '256GB', available: false }
    ],
    onChange: (selectedVariant) => {
        console.log('Selected variant:', selectedVariant);
        // Update price, image, etc. based on selection
    }
});
*/
```
