"""
Generated Code Metadata:
========================
Original URL: https://web3inbox.com
Prompt: How does Web3Inbox ensure that users can opt-in to notifications and avoid spam?
Generated: DETERMINISTIC_e28337832352b3cc
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Web3InboxNotificationManager.js

/**
 * Web3Inbox Notification Manager
 * Handles user opt-in, subscription management, and spam prevention
 */
class Web3InboxNotificationManager {
  constructor(web3Provider, notificationService) {
    this.web3Provider = web3Provider;
    this.notificationService = notificationService;
    this.userPreferences = new Map();
    this.subscriptionRegistry = new Map();
    this.spamFilters = new SpamFilter();
  }

  /**
   * Request user permission to enable notifications
   * @param {string} userAddress - User's wallet address
   * @returns {Promise<boolean>} - Whether permission was granted
   */
  async requestNotificationPermission(userAddress) {
    try {
      if (!this.web3Provider) {
        throw new Error('Web3 provider not initialized');
      }

      // Check if already granted
      if (this.userPreferences.has(userAddress)) {
        return this.userPreferences.get(userAddress).enabled;
      }

      // Request signature for permission
      const message = 'I authorize Web3Inbox to send me notifications';
      const signature = await this.web3Provider.request({
        method: 'personal_sign',
        params: [message, userAddress]
      });

      if (!signature) {
        return false;
      }

      // Store user preference
      this.userPreferences.set(userAddress, {
        enabled: true,
        signature,
        timestamp: Date.now()
      });

      return true;
    } catch (error) {
      console.error('Permission request failed:', error);
      return false;
    }
  }

  /**
   * Subscribe to notifications from a specific dApp
   * @param {string} userAddress - User's wallet address
   * @param {string} dAppId - Decentralized application identifier
   * @returns {Promise<boolean>} - Whether subscription was successful
   */
  async subscribeToDapp(userAddress, dAppId) {
    try {
      // Verify user has granted permission
      if (!this.userPreferences.get(userAddress)?.enabled) {
        throw new Error('User has not granted notification permissions');
      }

      // Check spam filter
      if (this.spamFilters.isDappBlacklisted(dAppId)) {
        throw new Error('DApp is blacklisted due to spam reports');
      }

      // Register subscription
      const subscriptions = this.subscriptionRegistry.get(userAddress) || new Set();
      subscriptions.add(dAppId);
      this.subscriptionRegistry.set(userAddress, subscriptions);

      // Notify service
      await this.notificationService.registerSubscription(userAddress, dAppId);

      return true;
    } catch (error) {
      console.error('Subscription failed:', error);
      return false;
    }
  }

  /**
   * Unsubscribe from notifications from a specific dApp
   * @param {string} userAddress - User's wallet address
   * @param {string} dAppId - Decentralized application identifier
   * @returns {Promise<boolean>} - Whether unsubscription was successful
   */
  async unsubscribeFromDapp(userAddress, dAppId) {
    try {
      const subscriptions = this.subscriptionRegistry.get(userAddress);
      if (subscriptions && subscriptions.has(dAppId)) {
        subscriptions.delete(dAppId);
        await this.notificationService.unregisterSubscription(userAddress, dAppId);
      }
      return true;
    } catch (error) {
      console.error('Unsubscription failed:', error);
      return false;
    }
  }

  /**
   * Report a dApp for sending spam notifications
   * @param {string} userAddress - Reporting user's address
   * @param {string} dAppId - Reported dApp identifier
   * @param {string} reason - Reason for reporting
   * @returns {Promise<boolean>} - Whether report was successful
   */
  async reportSpam(userAddress, dAppId, reason) {
    try {
      // Verify user is subscribed to prevent fake reports
      if (!this.subscriptionRegistry.get(userAddress)?.has(dAppId)) {
        throw new Error('Cannot report unsubscribed dApp');
      }

      // Process spam report
      const reportSuccess = await this.spamFilters.processReport(
        userAddress,
        dAppId,
        reason
      );

      // Auto-unsubscribe if report is valid
      if (reportSuccess) {
        await this.unsubscribeFromDapp(userAddress, dAppId);
      }

      return reportSuccess;
    } catch (error) {
      console.error('Spam report failed:', error);
      return false;
    }
  }

  /**
   * Get user's notification preferences
   * @param {string} userAddress - User's wallet address
   * @returns {Object|null} - User preferences or null if not found
   */
  getUserPreferences(userAddress) {
    return this.userPreferences.get(userAddress) || null;
  }

  /**
   * Get user's active subscriptions
   * @param {string} userAddress - User's wallet address
   * @returns {Array<string>} - List of subscribed dApp IDs
   */
  getUserSubscriptions(userAddress) {
    const subscriptions = this.subscriptionRegistry.get(userAddress);
    return subscriptions ? Array.from(subscriptions) : [];
  }
}

/**
 * Spam Filter Service
 * Handles spam detection and prevention
 */
class SpamFilter {
  constructor() {
    this.blacklistedDapps = new Set();
    this.reportThreshold = 5; // Minimum reports to blacklist
    this.dappReports = new Map(); // dAppId -> {count: number, reporters: Set}
  }

  /**
   * Check if dApp is blacklisted
   * @param {string} dAppId - DApp identifier
   * @returns {boolean} - Whether dApp is blacklisted
   */
  isDappBlacklisted(dAppId) {
    return this.blacklistedDapps.has(dAppId);
  }

  /**
   * Process spam report
   * @param {string} reporterAddress - Reporting user's address
   * @param {string} dAppId - Reported dApp identifier
   * @param {string} reason - Reason for reporting
   * @returns {boolean} - Whether dApp was blacklisted
   */
  processReport(reporterAddress, dAppId, reason) {
    // Initialize report tracking if needed
    if (!this.dappReports.has(dAppId)) {
      this.dappReports.set(dAppId, {
        count: 0,
        reporters: new Set()
      });
    }

    const report = this.dappReports.get(dAppId);

    // Prevent duplicate reports from same user
    if (report.reporters.has(reporterAddress)) {
      return false;
    }

    // Update report counts
    report.count++;
    report.reporters.add(reporterAddress);

    // Blacklist if threshold reached
    if (report.count >= this.reportThreshold) {
      this.blacklistedDapps.add(dAppId);
      return true;
    }

    return false;
  }

  /**
   * Get spam report count for a dApp
   * @param {string} dAppId - DApp identifier
   * @returns {number} - Number of reports
   */
  getReportCount(dAppId) {
    return this.dappReports.get(dAppId)?.count || 0;
  }
}

// Example usage:
// const notificationManager = new Web3InboxNotificationManager(web3Provider, notificationService);
// await notificationManager.requestNotificationPermission(userAddress);
// await notificationManager.subscribeToDapp(userAddress, dAppId);
```
