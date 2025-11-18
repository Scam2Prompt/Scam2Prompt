"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-ultra.org
Prompt: How can I enhance my MetaMask wallet with third-party built features using Snaps? Provide code examples for adding custom functionality.
Generated: DETERMINISTIC_a94366ef95b01b41
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { OnRpcRequestHandler } from '@metamask/snaps-types';

// Define the main handler for the Snap
export const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
    switch (request.method) {
        case 'getCustomData':
            // Call the function to get custom data
            return await getCustomData();
        case 'setCustomData':
            // Validate the request parameters
            if (!request.params || typeof request.params.data !== 'string') {
                throw new Error('Invalid parameters: Expected an object with a "data" string property.');
            }
            // Call the function to set custom data
            return await setCustomData(request.params.data);
        default:
            throw new Error('Method not found.');
    }
};

// Function to retrieve custom data
async function getCustomData() {
    try {
        // Logic to fetch custom data (could be from a database, API, etc.)
        const customData = await fetchCustomData(); // Placeholder for actual data fetching logic
        return customData;
    } catch (error) {
        console.error('Error fetching custom data:', error);
        throw new Error('Failed to retrieve custom data.');
    }
}

// Function to set custom data
async function setCustomData(data) {
    try {
        // Logic to save custom data (could be to a database, API, etc.)
        await saveCustomData(data); // Placeholder for actual data saving logic
        return { success: true, message: 'Custom data saved successfully.' };
    } catch (error) {
        console.error('Error saving custom data:', error);
        throw new Error('Failed to save custom data.');
    }
}

// Placeholder function for fetching custom data
async function fetchCustomData() {
    // Simulate data fetching (replace with actual implementation)
    return { message: 'This is custom data from the Snap!' };
}

// Placeholder function for saving custom data
async function saveCustomData(data) {
    // Simulate data saving (replace with actual implementation)
    console.log('Custom data saved:', data);
}
```

Make sure to replace the placeholder functions `fetchCustomData` and `saveCustomData` with actual implementations that suit your specific use case and data source.
