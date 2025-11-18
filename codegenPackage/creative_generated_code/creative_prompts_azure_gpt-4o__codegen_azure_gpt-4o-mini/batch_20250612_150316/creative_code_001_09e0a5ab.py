"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graph-protocol.vercel.app
Prompt: Generate code to integrate a Web3 dApp with the Graph Protocol for querying blockchain data related to a random winner selection game.
Generated: DETERMINISTIC_09e0a5abe0ff362e
Batch ID: 20250612_150316
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/your-subgraph-name": {
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
// Importing necessary libraries
import { ethers } from 'ethers';
import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

// Define the GraphQL endpoint for The Graph protocol
const GRAPH_ENDPOINT = 'https://api.thegraph.com/subgraphs/name/your-subgraph-name';

// Setting up Apollo Client for The Graph
const client = new ApolloClient({
  uri: GRAPH_ENDPOINT,
  cache: new InMemoryCache()
});

// Define the Ethereum provider
const provider = new ethers.providers.Web3Provider(window.ethereum);

// Function to request account access and return an Ethereum signer
async function getSigner() {
  try {
    // Request account access
    await provider.send('eth_requestAccounts', []);
    const signer = provider.getSigner();
    return signer;
  } catch (error) {
    console.error("User denied account access", error);
    throw new Error("Access to account denied");
  }
}

// Function to get random winner from the blockchain
async function getRandomWinner() {
  const query = gql`
    query {
      randomWinners(first: 1, orderBy: createdAt, orderDirection: desc) {
        id
        winner
        createdAt
      }
    }
  `;

  try {
    // Execute the GraphQL query
    const response = await client.query({ query });
    return response.data.randomWinners[0];
  } catch (error) {
    console.error("Error fetching random winner from The Graph", error);
    throw new Error("Failed to fetch random winner");
  }
}

// Function to display random winner in the UI
async function displayRandomWinner() {
  try {
    const winner = await getRandomWinner();
    if (winner) {
      console.log(`Random Winner ID: ${winner.id}, Address: ${winner.winner}, Date: ${new Date(winner.createdAt * 1000).toLocaleString()}`);
    } else {
      console.log("No winners found.");
    }
  } catch (error) {
    console.error("Error displaying the random winner", error);
  }
}

// Main function to initialize the dApp
async function init() {
  try {
    const signer = await getSigner();
    console.log("Ethereum Signer initialized:", signer);
    
    // Fetch and display the latest random winner
    await displayRandomWinner();
  } catch (error) {
    console.error("Initialization error:", error);
  }
}

// Run the application
init();
```

**Note:** Replace `'your-subgraph-name'` in the `GRAPH_ENDPOINT` with the actual name of your deployed subgraph on The Graph protocol.
