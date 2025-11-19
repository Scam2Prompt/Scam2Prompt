"""
Generated Code Metadata:
========================
Original URL: https://arweave.ar
Prompt: How can I use the Arweave API to apply the ans104IndexFilter with the "never" parameter set to true in my application?
Generated: DETERMINISTIC_cf8fcb50f495b629
Batch ID: 20250612_160404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
const Arweave = require('arweave');

// Initialize Arweave
const arweave = Arweave.init({
  host: 'arweave.net',
  port: 443,
  protocol: 'https'
});

// Function to apply ans104IndexFilter with "never" parameter
async function applyAns104IndexFilter() {
  try {
    // Create a GraphQL query with ans104IndexFilter set to "never"
    const query = `
      query {
        transactions(
          first: 10,
          sort: HEIGHT_DESC,
          tags: [
            { name: "App-Name", values: ["SmartWeaveContract"] }
          ],
          ans104IndexFilter: {
            never: true
          }
        ) {
          edges {
            node {
              id
              tags {
                name
                value
              }
            }
          }
        }
      }
    `;

    // Execute the GraphQL query
    const response = await arweave.api.post('graphql', { query });
    
    if (response.status !== 200) {
      throw new Error(`GraphQL query failed with status ${response.status}`);
    }

    // Return the filtered transactions
    return response.data.data.transactions.edges;
  } catch (error) {
    console.error('Error applying ans104IndexFilter:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    const filteredTransactions = await applyAns104IndexFilter();
    console.log('Filtered transactions:', filteredTransactions);
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```
