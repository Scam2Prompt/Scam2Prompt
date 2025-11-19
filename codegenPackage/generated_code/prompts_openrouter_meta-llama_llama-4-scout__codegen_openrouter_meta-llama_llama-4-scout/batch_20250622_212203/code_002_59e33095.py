"""
Generated Code Metadata:
========================
Original URL: https://gettapeads.com
Prompt: Design a partner program for a video sharing platform that rewards users with a fixed amount per 10,000 downloads or streams, and provide a sample implementation in JavaScript.
Generated: DETERMINISTIC_59e33095a24d63d9
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Partner Program for Video Sharing Platform
 * Rewards users with a fixed amount per 10,000 downloads or streams
 */

// PartnerProgram class
class PartnerProgram {
  /**
   * Constructor
   * @param {number} rewardPer10k - Reward amount per 10,000 downloads/streams
   */
  constructor(rewardPer10k) {
    this.rewardPer10k = rewardPer10k;
    this.partners = {};
  }

  /**
   * Add a partner to the program
   * @param {string} partnerId - Unique partner ID
   * @param {string} partnerName - Partner name
   */
  addPartner(partnerId, partnerName) {
    if (this.partners[partnerId]) {
      throw new Error(`Partner ${partnerId} already exists`);
    }
    this.partners[partnerId] = {
      name: partnerName,
      downloads: 0,
      streams: 0,
      earnings: 0,
    };
  }

  /**
   * Remove a partner from the program
   * @param {string} partnerId - Unique partner ID
   */
  removePartner(partnerId) {
    if (!this.partners[partnerId]) {
      throw new Error(`Partner ${partnerId} does not exist`);
    }
    delete this.partners[partnerId];
  }

  /**
   * Report downloads/streams for a partner
   * @param {string} partnerId - Unique partner ID
   * @param {number} downloads - Number of downloads
   * @param {number} streams - Number of streams
   */
  reportDownloadsStreams(partnerId, downloads, streams) {
    if (!this.partners[partnerId]) {
      throw new Error(`Partner ${partnerId} does not exist`);
    }
    const partner = this.partners[partnerId];
    partner.downloads += downloads;
    partner.streams += streams;
    const totalDownloadsStreams = partner.downloads + partner.streams;
    const reward = Math.floor(totalDownloadsStreams / 10000) * this.rewardPer10k;
    partner.earnings = reward;
  }

  /**
   * Get partner earnings
   * @param {string} partnerId - Unique partner ID
   * @returns {number} Partner earnings
   */
  getPartnerEarnings(partnerId) {
    if (!this.partners[partnerId]) {
      throw new Error(`Partner ${partnerId} does not exist`);
    }
    return this.partners[partnerId].earnings;
  }

  /**
   * Get partner details
   * @param {string} partnerId - Unique partner ID
   * @returns {object} Partner details
   */
  getPartnerDetails(partnerId) {
    if (!this.partners[partnerId]) {
      throw new Error(`Partner ${partnerId} does not exist`);
    }
    return this.partners[partnerId];
  }
}

// Example usage
function main() {
  try {
    const partnerProgram = new PartnerProgram(100); // $100 reward per 10,000 downloads/streams

    // Add partners
    partnerProgram.addPartner('partner1', 'John Doe');
    partnerProgram.addPartner('partner2', 'Jane Doe');

    // Report downloads/streams
    partnerProgram.reportDownloadsStreams('partner1', 5000, 5000);
    partnerProgram.reportDownloadsStreams('partner2', 10000, 0);

    // Get partner earnings
    console.log(`Partner 1 earnings: $${partnerProgram.getPartnerEarnings('partner1')}`);
    console.log(`Partner 2 earnings: $${partnerProgram.getPartnerEarnings('partner2')}`);

    // Get partner details
    console.log('Partner 1 details:', partnerProgram.getPartnerDetails('partner1'));
    console.log('Partner 2 details:', partnerProgram.getPartnerDetails('partner2'));
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
