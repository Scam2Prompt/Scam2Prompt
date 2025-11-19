"""
Generated Code Metadata:
========================
Original URL: https://walletdapp.netlify.app
Prompt: Write a React application using the Truffle Box framework to create a decentralized wallet dApp. Ensure JavaScript is enabled for the app to function properly.
Generated: DETERMINISTIC_6ec28bd5359d81ef
Batch ID: 20250612_151345
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
import Web3 from 'web3';
import WalletContract from './contracts/Wallet.json'; // Assuming the contract is compiled and available

// Main App component
const App = () => {
  const [account, setAccount] = useState('');
  const [balance, setBalance] = useState(0);
  const [contract, setContract] = useState(null);
  const [loading, setLoading] = useState(true);

  // Initialize Web3 and load the contract
  useEffect(() => {
    const initWeb3 = async () => {
      try {
        // Check if Web3 is injected by the browser (MetaMask)
        if (window.ethereum) {
          const web3 = new Web3(window.ethereum);
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);

          // Load the contract
          const networkId = await web3.eth.net.getId();
          const deployedNetwork = WalletContract.networks[networkId];
          const instance = new web3.eth.Contract(
            WalletContract.abi,
            deployedNetwork && deployedNetwork.address,
          );
          setContract(instance);

          // Fetch initial balance
          const initialBalance = await instance.methods.getBalance(accounts[0]).call();
          setBalance(initialBalance);
        } else {
          alert('Please install MetaMask to use this dApp');
        }
      } catch (error) {
        console.error("Error initializing Web3: ", error);
        alert('Failed to load Web3 or account. Check console for details.');
      } finally {
        setLoading(false);
      }
    };

    initWeb3();
  }, []);

  // Function to handle deposit
  const handleDeposit = async (amount) => {
    if (!contract) return;
    try {
      await contract.methods.deposit().send({ from: account, value: amount });
      const updatedBalance = await contract.methods.getBalance(account).call();
      setBalance(updatedBalance);
    } catch (error) {
      console.error("Error during deposit: ", error);
      alert('Failed to deposit. Check console for details.');
    }
  };

  // Function to handle withdrawal
  const handleWithdraw = async (amount) => {
    if (!contract) return;
    try {
      await contract.methods.withdraw(amount).send({ from: account });
      const updatedBalance = await contract.methods.getBalance(account).call();
      setBalance(updatedBalance);
    } catch (error) {
      console.error("Error during withdrawal: ", error);
      alert('Failed to withdraw. Check console for details.');
    }
  };

  // Render the application
  return (
    <div>
      <h1>Decentralized Wallet dApp</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <p>Account: {account}</p>
          <p>Balance: {Web3.utils.fromWei(balance, 'ether')} ETH</p>
          <button onClick={() => handleDeposit(Web3.utils.toWei('0.1', 'ether'))}>Deposit 0.1 ETH</button>
          <button onClick={() => handleWithdraw(Web3.utils.toWei('0.1', 'ether'))}>Withdraw 0.1 ETH</button>
        </div>
      )}
    </div>
  );
};

export default App;
```

### Additional Notes:
- Ensure you have the necessary dependencies installed, including `react`, `web3`, and the Truffle Box framework.
- The smart contract should have `deposit` and `withdraw` methods, along with a `getBalance` method.
- This code assumes that the smart contract is already deployed and the ABI is available in the `Wallet.json` file.
