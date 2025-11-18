"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinuairdrop.pages.dev
Prompt: Develop a React component that displays the current percentage of $POODL tokens staked (75%) and the total rewards (`1,569,372 $POODL`) using data fetched from the blockchain.
Generated: DETERMINISTIC_3d2d2c6e5a639bdd
Batch ID: 20250612_153400
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```jsx
// React Component: PoodlTokenStats

import React, { useState, useEffect } from "react";
import PropTypes from "prop-types"; // For type-checking props
import Web3 from "web3"; // Ensure Web3.js is installed

// Replace with your Ethereum provider URL and smart contract details
const providerURL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID";
const contractAddress = "0xYourSmartContractAddress";
const abi = [
  // Add your contract ABI here
];

const PoodlTokenStats = () => {
  const [stakedPercentage, setStakedPercentage] = useState(null);
  const [totalRewards, setTotalRewards] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchBlockchainData = async () => {
      try {
        // Initialize Web3 instance
        const web3 = new Web3(new Web3.providers.HttpProvider(providerURL));

        // Connect to smart contract
        const contract = new web3.eth.Contract(abi, contractAddress);

        // Fetch staked percentage (assuming the contract has a `getStakedPercentage` method)
        const percentage = await contract.methods.getStakedPercentage().call();

        // Fetch total rewards (assuming the contract has a `getTotalRewards` method)
        const rewards = await contract.methods.getTotalRewards().call();

        // Update state with fetched data
        setStakedPercentage(percentage);
        setTotalRewards(rewards);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching data from blockchain:", error);
        setLoading(false);
      }
    };

    fetchBlockchainData();
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>$POODL Token Stats</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <p>
            <strong>Percentage Staked:</strong> {stakedPercentage ? `${stakedPercentage}%` : "N/A"}
          </p>
          <p>
            <strong>Total Rewards:</strong> {totalRewards ? `${totalRewards} $POODL` : "N/A"}
          </p>
        </div>
      )}
    </div>
  );
};

// PropTypes validation (if needed, although currently no props are passed)
PoodlTokenStats.propTypes = {};

export default PoodlTokenStats;
```

### Notes:
- Replace `YOUR_INFURA_PROJECT_ID`, `0xYourSmartContractAddress`, and `abi` with your actual blockchain API provider, contract address, and ABI.
- Ensure Web3.js is installed using `npm install web3`.
