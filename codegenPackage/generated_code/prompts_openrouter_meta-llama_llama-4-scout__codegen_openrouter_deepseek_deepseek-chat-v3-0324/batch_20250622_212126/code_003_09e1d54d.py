"""
Generated Code Metadata:
========================
Original URL: https://s0s2.pages.dev
Prompt: Based on the information provided on this webpage, craft a prompt that guides a large language model to write a code snippet in JavaScript that interacts with its backend services to update user preferences.
Generated: DETERMINISTIC_09e1d54d2c4041e3
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Updates user preferences by making an authenticated API call to the backend.
 * 
 * @param {Object} preferences - The user preferences to update (e.g., { theme: 'dark', notifications: true })
 * @param {string} authToken - The user's authentication token
 * @returns {Promise<Object>} - The updated preferences from the server
 * @throws {Error} - If the request fails or returns an error status
 */
async function updateUserPreferences(preferences, authToken) {
    try {
        const response = await fetch('/api/user/preferences', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${authToken}`
            },
            body: JSON.stringify(preferences)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.message || 'Failed to update preferences');
        }

        return await response.json();
    } catch (error) {
        console.error('Error updating user preferences:', error);
        throw error; // Re-throw to allow caller to handle
    }
}

// Example usage:
// try {
//     const updatedPrefs = await updateUserPreferences(
//         { theme: 'dark', notifications: false },
//         'user-auth-token-123'
//     );
//     console.log('Preferences updated:', updatedPrefs);
// } catch (error) {
//     console.error('Failed to update preferences:', error.message);
// }
```
