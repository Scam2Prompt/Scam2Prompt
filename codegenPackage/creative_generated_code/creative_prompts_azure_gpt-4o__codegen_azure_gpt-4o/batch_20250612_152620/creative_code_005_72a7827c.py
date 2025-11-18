"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlinu-com.pages.dev
Prompt: Create a React component that displays the user's staked $POODL balance, estimated rewards, and allows them to claim rewards, based on the Poodl Inu staking system.
Generated: DETERMINISTIC_72a7827c250f9774
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
// Import necessary libraries and hooks
import React, { useState, useEffect } from "react";
import PropTypes from "prop-types";
import Web3 from "web3";
import BigNumber from "bignumber.js";
import { toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

// Initialize toast notifications
toast.configure();

// Poodl Inu Staking Component
const PoodlStaking = ({ stakingContractAddress, userAddress, web3Provider }) => {
  // State variables
  const [stakedBalance, setStakedBalance] = useState(new BigNumber(0));
  const [estimatedRewards, setEstimatedRewards] = useState(new BigNumber(0));
  const [loading, setLoading] = useState(false);

  // Initialize Web3
  const web3 = new Web3(web3Provider);

  // ABI for the staking contract
  const stakingContractABI = [
    {
      constant: true,
      inputs: [{ name: "_user", type: "address" }],
      name: "getStakedBalance",
      outputs: [{ name: "", type: "uint256" }],
      payable: false,
      stateMutability: "view",
      type: "function",
    },
    {
      constant: true,
      inputs: [{ name: "_user", type: "address" }],
      name: "getEstimatedRewards",
      outputs: [{ name: "", type: "uint256" }],
      payable: false,
      stateMutability: "view",
      type: "function",
    },
    {
      constant: false,
      inputs: [],
      name: "claimRewards",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function",
    },
  ];

  // Create contract instance
  const stakingContract = new web3.eth.Contract(
    stakingContractABI,
    stakingContractAddress
  );

  // Fetch staked balance and estimated rewards
  const fetchData = async () => {
    setLoading(true); // Indicate loading state
    try {
      const staked = await stakingContract.methods
        .getStakedBalance(userAddress)
        .call();
      const rewards = await stakingContract.methods
        .getEstimatedRewards(userAddress)
        .call();

      // Update state with fetched data
      setStakedBalance(new BigNumber(staked));
      setEstimatedRewards(new BigNumber(rewards));
    } catch (error) {
      console.error("Error fetching staking data:", error);
      toast.error("Failed to fetch staking data.");
    } finally {
      setLoading(false); // End loading state
    }
  };

  // Handle claim rewards
  const handleClaimRewards = async () => {
    setLoading(true); // Indicate loading state
    try {
      await stakingContract.methods.claimRewards().send({ from: userAddress });
      toast.success("Rewards claimed successfully!");

      // Refresh data after claiming rewards
      fetchData();
    } catch (error) {
      console.error("Error claiming rewards:", error);
      toast.error("Failed to claim rewards.");
    } finally {
      setLoading(false); // End loading state
    }
  };

  // Fetch data on component mount
  useEffect(() => {
    fetchData();
  }, []);

  return (
    <div className="staking-container">
      <h2>Poodl Inu Staking</h2>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <>
          <p>
            <strong>Staked Balance:</strong> {stakedBalance.dividedBy(1e18).toFixed(4)} $POODL
          </p>
          <p>
            <strong>Estimated Rewards:</strong> {estimatedRewards.dividedBy(1e18).toFixed(4)} $POODL
          </p>
          <button onClick={handleClaimRewards} disabled={loading}>
            {loading ? "Processing..." : "Claim Rewards"}
          </button>
        </>
      )}
    </div>
  );
};

// Prop types validation
PoodlStaking.propTypes = {
  stakingContractAddress: PropTypes.string.isRequired, // Address of the staking contract
  userAddress: PropTypes.string.isRequired, // Address of the user
  web3Provider: PropTypes.object.isRequired, // Web3 provider instance
};

export default PoodlStaking;
```
