"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-catecoin-club.pages.dev
Prompt: Develop a React component to connect a wallet and display active and completed Catecoin stakes, including the ability to withdraw tokens.
Generated: DETERMINISTIC_e95570cac60dc11c
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import CatecoinStakingABI from './CatecoinStakingABI.json'; // Replace with actual ABI
import CatecoinTokenABI from './CatecoinTokenABI.json'; // Replace with actual ABI

// Replace with your contract addresses
const STAKING_CONTRACT_ADDRESS = '0xYourStakingContractAddress';
const TOKEN_CONTRACT_ADDRESS = '0xYourTokenContractAddress';

const WalletConnect = () => {
  const [web3, setWeb3] = useState(null);
  const [account, setAccount] = useState(null);
  const [activeStakes, setActiveStakes] = useState([]);
  const [completedStakes, setCompletedStakes] = useState([]);
  const [stakingContract, setStakingContract] = useState(null);
  const [tokenContract, setTokenContract] = useState(null);
  const [loading, setLoading] = useState(false);

  // Initialize Web3 and contracts
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
          setAccount(accounts[0]);
          const staking = new web3Instance.eth.Contract(CatecoinStakingABI, STAKING_CONTRACT_ADDRESS);
          const token = new web3Instance.eth.Contract(CatecoinTokenABI, TOKEN_CONTRACT_ADDRESS);
          setStakingContract(staking);
          setTokenContract(token);
        } catch (error) {
          console.error('Error connecting to wallet:', error);
          alert('Failed to connect wallet.');
        }
      } else {
        alert('Please install a Web3 wallet (e.g., MetaMask).');
      }
    };

    initWeb3();
  }, []);

  // Fetch active and completed stakes
  useEffect(() => {
    const fetchStakes = async () => {
      if (stakingContract && account) {
        setLoading(true);
        try {
          // Fetch active stakes
          const active = await stakingContract.methods.getActiveStakes(account).call();
          setActiveStakes(active);

          // Fetch completed stakes
          const completed = await stakingContract.methods.getCompletedStakes(account).call();
          setCompletedStakes(completed);
        } catch (error) {
          console.error('Error fetching stakes:', error);
        }
        setLoading(false);
      }
    };

    fetchStakes();
  }, [stakingContract, account]);

  // Withdraw tokens
  const withdrawTokens = async (stakeId) => {
    if (stakingContract && account) {
      try {
        setLoading(true);
        await stakingContract.methods.withdraw(stakeId).send({ from: account });
        alert('Tokens withdrawn successfully!');
        // Refresh stakes after withdrawal
        const active = await stakingContract.methods.getActiveStakes(account).call();
        const completed = await stakingContract.methods.getCompletedStakes(account).call();
        setActiveStakes(active);
        setCompletedStakes(completed);
      } catch (error) {
        console.error('Error withdrawing tokens:', error);
        alert('Failed to withdraw tokens.');
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <div>
      <h1>Catecoin Staking Dashboard</h1>
      {!account && <p>Please connect your wallet to continue.</p>}
      {loading && <p>Loading...</p>}
      {account && (
        <div>
          <h2>Connected Wallet: {account}</h2>

          <h3>Active Stakes</h3>
          {activeStakes.length > 0 ? (
            <ul>
              {activeStakes.map((stake, index) => (
                <li key={index}>
                  <span>Amount: {stake.amount}</span>, <span>End Date: {new Date(stake.endDate * 1000).toLocaleString()}</span>
                </li>
              ))}
            </ul>
          ) : (
            <p>No active stakes found.</p>
          )}

          <h3>Completed Stakes</h3>
          {completedStakes.length > 0 ? (
            <ul>
              {completedStakes.map((stake, index) => (
                <li key={index}>
                  <span>Amount: {stake.amount}</span>, <span>End Date: {new Date(stake.endDate * 1000).toLocaleString()}</span>
                  <button onClick={() => withdrawTokens(stake.id)}>Withdraw</button>
                </li>
              ))}
            </ul>
          ) : (
            <p>No completed stakes found.</p>
          )}
        </div>
      )}
    </div>
  );
};

export default WalletConnect;
```
