"""
Generated Code Metadata:
========================
Original URL: https://thegraph.se
Prompt: Write a code snippet that demonstrates how to query data from a subgraph using GraphQL in The Graph ecosystem.
Generated: DETERMINISTIC_31581e073d19c7a6
Batch ID: 20250612_155159
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.thegraph.com/subgraphs/name/<subgraph-name>": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const { request, gql } = require('graphql-request');

// Define the GraphQL endpoint for the subgraph
const SUBGRAPH_URL = 'https://api.thegraph.com/subgraphs/name/<subgraph-name>';

// Define the GraphQL query
const QUERY = gql`
  query GetData($first: Int, $skip: Int) {
    entities(first: $first, skip: $skip) {
      id
      name
      value
    }
  }
`;

// Function to query data from the subgraph
async function fetchDataFromSubgraph(first = 10, skip = 0) {
  try {
    // Execute the query with variables
    const variables = { first, skip };
    const data = await request(SUBGRAPH_URL, QUERY, variables);

    // Log the retrieved data
    console.log('Data retrieved from subgraph:', data);

    // Return the data for further processing
    return data;
  } catch (error) {
    // Handle errors gracefully
    console.error('Error querying subgraph:', error.message);
    throw new Error('Failed to fetch data from subgraph');
  }
}

// Example usage of the function
(async () => {
  try {
    const result = await fetchDataFromSubgraph(10, 0);
    console.log('Result:', result);
  } catch (error) {
    console.error('Error in example usage:', error.message);
  }
})();
```

> **Note:** Replace `<subgraph-name>` in the `SUBGRAPH_URL` with the actual name of the subgraph you want to query. Ensure you have installed the `graphql-request` package (`npm install graphql-request`) before running the code.
