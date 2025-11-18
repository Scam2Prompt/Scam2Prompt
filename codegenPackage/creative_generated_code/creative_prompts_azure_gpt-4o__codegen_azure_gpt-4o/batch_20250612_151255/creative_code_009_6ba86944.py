"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantle-xyz.pages.dev
Prompt: Write a tutorial for integrating Mantle subgraph into a decentralized application to fetch governance proposal data and token holder voting results.
Generated: DETERMINISTIC_6ba869442f6eec60
Batch ID: 20250612_151255
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.thegraph.com/subgraphs/name/mantle/proposals": {
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
// Tutorial Code: Integrating Mantle Subgraph into a Decentralized Application
// This code demonstrates fetching governance proposal data and token holder voting results using Mantle Subgraph.

import { ApolloClient, InMemoryCache, gql } from '@apollo/client';

/**
 * Step 1: Initialize Apollo Client
 * Mantle Subgraph GraphQL API endpoint must be specified here.
 */
const MANTLE_SUBGRAPH_API_URL = 'https://api.thegraph.com/subgraphs/name/mantle/proposals'; // Replace with the correct Mantle Subgraph URL

const client = new ApolloClient({
  uri: MANTLE_SUBGRAPH_API_URL,
  cache: new InMemoryCache(),
});

/**
 * Step 2: Define GraphQL Queries
 * Query for governance proposals and token holder voting results.
 */
const GET_PROPOSALS_QUERY = gql`
  query GetProposals {
    proposals {
      id
      title
      description
      createdTimestamp
      endTimestamp
    }
  }
`;

const GET_VOTING_RESULTS_QUERY = gql`
  query GetVotingResults($proposalId: ID!) {
    proposal(id: $proposalId) {
      id
      votes {
        voter
        choice
        votingPower
      }
    }
  }
`;

/**
 * Step 3: Fetch Governance Proposal Data
 * Retrieves a list of proposals from the Mantle Subgraph.
 */
async function fetchProposals() {
  try {
    const response = await client.query({ query: GET_PROPOSALS_QUERY });
    return response.data.proposals; // Returns array of proposals
  } catch (error) {
    console.error('Error fetching proposals:', error.message);
    throw new Error('Unable to fetch proposals. Please check the Mantle Subgraph API URL or query syntax.');
  }
}

/**
 * Step 4: Fetch Token Holder Voting Results
 * Retrieves voting results for a specific proposal.
 * @param {string} proposalId - The ID of the proposal to fetch voting results for.
 */
async function fetchVotingResults(proposalId) {
  try {
    const response = await client.query({
      query: GET_VOTING_RESULTS_QUERY,
      variables: { proposalId },
    });
    return response.data.proposal.votes; // Returns array of votes
  } catch (error) {
    console.error(`Error fetching voting results for proposal ID ${proposalId}:`, error.message);
    throw new Error('Unable to fetch voting results. Please check the proposal ID or query syntax.');
  }
}

/**
 * Step 5: Example Usage
 * Demonstrates fetching proposals and voting results.
 */
async function main() {
  try {
    // Fetch governance proposals
    const proposals = await fetchProposals();
    console.log('Proposals:', proposals);

    // Example: Fetch voting results for the first proposal
    if (proposals.length > 0) {
      const proposalId = proposals[0].id; // Assuming there is at least one proposal
      const votes = await fetchVotingResults(proposalId);
      console.log(`Voting results for proposal ${proposalId}:`, votes);
    } else {
      console.log('No proposals found.');
    }
  } catch (error) {
    console.error('Error in main execution:', error.message);
  }
}

// Execute the example
main();
```
