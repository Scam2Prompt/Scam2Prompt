"""
Generated Code Metadata:
========================
Original URL: https://dog-68c.pages.dev
Prompt: Generate code to display a token presale interface with tiered ETH contributions (e.g., 0.1 ETH, 0.2 ETH, etc.) and a total supply of 100,000,000 tokens.
Generated: DETERMINISTIC_0ae0216b4469f484
Batch ID: 20250622_210806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

// Define the TokenPresale component
function TokenPresale() {
  // Define the token presale tiers
  const tiers = [
    { amount: 0.1, tokens: 10000 },
    { amount: 0.2, tokens: 20000 },
    { amount: 0.5, tokens: 50000 },
    { amount: 1, tokens: 100000 },
  ];

  // Define the total token supply
  const totalSupply = 100000000;

  // Initialize state variables
  const [selectedTier, setSelectedTier] = useState(null);
  const [contributionAmount, setContributionAmount] = useState(0);
  const [tokenBalance, setTokenBalance] = useState(0);
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState(null);

  // Initialize Web3 on component mount
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
        const accounts = await web3Instance.eth.getAccounts();
        setAccounts(accounts);
      } else {
        console.error('No Ethereum provider found');
      }
    };
    initWeb3();
  }, []);

  // Handle tier selection
  const handleTierSelect = (tier) => {
    setSelectedTier(tier);
    setContributionAmount(tier.amount);
  };

  // Handle contribution
  const handleContribute = async () => {
    if (!web3 || !accounts) return;
    try {
      // Calculate token reward
      const tokenReward = selectedTier.tokens;

      // Update token balance
      setTokenBalance(tokenBalance + tokenReward);

      // Send transaction (example only, not implemented)
      const tx = await web3.eth.sendTransaction({
        from: accounts[0],
        to: '0x... contract address ...',
        value: web3.utils.toWei(contributionAmount.toString(), 'ether'),
      });
      console.log('Transaction sent:', tx);
    } catch (error) {
      console.error('Contribution error:', error);
    }
  };

  return (
    <div>
      <h1>Token Presale</h1>
      <p>Total Supply: {totalSupply} tokens</p>

      <h2>Tiers</h2>
      <ul>
        {tiers.map((tier, index) => (
          <li key={index}>
            <button onClick={() => handleTierSelect(tier)}>
              {tier.amount} ETH ({tier.tokens} tokens)
            </button>
          </li>
        ))}
      </ul>

      {selectedTier && (
        <div>
          <p>Selected Tier: {selectedTier.amount} ETH</p>
          <p>Token Reward: {selectedTier.tokens} tokens</p>
          <button onClick={handleContribute}>Contribute</button>
        </div>
      )}

      <p>Token Balance: {tokenBalance} tokens</p>
    </div>
  );
}

export default TokenPresale;
```

```css
/* Optional styling */
.TokenPresale {
  max-width: 400px;
  margin: 40px auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.TokenPresale ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.TokenPresale li {
  margin-bottom: 10px;
}

.TokenPresale button {
  background-color: #4CAF50;
  color: #fff;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.TokenPresale button:hover {
  background-color: #3e8e41;
}
```

```html
<!-- Example usage -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Token Presale</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="root"></div>
  <script src="index.js"></script>
</body>
</html>
```
