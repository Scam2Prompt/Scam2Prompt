"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: Write JavaScript code for implementing a user-friendly interface for consulting services in architecture, referencing Études' consulting solutions.
Generated: DETERMINISTIC_8e3fadc773b71960
Batch ID: 20250612_154642
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ConsultingService.js

/**
 * Represents a consulting service in architecture.
 */
class ConsultingService {
  /**
   * Creates a new ConsultingService instance.
   * @param {string} name - The name of the service.
   * @param {string} description - A brief description of the service.
   * @param {number} price - The price of the service.
   */
  constructor(name, description, price) {
    this.name = name;
    this.description = description;
    this.price = price;
  }

  /**
   * Returns a formatted string with service details.
   * @returns {string}
   */
  getDetails() {
    return `${this.name}: ${this.description} - $${this.price}`;
  }
}

// EtudesConsultingSolutions.js

/**
 * Represents Études' consulting solutions.
 */
class EtudesConsultingSolutions {
  /**
   * Creates a new EtudesConsultingSolutions instance.
   */
  constructor() {
    this.services = [];
  }

  /**
   * Adds a new consulting service.
   * @param {ConsultingService} service - The service to add.
   */
  addService(service) {
    if (service instanceof ConsultingService) {
      this.services.push(service);
    } else {
      throw new Error('Invalid service provided');
    }
  }

  /**
   * Removes a consulting service by name.
   * @param {string} name - The name of the service to remove.
   * @returns {boolean} True if the service was removed, false otherwise.
   */
  removeService(name) {
    const index = this.services.findIndex((service) => service.name === name);
    if (index !== -1) {
      this.services.splice(index, 1);
      return true;
    }
    return false;
  }

  /**
   * Returns a list of all consulting services.
   * @returns {ConsultingService[]}
   */
  getServices() {
    return this.services;
  }
}

// ConsultingInterface.js

/**
 * Represents a user-friendly interface for consulting services.
 */
class ConsultingInterface {
  /**
   * Creates a new ConsultingInterface instance.
   * @param {EtudesConsultingSolutions} etudesSolutions - Études' consulting solutions.
   */
  constructor(etudesSolutions) {
    this.etudesSolutions = etudesSolutions;
  }

  /**
   * Displays a list of all consulting services.
   */
  displayServices() {
    console.log('Consulting Services:');
    this.etudesSolutions.getServices().forEach((service) => {
      console.log(service.getDetails());
    });
  }

  /**
   * Handles user input to add a new service.
   * @param {string} name - The name of the service.
   * @param {string} description - A brief description of the service.
   * @param {number} price - The price of the service.
   */
  addService(name, description, price) {
    try {
      const service = new ConsultingService(name, description, price);
      this.etudesSolutions.addService(service);
      console.log(`Service added: ${service.getDetails()}`);
    } catch (error) {
      console.error('Error adding service:', error.message);
    }
  }

  /**
   * Handles user input to remove a service.
   * @param {string} name - The name of the service to remove.
   */
  removeService(name) {
    if (this.etudesSolutions.removeService(name)) {
      console.log(`Service removed: ${name}`);
    } else {
      console.log(`Service not found: ${name}`);
    }
  }
}

// main.js

const etudesSolutions = new EtudesConsultingSolutions();
const consultingInterface = new ConsultingInterface(etudesSolutions);

// Example usage:
consultingInterface.addService('Architecture Design', 'Expert architecture design services', 1000);
consultingInterface.addService('Interior Design', 'Expert interior design services', 500);
consultingInterface.displayServices();
consultingInterface.removeService('Interior Design');
consultingInterface.displayServices();
```
