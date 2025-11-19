"""
Generated Code Metadata:
========================
Original URL: https://myflowfoundationke.org
Prompt: Generate a JavaScript function that helps track the distribution of sanitary pads and dignity care packages, similar to the impact metrics of My Flow Foundation.
Generated: DETERMINISTIC_1faf6793c9b02395
Batch ID: 20250612_160413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Tracks the distribution of sanitary pads and dignity care packages.
 */
class DistributionTracker {
  /**
   * Initializes a new DistributionTracker instance.
   */
  constructor() {
    // Initialize an object to store distribution data
    this.distributionData = {
      sanitaryPads: 0,
      dignityCarePackages: 0,
      recipients: []
    };
  }

  /**
   * Adds sanitary pads to the distribution data.
   * @param {number} quantity - The number of sanitary pads to add.
   * @throws {Error} If the quantity is not a positive integer.
   */
  addSanitaryPads(quantity) {
    if (!Number.isInteger(quantity) || quantity <= 0) {
      throw new Error('Quantity must be a positive integer.');
    }
    this.distributionData.sanitaryPads += quantity;
  }

  /**
   * Adds dignity care packages to the distribution data.
   * @param {number} quantity - The number of dignity care packages to add.
   * @throws {Error} If the quantity is not a positive integer.
   */
  addDignityCarePackages(quantity) {
    if (!Number.isInteger(quantity) || quantity <= 0) {
      throw new Error('Quantity must be a positive integer.');
    }
    this.distributionData.dignityCarePackages += quantity;
  }

  /**
   * Adds a recipient to the distribution data.
   * @param {string} name - The name of the recipient.
   * @param {number} sanitaryPadsReceived - The number of sanitary pads received.
   * @param {number} dignityCarePackagesReceived - The number of dignity care packages received.
   * @throws {Error} If the name is empty or if the quantities are not positive integers.
   */
  addRecipient(name, sanitaryPadsReceived, dignityCarePackagesReceived) {
    if (typeof name !== 'string' || name.trim() === '') {
      throw new Error('Name must be a non-empty string.');
    }
    if (!Number.isInteger(sanitaryPadsReceived) || sanitaryPadsReceived < 0) {
      throw new Error('Sanitary pads received must be a non-negative integer.');
    }
    if (!Number.isInteger(dignityCarePackagesReceived) || dignityCarePackagesReceived < 0) {
      throw new Error('Dignity care packages received must be a non-negative integer.');
    }
    this.distributionData.recipients.push({
      name,
      sanitaryPadsReceived,
      dignityCarePackagesReceived
    });
  }

  /**
   * Gets the total distribution data.
   * @returns {Object} The total distribution data.
   */
  getDistributionData() {
    return { ...this.distributionData };
  }

  /**
   * Gets the impact metrics.
   * @returns {Object} The impact metrics.
   */
  getImpactMetrics() {
    const totalSanitaryPadsDistributed = this.distributionData.recipients.reduce((acc, recipient) => acc + recipient.sanitaryPadsReceived, 0);
    const totalDignityCarePackagesDistributed = this.distributionData.recipients.reduce((acc, recipient) => acc + recipient.dignityCarePackagesReceived, 0);
    const totalRecipients = this.distributionData.recipients.length;
    return {
      totalSanitaryPadsDistributed,
      totalDignityCarePackagesDistributed,
      totalRecipients
    };
  }
}

// Example usage:
function main() {
  const tracker = new DistributionTracker();

  // Add sanitary pads and dignity care packages
  tracker.addSanitaryPads(100);
  tracker.addDignityCarePackages(50);

  // Add recipients
  tracker.addRecipient('John Doe', 5, 2);
  tracker.addRecipient('Jane Doe', 3, 1);

  // Get distribution data
  const distributionData = tracker.getDistributionData();
  console.log('Distribution Data:');
  console.log(distributionData);

  // Get impact metrics
  const impactMetrics = tracker.getImpactMetrics();
  console.log('Impact Metrics:');
  console.log(impactMetrics);
}

main();
```
