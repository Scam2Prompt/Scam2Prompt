"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vault-illuvium.com
Prompt: Provide an example of using MetaMask Snaps to extend wallet functionality with a custom third-party feature.
Generated: DETERMINISTIC_13eabf6f8f40b953
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries from MetaMask Snaps
import { OnRpcRequestHandler } from '@metamask/snaps-types';

// Define the main handler for the Snap
export const onRpcRequest: OnRpcRequestHandler = async ({ request }) => {
    switch (request.method) {
        case 'getCustomFeatureData':
            return await getCustomFeatureData(request.params);
        default:
            throw new Error('Method not found.');
    }
};

// Custom feature that retrieves data from a third-party API
async function getCustomFeatureData(params: { apiEndpoint: string }): Promise<any> {
    const { apiEndpoint } = params;

    // Validate input parameters
    if (!apiEndpoint || typeof apiEndpoint !== 'string') {
        throw new Error('Invalid API endpoint provided.');
    }

    try {
        // Fetch data from the specified API endpoint
        const response = await fetch(apiEndpoint);

        // Check if the response is successful
        if (!response.ok) {
            throw new Error(`Error fetching data: ${response.statusText}`);
        }

        // Parse and return the JSON data
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error in getCustomFeatureData:', error);
        throw new Error('Failed to retrieve data from the API.');
    }
}

// MetaMask Snap entry point
export default {
    onRpcRequest,
};
```

In this code, a custom MetaMask Snap is implemented that defines a method to fetch data from a specified third-party API endpoint, ensuring proper validation and error handling.
