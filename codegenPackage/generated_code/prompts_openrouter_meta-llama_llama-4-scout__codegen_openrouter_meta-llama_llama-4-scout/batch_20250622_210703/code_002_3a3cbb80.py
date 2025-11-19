"""
Generated Code Metadata:
========================
Original URL: https://reparaciondeturbo.cl
Prompt: Generate a code snippet in JavaScript to create a simple website chatbot that provides information about diesel turbocharger repair services, including diagnosis, repair times, and contact details.
Generated: DETERMINISTIC_3a3cbb8022e27623
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Define a class for the chatbot
class DieselTurbochargerChatbot {
  /**
   * Constructor to initialize the chatbot's data
   */
  constructor() {
    // Data for diesel turbocharger repair services
    this.services = {
      diagnosis: {
        description: "Diagnose the issue with your diesel turbocharger",
        time: "30 minutes to 1 hour",
        price: "$100"
      },
      repair: {
        description: "Repair or replace the diesel turbocharger",
        time: "2-5 hours",
        price: "$500-$2000"
      }
    };

    // Contact details
    this.contact = {
      phone: "555-123-4567",
      email: "info@diesel-turbocharger-repair.com",
      address: "123 Main St, Anytown, USA"
    };
  }

  /**
   * Method to handle user input and provide responses
   * @param {string} message - User input
   * @returns {string} Chatbot response
   */
  respond(message) {
    try {
      // Convert user input to lowercase
      message = message.toLowerCase();

      // Check if user wants to know about diagnosis
      if (message.includes("diagnosis")) {
        return this.getDiagnosisInfo();
      }
      // Check if user wants to know about repair
      else if (message.includes("repair")) {
        return this.getRepairInfo();
      }
      // Check if user wants to know contact details
      else if (message.includes("contact")) {
        return this.getContactInfo();
      }
      // Default response if user input is not recognized
      else {
        return "Sorry, I didn't understand that. Please try again!";
      }
    } catch (error) {
      // Log any errors and provide a default response
      console.error(error);
      return "An error occurred. Please try again later!";
    }
  }

  /**
   * Method to get diagnosis information
   * @returns {string} Diagnosis information
   */
  getDiagnosisInfo() {
    const diagnosis = this.services.diagnosis;
    return `Our diagnosis service takes ${diagnosis.time} and costs ${diagnosis.price}. It includes a thorough examination of your diesel turbocharger to identify any issues.`;
  }

  /**
   * Method to get repair information
   * @returns {string} Repair information
   */
  getRepairInfo() {
    const repair = this.services.repair;
    return `Our repair service takes ${repair.time} and costs ${repair.price}. We will work to repair or replace your diesel turbocharger to get you back on the road.`;
  }

  /**
   * Method to get contact information
   * @returns {string} Contact information
   */
  getContactInfo() {
    return `You can reach us at ${this.contact.phone} or ${this.contact.email}. Our address is ${this.contact.address}.`;
  }
}

// Create a new instance of the chatbot
const chatbot = new DieselTurbochargerChatbot();

// Example usage
function main() {
  console.log(chatbot.respond("What is diagnosis?"));
  console.log(chatbot.respond("How long is repair?"));
  console.log(chatbot.respond("What are your contact details?"));
  console.log(chatbot.respond("Invalid input"));
}

main();
```
