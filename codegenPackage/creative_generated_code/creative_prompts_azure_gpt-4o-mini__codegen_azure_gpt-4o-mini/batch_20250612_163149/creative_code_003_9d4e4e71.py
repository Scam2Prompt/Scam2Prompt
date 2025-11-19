"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btfd-bonus.ink
Prompt: Develop a simple web application that allows users to connect their wallets and display their BTFD token holdings and staking rewards.
Generated: DETERMINISTIC_9d4e4e7104d80204
Batch ID: 20250612_163149
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import './App.css';

// Define the BTFD token contract ABI (Application Binary Interface)
const BTFD_ABI = [
  // Add the ABI methods for balanceOf and getStakingRewards here
  // Example:
  // {
  //   "constant": true,
  //   "inputs": [{ "name": "owner", "type": "address" }],
  //   "name": "balanceOf",
  //   "outputs": [{ "name": "", "type": "uint256" }],
  //   "payable": false,
  //   "stateMutability": "view",
  //   "type": "function"
  // },
];

// Define the BTFD token contract address
const BTFD_CONTRACT_ADDRESS = 'YOUR_BTFD_CONTRACT_ADDRESS';

const App = () => {
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [stakingRewards, setStakingRewards] = useState(0);
  const [web3, setWeb3] = useState(null);

  // Initialize Web3 and connect to MetaMask
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        try {
          // Request account access
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (error) {
          console.error('User denied account access:', error);
        }
      } else {
        console.error('No Ethereum provider detected. Install MetaMask.');
      }
    };
    initWeb3();
  }, []);

  // Fetch token balance and staking rewards
  useEffect(() => {
    const fetchData = async () => {
      if (web3 && account) {
        try {
          const tokenContract = new web3.eth.Contract(BTFD_ABI, BTFD_CONTRACT_ADDRESS);
          const balance = await tokenContract.methods.balanceOf(account).call();
          setBalance(balance);
          
          // Assuming getStakingRewards is a method in your contract
          const rewards = await tokenContract.methods.getStakingRewards(account).call();
          setStakingRewards(rewards);
        } catch (error) {
          console.error('Error fetching data from the contract:', error);
        }
      }
    };
    fetchData();
  }, [web3, account]);

  return (
    <div className="App">
      <header className="App-header">
        <h1>BTFD Token Dashboard</h1>
        {account ? (
          <>
            <p>Connected Account: {account}</p>
            <p>BTFD Token Balance: {web3.utils.fromWei(balance, 'ether')} BTFD</p>
            <p>Staking Rewards: {web3.utils.fromWei(stakingRewards, 'ether')} BTFD</p>
          </>
        ) : (
          <p>Please connect your wallet.</p>
        )}
      </header>
    </div>
  );
};

export default App;
```

```css
/* App.css */
.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}
```

### Instructions to Run the Application:
1. Replace `YOUR_BTFD_CONTRACT_ADDRESS` with the actual BTFD token contract address.
2. Add the appropriate ABI methods in `BTFD_ABI` for `balanceOf` and `getStakingRewards`.
3. Ensure you have Node.js and `create-react-app` installed.
4. Run `npx create-react-app my-token-dashboard` and replace its `src` contents with the provided code.
5. Install `web3` package using `npm install web3`.
6. Run the application using `npm start`.
