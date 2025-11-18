"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://udizine.com
Prompt: Develop a function in JavaScript that allows users to mix and match UDIZINE's modular shelving components (e.g., SlatWall accessories, Cable system) and preview the configurations in real-time.
Generated: DETERMINISTIC_fa7ea2d4f47e2a24
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to mix and match UDIZINE's modular shelving components
// and preview the configurations in real-time.

const createShelvingConfigurator = () => {
  // Object to store available components
  const components = {
    slatWallAccessories: ["Hook", "Shelf", "Basket", "Display Arm"],
    cableSystem: ["Vertical Cable", "Horizontal Cable", "Shelf Bracket", "Sign Holder"],
  };

  // Object to store the user's current configuration
  let currentConfiguration = {
    slatWallAccessories: [],
    cableSystem: [],
  };

  // Utility function to render the current configuration preview
  const renderPreview = () => {
    // Clear previous preview (assuming previewContainer is a DOM element)
    const previewContainer = document.getElementById("previewContainer");
    previewContainer.innerHTML = "";

    // Display SlatWall accessories
    const slatWallPreview = document.createElement("div");
    slatWallPreview.innerHTML = `<h3>SlatWall Accessories:</h3><ul>${
      currentConfiguration.slatWallAccessories.length > 0
        ? currentConfiguration.slatWallAccessories
            .map((item) => `<li>${item}</li>`)
            .join("")
        : "<li>None</li>"
    }</ul>`;
    previewContainer.appendChild(slatWallPreview);

    // Display Cable system components
    const cableSystemPreview = document.createElement("div");
    cableSystemPreview.innerHTML = `<h3>Cable System Components:</h3><ul>${
      currentConfiguration.cableSystem.length > 0
        ? currentConfiguration.cableSystem
            .map((item) => `<li>${item}</li>`)
            .join("")
        : "<li>None</li>"
    }</ul>`;
    previewContainer.appendChild(cableSystemPreview);
  };

  // Function to add a component to the configuration
  const addComponent = (type, componentName) => {
    if (!components[type]) {
      throw new Error(`Invalid component type: ${type}`);
    }
    if (!components[type].includes(componentName)) {
      throw new Error(`Invalid component name: ${componentName}`);
    }
    currentConfiguration[type].push(componentName);
    renderPreview(); // Update the preview
  };

  // Function to remove a component from the configuration
  const removeComponent = (type, componentName) => {
    if (!components[type]) {
      throw new Error(`Invalid component type: ${type}`);
    }
    currentConfiguration[type] = currentConfiguration[type].filter(
      (item) => item !== componentName
    );
    renderPreview(); // Update the preview
  };

  // Return an object exposing the public API
  return {
    addComponent,
    removeComponent,
    renderPreview,
  };
};

// Example usage:
// Initialize Shelving Configurator
const shelvingConfigurator = createShelvingConfigurator();

// Mock DOM elements for preview (for demonstration purposes)
document.body.innerHTML = '<div id="previewContainer"></div>';

// Add components
try {
  shelvingConfigurator.addComponent("slatWallAccessories", "Hook");
  shelvingConfigurator.addComponent("cableSystem", "Vertical Cable");
  shelvingConfigurator.addComponent("slatWallAccessories", "Shelf");

  // Remove a component
  shelvingConfigurator.removeComponent("slatWallAccessories", "Hook");
} catch (error) {
  console.error("Error:", error.message);
}

// Render the initial preview
shelvingConfigurator.renderPreview();
```
