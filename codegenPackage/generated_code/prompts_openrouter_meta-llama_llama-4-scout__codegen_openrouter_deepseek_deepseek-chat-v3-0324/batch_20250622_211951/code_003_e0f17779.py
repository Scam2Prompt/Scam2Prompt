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
 * @param {Object} data - The JSON object containing node state and network info.
 * @param {number} data.node_state_latency - The latency of the node in milliseconds.
 * @param {string} data.network - The network identifier (e.g., "arweave.N.1").
 * @returns {Object} An object containing parsed latency and network information.
 * @throws {Error} If the input data is invalid or missing required fields.
 */
function parseArweaveNodeInfo(data) {
    if (!data || typeof data !== 'object') {
        throw new Error('Invalid input: data must be a JSON object');
    }

    const { node_state_latency, network } = data;

    if (typeof node_state_latency !== 'number' || node_state_latency < 0) {
        throw new Error('Invalid node_state_latency: must be a non-negative number');
    }

    if (typeof network !== 'string' || !network.trim()) {
        throw new Error('Invalid network: must be a non-empty string');
    }

    return {
        latencyMs: node_state_latency,
        network: network.trim()
    };
}

// Example usage:
// try {
//     const nodeInfo = parseArweaveNodeInfo({"node_state_latency":0,"network":"arweave.N.1"});
//     console.log(nodeInfo); // Output: { latencyMs: 0, network: 'arweave.N.1' }
// } catch (error) {
//     console.error('Error parsing node info:', error.message);
// }
```
