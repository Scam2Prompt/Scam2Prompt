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

```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define the Presale component
const Presale = () => {
  // State variables
  const [account, setAccount] = useState('');
  const [contribution, setContribution] = useState(0.1);
  const [web3, setWeb3] = useState(null);
  const [error, setError] = useState('');

  // Initialize web3 and connect to Ethereum wallet
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        try {
          const web3Instance = new Web3(window.ethereum);
          setWeb3(web3Instance);
          await window.ethereum.enable(); // Request wallet connection
          const accounts = await web3Instance.eth.getAccounts();
          setAccount(accounts[0]);
        } catch (err) {
          setError('Failed to connect wallet. Please try again.');
          console.error(err);
        }
      } else {
        setError('Please install MetaMask to use this feature.');
      }
    };

    initWeb3();
  }, []);

  // Handle contribution change
  const handleContributionChange = (event) => {
    const value = parseFloat(event.target.value);
    if (value >= 0.1 && value <= 0.5) {
      setContribution(value);
      setError('');
    } else {
      setError('Contribution must be between 0.1 ETH and 0.5 ETH.');
    }
  };

  // Handle contribution submission
  const handleSubmit = async (event) => {
    event.preventDefault();
    if (!web3) {
      setError('Web3 is not initialized. Please connect your wallet.');
      return;
    }

    try {
      // Replace with your presale contract details
      const presaleContractAddress = '0xYourPresaleContractAddress';
      const presaleContract = new web3.eth.Contract([], presaleContractAddress);

      // Send contribution
      await presaleContract.methods.contribute().send({
        from: account,
        value: web3.utils.toWei(contribution.toString(), 'ether'),
      });
      alert('Contribution successful!');
    } catch (err) {
      setError('Failed to contribute. Please check your wallet and try again.');
      console.error(err);
    }
  };

  return (
    <div className="presale-container">
      <h1>Cryptocurrency Presale</h1>
      {error && <p className="error">{error}</p>}
      <button onClick={() => window.ethereum && window.ethereum.request({ method: 'eth_requestAccounts' })}>
        Connect Wallet
      </button>
      {account && (
        <form onSubmit={handleSubmit}>
          <label>
            Contribution Amount (ETH):
            <input
              type="number"
              value={contribution}
              onChange={handleContributionChange}
              min="0.1"
              max="0.5"
              step="0.01"
            />
          </label>
          <button type="submit">Contribute</button>
        </form>
      )}
    </div>
  );
};

export default Presale;
```

```css
/* Add some basic styles for the presale interface */
.presale-container {
  padding: 20px;
  text-align: center;
}

.error {
  color: red;
  font-weight: bold;
}
```
