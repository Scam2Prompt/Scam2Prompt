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
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import optimismABI from './optimismTokenHouseABI.json'; // Replace with the actual ABI of Optimism's Token House Governance

// Constants
const TOKEN_HOUSE_ADDRESS = '0xYourTokenHouseContractAddress'; // Replace with the actual contract address
const INFURA_PROJECT_ID = 'your-infura-project-id'; // Replace with your Infura project ID

// Main App Component
const App = () => {
  const [provider, setProvider] = useState(null);
  const [signer, setSigner] = useState(null);
  const [contract, setContract] = useState(null);
  const [proposals, setProposals] = useState([]);
  const [error, setError] = useState(null);

  // Initialize Ethereum provider and contract
  useEffect(() => {
    const initialize = async () => {
      try {
        // Connect to Ethereum provider
        const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
        await window.ethereum.request({ method: 'eth_requestAccounts' }); // Request wallet connection
        const signer = web3Provider.getSigner();

        // Connect to Optimism's Token House Governance contract
        const contract = new ethers.Contract(TOKEN_HOUSE_ADDRESS, optimismABI, signer);

        // Set state
        setProvider(web3Provider);
        setSigner(signer);
        setContract(contract);
      } catch (err) {
        console.error('Error initializing provider or contract:', err);
        setError('Failed to connect to Ethereum provider or contract.');
      }
    };

    initialize();
  }, []);

  // Fetch proposals from the contract
  const fetchProposals = async () => {
    try {
      if (!contract) {
        throw new Error('Contract not initialized.');
      }

      const proposalCount = await contract.getProposalCount(); // Assuming the contract has a `getProposalCount` method
      const proposals = [];

      for (let i = 0; i < proposalCount; i++) {
        const proposal = await contract.getProposal(i); // Assuming the contract has a `getProposal` method
        proposals.push(proposal);
      }

      setProposals(proposals);
    } catch (err) {
      console.error('Error fetching proposals:', err);
      setError('Failed to fetch proposals.');
    }
  };

  // Vote on a proposal
  const voteOnProposal = async (proposalId, support) => {
    try {
      if (!contract) {
        throw new Error('Contract not initialized.');
      }

      const tx = await contract.vote(proposalId, support); // Assuming the contract has a `vote` method
      await tx.wait(); // Wait for transaction confirmation
      alert('Vote submitted successfully!');
    } catch (err) {
      console.error('Error voting on proposal:', err);
      setError('Failed to submit vote.');
    }
  };

  return (
    <div>
      <h1>Optimism Token House Governance</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <button onClick={fetchProposals}>Fetch Proposals</button>
      <ul>
        {proposals.map((proposal, index) => (
          <li key={index}>
            <p>Proposal ID: {proposal.id}</p>
            <p>Description: {proposal.description}</p>
            <button onClick={() => voteOnProposal(proposal.id, true)}>Vote For</button>
            <button onClick={() => voteOnProposal(proposal.id, false)}>Vote Against</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
```

### Notes:
1. Replace `optimismTokenHouseABI.json` with the actual ABI file for Optimism's Token House Governance contract.
2. Replace `0xYourTokenHouseContractAddress` with the actual contract address.
3. Replace `your-infura-project-id` with your Infura project ID or use another Ethereum provider.
4. Ensure the contract methods (`getProposalCount`, `getProposal`, `vote`) match the actual contract's ABI and functionality.
