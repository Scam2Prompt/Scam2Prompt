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
// Web3Inbox Notification Opt-in and Spam Prevention System

/**
 * Represents a user's notification preferences.
 */
class UserPreferences {
  /**
   * Creates a new UserPreferences instance.
   * @param {string} userId - The ID of the user.
   */
  constructor(userId) {
    this.userId = userId;
    this.optedInNotifications = new Set(); // Set of notification types user has opted into.
    this.blockedSenders = new Set(); // Set of senders user has blocked.
  }

  /**
   * Adds a notification type to the user's opt-in list.
   * @param {string} notificationType - The type of notification to opt into.
   */
  optIn(notificationType) {
    this.optedInNotifications.add(notificationType);
  }

  /**
   * Removes a notification type from the user's opt-in list.
   * @param {string} notificationType - The type of notification to opt out of.
   */
  optOut(notificationType) {
    this.optedInNotifications.delete(notificationType);
  }

  /**
   * Blocks a sender from sending notifications to the user.
   * @param {string} senderId - The ID of the sender to block.
   */
  blockSender(senderId) {
    this.blockedSenders.add(senderId);
  }

  /**
   * Unblocks a sender, allowing them to send notifications to the user again.
   * @param {string} senderId - The ID of the sender to unblock.
   */
  unblockSender(senderId) {
    this.blockedSenders.delete(senderId);
  }

  /**
   * Checks if the user has opted into a specific notification type and is not blocked by the sender.
   * @param {string} notificationType - The type of notification.
   * @param {string} senderId - The ID of the sender.
   * @returns {boolean} True if the user has opted into the notification and the sender is not blocked, false otherwise.
   */
  isAllowedNotification(notificationType, senderId) {
    return this.optedInNotifications.has(notificationType) && !this.blockedSenders.has(senderId);
  }
}

/**
 * Represents the Web3Inbox notification system.
 */
class Web3Inbox {
  /**
   * Creates a new Web3Inbox instance.
   */
  constructor() {
    this.userPreferences = {}; // Map of user IDs to their preferences.
  }

  /**
   * Registers a new user with the Web3Inbox system.
   * @param {string} userId - The ID of the user.
   */
  registerUser(userId) {
    if (!this.userPreferences[userId]) {
      this.userPreferences[userId] = new UserPreferences(userId);
    }
  }

  /**
   * Unregisters a user from the Web3Inbox system.
   * @param {string} userId - The ID of the user.
   */
  unregisterUser(userId) {
    delete this.userPreferences[userId];
  }

  /**
   * Sends a notification to a user if they have opted into it and the sender is not blocked.
   * @param {string} userId - The ID of the user.
   * @param {string} notificationType - The type of notification.
   * @param {string} senderId - The ID of the sender.
   * @param {string} message - The notification message.
   * @returns {boolean} True if the notification was sent, false otherwise.
   */
  sendNotification(userId, notificationType, senderId, message) {
    try {
      if (!this.userPreferences[userId]) {
        throw new Error(`User ${userId} is not registered.`);
      }

      const userPreference = this.userPreferences[userId];
      if (userPreference.isAllowedNotification(notificationType, senderId)) {
        // Simulate sending the notification (replace with actual implementation).
        // eslint-disable-next-line no-console
        console.log(`Sending notification to user ${userId}: ${message}`);
        return true;
      } else {
        // eslint-disable-next-line no-console
        console.log(`Notification blocked for user ${userId} from sender ${senderId}.`);
        return false;
      }
    } catch (error) {
      // eslint-disable-next-line no-console
      console.error(`Error sending notification: ${error.message}`);
      return false;
    }
  }
}

// Example usage:
const web3Inbox = new Web3Inbox();
web3Inbox.registerUser("user123");
web3Inbox.userPreferences["user123"].optIn("new_message");

web3Inbox.sendNotification("user123", "new_message", "sender456", "Hello, world!");
web3Inbox.sendNotification("user123", "new_message", "blocked_sender", "This should be blocked.");

web3Inbox.userPreferences["user123"].blockSender("blocked_sender");
web3Inbox.sendNotification("user123", "new_message", "blocked_sender", "This should still be blocked.");
```
