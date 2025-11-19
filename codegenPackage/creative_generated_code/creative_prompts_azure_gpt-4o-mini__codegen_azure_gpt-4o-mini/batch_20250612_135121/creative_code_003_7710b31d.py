"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocation-blast.io
Prompt: Provide an example of how to implement MetaMask Snaps to enhance wallet functionality in a decentralized application.
Generated: DETERMINISTIC_7710b31dfe1ffd50
Batch ID: 20250612_135121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and functions
import { SnapsGlobal, OnRpcRequestHandler } from '@metamask/snaps-utils';

// Define the Snap's onRpcRequest handler
const onRpcRequest: OnRpcRequestHandler = async ({ origin, request }) => {
    switch (request.method) {
        case 'getCustomData':
            return getCustomData(origin);
        case 'setCustomData':
            return setCustomData(origin, request.data);
        default:
            throw new Error('Method not found.');
    }
};

// Function to retrieve custom data for a specific origin
async function getCustomData(origin: string): Promise<any> {
    try {
        // Retrieve data from a storage (e.g., user preferences)
        const data = await SnapsGlobal.storage.get(`customData_${origin}`);
        return data || null; // Return null if no data exists
    } catch (error) {
        console.error('Error retrieving custom data:', error);
        throw new Error('Failed to retrieve custom data.');
    }
}

// Function to set custom data for a specific origin
async function setCustomData(origin: string, data: any): Promise<void> {
    try {
        // Validate input data (e.g., check for null or undefined)
        if (data === null || data === undefined) {
            throw new Error('Invalid data provided.');
        }

        // Store the data using Snap's storage
        await SnapsGlobal.storage.set(`customData_${origin}`, data);
    } catch (error) {
        console.error('Error setting custom data:', error);
        throw new Error('Failed to set custom data.');
    }
}

// Export the onRpcRequest handler for the Snap
export { onRpcRequest };
```

This code provides a simple implementation of MetaMask Snaps, allowing users to store and retrieve custom data related to their wallet. It includes error handling and data validation to ensure robustness in a production environment.
