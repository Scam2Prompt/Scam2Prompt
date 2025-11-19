"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Create a JavaScript function that dynamically displays the service areas of Coastal Roofing & Waterproofing on a webpage.
Generated: DETERMINISTIC_263a384df1361418
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ServiceAreaDisplay.js

/**
 * Displays the service areas of Coastal Roofing & Waterproofing on a webpage.
 */

// Define the service areas data
const serviceAreas = [
  { id: 1, name: 'Beachside', description: 'Coastal areas along beaches' },
  { id: 2, name: 'Coastal Towns', description: 'Towns and cities along the coast' },
  { id: 3, name: 'Inland Coastal', description: 'Inland areas near the coast' },
  // Add more service areas as needed
];

/**
 * Displays the service areas on the webpage.
 * @param {HTMLElement} containerElement - The container element to display the service areas in.
 */
function displayServiceAreas(containerElement) {
  try {
    // Check if the container element exists
    if (!containerElement) {
      throw new Error('Container element not found');
    }

    // Create the service areas container
    const serviceAreasContainer = document.createElement('div');
    serviceAreasContainer.classList.add('service-areas-container');

    // Iterate over the service areas and create HTML elements
    serviceAreas.forEach((serviceArea) => {
      const serviceAreaElement = document.createElement('div');
      serviceAreaElement.classList.add('service-area');

      const nameElement = document.createElement('h2');
      nameElement.textContent = serviceArea.name;
      serviceAreaElement.appendChild(nameElement);

      const descriptionElement = document.createElement('p');
      descriptionElement.textContent = serviceArea.description;
      serviceAreaElement.appendChild(descriptionElement);

      serviceAreasContainer.appendChild(serviceAreaElement);
    });

    // Append the service areas container to the container element
    containerElement.appendChild(serviceAreasContainer);
  } catch (error) {
    console.error('Error displaying service areas:', error);
  }
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const serviceAreasContainer = document.getElementById('service-areas');
  displayServiceAreas(serviceAreasContainer);
});
```

```css
/* styles.css */

.service-areas-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
}

.service-area {
  margin: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: calc(33.33% - 20px);
}

.service-area h2 {
  margin-top: 0;
}

.service-area p {
  margin-bottom: 20px;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Coastal Roofing & Waterproofing Service Areas</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="service-areas"></div>
  <script src="ServiceAreaDisplay.js"></script>
</body>
</html>
```
