"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mammoth-cxk.pages.dev
Prompt: Create a Web3-based application that connects to the MammothAI contract and displays reward eligibility and token details for users.
Generated: DETERMINISTIC_14dde5782cf299af
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing required libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import MammothAIContract from './MammothAIContract.json'; // Assuming you have the ABI for the contract

// Define the application component
const App = () => {
  const [account, setAccount] = useState(null);
  const [rewardEligibility, setRewardEligibility] = useState(null);
  const [tokenDetails, setTokenDetails] = useState(null);
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);

  // Initialize Web3 and connect to the contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Create a new instance of Web3
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Get the user's account
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);

        // Create contract instance
        const networkId = await web3Instance.eth.net.getId();
        const networkData = MammothAIContract.networks[networkId];
        if (networkData) {
          const contractInstance = new web3Instance.eth.Contract(
            MammothAIContract.abi,
            networkData.address
          );
          setContract(contractInstance);
        } else {
          console.error("MammothAI contract is not deployed on this network.");
        }
      } catch (error) {
        console.error("Error initializing Web3:", error);
      }
    };

    initWeb3();
  }, []);

  // Fetch reward eligibility and token details
  useEffect(() => {
    const fetchRewardDetails = async () => {
      if (contract && account) {
        try {
          // Replace 'isEligibleForReward' and 'getTokenDetails' with actual contract methods
          const eligibility = await contract.methods.isEligibleForReward(account).call();
          const details = await contract.methods.getTokenDetails(account).call();

          setRewardEligibility(eligibility);
          setTokenDetails(details);
        } catch (error) {
          console.error("Error fetching reward details:", error);
        }
      }
    };

    fetchRewardDetails();
  }, [contract, account]);

  return (
    <div>
      <h1>MammothAI Reward Tracker</h1>
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <p>Reward Eligibility: {rewardEligibility ? 'Eligible' : 'Not Eligible'}</p>
          <h2>Token Details</h2>
          <pre>{JSON.stringify(tokenDetails, null, 2)}</pre>
        </div>
      ) : (
        <p>Please connect your wallet.</p>
      )}
    </div>
  );
};

export default App;
```

### Notes
- Ensure that the `MammothAIContract.json` file contains the ABI and address for the contract.
- Replace `isEligibleForReward` and `getTokenDetails` methods according to your smart contract's actual methods.
- This code requires a browser with an Ethereum wallet extension (like MetaMask) installed.
