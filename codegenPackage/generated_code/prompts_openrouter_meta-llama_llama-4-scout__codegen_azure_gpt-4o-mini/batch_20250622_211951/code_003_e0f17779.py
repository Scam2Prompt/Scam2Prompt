"""
Generated Code Metadata:
========================
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Write a JavaScript function to parse the Arweave node state latency and network information from a JSON object like `{"node_state_latency":0,"network":"arweave.N.1"}`.
Generated: DETERMINISTIC_e0f1777933496300
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Parses the Arweave node state latency and network information from a JSON object.
 * 
 * @param {Object} jsonData - The JSON object containing node state latency and network information.
 * @returns {Object} - An object containing the parsed latency and network information.
 * @throws {Error} - Throws an error if the input is not a valid JSON object or if required properties are missing.
 */
function parseArweaveNodeState(jsonData) {
    // Validate input
    if (typeof jsonData !== 'object' || jsonData === null) {
        throw new Error('Invalid input: Expected a JSON object.');
    }

    // Destructure the required properties from the JSON object
    const { node_state_latency, network } = jsonData;

    // Validate required properties
    if (typeof node_state_latency !== 'number') {
        throw new Error('Invalid input: node_state_latency must be a number.');
    }
    if (typeof network !== 'string') {
        throw new Error('Invalid input: network must be a string.');
    }

    // Return the parsed information
    return {
        latency: node_state_latency,
        network: network
    };
}

// Example usage
try {
    const jsonData = {"node_state_latency": 0, "network": "arweave.N.1"};
    const parsedData = parseArweaveNodeState(jsonData);
    console.log(parsedData);
} catch (error) {
    console.error('Error parsing Arweave node state:', error.message);
}
```
