"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-apedvip.pages.dev
Prompt: Develop a React component for a cryptocurrency presale interface that includes a "Connect Wallet" button and contribution options (0.1 ETH to 0.5 ETH), inspired by the APED presale page.
Generated: DETERMINISTIC_1fff7f3475a46520
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```jsx
import React, { useState } from 'react';
import Web3 from 'web3'; // Ensure Web3 is installed via npm: `npm install web3`

// Define the PresaleComponent as a functional React component.
const PresaleComponent = () => {
  // State for storing the wallet connection status and address
  const [walletAddress, setWalletAddress] = useState('');
  
  // State for handling Web3 instance
  const [web3, setWeb3] = useState(null);

  // Ethereum contribution options
  const contributionOptions = [0.1, 0.2, 0.3, 0.4, 0.5];

  /**
   * Function to handle wallet connection
   * Uses Web3 to detect MetaMask and connect the wallet
   */
  const connectWallet = async () => {
    try {
      // Check if MetaMask is available
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);

        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setWalletAddress(accounts[0]); // Save the connected wallet address

      } else {
        alert('MetaMask not detected. Please install MetaMask to continue.');
      }
    } catch (error) {
      console.error('Error connecting wallet:', error);
      alert('Failed to connect wallet. Please try again.');
    }
  };

  /**
   * Function to handle ETH contribution
   * Sends the specified amount of ETH from the connected wallet
   */
  const contribute = async (amount) => {
    try {
      if (!walletAddress || !web3) {
        alert('Please connect your wallet before making a contribution.');
        return;
      }

      // Perform a transaction to send ETH
      await web3.eth.sendTransaction({
        from: walletAddress,
        to: '0xYOUR_CONTRACT_ADDRESS', // Replace with your presale smart contract address
        value: web3.utils.toWei(String(amount), 'ether'),
      });

      alert(`Successfully contributed ${amount} ETH!`);
    } catch (error) {
      console.error('Error during contribution:', error);
      alert('Failed to send the contribution. Please try again.');
    }
  };

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <h1>Cryptocurrency Presale</h1>
      <p>Participate in the presale by connecting your wallet and contributing ETH.</p>

      {/* Connect Wallet Button */}
      <button 
        onClick={connectWallet} 
        style={{ padding: '10px 20px', margin: '10px', cursor: 'pointer' }}
      >
        {walletAddress ? `Wallet Connected: ${walletAddress.substring(0, 10)}...` : 'Connect Wallet'}
      </button>

      {/* Contribution Options */}
      <div style={{ marginTop: '20px' }}>
        <h3>Contribution Options</h3>
        {contributionOptions.map((amount) => (
          <button
            key={amount}
            onClick={() => contribute(amount)}
            style={{
              padding: '10px 20px',
              margin: '5px',
              cursor: 'pointer',
              backgroundColor: '#f4f4f4',
            }}
          >
            Contribute {amount} ETH
          </button>
        ))}
      </div>
    </div>
  );
};

export default PresaleComponent;
```

### Notes:
- Replace `'0xYOUR_CONTRACT_ADDRESS'` with the actual smart contract address where contributions should be sent.
- Ensure `web3` is installed as a dependency using `npm install web3`.
- MetaMask must be installed in the user's browser for wallet connectivity to work.
- Use HTTPS for secure presale pages in production.
