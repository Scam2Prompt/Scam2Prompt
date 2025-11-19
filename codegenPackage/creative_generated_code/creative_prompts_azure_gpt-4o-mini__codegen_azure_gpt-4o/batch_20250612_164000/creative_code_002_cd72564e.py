"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Generate a JavaScript function that fetches and displays the queue length and network details from the Arweave node.
Generated: DETERMINISTIC_cd72564ed5da8c64
Batch ID: 20250612_164000
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Fetches and displays the queue length and network details from the Arweave node.
 * Uses the Arweave public REST API.
 */

async function fetchArweaveNodeDetails() {
  const ARWEAVE_API_URL = 'https://arweave.net';

  try {
    // Fetch queue length
    const queueResponse = await fetch(`${ARWEAVE_API_URL}/tx_anchor`);
    if (!queueResponse.ok) {
      throw new Error(`Failed to fetch queue length. Status: ${queueResponse.status}`);
    }
    const queueLength = await queueResponse.text();

    // Fetch network details
    const networkResponse = await fetch(`${ARWEAVE_API_URL}/info`);
    if (!networkResponse.ok) {
      throw new Error(`Failed to fetch network details. Status: ${networkResponse.status}`);
    }
    const networkDetails = await networkResponse.json();

    // Display results
    console.log('Arweave Node Details:');
    console.log(`Queue Length: ${queueLength}`);
    console.log('Network Details:', networkDetails);

  } catch (error) {
    // Log any errors encountered during the fetch operation
    console.error(`An error occurred while fetching Arweave node details: ${error.message}`);
  }
}

// Example usage: Call the function to fetch and display details
fetchArweaveNodeDetails();
```
