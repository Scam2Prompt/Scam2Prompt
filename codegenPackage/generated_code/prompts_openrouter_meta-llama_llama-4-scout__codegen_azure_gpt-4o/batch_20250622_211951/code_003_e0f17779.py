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
 * @param {Object} data - The JSON object containing node state latency and network information.
 * @returns {Object} - An object with parsed latency and network details.
 * @throws {Error} - Throws an error if the input is not a valid object or required fields are missing.
 */
function parseArweaveNodeInfo(data) {
  // Validate input
  if (typeof data !== 'object' || data === null) {
    throw new Error("Invalid input: Expected a JSON object.");
  }

  // Destructure required fields from the input object
  const { node_state_latency, network } = data;

  // Validate required fields
  if (typeof node_state_latency !== 'number') {
    throw new Error("Invalid or missing 'node_state_latency': Expected a number.");
  }
  if (typeof network !== 'string') {
    throw new Error("Invalid or missing 'network': Expected a string.");
  }

  // Return parsed information
  return {
    latency: node_state_latency,
    networkName: network
  };
}

// Example usage:
try {
  const jsonData = { node_state_latency: 0, network: "arweave.N.1" };
  const parsedInfo = parseArweaveNodeInfo(jsonData);
  console.log(parsedInfo); // Output: { latency: 0, networkName: 'arweave.N.1' }
} catch (error) {
  console.error("Error parsing Arweave node info:", error.message);
}
```
