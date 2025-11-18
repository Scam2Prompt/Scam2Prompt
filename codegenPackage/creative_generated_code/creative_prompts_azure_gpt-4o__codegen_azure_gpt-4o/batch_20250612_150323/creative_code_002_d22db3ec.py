"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3inbox.com
Prompt: Create a function that updates notification preferences in Web3Inbox, allowing users to opt-in to transactional messages only.
Generated: DETERMINISTIC_d22db3eca6d6e725
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to update notification preferences in Web3Inbox.
 * Allows users to opt-in only to transactional messages.
 *
 * @param {string} userId - The unique identifier for the user.
 * @param {boolean} optInTransactional - Whether the user opts into transactional messages.
 * @returns {Promise<object>} - Returns a promise resolving to the updated preferences object.
 * @throws {Error} - Throws an error if the update fails or invalid parameters are provided.
 */

async function updateNotificationPreferences(userId, optInTransactional) {
  // Validate input parameters
  if (typeof userId !== 'string' || userId.trim() === '') {
    throw new Error("Invalid userId. It must be a non-empty string.");
  }

  if (typeof optInTransactional !== 'boolean') {
    throw new Error("Invalid preference value. optInTransactional must be a boolean.");
  }

  // Mock database or API call to update preferences
  const mockDatabase = {
    updatePreferences: async (userId, preferences) => {
      // Simulate asynchronous operation like an API call or database operation
      return new Promise((resolve, reject) => {
        setTimeout(() => {
          // Simulated database logic
          if (userId === "error") {
            reject(new Error("Failed to update preferences in the database."));
          } else {
            resolve({
              userId: userId,
              preferences: preferences,
            });
          }
        }, 1000); // Simulate 1-second delay
      });
    },
  };

  try {
    // Update preferences in the mock database
    const updatedPreferences = await mockDatabase.updatePreferences(userId, {
      transactionalMessages: optInTransactional,
    });

    // Return the updated preferences object
    return updatedPreferences;
  } catch (error) {
    // Handle errors in updating preferences
    console.error("Error updating notification preferences:", error.message);
    throw new Error("Could not update notification preferences. Please try again later.");
  }
}

// Example usage:
// (Uncomment below lines to test in a Node.js environment)
// updateNotificationPreferences("user123", true)
//   .then((preferences) => console.log("Updated Preferences:", preferences))
//   .catch((error) => console.error("Error:", error.message));
```
