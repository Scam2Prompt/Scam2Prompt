"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimspopofrog.web.app
Prompt: Create a React component that integrates with MetaMask to connect a wallet and display the user's staked $FROP tokens, along with options to claim or migrate them.
Generated: DETERMINISTIC_f97c424c5151cd95
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';

// Replace with your contract ABI and address
const CONTRACT_ABI = [ /* Your ERC20 contract ABI */ ];
const CONTRACT_ADDRESS = '0xYourContractAddressHere';

const StakedTokens = () => {
  const [account, setAccount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [stakedTokens, setStakedTokens] = useState(0);
  const [error, setError] = useState(null);

  // Initialize web3 and MetaMask connection
  const initWeb3 = async () => {
    if (window.ethereum) {
      const web3Instance = new Web3(window.ethereum);
      setWeb3(web3Instance);
      try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        const accounts = await web3Instance.eth.getAccounts();
        setAccount(accounts[0]);
      } catch (err) {
        setError('User denied account access');
      }
    } else {
      setError('MetaMask is not installed. Please install it to use this feature.');
    }
  };

  // Fetch staked tokens from the contract
  const fetchStakedTokens = async () => {
    if (!web3 || !account) return;

    const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
    try {
      const stakedAmount = await contract.methods.stakedTokens(account).call();
      setStakedTokens(web3.utils.fromWei(stakedAmount, 'ether'));
    } catch (err) {
      setError('Failed to fetch staked tokens. Please try again later.');
    }
  };

  // Claim staked tokens
  const claimTokens = async () => {
    if (!web3 || !account) return;

    const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
    try {
      await contract.methods.claimTokens().send({ from: account });
      fetchStakedTokens(); // Refresh staked tokens after claiming
    } catch (err) {
      setError('Failed to claim tokens. Please try again later.');
    }
  };

  // Migrate staked tokens
  const migrateTokens = async () => {
    if (!web3 || !account) return;

    const contract = new web3.eth.Contract(CONTRACT_ABI, CONTRACT_ADDRESS);
    try {
      await contract.methods.migrateTokens().send({ from: account });
      fetchStakedTokens(); // Refresh staked tokens after migration
    } catch (err) {
      setError('Failed to migrate tokens. Please try again later.');
    }
  };

  useEffect(() => {
    initWeb3();
  }, []);

  useEffect(() => {
    fetchStakedTokens();
  }, [web3, account]);

  return (
    <div>
      <h1>Staked $FROP Tokens</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <p>Your wallet: {account || 'Please connect your wallet'}</p>
      <p>Staked Amount: {stakedTokens} $FROP</p>
      <button onClick={claimTokens} disabled={!account}>
        Claim Tokens
      </button>
      <button onClick={migrateTokens} disabled={!account}>
        Migrate Tokens
      </button>
    </div>
  );
};

export default StakedTokens;
```
