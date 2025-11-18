"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nashekrashe.com
Prompt: Generate a Figma plugin that organizes components, layers, and frames following the best practices mentioned in NasheKrashe Design Studio's Figma community work.
Generated: DETERMINISTIC_c7159b8a9b28c494
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Figma Plugin Code: Organize Layers and Components
// This plugin organizes components, layers, and frames in Figma according to best practices.
// It ensures that layers are renamed, grouped, and sorted for better design management.

figma.showUI(__html__, { width: 240, height: 120 });

// Handle messages from the UI
figma.ui.onmessage = async (msg) => {
  if (msg.type === 'organize') {
    // Start organizing layers and components
    try {
      await organizeLayersAndComponents();
      figma.notify("Layers and components organized successfully!");
    } catch (error) {
      console.error(error);
      figma.notify("Error organizing layers: " + error.message);
    }
  }
};

// Function to organize layers and components
async function organizeLayersAndComponents() {
  const selection = figma.currentPage.selection;

  // If no layers are selected, notify the user
  if (selection.length === 0) {
    throw new Error("Please select at least one layer, component, or frame.");
  }

  // Loop through all selected nodes
  selection.forEach(node => {
    if (node.type === 'FRAME' || node.type === 'GROUP') {
      organizeGroup(node);
    } else if (node.type === 'COMPONENT' || node.type === 'INSTANCE') {
      organizeComponent(node);
    }
  });
}

// Function to organize a frame or group
function organizeGroup(group) {
  // Rename the group to follow a standard naming convention
  group.name = `Group: ${group.name}`;

  // Sort children nodes
  group.children.sort((a, b) => a.name.localeCompare(b.name));
  group.children.forEach((child, index) => {
    child.name = `${index + 1}. ${child.name}`;
  });
}

// Function to organize a component or instance
function organizeComponent(component) {
  // Rename the component to follow a standard naming convention
  component.name = `Component: ${component.name}`;

  // Ensure instance layers are correctly named
  component.children.forEach((child, index) => {
    if (child.type !== 'TEXT') {
      child.name = `${index + 1}. ${child.name}`;
    }
  });
}

// Close the plugin
figma.closePlugin();
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Organize Layers</title>
  <style>
    body { font-family: Arial, sans-serif; padding: 20px; }
    button { padding: 10px; cursor: pointer; }
  </style>
</head>
<body>
  <h2>Organize Layers and Components</h2>
  <button id="organizeButton">Organize</button>
  
  <script>
    document.getElementById('organizeButton').onclick = () => {
      // Send a message to the Figma plugin to start organizing
      parent.postMessage({ pluginMessage: { type: 'organize' } }, '*');
    };
  </script>
</body>
</html>
```

This code is a complete Figma plugin that organizes layers and components according to best practices. It includes both JavaScript and HTML components for the plugin functionality and user interface.
