"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: Write a script in JavaScript to dynamically display a list of school locations and services, similar to the "Nuestras Sedes" section on the Politécnico Municipal de Cali's website.
Generated: DETERMINISTIC_a2e73de31919378d
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SchoolLocation.js

class SchoolLocation {
  /**
   * Represents a school location.
   * @param {string} name - Location name.
   * @param {string} address - Location address.
   * @param {string} phone - Location phone number.
   * @param {string[]} services - List of services offered.
   */
  constructor(name, address, phone, services) {
    this.name = name;
    this.address = address;
    this.phone = phone;
    this.services = services;
  }
}

// SchoolLocationService.js

class SchoolLocationService {
  /**
   * Manages school locations.
   */
  constructor() {
    this.locations = [];
  }

  /**
   * Adds a school location.
   * @param {SchoolLocation} location - School location to add.
   */
  addLocation(location) {
    this.locations.push(location);
  }

  /**
   * Retrieves all school locations.
   * @returns {SchoolLocation[]} List of school locations.
   */
  getLocations() {
    return this.locations;
  }

  /**
   * Retrieves a school location by name.
   * @param {string} name - Name of the location to retrieve.
   * @returns {SchoolLocation|null} School location or null if not found.
   */
  getLocationByName(name) {
    return this.locations.find((location) => location.name === name) || null;
  }
}

// school-locations.js

// Import required modules
import { SchoolLocation } from './SchoolLocation.js';
import { SchoolLocationService } from './SchoolLocationService.js';

// Create school location service
const schoolLocationService = new SchoolLocationService();

// Sample data
const locations = [
  new SchoolLocation(
    'Sede Principal',
    'Calle 10 # 5-50',
    '1234567',
    ['Secretaría', 'Biblioteca', 'Laboratorios']
  ),
  new SchoolLocation(
    'Sede Secundaria',
    'Calle 20 # 10-20',
    '8901234',
    ['Aulas', 'Gimnasio', 'Zona de Recreación']
  ),
];

// Add locations to service
locations.forEach((location) => schoolLocationService.addLocation(location));

// Function to display locations
function displayLocations(locations) {
  const locationsElement = document.getElementById('locations');

  if (!locationsElement) {
    console.error('Locations element not found');
    return;
  }

  locations.forEach((location) => {
    const locationElement = document.createElement('div');
    locationElement.innerHTML = `
      <h2>${location.name}</h2>
      <p>Dirección: ${location.address}</p>
      <p>Teléfono: ${location.phone}</p>
      <h3>Servicios:</h3>
      <ul>
        ${location.services.map((service) => `<li>${service}</li>`).join('')}
      </ul>
    `;
    locationsElement.appendChild(locationElement);
  });
}

// Main function
function main() {
  try {
    const locations = schoolLocationService.getLocations();
    displayLocations(locations);
  } catch (error) {
    console.error('Error displaying locations:', error);
  }
}

// Call main function
main();
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nuestras Sedes</title>
  <style>
    /* Basic styling for demonstration purposes */
    body {
      font-family: Arial, sans-serif;
    }
    #locations {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .location {
      margin: 20px;
      padding: 20px;
      border: 1px solid #ddd;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
  </style>
</head>
<body>
  <h1>Nuestras Sedes</h1>
  <div id="locations"></div>

  <script type="module" src="school-locations.js"></script>
</body>
</html>
```
