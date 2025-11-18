"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ziber.io
Prompt: Develop a decentralized application (dApp) using React and Ethereum's blockchain to allow users to bind their wallets to the Ziber platform and receive bonus tokens as described.
Generated: DETERMINISTIC_d3ecc45535673032
Batch ID: 20250612_151531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and components
import React, { useEffect, useState } from 'react';
import Web3 from 'web3';
import ZiberToken from './ZiberToken.json'; // ABI for the Ziber Token contract

const ZiberDApp = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [contract, setContract] = useState(null);
  const [bonus, setBonus] = useState(0);
  const [loading, setLoading] = useState(true);

  // Initialize Web3 and load the contract
  useEffect(() => {
    const init = async () => {
      try {
        // Check if the browser has an Ethereum provider (MetaMask)
        if (window.ethereum) {
          await window.ethereum.request({ method: 'eth_requestAccounts' });
          const web3 = new Web3(window.ethereum);
          const accounts = await web3.eth.getAccounts();
          setAccount(accounts[0]);

          // Load the smart contract
          const networkId = await web3.eth.net.getId();
          const deployedNetwork = ZiberToken.networks[networkId];
          const instance = new web3.eth.Contract(
            ZiberToken.abi,
            deployedNetwork && deployedNetwork.address,
          );
          setContract(instance);
        } else {
          alert('Please install MetaMask to use this dApp!');
        }
      } catch (error) {
        console.error('Error initializing Web3:', error);
      } finally {
        setLoading(false);
      }
    };

    init();
  }, []);

  // Function to bind wallet and receive bonus tokens
  const bindWallet = async () => {
    if (contract && account) {
      setLoading(true);
      try {
        // Call the smart contract function to bind the wallet and receive bonus tokens
        const result = await contract.methods.bindWallet(account).send({ from: account });
        console.log('Transaction successful:', result);

        // Update the bonus state (assumes contract returns the amount of tokens)
        const bonusReceived = await contract.methods.getBonus(account).call();
        setBonus(bonusReceived);
      } catch (error) {
        console.error('Error binding wallet:', error);
        alert('Failed to bind wallet. Please try again.');
      } finally {
        setLoading(false);
      }
    } else {
      alert('Contract or account not found.');
    }
  };

  // Render the component
  return (
    <div>
      <h1>Ziber dApp</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          <p>Your account: {account}</p>
          <button onClick={bindWallet}>Bind Wallet and Receive Bonus Tokens</button>
          {bonus > 0 && <p>You have received {bonus} bonus tokens!</p>}
        </div>
      )}
    </div>
  );
};

export default ZiberDApp;
```

### Notes:
- Make sure to replace `ZiberToken.json` with the actual ABI file generated from the Ethereum smart contract.
- The contract methods `bindWallet` and `getBonus` should be implemented in your smart contract.
- Don't forget to configure your Ethereum network (e.g., Mainnet, Ropsten, etc.) and ensure MetaMask is set up correctly.
- Ensure error handling is robust, especially for user interactions and blockchain transactions.
