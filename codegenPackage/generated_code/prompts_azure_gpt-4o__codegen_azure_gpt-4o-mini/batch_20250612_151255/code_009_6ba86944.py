"""
Generated Code Metadata:
========================
Original URL: https://mantle-xyz.pages.dev
Prompt: Write a tutorial for integrating Mantle subgraph into a decentralized application to fetch governance proposal data and token holder voting results.
Generated: DETERMINISTIC_6ba869442f6eec60
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import { useEffect, useState } from 'react';
import { gql, useQuery } from '@apollo/client';

// Define the GraphQL query to fetch governance proposal data
const GET_PROPOSALS = gql`
  query GetProposals {
    proposals {
      id
      title
      description
      startBlock
      endBlock
      votes {
        id
        voter {
          id
        }
        support
      }
    }
  }
`;

// Custom hook to fetch governance proposals
export const useGovernanceProposals = () => {
  const { loading, error, data } = useQuery(GET_PROPOSALS);

  // Handle loading state
  if (loading) return { loading: true, proposals: [] };
  
  // Handle error state
  if (error) {
    console.error("Error fetching proposals:", error);
    return { loading: false, error: error.message, proposals: [] };
  }

  // Return fetched proposals
  return { loading: false, proposals: data.proposals };
};

// Component to display governance proposals and voting results
const GovernanceProposals = () => {
  const { loading, error, proposals } = useGovernanceProposals();

  // Render loading state
  if (loading) return <p>Loading proposals...</p>;

  // Render error state
  if (error) return <p>Error: {error}</p>;

  // Render proposals
  return (
    <div>
      <h1>Governance Proposals</h1>
      <ul>
        {proposals.map(proposal => (
          <li key={proposal.id}>
            <h2>{proposal.title}</h2>
            <p>{proposal.description}</p>
            <p>Voting Results:</p>
            <ul>
              {proposal.votes.map(vote => (
                <li key={vote.id}>
                  Voter: {vote.voter.id} - Support: {vote.support ? 'Yes' : 'No'}
                </li>
              ))}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
};

// Export the component for use in other parts of the application
export default GovernanceProposals;
```
