"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iensooa.pages.dev
Prompt: Explain how to set notification preferences in the Web3Inbox app to receive only transactional messages.
Generated: DETERMINISTIC_fe3d5ab33bdc9a7c
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary Web3Inbox library or modules
import { Web3Inbox } from 'web3inbox-sdk';

// Function to set notification preferences for receiving only transactional messages
async function setNotificationPreferences(userId) {
  try {
    // Initialize Web3Inbox instance (ensure proper configuration is done elsewhere in the app)
    const web3Inbox = new Web3Inbox();

    // Fetch current user preferences
    const currentPreferences = await web3Inbox.getNotificationPreferences(userId);

    // Update preferences to allow only transactional messages
    const updatedPreferences = {
      ...currentPreferences, // Retain existing preferences
      preferences: {
        transactional: true, // Enable transactional notifications
        promotional: false,  // Disable promotional notifications
        social: false,       // Disable social notifications
      },
    };

    // Save updated preferences
    await web3Inbox.setNotificationPreferences(userId, updatedPreferences);

    console.log('Notification preferences updated successfully.');
  } catch (error) {
    // Handle errors gracefully
    console.error('Failed to update notification preferences:', error.message);
  }
}

// Example usage
const userId = 'user-123'; // Replace with the actual user ID
setNotificationPreferences(userId);
```
