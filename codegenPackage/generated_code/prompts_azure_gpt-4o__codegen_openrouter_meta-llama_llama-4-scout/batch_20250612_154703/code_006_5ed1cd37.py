"""
Generated Code Metadata:
========================
Original URL: https://stellarterm.org
Prompt: Generate code to implement a StellarTerm-like modal for swapping assets (e.g., XLM to USDC) on the Stellar Decentralized Exchange, ensuring it adheres to the open-source principles of StellarTerm.
Generated: DETERMINISTIC_5ed1cd37bafcd7f5
Batch ID: 20250612_154703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://horizon.stellar.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
import React, { useState, useEffect } from 'react';
import { 
  Asset, 
  AssetType, 
  Horizon, 
  Server, 
  TransactionBuilder, 
  Account, 
  Keypair 
} from 'stellar-sdk';

// Define the modal component for swapping assets
function SwapAssetsModal({ isOpen, onClose, serverUrl }) {
  // Initialize state for the modal
  const [fromAsset, setFromAsset] = useState('XLM');
  const [toAsset, setToAsset] = useState('USDC');
  const [fromAmount, setFromAmount] = useState('');
  const [toAmount, setToAmount] = useState('');
  const [userAccount, setUserAccount] = useState(null);
  const [error, setError] = useState(null);

  // Create a Stellar server instance
  const server = new Server(serverUrl);

  // Load user account when the modal opens
  useEffect(() => {
    if (isOpen) {
      loadUserAccount();
    }
  }, [isOpen]);

  // Load user account from the Stellar network
  const loadUserAccount = async () => {
    try {
      const accountResponse = await server.loadAccount('user-account-public-key');
      setUserAccount(accountResponse);
    } catch (error) {
      setError('Failed to load user account');
    }
  };

  // Handle from asset change
  const handleFromAssetChange = (asset) => {
    setFromAsset(asset);
    calculateSwapAmount();
  };

  // Handle to asset change
  const handleToAssetChange = (asset) => {
    setToAsset(asset);
    calculateSwapAmount();
  };

  // Handle from amount change
  const handleFromAmountChange = (amount) => {
    setFromAmount(amount);
    calculateSwapAmount();
  };

  // Calculate swap amount
  const calculateSwapAmount = async () => {
    try {
      const fromAssetInstance = Asset.fromCode(fromAsset);
      const toAssetInstance = Asset.fromCode(toAsset);
      const response = await server.orderbook(fromAssetInstance, toAssetInstance).call();
      const price = response.bids[0].price;
      const toAmount = fromAmount * price;
      setToAmount(toAmount.toString());
    } catch (error) {
      setError('Failed to calculate swap amount');
    }
  };

  // Handle swap assets
  const handleSwapAssets = async () => {
    try {
      // Create a new transaction
      const transaction = new TransactionBuilder({
        networkPassphrase: Network.PUBLIC_NETWORK_PASSPHRASE,
        baseFee: 100,
        account: userAccount,
      }).append(
        // Create a path payment strict send operation
        PathPaymentStrictSend({
          sendAsset: Asset.fromCode(fromAsset),
          destination: userAccount.accountId,
          sendAmount: fromAmount,
          destinationMin: toAmount,
          path: [Asset.fromCode(toAsset)],
        }),
      ).setTimeout(30).build();

      // Sign the transaction
      const keypair = Keypair.fromSecret('user-account-secret-key');
      transaction.sign(keypair);

      // Submit the transaction to the Stellar network
      const response = await server.submitTransaction(transaction);
      onClose();
    } catch (error) {
      setError('Failed to swap assets');
    }
  };

  // Render the modal
  if (!isOpen) return null;
  return (
    <div>
      <h2>Swap Assets</h2>
      <form>
        <label>
          From:
          <select value={fromAsset} onChange={(e) => handleFromAssetChange(e.target.value)}>
            <option value="XLM">XLM</option>
            <option value="USDC">USDC</option>
          </select>
          <input type="number" value={fromAmount} onChange={(e) => handleFromAmountChange(e.target.value)} />
        </label>
        <br />
        <label>
          To:
          <select value={toAsset} onChange={(e) => handleToAssetChange(e.target.value)}>
            <option value="XLM">XLM</option>
            <option value="USDC">USDC</option>
          </select>
          <input type="number" value={toAmount} readOnly />
        </label>
        <br />
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="button" onClick={handleSwapAssets}>
          Swap Assets
        </button>
      </form>
    </div>
  );
}

// Export the modal component
export default SwapAssetsModal;
```

```css
/* Add some basic styling to the modal */
.swap-assets-modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: #fff;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.swap-assets-modal h2 {
  margin-top: 0;
}

.swap-assets-modal form {
  margin-top: 20px;
}

.swap-assets-modal label {
  display: block;
  margin-bottom: 10px;
}

.swap-assets-modal input[type="number"] {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

.swap-assets-modal select {
  width: 100%;
  height: 30px;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ccc;
}

.swap-assets-modal button[type="button"] {
  width: 100%;
  height: 30px;
  background-color: #4CAF50;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.swap-assets-modal button[type="button"]:hover {
  background-color: #3e8e41;
}
```

```javascript
// Usage example
import React from 'react';
import ReactDOM from 'react-dom';
import SwapAssetsModal from './SwapAssetsModal';

const App = () => {
  const [isOpen, setIsOpen] = React.useState(false);

  const handleOpenModal = () => {
    setIsOpen(true);
  };

  const handleCloseModal = () => {
    setIsOpen(false);
  };

  return (
    <div>
      <button onClick={handleOpenModal}>Open Swap Assets Modal</button>
      <SwapAssetsModal isOpen={isOpen} onClose={handleCloseModal} serverUrl="https://horizon.stellar.org" />
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));
```
