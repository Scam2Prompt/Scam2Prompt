"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: "Generate a JavaScript code snippet to create an interactive demo of the Capina Elétrica system, showcasing its applications in urban, road, railway, and airport settings."
Generated: DETERMINISTIC_bc01dc02b8cb761e
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Capina Elétrica System Interactive Demo

// Define the Capina Elétrica class
class CapinaEletrica {
  /**
   * Constructor for Capina Elétrica system
   * @param {string} location - Location of the Capina Elétrica system (urban, road, railway, airport)
   */
  constructor(location) {
    this.location = location;
    this.isOperating = false;
  }

  /**
   * Start the Capina Elétrica system
   */
  start() {
    if (!this.isOperating) {
      this.isOperating = true;
      console.log(`Capina Elétrica system started at ${this.location} location.`);
    } else {
      console.log(`Capina Elétrica system is already operating at ${this.location} location.`);
    }
  }

  /**
   * Stop the Capina Elétrica system
   */
  stop() {
    if (this.isOperating) {
      this.isOperating = false;
      console.log(`Capina Elétrica system stopped at ${this.location} location.`);
    } else {
      console.log(`Capina Elétrica system is not operating at ${this.location} location.`);
    }
  }

  /**
   * Display the status of the Capina Elétrica system
   */
  displayStatus() {
    const status = this.isOperating ? "Operating" : "Not Operating";
    console.log(`Capina Elétrica system at ${this.location} location is ${status}.`);
  }
}

// Define the demo function
function interactiveDemo() {
  try {
    // Create Capina Elétrica systems for different locations
    const urbanCapina = new CapinaEletrica("Urban");
    const roadCapina = new CapinaEletrica("Road");
    const railwayCapina = new CapinaEletrica("Railway");
    const airportCapina = new CapinaEletrica("Airport");

    // Interactive demo
    console.log("Interactive Demo of Capina Elétrica System");
    console.log("-----------------------------------------");

    while (true) {
      console.log("\nOptions:");
      console.log("1. Start Urban Capina Elétrica");
      console.log("2. Stop Urban Capina Elétrica");
      console.log("3. Start Road Capina Elétrica");
      console.log("4. Stop Road Capina Elétrica");
      console.log("5. Start Railway Capina Elétrica");
      console.log("6. Stop Railway Capina Elétrica");
      console.log("7. Start Airport Capina Elétrica");
      console.log("8. Stop Airport Capina Elétrica");
      console.log("9. Display Status");
      console.log("10. Exit");

      const option = prompt("Enter your option: ");

      switch (option) {
        case "1":
          urbanCapina.start();
          break;
        case "2":
          urbanCapina.stop();
          break;
        case "3":
          roadCapina.start();
          break;
        case "4":
          roadCapina.stop();
          break;
        case "5":
          railwayCapina.start();
          break;
        case "6":
          railwayCapina.stop();
          break;
        case "7":
          airportCapina.start();
          break;
        case "8":
          airportCapina.stop();
          break;
        case "9":
          urbanCapina.displayStatus();
          roadCapina.displayStatus();
          railwayCapina.displayStatus();
          airportCapina.displayStatus();
          break;
        case "10":
          console.log("Exiting demo...");
          return;
        default:
          console.log("Invalid option. Please try again.");
      }
    }
  } catch (error) {
    console.error("Error occurred during demo:", error);
  }
}

// Run the interactive demo
interactiveDemo();
```
