"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: "Write a JavaScript code snippet to display berthing updates and cargo handling information on a website, similar to ENL Consortium's port operation management system."
Generated: DETERMINISTIC_f6e4d34d0d9c3905
Batch ID: 20250622_204704
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Berthing Updates and Cargo Handling Information Display

class BerthingUpdate {
  /**
   * Constructor for BerthingUpdate
   * @param {string} vesselName - Name of the vessel
   * @param {string} berthNumber - Berth number where the vessel is docked
   * @param {string} arrivalTime - Time of arrival
   * @param {string} departureTime - Time of departure
   */
  constructor(vesselName, berthNumber, arrivalTime, departureTime) {
    this.vesselName = vesselName;
    this.berthNumber = berthNumber;
    this.arrivalTime = arrivalTime;
    this.departureTime = departureTime;
  }
}

class CargoHandlingInfo {
  /**
   * Constructor for CargoHandlingInfo
   * @param {string} cargoType - Type of cargo
   * @param {number} quantity - Quantity of cargo
   * @param {string} handlingStatus - Status of cargo handling
   */
  constructor(cargoType, quantity, handlingStatus) {
    this.cargoType = cargoType;
    this.quantity = quantity;
    this.handlingStatus = handlingStatus;
  }
}

class PortOperationSystem {
  /**
   * Constructor for PortOperationSystem
   */
  constructor() {
    this.berthingUpdates = [];
    this.cargoHandlingInfos = [];
  }

  /**
   * Add berthing update
   * @param {BerthingUpdate} berthingUpdate - Berthing update to add
   */
  addBerthingUpdate(berthingUpdate) {
    if (berthingUpdate instanceof BerthingUpdate) {
      this.berthingUpdates.push(berthingUpdate);
    } else {
      throw new Error('Invalid berthing update');
    }
  }

  /**
   * Add cargo handling information
   * @param {CargoHandlingInfo} cargoHandlingInfo - Cargo handling information to add
   */
  addCargoHandlingInfo(cargoHandlingInfo) {
    if (cargoHandlingInfo instanceof CargoHandlingInfo) {
      this.cargoHandlingInfos.push(cargoHandlingInfo);
    } else {
      throw new Error('Invalid cargo handling information');
    }
  }

  /**
   * Display berthing updates
   */
  displayBerthingUpdates() {
    const berthingUpdatesHtml = this.berthingUpdates.map((update, index) => {
      return `
        <div key=${index}>
          <h2>Vessel: ${update.vesselName}</h2>
          <p>Berth Number: ${update.berthNumber}</p>
          <p>Arrival Time: ${update.arrivalTime}</p>
          <p>Departure Time: ${update.departureTime}</p>
        </div>
      `;
    }).join('');
    document.getElementById('berthing-updates').innerHTML = berthingUpdatesHtml;
  }

  /**
   * Display cargo handling information
   */
  displayCargoHandlingInfos() {
    const cargoHandlingInfosHtml = this.cargoHandlingInfos.map((info, index) => {
      return `
        <div key=${index}>
          <h2>Cargo Type: ${info.cargoType}</h2>
          <p>Quantity: ${info.quantity}</p>
          <p>Handling Status: ${info.handlingStatus}</p>
        </div>
      `;
    }).join('');
    document.getElementById('cargo-handling-infos').innerHTML = cargoHandlingInfosHtml;
  }
}

// Example usage
try {
  const portOperationSystem = new PortOperationSystem();

  const berthingUpdate1 = new BerthingUpdate('Vessel 1', 'Berth 1', '2022-01-01 10:00:00', '2022-01-01 12:00:00');
  const berthingUpdate2 = new BerthingUpdate('Vessel 2', 'Berth 2', '2022-01-02 10:00:00', '2022-01-02 12:00:00');

  portOperationSystem.addBerthingUpdate(berthingUpdate1);
  portOperationSystem.addBerthingUpdate(berthingUpdate2);

  const cargoHandlingInfo1 = new CargoHandlingInfo('Container', 100, 'Loaded');
  const cargoHandlingInfo2 = new CargoHandlingInfo('Bulk Cargo', 500, 'Unloaded');

  portOperationSystem.addCargoHandlingInfo(cargoHandlingInfo1);
  portOperationSystem.addCargoHandlingInfo(cargoHandlingInfo2);

  portOperationSystem.displayBerthingUpdates();
  portOperationSystem.displayCargoHandlingInfos();
} catch (error) {
  console.error(error);
  document.getElementById('error-message').innerHTML = error.message;
}
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Port Operation Management System</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Berthing Updates</h1>
  <div id="berthing-updates"></div>

  <h1>Cargo Handling Information</h1>
  <div id="cargo-handling-infos"></div>

  <h1>Error Message</h1>
  <div id="error-message"></div>

  <script src="script.js"></script>
</body>
</html>
```
