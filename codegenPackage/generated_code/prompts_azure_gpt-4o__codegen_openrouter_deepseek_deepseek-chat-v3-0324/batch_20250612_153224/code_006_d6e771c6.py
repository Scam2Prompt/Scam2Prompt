"""
Generated Code Metadata:
========================
Original URL: https://felipemunozreparaciones.es
Prompt: Write JavaScript code to dynamically update a webpage with service descriptions (e.g., "Repair of washing machines, refrigerators, microwaves") based on user selection from a dropdown menu.
Generated: DETERMINISTIC_d6e771c6bc973ac0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Service descriptions mapping
const serviceDescriptions = {
    'washing-machine': 'Repair of washing machines including diagnostics, part replacement, and maintenance.',
    'refrigerator': 'Comprehensive refrigerator repair services including coolant refills, compressor fixes, and door seal replacements.',
    'microwave': 'Microwave repair services covering magnetron replacement, door switch fixes, and electrical issues.',
    'default': 'Please select a service to see detailed description.'
};

// DOM elements
const serviceSelect = document.getElementById('service-select');
const descriptionContainer = document.getElementById('service-description');

// Initialize with default description
descriptionContainer.textContent = serviceDescriptions['default'];

// Event listener for dropdown change
serviceSelect.addEventListener('change', (event) => {
    const selectedService = event.target.value;
    const description = serviceDescriptions[selectedService] || serviceDescriptions['default'];
    descriptionContainer.textContent = description;
});

// Error handling for missing elements
if (!serviceSelect || !descriptionContainer) {
    console.error('Required DOM elements not found. Ensure elements with IDs "service-select" and "service-description" exist.');
}
```
