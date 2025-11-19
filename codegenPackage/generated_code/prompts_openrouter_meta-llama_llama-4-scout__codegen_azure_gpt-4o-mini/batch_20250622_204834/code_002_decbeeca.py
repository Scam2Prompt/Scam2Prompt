"""
Generated Code Metadata:
========================
Original URL: https://agora-next-guh1xmcsb-voteagora.vercel.app
Prompt: Generate a code example for integrating Optimism's token house governance with a frontend application, similar to Agora.
Generated: DETERMINISTIC_decbeeca59e94779
Batch ID: 20250622_204834
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import { ethers } from 'ethers';
import { TokenHouse } from '@optimism/token-house-sdk'; // Hypothetical SDK for Token House

// Define the main component
const GovernanceApp = () => {
  // State variables
  const [proposals, setProposals] = useState([]);
  const [account, setAccount] = useState(null);
  const [loading, setLoading] = useState(true);

  // Initialize the Ethereum provider
  const initProvider = async () => {
    if (window.ethereum) {
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner();
      const userAddress = await signer.getAddress();
      setAccount(userAddress);
      return provider;
    } else {
      throw new Error('Ethereum provider not found. Please install MetaMask.');
    }
  };

  // Fetch proposals from the Token House
  const fetchProposals = async (provider) => {
    try {
      const tokenHouse = new TokenHouse(provider);
      const fetchedProposals = await tokenHouse.getProposals();
      setProposals(fetchedProposals);
    } catch (error) {
      console.error('Error fetching proposals:', error);
      alert('Failed to fetch proposals. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  // Connect to Ethereum and fetch proposals on component mount
  useEffect(() => {
    const loadBlockchainData = async () => {
      try {
        const provider = await initProvider();
        await fetchProposals(provider);
      } catch (error) {
        console.error('Error initializing provider:', error);
        alert('Failed to connect to Ethereum. Please check your wallet.');
      }
    };

    loadBlockchainData();
  }, []);

  // Render the component
  return (
    <div>
      <h1>Token House Governance</h1>
      {loading ? (
        <p>Loading proposals...</p>
      ) : (
        <div>
          <h2>Proposals</h2>
          {proposals.length > 0 ? (
            <ul>
              {proposals.map((proposal) => (
                <li key={proposal.id}>
                  <h3>{proposal.title}</h3>
                  <p>{proposal.description}</p>
                  <button onClick={() => voteOnProposal(proposal.id)}>Vote</button>
                </li>
              ))}
            </ul>
          ) : (
            <p>No proposals available.</p>
          )}
        </div>
      )}
    </div>
  );
};

// Function to handle voting on a proposal
const voteOnProposal = async (proposalId) => {
  try {
    const provider = await initProvider();
    const tokenHouse = new TokenHouse(provider);
    const signer = provider.getSigner();
    
    // Cast vote (assuming the method exists in the SDK)
    await tokenHouse.vote(proposalId, true, { from: await signer.getAddress() });
    alert('Vote cast successfully!');
  } catch (error) {
    console.error('Error voting on proposal:', error);
    alert('Failed to cast vote. Please try again later.');
  }
};

// Export the component
export default GovernanceApp;
```
