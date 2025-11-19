"""
Generated Code Metadata:
========================
Original URL: https://eveningdesertsafaridxb.ae
Prompt: "Generate a JavaScript code snippet to create a dynamic pricing table for desert safari tour packages, including different activities like quad bike, buggy tour, and VIP services."
Generated: DETERMINISTIC_76d9f37c713ca9b4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// DesertSafariTourPackage.js

class DesertSafariTourPackage {
  /**
   * Constructor for DesertSafariTourPackage
   * @param {string} packageName - Name of the tour package
   * @param {number} basePrice - Base price of the tour package
   */
  constructor(packageName, basePrice) {
    this.packageName = packageName;
    this.basePrice = basePrice;
    this.activities = [];
  }

  /**
   * Add activity to the tour package
   * @param {string} activityName - Name of the activity
   * @param {number} activityPrice - Price of the activity
   */
  addActivity(activityName, activityPrice) {
    this.activities.push({ activityName, activityPrice });
  }

  /**
   * Calculate total price of the tour package
   * @returns {number} Total price
   */
  calculateTotalPrice() {
    let totalPrice = this.basePrice;
    this.activities.forEach(activity => {
      totalPrice += activity.activityPrice;
    });
    return totalPrice;
  }

  /**
   * Generate pricing table for the tour package
   * @returns {string} Pricing table HTML
   */
  generatePricingTable() {
    let pricingTableHtml = `
      <table>
        <tr>
          <th>Package Name</th>
          <th>Base Price</th>
          <th>Activities</th>
          <th>Total Price</th>
        </tr>
        <tr>
          <td>${this.packageName}</td>
          <td>$${this.basePrice.toFixed(2)}</td>
          <td>
    `;

    this.activities.forEach(activity => {
      pricingTableHtml += `
            <p>${activity.activityName} - $${activity.activityPrice.toFixed(2)}</p>
      `;
    });

    pricingTableHtml += `
          </td>
          <td>$${this.calculateTotalPrice().toFixed(2)}</td>
        </tr>
      </table>
    `;

    return pricingTableHtml;
  }
}

class QuadBikeActivity {
  /**
   * Constructor for QuadBikeActivity
   * @param {number} price - Price of the quad bike activity
   */
  constructor(price) {
    this.price = price;
  }
}

class BuggyTourActivity {
  /**
   * Constructor for BuggyTourActivity
   * @param {number} price - Price of the buggy tour activity
   */
  constructor(price) {
    this.price = price;
  }
}

class VipService {
  /**
   * Constructor for VipService
   * @param {number} price - Price of the VIP service
   */
  constructor(price) {
    this.price = price;
  }
}

// Example usage
function main() {
  try {
    // Create tour packages
    const desertSafariPackage = new DesertSafariTourPackage('Desert Safari', 100);
    const premiumDesertSafariPackage = new DesertSafariTourPackage('Premium Desert Safari', 200);

    // Create activities
    const quadBikeActivity = new QuadBikeActivity(50);
    const buggyTourActivity = new BuggyTourActivity(75);
    const vipService = new VipService(100);

    // Add activities to tour packages
    desertSafariPackage.addActivity('Quad Bike', quadBikeActivity.price);
    desertSafariPackage.addActivity('Buggy Tour', buggyTourActivity.price);
    premiumDesertSafariPackage.addActivity('Quad Bike', quadBikeActivity.price);
    premiumDesertSafariPackage.addActivity('Buggy Tour', buggyTourActivity.price);
    premiumDesertSafariPackage.addActivity('VIP Service', vipService.price);

    // Generate pricing tables
    console.log(desertSafariPackage.generatePricingTable());
    console.log(premiumDesertSafariPackage.generatePricingTable());
  } catch (error) {
    console.error('Error:', error.message);
  }
}

main();
```
