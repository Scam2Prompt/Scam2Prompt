"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-next-j658wjc9e-voteagora.vercel.app
Prompt: Create a user interface for submitting and voting on proposals in an on-chain governance platform, inspired by the Optimism Agora design.
Generated: DETERMINISTIC_51df92ed52e0aa12
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules and libraries
import React, { useState, useEffect } from "react";
import { ethers } from "ethers";
import "./App.css";

// Smart contract interactions (replace with your contract's address and ABI)
const CONTRACT_ADDRESS = "0xYourSmartContractAddressHere";
const CONTRACT_ABI = [
  // Add your smart contract's ABI here
];

function App() {
  const [proposals, setProposals] = useState([]);
  const [newProposal, setNewProposal] = useState("");
  const [walletConnected, setWalletConnected] = useState(false);
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);

  // Connect to MetaMask wallet
  const connectWallet = async () => {
    try {
      if (!window.ethereum) {
        alert("Please install MetaMask!");
        return;
      }

      const web3Provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = web3Provider.getSigner();
      const governanceContract = new ethers.Contract(
        CONTRACT_ADDRESS,
        CONTRACT_ABI,
        signer
      );

      setProvider(web3Provider);
      setContract(governanceContract);
      setWalletConnected(true);
    } catch (error) {
      console.error("Wallet connection failed:", error);
    }
  };

  // Fetch proposals from the blockchain
  const fetchProposals = async () => {
    try {
      if (!contract) return;

      const proposalCount = await contract.getProposalCount();
      const fetchedProposals = [];
      for (let i = 0; i < proposalCount; i++) {
        const proposal = await contract.getProposal(i);
        fetchedProposals.push({
          id: i,
          description: proposal.description,
          votes: proposal.votes.toNumber(),
        });
      }
      setProposals(fetchedProposals);
    } catch (error) {
      console.error("Failed to fetch proposals:", error);
    }
  };

  // Submit a new proposal
  const submitProposal = async () => {
    try {
      if (!contract || !newProposal.trim()) {
        alert("Proposal description cannot be empty.");
        return;
      }

      const tx = await contract.createProposal(newProposal);
      await tx.wait();
      setNewProposal("");
      fetchProposals();
    } catch (error) {
      console.error("Failed to submit proposal:", error);
    }
  };

  // Vote on a proposal
  const voteOnProposal = async (proposalId) => {
    try {
      if (!contract) return;

      const tx = await contract.vote(proposalId);
      await tx.wait();
      fetchProposals();
    } catch (error) {
      console.error("Failed to vote on proposal:", error);
    }
  };

  // Load proposals on component mount
  useEffect(() => {
    if (walletConnected) {
      fetchProposals();
    }
  }, [walletConnected, contract]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>On-Chain Governance Platform</h1>
        {!walletConnected ? (
          <button onClick={connectWallet}>Connect Wallet</button>
        ) : (
          <div>
            <h2>Submit a New Proposal</h2>
            <input
              type="text"
              placeholder="Enter proposal description"
              value={newProposal}
              onChange={(e) => setNewProposal(e.target.value)}
            />
            <button onClick={submitProposal}>Submit Proposal</button>
            <h2>Proposals</h2>
            {proposals.length === 0 ? (
              <p>No proposals found.</p>
            ) : (
              <ul>
                {proposals.map((proposal) => (
                  <li key={proposal.id}>
                    <p>{proposal.description}</p>
                    <p>Votes: {proposal.votes}</p>
                    <button onClick={() => voteOnProposal(proposal.id)}>
                      Vote
                    </button>
                  </li>
                ))}
              </ul>
            )}
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
```

**Note**: 
1. Replace `CONTRACT_ADDRESS` and `CONTRACT_ABI` with the actual smart contract address and ABI.
2. Ensure the smart contract has methods `getProposalCount`, `getProposal`, `createProposal`, and `vote` implemented.
3. Styling (`App.css`) is assumed to be in place for the UI to look polished.
