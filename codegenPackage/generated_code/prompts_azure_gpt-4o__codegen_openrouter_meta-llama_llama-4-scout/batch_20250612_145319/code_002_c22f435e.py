"""
Generated Code Metadata:
========================
Original URL: https://ww-magiceden-connect-tw.blogspot.com
Prompt: Generate code in JavaScript to display a list of automotive service center addresses dynamically, including locations such as Passo Fundo and Novo Hamburgo, using data from a JSON file.
Generated: DETERMINISTIC_c22f435eba819af9
Batch ID: 20250612_145319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// serviceCenters.js
/**
 * Service center data model.
 * @typedef {Object} ServiceCenter
 * @property {string} name - Service center name.
 * @property {string} address - Service center address.
 * @property {string} city - Service center city.
 */

// Load service center data from JSON file
async function loadServiceCenters() {
  try {
    const response = await fetch('serviceCenters.json');
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Error loading service centers:', error);
    return [];
  }
}

// Render service center list
async function renderServiceCenterList() {
  const serviceCenters = await loadServiceCenters();
  const serviceCenterListElement = document.getElementById('service-center-list');

  if (!serviceCenterListElement) {
    console.error('Service center list element not found');
    return;
  }

  serviceCenters.forEach((serviceCenter) => {
    const listItemElement = document.createElement('li');
    listItemElement.textContent = `${serviceCenter.name} - ${serviceCenter.address}, ${serviceCenter.city}`;
    serviceCenterListElement.appendChild(listItemElement);
  });
}

// Initialize service center list on page load
document.addEventListener('DOMContentLoaded', renderServiceCenterList);
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Service Center List</title>
  <style>
    /* Basic styling for service center list */
    #service-center-list {
      list-style: none;
      padding: 0;
      margin: 0;
    }
    #service-center-list li {
      padding: 10px;
      border-bottom: 1px solid #ccc;
    }
  </style>
</head>
<body>
  <h1>Service Center List</h1>
  <ul id="service-center-list"></ul>
  <script src="serviceCenters.js"></script>
</body>
</html>
```

```json
// serviceCenters.json
[
  {
    "name": "Service Center 1",
    "address": "Rua 1, 123",
    "city": "Passo Fundo"
  },
  {
    "name": "Service Center 2",
    "address": "Avenida 2, 456",
    "city": "Novo Hamburgo"
  },
  {
    "name": "Service Center 3",
    "address": "Rua 3, 789",
    "city": "Porto Alegre"
  }
]
```
