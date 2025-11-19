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
 * Parses Arweave node state latency and network information from a JSON object.
 * 
 * @param {Object} data - JSON object containing node state latency and network information.
 * @returns {Object} - Parsed object with node state latency and network information.
 */
function parseArweaveNodeInfo(data) {
    // Check if input data is a valid object
    if (typeof data !== 'object' || Array.isArray(data) || data === null) {
        throw new Error('Invalid input data. Expected a JSON object.');
    }

    // Destructure the input object to get node state latency and network information
    const { node_state_latency, network } = data;

    // Check if node state latency and network information exist in the input data
    if (node_state_latency === undefined || network === undefined) {
        throw new Error('Input data must contain "node_state_latency" and "network" properties.');
    }

    // Check if node state latency is a valid number
    if (typeof node_state_latency !== 'number') {
        throw new Error('Invalid node state latency. Expected a number.');
    }

    // Check if network is a valid string
    if (typeof network !== 'string') {
        throw new Error('Invalid network. Expected a string.');
    }

    // Return the parsed object with node state latency and network information
    return {
        nodeStateLatency: node_state_latency,
        network,
    };
}

// Example usage:
try {
    const data = JSON.parse('{"node_state_latency":0,"network":"arweave.N.1"}');
    const nodeInfo = parseArweaveNodeInfo(data);
    console.log(nodeInfo);
} catch (error) {
    console.error(error.message);
}
```
