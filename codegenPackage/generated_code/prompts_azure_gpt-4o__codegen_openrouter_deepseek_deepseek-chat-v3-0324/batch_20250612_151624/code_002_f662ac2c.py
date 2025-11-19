"""
Generated Code Metadata:
========================
Original URL: https://unitedcabinetry.com.au
Prompt: Create a function in JavaScript to automate the process of collecting user inputs for cabinetry specifications (e.g., appliance selections, plumbing fixtures, cabinetry colors) as described in the design stage on United Cabinetry.
Generated: DETERMINISTIC_f662ac2ce75d548f
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Collects cabinetry specifications from user inputs.
 * @returns {Object} An object containing all collected specifications
 * @throws {Error} If required fields are missing or invalid
 */
function collectCabinetrySpecifications() {
    // Validate required fields exist in the DOM
    const requiredFields = [
        'appliance-selection',
        'plumbing-fixtures',
        'cabinetry-color',
        'cabinetry-style',
        'countertop-material'
    ];

    const missingFields = requiredFields.filter(fieldId => !document.getElementById(fieldId));
    if (missingFields.length > 0) {
        throw new Error(`Missing required fields: ${missingFields.join(', ')}`);
    }

    // Collect values from form inputs
    const specifications = {
        appliances: getSelectedValues('appliance-selection'),
        plumbingFixtures: getSelectedValues('plumbing-fixtures'),
        cabinetryColor: document.getElementById('cabinetry-color').value.trim(),
        cabinetryStyle: document.getElementById('cabinetry-style').value.trim(),
        countertopMaterial: document.getElementById('countertop-material').value.trim(),
        additionalFeatures: getSelectedValues('additional-features'),
        notes: document.getElementById('notes')?.value.trim() || ''
    };

    // Validate required values
    if (!specifications.cabinetryColor || !specifications.cabinetryStyle || !specifications.countertopMaterial) {
        throw new Error('Cabinetry color, style, and countertop material are required');
    }

    if (specifications.appliances.length === 0) {
        throw new Error('At least one appliance must be selected');
    }

    return specifications;
}

/**
 * Helper function to get selected values from multi-select or checkbox groups
 * @param {string} fieldId - The ID of the field to get values from
 * @returns {Array} Array of selected values
 */
function getSelectedValues(fieldId) {
    const field = document.getElementById(fieldId);
    if (!field) return [];

    if (field.type === 'select-multiple') {
        return Array.from(field.selectedOptions).map(option => option.value);
    }

    if (field.type === 'checkbox') {
        return field.checked ? [field.value] : [];
    }

    // Handle checkbox groups
    const checkboxes = document.querySelectorAll(`input[name="${fieldId}"]:checked`);
    if (checkboxes.length > 0) {
        return Array.from(checkboxes).map(checkbox => checkbox.value);
    }

    // Fallback to single value
    return field.value ? [field.value] : [];
}

/**
 * Event handler for form submission
 * @param {Event} event - The form submission event
 */
function handleSpecificationSubmit(event) {
    event.preventDefault();
    
    try {
        const specifications = collectCabinetrySpecifications();
        // Process the specifications (e.g., send to server, display confirmation)
        console.log('Collected specifications:', specifications);
        alert('Specifications submitted successfully!');
    } catch (error) {
        console.error('Error collecting specifications:', error);
        alert(`Error: ${error.message}`);
    }
}

// Initialize form submission handler if the form exists
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('cabinetry-spec-form');
    if (form) {
        form.addEventListener('submit', handleSpecificationSubmit);
    }
});
```
