"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felipemunozreparaciones.es
Prompt: Write JavaScript code to dynamically update a webpage with service descriptions (e.g., "Repair of washing machines, refrigerators, microwaves") based on user selection from a dropdown menu.
Generated: DETERMINISTIC_d6e771c6bc973ac0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML Structure:
// <select id="serviceDropdown">
//   <option value="washingMachines">Washing Machines</option>
//   <option value="refrigerators">Refrigerators</option>
//   <option value="microwaves">Microwaves</option>
// </select>
// <div id="serviceDescription"></div>

// JavaScript Code:
document.addEventListener("DOMContentLoaded", () => {
    // Map of services and their descriptions
    const serviceDescriptions = {
        washingMachines: "Repair of washing machines - fast and reliable service.",
        refrigerators: "Repair of refrigerators - keeping your food fresh.",
        microwaves: "Repair of microwaves - efficient and effective solutions."
    };

    // Dropdown and description container elements
    const serviceDropdown = document.getElementById("serviceDropdown");
    const serviceDescription = document.getElementById("serviceDescription");

    // Function to update the service description based on user selection
    const updateServiceDescription = () => {
        // Get the selected value
        const selectedService = serviceDropdown.value;

        // Update the description container with the selected service's description
        if (serviceDescriptions[selectedService]) {
            serviceDescription.textContent = serviceDescriptions[selectedService];
        } else {
            // Handle case for unknown or missing service
            serviceDescription.textContent = "Please select a valid service.";
        }
    };

    // Attach event listener to dropdown menu for change events
    serviceDropdown.addEventListener("change", updateServiceDescription);

    // Initialize with default description
    updateServiceDescription();
});
```
