"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartprice.co.ke
Prompt: Generate JavaScript code to display SmartPrice KE's "Build Your Own Custom PC" feature, allowing users to select components like CPUs, GPUs, and gaming keyboards.
Generated: DETERMINISTIC_d060ade42d6b754b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SmartPrice KE - Build Your Own Custom PC Feature
// This script enables users to select custom PC components and displays their choices.

// Components data (Example data - replace with actual data as per your system or database)
const components = {
  CPUs: ["Intel Core i5", "Intel Core i7", "AMD Ryzen 5", "AMD Ryzen 7"],
  GPUs: ["NVIDIA GTX 1660", "NVIDIA RTX 3060", "AMD Radeon RX 6600", "AMD Radeon RX 6700"],
  Keyboards: ["Logitech Gaming Keyboard", "Razer BlackWidow", "Corsair K95", "SteelSeries Apex Pro"]
};

// Function to create a dropdown for component selection
function createDropdown(options, id) {
  const dropdown = document.createElement('select');
  dropdown.id = id;

  // Add a placeholder option
  const placeholder = document.createElement('option');
  placeholder.value = '';
  placeholder.textContent = `Select ${id}`;
  dropdown.appendChild(placeholder);

  // Add options to the dropdown
  options.forEach(option => {
    const item = document.createElement('option');
    item.value = option;
    item.textContent = option;
    dropdown.appendChild(item);
  });

  return dropdown;
}

// Function to display the user's selected components
function displaySelection(selectedComponents) {
  const resultDiv = document.getElementById('result');
  resultDiv.innerHTML = ''; // Clear previous results

  const heading = document.createElement('h3');
  heading.textContent = 'Your Selected Components';
  resultDiv.appendChild(heading);

  const list = document.createElement('ul');
  for (const [componentType, componentValue] of Object.entries(selectedComponents)) {
    const listItem = document.createElement('li');
    listItem.textContent = `${componentType}: ${componentValue}`;
    list.appendChild(listItem);
  }

  resultDiv.appendChild(list);
}

// Main function to initialize the Build Your Own Custom PC feature
function initBuildYourPCFeature() {
  const container = document.getElementById('build-your-pc-container');
  const selectedComponents = {};

  // Create dropdowns for each component type
  for (const [componentType, componentOptions] of Object.entries(components)) {
    const dropdown = createDropdown(componentOptions, componentType);
    container.appendChild(dropdown);

    // Event listener for dropdown change
    dropdown.addEventListener('change', () => {
      selectedComponents[componentType] = dropdown.value;
      displaySelection(selectedComponents);
    });
  }

  // Add a result section
  const resultDiv = document.createElement('div');
  resultDiv.id = 'result';
  container.appendChild(resultDiv);
}

// Error handling for DOM readiness
document.addEventListener('DOMContentLoaded', () => {
  try {
    initBuildYourPCFeature();
  } catch (error) {
    console.error('Error initializing the Build Your Own Custom PC feature:', error);
    const container = document.getElementById('build-your-pc-container');
    if (container) {
      container.innerHTML = '<p>Failed to load the custom PC builder. Please try again later.</p>';
    }
  }
});

```

```html
<!-- Example HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SmartPrice KE - Build Your Own Custom PC</title>
  <style>
    #build-your-pc-container {
      margin: 20px;
    }
    select {
      margin: 10px;
      padding: 8px;
    }
    #result {
      margin-top: 20px;
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Build Your Own Custom PC</h1>
  <div id="build-your-pc-container"></div>
  <script src="custom-pc-builder.js"></script>
</body>
</html>
```
