"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aydinspirate.com
Prompt: Write JavaScript code to create a user interface for controlling "Toldos Verticales" awnings, referencing the customization options mentioned on the Ayd Inspirate website.
Generated: DETERMINISTIC_28dc9dbf214b4d40
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// JavaScript code to create a user interface for controlling "Toldos Verticales" awnings

// Ensure the DOM has fully loaded
document.addEventListener("DOMContentLoaded", () => {
    // Create the main container for the UI
    const appContainer = document.createElement("div");
    appContainer.id = "awningController";
    appContainer.style.fontFamily = "Arial, sans-serif";
    appContainer.style.padding = "20px";
    appContainer.style.maxWidth = "400px";
    appContainer.style.margin = "auto";
    appContainer.style.border = "1px solid #ccc";
    appContainer.style.borderRadius = "8px";
    appContainer.style.boxShadow = "0px 4px 8px rgba(0, 0, 0, 0.1)";
    
    // Header section
    const header = document.createElement("h2");
    header.textContent = "Toldos Verticales Controller";
    header.style.textAlign = "center";
    header.style.marginBottom = "20px";
    appContainer.appendChild(header);

    // Functionality: Open/Close Awnings
    const statusText = document.createElement("p");
    statusText.id = "status";
    statusText.textContent = "Status: Closed";
    statusText.style.color = "#333";
    statusText.style.fontWeight = "bold";
    appContainer.appendChild(statusText);

    const toggleButton = document.createElement("button");
    toggleButton.id = "toggleButton";
    toggleButton.textContent = "Open Awnings";
    toggleButton.style.display = "block";
    toggleButton.style.margin = "10px auto";
    toggleButton.style.padding = "10px 20px";
    toggleButton.style.border = "none";
    toggleButton.style.borderRadius = "5px";
    toggleButton.style.backgroundColor = "#28a745";
    toggleButton.style.color = "#fff";
    toggleButton.style.cursor = "pointer";

    // Toggle open/close status
    toggleButton.addEventListener("click", () => {
        if (statusText.textContent.includes("Closed")) {
            statusText.textContent = "Status: Open";
            toggleButton.textContent = "Close Awnings";
            toggleButton.style.backgroundColor = "#dc3545";
        } else {
            statusText.textContent = "Status: Closed";
            toggleButton.textContent = "Open Awnings";
            toggleButton.style.backgroundColor = "#28a745";
        }
    });
    appContainer.appendChild(toggleButton);

    // Functionality: Adjust Awning Height
    const heightLabel = document.createElement("label");
    heightLabel.textContent = "Adjust Height (%):";
    heightLabel.htmlFor = "heightSlider";
    heightLabel.style.display = "block";
    heightLabel.style.marginTop = "20px";
    heightLabel.style.fontWeight = "bold";
    appContainer.appendChild(heightLabel);

    const heightSlider = document.createElement("input");
    heightSlider.id = "heightSlider";
    heightSlider.type = "range";
    heightSlider.min = "0";
    heightSlider.max = "100";
    heightSlider.value = "100";
    heightSlider.style.width = "100%";
    heightSlider.style.marginTop = "10px";
    appContainer.appendChild(heightSlider);

    const heightValueDisplay = document.createElement("p");
    heightValueDisplay.id = "heightValue";
    heightValueDisplay.textContent = "Current Height: 100%";
    heightValueDisplay.style.textAlign = "center";
    heightValueDisplay.style.marginTop = "10px";
    appContainer.appendChild(heightValueDisplay);

    // Update height value dynamically
    heightSlider.addEventListener("input", () => {
        heightValueDisplay.textContent = `Current Height: ${heightSlider.value}%`;
    });

    // Functionality: Change Awning Color
    const colorLabel = document.createElement("label");
    colorLabel.textContent = "Choose Awning Color:";
    colorLabel.htmlFor = "colorPicker";
    colorLabel.style.display = "block";
    colorLabel.style.marginTop = "20px";
    colorLabel.style.fontWeight = "bold";
    appContainer.appendChild(colorLabel);

    const colorPicker = document.createElement("input");
    colorPicker.id = "colorPicker";
    colorPicker.type = "color";
    colorPicker.value = "#ff6600";
    colorPicker.style.display = "block";
    colorPicker.style.marginTop = "10px";
    colorPicker.style.marginBottom = "20px";
    colorPicker.style.width = "100%";
    colorPicker.style.height = "40px";
    appContainer.appendChild(colorPicker);

    const colorDisplay = document.createElement("p");
    colorDisplay.id = "colorDisplay";
    colorDisplay.textContent = "Selected Color: #ff6600";
    colorDisplay.style.textAlign = "center";
    appContainer.appendChild(colorDisplay);

    // Update color dynamically
    colorPicker.addEventListener("input", () => {
        colorDisplay.textContent = `Selected Color: ${colorPicker.value}`;
        appContainer.style.borderColor = colorPicker.value; // Optional: change border color
    });

    // Append the UI to the body
    document.body.appendChild(appContainer);
});
```
