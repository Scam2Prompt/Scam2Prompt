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
// Window Configuration Tool
// This tool allows users to select window types and view their specifications.

class WindowType {
    constructor(name, specifications) {
        this.name = name;
        this.specifications = specifications;
    }
}

// Sample window types with specifications
const windowTypes = [
    new WindowType("Aluplast Ideal 5000", {
        dimensions: "1200mm x 1400mm",
        material: "uPVC",
        color: "White",
        energyEfficiency: "A+",
        warranty: "10 years"
    }),
    new WindowType("Aluplast Ideal 4000", {
        dimensions: "1200mm x 1400mm",
        material: "uPVC",
        color: "Brown",
        energyEfficiency: "A",
        warranty: "10 years"
    }),
    new WindowType("Aluplast Ideal 7000", {
        dimensions: "1200mm x 1400mm",
        material: "uPVC",
        color: "Grey",
        energyEfficiency: "A++",
        warranty: "10 years"
    })
];

// Function to create the window configuration tool
function createWindowConfigTool() {
    // Create a dropdown for window types
    const selectElement = document.createElement("select");
    selectElement.id = "windowTypeSelect";

    // Populate dropdown with window types
    windowTypes.forEach(windowType => {
        const option = document.createElement("option");
        option.value = windowType.name;
        option.textContent = windowType.name;
        selectElement.appendChild(option);
    });

    // Create a div to display specifications
    const specsDisplay = document.createElement("div");
    specsDisplay.id = "specsDisplay";
    specsDisplay.style.marginTop = "20px";

    // Event listener to update specifications on selection change
    selectElement.addEventListener("change", (event) => {
        const selectedType = windowTypes.find(type => type.name === event.target.value);
        if (selectedType) {
            displaySpecifications(selectedType);
        } else {
            specsDisplay.textContent = "Specifications not found.";
        }
    });

    // Append elements to the body
    document.body.appendChild(selectElement);
    document.body.appendChild(specsDisplay);

    // Initialize with the first window type
    displaySpecifications(windowTypes[0]);
}

// Function to display specifications of the selected window type
function displaySpecifications(windowType) {
    const specsDisplay = document.getElementById("specsDisplay");
    specsDisplay.innerHTML = `
        <h3>Specifications for ${windowType.name}</h3>
        <ul>
            <li><strong>Dimensions:</strong> ${windowType.specifications.dimensions}</li>
            <li><strong>Material:</strong> ${windowType.specifications.material}</li>
            <li><strong>Color:</strong> ${windowType.specifications.color}</li>
            <li><strong>Energy Efficiency:</strong> ${windowType.specifications.energyEfficiency}</li>
            <li><strong>Warranty:</strong> ${windowType.specifications.warranty}</li>
        </ul>
    `;
}

// Error handling for DOMContentLoaded event
document.addEventListener("DOMContentLoaded", () => {
    try {
        createWindowConfigTool();
    } catch (error) {
        console.error("Error initializing the window configuration tool:", error);
    }
});
```
