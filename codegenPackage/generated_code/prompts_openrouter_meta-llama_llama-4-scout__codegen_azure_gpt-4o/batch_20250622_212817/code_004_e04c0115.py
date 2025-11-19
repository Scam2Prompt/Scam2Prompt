"""
Generated Code Metadata:
========================
Original URL: https://beta.portal-bridge.com
Prompt: Design a simple UI component for a blockchain wallet that integrates the Portal Token Bridge, allowing users to select chains and tokens for transfer, and display the maximum transfer amount.
Generated: DETERMINISTIC_e04c0115d325b9eb
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and dependencies
import React, { useState, useEffect } from 'react';
import axios from 'axios'; // For API calls
import PropTypes from 'prop-types'; // For type checking
import './BlockchainWallet.css'; // Import CSS for styling

// BlockchainWallet Component
const BlockchainWallet = ({ tokenBridgeAPI }) => {
  // State variables
  const [chains, setChains] = useState([]); // Available chains
  const [tokens, setTokens] = useState([]); // Available tokens
  const [selectedChain, setSelectedChain] = useState(''); // User-selected chain
  const [selectedToken, setSelectedToken] = useState(''); // User-selected token
  const [maxTransferAmount, setMaxTransferAmount] = useState(0); // Maximum transfer amount
  const [error, setError] = useState(null); // Error handling

  // Fetch chains and tokens from the Portal Token Bridge API
  useEffect(() => {
    const fetchChainsAndTokens = async () => {
      try {
        const response = await axios.get(`${tokenBridgeAPI}/chains-and-tokens`);
        setChains(response.data.chains);
        setTokens(response.data.tokens);
      } catch (err) {
        setError('Failed to fetch chains and tokens. Please try again later.');
      }
    };

    fetchChainsAndTokens();
  }, [tokenBridgeAPI]);

  // Fetch maximum transfer amount based on selected chain and token
  useEffect(() => {
    const fetchMaxTransferAmount = async () => {
      if (selectedChain && selectedToken) {
        try {
          const response = await axios.get(
            `${tokenBridgeAPI}/max-transfer-amount`,
            {
              params: {
                chain: selectedChain,
                token: selectedToken,
              },
            }
          );
          setMaxTransferAmount(response.data.maxAmount);
        } catch (err) {
          setError('Failed to fetch maximum transfer amount. Please try again.');
        }
      }
    };

    fetchMaxTransferAmount();
  }, [selectedChain, selectedToken, tokenBridgeAPI]);

  // Handle chain selection
  const handleChainChange = (event) => {
    setSelectedChain(event.target.value);
    setSelectedToken(''); // Reset token selection when chain changes
    setMaxTransferAmount(0); // Reset max transfer amount
  };

  // Handle token selection
  const handleTokenChange = (event) => {
    setSelectedToken(event.target.value);
  };

  return (
    <div className="blockchain-wallet">
      <h1>Blockchain Wallet</h1>
      {error && <p className="error-message">{error}</p>}
      <div className="form-group">
        <label htmlFor="chain-select">Select Chain:</label>
        <select
          id="chain-select"
          value={selectedChain}
          onChange={handleChainChange}
        >
          <option value="">-- Select Chain --</option>
          {chains.map((chain) => (
            <option key={chain.id} value={chain.id}>
              {chain.name}
            </option>
          ))}
        </select>
      </div>
      <div className="form-group">
        <label htmlFor="token-select">Select Token:</label>
        <select
          id="token-select"
          value={selectedToken}
          onChange={handleTokenChange}
          disabled={!selectedChain} // Disable token selection until chain is selected
        >
          <option value="">-- Select Token --</option>
          {tokens
            .filter((token) => token.chainId === selectedChain)
            .map((token) => (
              <option key={token.id} value={token.id}>
                {token.name}
              </option>
            ))}
        </select>
      </div>
      <div className="form-group">
        <label>Maximum Transfer Amount:</label>
        <p>{maxTransferAmount || 'N/A'}</p>
      </div>
    </div>
  );
};

// PropTypes for type checking
BlockchainWallet.propTypes = {
  tokenBridgeAPI: PropTypes.string.isRequired, // API endpoint for the Portal Token Bridge
};

// Export the component
export default BlockchainWallet;
```

### Notes:
- Ensure you replace `tokenBridgeAPI` with the actual API endpoint URL for the Portal Token Bridge.
- Create a `BlockchainWallet.css` file for styling the component as needed.
