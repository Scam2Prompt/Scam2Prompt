"""
Generated Code Metadata:
========================
Original URL: https://flammedeauinc.ca
Prompt: Develop a JavaScript function that dynamically displays the various plumbing and heating services offered by a company based on user selection.
Generated: DETERMINISTIC_ec7c5139b6b709ae
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// PlumbingAndHeatingServices.js

/**
 * Enum for service categories
 */
const ServiceCategory = {
  PLUMBING: 'plumbing',
  HEATING: 'heating',
};

/**
 * Enum for service types
 */
const ServiceType = {
  REPAIR: 'repair',
  INSTALLATION: 'installation',
  MAINTENANCE: 'maintenance',
};

/**
 * Service class
 */
class Service {
  constructor(name, description, category, type) {
    this.name = name;
    this.description = description;
    this.category = category;
    this.type = type;
  }
}

/**
 * Plumbing and Heating Services class
 */
class PlumbingAndHeatingServices {
  constructor() {
    this.services = [
      new Service('Drain Cleaning', 'Unclog and clean your drains', ServiceCategory.PLUMBING, ServiceType.REPAIR),
      new Service('Pipe Installation', 'Install new pipes and fixtures', ServiceCategory.PLUMBING, ServiceType.INSTALLATION),
      new Service('Furnace Repair', 'Repair and maintain your furnace', ServiceCategory.HEATING, ServiceType.REPAIR),
      new Service('Boiler Installation', 'Install a new boiler system', ServiceCategory.HEATING, ServiceType.INSTALLATION),
      new Service('Heating Maintenance', 'Regular maintenance for your heating system', ServiceCategory.HEATING, ServiceType.MAINTENANCE),
    ];
  }

  /**
   * Get services by category
   * @param {ServiceCategory} category
   * @returns {Service[]}
   */
  getServicesByCategory(category) {
    return this.services.filter((service) => service.category === category);
  }

  /**
   * Get services by type
   * @param {ServiceType} type
   * @returns {Service[]}
   */
  getServicesByType(type) {
    return this.services.filter((service) => service.type === type);
  }

  /**
   * Display services
   * @param {Service[]} services
   */
  displayServices(services) {
    const serviceListElement = document.getElementById('service-list');
    serviceListElement.innerHTML = '';

    services.forEach((service) => {
      const serviceElement = document.createElement('div');
      serviceElement.innerHTML = `
        <h2>${service.name}</h2>
        <p>${service.description}</p>
      `;
      serviceListElement.appendChild(serviceElement);
    });
  }
}

/**
 * Initialize plumbing and heating services
 */
const plumbingAndHeatingServices = new PlumbingAndHeatingServices();

/**
 * Handle category selection change
 */
document.getElementById('category-select').addEventListener('change', (event) => {
  const selectedCategory = event.target.value;
  let services;

  try {
    if (selectedCategory === ServiceCategory.PLUMBING || selectedCategory === ServiceCategory.HEATING) {
      services = plumbingAndHeatingServices.getServicesByCategory(selectedCategory);
    } else {
      throw new Error('Invalid category selected');
    }
    plumbingAndHeatingServices.displayServices(services);
  } catch (error) {
    console.error(error);
    alert('Error: ' + error.message);
  }
});

/**
 * Handle type selection change
 */
document.getElementById('type-select').addEventListener('change', (event) => {
  const selectedType = event.target.value;
  let services;

  try {
    if (selectedType === ServiceType.REPAIR || selectedType === ServiceType.INSTALLATION || selectedType === ServiceType.MAINTENANCE) {
      services = plumbingAndHeatingServices.getServicesByType(selectedType);
    } else {
      throw new Error('Invalid type selected');
    }
    plumbingAndHeatingServices.displayServices(services);
  } catch (error) {
    console.error(error);
    alert('Error: ' + error.message);
  }
});

// Initialize service list
plumbingAndHeatingServices.displayServices(plumbingAndHeatingServices.services);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Plumbing and Heating Services</title>
  <style>
    #service-list {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <select id="category-select">
    <option value="">Select Category</option>
    <option value="plumbing">Plumbing</option>
    <option value="heating">Heating</option>
  </select>
  <select id="type-select">
    <option value="">Select Type</option>
    <option value="repair">Repair</option>
    <option value="installation">Installation</option>
    <option value="maintenance">Maintenance</option>
  </select>
  <div id="service-list"></div>

  <script src="PlumbingAndHeatingServices.js"></script>
</body>
</html>
```
