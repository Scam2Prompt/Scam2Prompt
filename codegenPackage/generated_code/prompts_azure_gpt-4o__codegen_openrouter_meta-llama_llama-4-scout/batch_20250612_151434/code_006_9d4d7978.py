"""
Generated Code Metadata:
========================
Original URL: https://uyhybuygu7ytgt7yug.pages.dev
Prompt: Create a web interface using React.js to allow users to connect their wallets (MetaMask, Coinbase, Trust Wallet) and claim $PSYOP tokens.
Generated: DETERMINISTIC_9d4d797892eb3c2b
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**WalletConnector.js**
```javascript
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';

const WalletConnector = () => {
  const [web3, setWeb3] = useState(null);
  const [accounts, setAccounts] = useState([]);
  const [walletConnected, setWalletConnected] = useState(false);
  const [tokenBalance, setTokenBalance] = useState(0);

  // Initialize web3
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
      } else if (window.web3) {
        const web3Instance = new Web3(window.web3.currentProvider);
        setWeb3(web3Instance);
      }
    };
    initWeb3();
  }, []);

  // Connect wallet
  const connectWallet = async () => {
    if (web3) {
      try {
        const accounts = await web3.eth.getAccounts();
        setAccounts(accounts);
        setWalletConnected(true);
      } catch (error) {
        console.error(error);
      }
    }
  };

  // Claim $PSYOP tokens
  const claimTokens = async () => {
    if (web3 && accounts.length > 0) {
      try {
        const contractAddress = '0x...'; // Replace with contract address
        const contractAbi = [...]; // Replace with contract ABI
        const contract = new web3.eth.Contract(contractAbi, contractAddress);
        const tx = await contract.methods.claimTokens().send({ from: accounts[0] });
        console.log(tx);
      } catch (error) {
        console.error(error);
      }
    }
  };

  // Get token balance
  const getTokenBalance = async () => {
    if (web3 && accounts.length > 0) {
      try {
        const contractAddress = '0x...'; // Replace with contract address
        const contractAbi = [...]; // Replace with contract ABI
        const contract = new web3.eth.Contract(contractAbi, contractAddress);
        const balance = await contract.methods.balanceOf(accounts[0]).call();
        setTokenBalance(balance);
      } catch (error) {
        console.error(error);
      }
    }
  };

  useEffect(() => {
    if (walletConnected) {
      getTokenBalance();
    }
  }, [walletConnected]);

  return (
    <div>
      <button onClick={connectWallet}>Connect Wallet</button>
      {walletConnected && (
        <div>
          <p>Connected to {accounts[0]}</p>
          <p>Token Balance: {tokenBalance}</p>
          <button onClick={claimTokens}>Claim $PSYOP Tokens</button>
        </div>
      )}
    </div>
  );
};

export default WalletConnector;
```

**WalletConnector.test.js**
```javascript
import React from 'react';
import { render, fireEvent, waitFor } from '@testing-library/react';
import WalletConnector from './WalletConnector';

jest.mock('web3', () => {
  return {
    __esModule: true,
    default: jest.fn(() => ({
      eth: {
        getAccounts: jest.fn(() => Promise.resolve(['0x...'])),
      },
    })),
  };
});

describe('WalletConnector', () => {
  it('renders connect wallet button', () => {
    const { getByText } = render(<WalletConnector />);
    expect(getByText('Connect Wallet')).toBeInTheDocument();
  });

  it('connects wallet on button click', async () => {
    const { getByText } = render(<WalletConnector />);
    const button = getByText('Connect Wallet');
    fireEvent.click(button);
    await waitFor(() => expect(getByText('Connected to 0x...')).toBeInTheDocument());
  });

  it('claims tokens on button click', async () => {
    const { getByText } = render(<WalletConnector />);
    const connectButton = getByText('Connect Wallet');
    fireEvent.click(connectButton);
    await waitFor(() => expect(getByText('Connected to 0x...')).toBeInTheDocument());
    const claimButton = getByText('Claim $PSYOP Tokens');
    fireEvent.click(claimButton);
    await waitFor(() => expect(console.log).toHaveBeenCalledTimes(1));
  });
});
```

**index.js**
```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import WalletConnector from './WalletConnector';

ReactDOM.render(
  <React.StrictMode>
    <WalletConnector />
  </React.StrictMode>,
  document.getElementById('root')
);
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Wallet Connector</title>
</head>
<body>
  <div id="root"></div>
</body>
</html>
```
