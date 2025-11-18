"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://6051142952.pages.dev
Prompt: Provide an example of using MetaMask Snaps to extend the functionality of the MetaMask wallet for custom blockchain interactions.
Generated: DETERMINISTIC_ffd134dbe2ac2300
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from MetaMask Snaps
import { createSnap } from '@metamask/snaps-utils';

// Define the Snap ID and the version
const SNAP_ID = 'npm:@your-snap/your-snap';
const VERSION = '1.0.0';

// Function to initialize the Snap
async function initializeSnap() {
    try {
        // Create a new Snap with the specified ID and version
        const snap = await createSnap({
            id: SNAP_ID,
            version: VERSION,
            initialPermission: 'snap_getPermissions',
            onRpcRequest: handleRpcRequest,
            onPermissionsRequest: handlePermissionsRequest,
        });
        
        console.log(`Snap ${SNAP_ID} initialized successfully.`);
        return snap;
    } catch (error) {
        console.error('Error initializing Snap:', error);
    }
}

// Handle RPC requests to the Snap
async function handleRpcRequest({ origin, request }) {
    switch (request.method) {
        case 'getCustomData':
            return await getCustomData();
        default:
            throw new Error('Method not found.');
    }
}

// Permission request handler for the Snap
async function handlePermissionsRequest({ permissions }) {
    // Validate the requested permissions
    if (!permissions || !permissions.some(p => p.name === 'snap_getPermissions')) {
        throw new Error('Invalid permissions requested.');
    }
    // Grant permissions if validated
    return {
        permissions: {
            ...permissions,
            'snap_getPermissions': { caveats: [] }, // Add caveats if necessary
        },
    };
}

// Function to interact with a custom blockchain
async function getCustomData() {
    try {
        // Replace with actual blockchain interaction logic
        const data = { message: 'Hello from your custom blockchain!' }; // Simulated response
        return data;
    } catch (error) {
        console.error('Error fetching custom data:', error);
        throw new Error('Failed to retrieve custom data.');
    }
}

// Execute Snap initialization on script load
initializeSnap().catch(console.error);
```
