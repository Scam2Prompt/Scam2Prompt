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
// Define a class for the modular shelving system
class ModularShelving {
    constructor() {
        // Initialize an empty array to hold the components
        this.components = [];
    }

    /**
     * Adds a component to the shelving configuration.
     * @param {string} component - The name of the component to add.
     * @throws Will throw an error if the component is already added.
     */
    addComponent(component) {
        if (this.components.includes(component)) {
            throw new Error(`Component "${component}" is already added.`);
        }
        this.components.push(component);
        this.render();
    }

    /**
     * Removes a component from the shelving configuration.
     * @param {string} component - The name of the component to remove.
     * @throws Will throw an error if the component is not found.
     */
    removeComponent(component) {
        const index = this.components.indexOf(component);
        if (index === -1) {
            throw new Error(`Component "${component}" not found.`);
        }
        this.components.splice(index, 1);
        this.render();
    }

    /**
     * Renders the current configuration of shelving components.
     * This method updates the visual representation in the DOM.
     */
    render() {
        const configContainer = document.getElementById('configContainer');
        configContainer.innerHTML = ''; // Clear previous configuration

        this.components.forEach(component => {
            const componentElement = document.createElement('div');
            componentElement.className = 'component';
            componentElement.innerText = component;
            configContainer.appendChild(componentElement);
        });
    }
}

// Initialize the modular shelving system
const shelvingSystem = new ModularShelving();

// Handle user input for adding/removing components
document.getElementById('addComponentButton').addEventListener('click', () => {
    const componentInput = document.getElementById('componentInput').value;
    if (componentInput) {
        try {
            shelvingSystem.addComponent(componentInput);
            document.getElementById('componentInput').value = ''; // Clear input
        } catch (error) {
            alert(error.message);
        }
    } else {
        alert('Please enter a component name.');
    }
});

document.getElementById('removeComponentButton').addEventListener('click', () => {
    const componentInput = document.getElementById('componentInput').value;
    if (componentInput) {
        try {
            shelvingSystem.removeComponent(componentInput);
            document.getElementById('componentInput').value = ''; // Clear input
        } catch (error) {
            alert(error.message);
        }
    } else {
        alert('Please enter a component name.');
    }
});
```

```html
<!-- HTML Structure for User Interface -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modular Shelving Configurator</title>
    <style>
        #configContainer {
            border: 1px solid #ccc;
            padding: 10px;
            margin-top: 10px;
        }
        .component {
            padding: 8px;
            border: 1px solid #999;
            margin: 5px 0;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Modular Shelving Configurator</h1>
    <input type="text" id="componentInput" placeholder="Enter component name">
    <button id="addComponentButton">Add Component</button>
    <button id="removeComponentButton">Remove Component</button>
    <div id="configContainer"></div>
    <script src="path/to/your/javascript/file.js"></script>
</body>
</html>
```
