"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iensooa.pages.dev
Prompt: Create a function to update notification preferences for a subscribed app in Web3Inbox, allowing users to refine the types of messages they receive.
Generated: DETERMINISTIC_8b43afd45d626c0e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to update notification preferences for a subscribed app in Web3Inbox.
 * This allows users to refine the types of messages they wish to receive.
 *
 * @param {string} userId - The unique identifier for the user.
 * @param {string} appId - The unique identifier for the subscribed app.
 * @param {Object} preferences - The updated notification preferences.
 * @param {boolean} preferences.directMessages - Whether to allow direct messages.
 * @param {boolean} preferences.groupMessages - Whether to allow group messages.
 * @param {boolean} preferences.promotionalMessages - Whether to allow promotional messages.
 * @returns {Promise<string>} - A message indicating the success or failure of the update.
 * @throws {Error} - Throws an error if the update fails due to validation or database issues.
 */
async function updateNotificationPreferences(userId, appId, preferences) {
  // Input validation
  if (!userId || typeof userId !== 'string') {
    throw new Error("Invalid userId. It must be a non-empty string.");
  }
  if (!appId || typeof appId !== 'string') {
    throw new Error("Invalid appId. It must be a non-empty string.");
  }
  if (
    !preferences ||
    typeof preferences !== 'object' ||
    preferences.directMessages === undefined ||
    preferences.groupMessages === undefined ||
    preferences.promotionalMessages === undefined
  ) {
    throw new Error(
      "Invalid preferences object. It must contain 'directMessages', 'groupMessages', and 'promotionalMessages' properties."
    );
  }

  try {
    // Simulate database update operation
    const updatedPreferences = {
      userId,
      appId,
      preferences,
      updatedAt: new Date().toISOString(), // Store the timestamp of the update
    };

    // Mock database update (replace with a real database call, e.g., MongoDB, PostgreSQL, etc.)
    const mockDatabase = {}; // Simulated database object
    mockDatabase[userId] = mockDatabase[userId] || {};
    mockDatabase[userId][appId] = updatedPreferences;

    // Return success message
    return `Notification preferences for user ${userId} on app ${appId} have been successfully updated.`;
  } catch (error) {
    // Log the error and rethrow it
    console.error("Failed to update notification preferences:", error);
    throw new Error("An error occurred while updating notification preferences.");
  }
}

// Example usage:
// updateNotificationPreferences("user123", "app456", { directMessages: true, groupMessages: false, promotionalMessages: true })
//   .then(console.log)
//   .catch(console.error);
```
