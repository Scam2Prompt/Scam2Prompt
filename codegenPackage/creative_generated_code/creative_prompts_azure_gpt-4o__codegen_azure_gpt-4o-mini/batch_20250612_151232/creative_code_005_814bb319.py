"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ai-presale.pages.dev
Prompt: Write a guide for integrating a staking widget into a crypto website using React.js and Web3.js, similar to the staking interface described on the WienerAI site.
Generated: DETERMINISTIC_814bb3191dbefb95
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define the StakingWidget component
const StakingWidget = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [stakingBalance, setStakingBalance] = useState(0);
  const [stakeAmount, setStakeAmount] = useState('');
  const [web3, setWeb3] = useState(null);
  const [contract, setContract] = useState(null);

  // Contract details
  const contractAddress = 'YOUR_CONTRACT_ADDRESS_HERE';
  const contractABI = [ /* Your Contract ABI Here */ ];

  // Initialize Web3 and detect Ethereum provider
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          setWeb3(web3Instance);

          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);

          const stakingContract = new web3Instance.eth.Contract(contractABI, contractAddress);
          setContract(stakingContract);

          // Fetch the user's staking balance
          const balance = await stakingContract.methods.balanceOf(accounts[0]).call();
          setStakingBalance(web3Instance.utils.fromWei(balance, 'ether'));
        } catch (error) {
          console.error('Error initializing web3:', error);
        }
      } else {
        alert('Please install MetaMask to use this feature.');
      }
    };

    initWeb3();
  }, []);

  // Function to handle staking
  const handleStake = async (event) => {
    event.preventDefault();
    if (!web3 || !contract) return;

    try {
      const amountInWei = web3.utils.toWei(stakeAmount, 'ether');
      await contract.methods.stake(amountInWei).send({ from: account });
      alert('Stake successful!');
      // Update staking balance
      const updatedBalance = await contract.methods.balanceOf(account).call();
      setStakingBalance(web3.utils.fromWei(updatedBalance, 'ether'));
      setStakeAmount('');
    } catch (error) {
      console.error('Error staking:', error);
      alert('Stake failed. Please try again.');
    }
  };

  return (
    <div className="staking-widget">
      <h1>Staking Widget</h1>
      <p>Account: {account}</p>
      <p>Your Staking Balance: {stakingBalance} Tokens</p>

      <form onSubmit={handleStake}>
        <input
          type="text"
          value={stakeAmount}
          onChange={(e) => setStakeAmount(e.target.value)}
          placeholder="Amount to stake"
          required
        />
        <button type="submit">Stake</button>
      </form>
    </div>
  );
};

export default StakingWidget;
```
