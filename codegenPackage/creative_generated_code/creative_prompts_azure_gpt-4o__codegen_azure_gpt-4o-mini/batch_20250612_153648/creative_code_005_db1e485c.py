"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Develop a front-end interface for an NFT minting platform that includes wallet selection and whitelist integration, similar to the Immortals NFT minting page.
Generated: DETERMINISTIC_db1e485cc3c2f52e
Batch ID: 20250612_153648
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
import { Button, Select, Input, Notification } from 'antd';
import 'antd/dist/antd.css'; // Ant Design CSS
import './App.css'; // Custom styles

const { Option } = Select;

// Main App component
const App = () => {
  const [walletAddress, setWalletAddress] = useState('');
  const [whitelistAddress, setWhitelistAddress] = useState('');
  const [isWhitelisted, setIsWhitelisted] = useState(false);
  const [web3, setWeb3] = useState(null);

  // Initialize Web3
  useEffect(() => {
    const initWeb3 = async () => {
      if (window.ethereum) {
        const web3Instance = new Web3(window.ethereum);
        setWeb3(web3Instance);
      } else {
        alert("Please install MetaMask!");
      }
    };
    initWeb3();
  }, []);

  // Function to connect to wallet
  const connectWallet = async () => {
    if (web3) {
      try {
        const accounts = await web3.eth.requestAccounts();
        setWalletAddress(accounts[0]);
        Notification.success({ message: 'Wallet connected!', description: accounts[0] });
      } catch (error) {
        Notification.error({ message: 'Wallet connection failed!', description: error.message });
      }
    }
  };

  // Function to check if the wallet is whitelisted
  const checkWhitelist = () => {
    const whitelist = ['0x123...', '0x456...']; // Example whitelist addresses
    if (whitelist.includes(walletAddress)) {
      setIsWhitelisted(true);
      Notification.success({ message: 'You are whitelisted!' });
    } else {
      setIsWhitelisted(false);
      Notification.error({ message: 'You are not whitelisted!' });
    }
  };

  // Function to mint NFT
  const mintNFT = async () => {
    if (isWhitelisted) {
      try {
        // Add your NFT minting logic here
        Notification.success({ message: 'NFT Minted Successfully!' });
      } catch (error) {
        Notification.error({ message: 'NFT Minting Failed!', description: error.message });
      }
    } else {
      Notification.warning({ message: 'You must be whitelisted to mint!' });
    }
  };

  return (
    <div className="app">
      <h1>NFT Minting Platform</h1>
      <Select placeholder="Select Wallet" style={{ width: 300, marginBottom: 20 }} onChange={setWalletAddress}>
        <Option value="metamask">MetaMask</Option>
        <Option value="walletconnect">WalletConnect</Option>
      </Select>
      <Button type="primary" onClick={connectWallet}>
        Connect Wallet
      </Button>
      <Input
        style={{ marginTop: 20 }}
        placeholder="Enter your whitelist address"
        onChange={(e) => setWhitelistAddress(e.target.value)}
      />
      <Button type="primary" onClick={checkWhitelist} style={{ marginTop: 20 }}>
        Check Whitelist
      </Button>
      <Button type="primary" onClick={mintNFT} style={{ marginTop: 20 }}>
        Mint NFT
      </Button>
    </div>
  );
};

export default App;
```

```css
/* App.css */

.app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f0f2f5;
}

h1 {
  color: #1890ff;
}

button {
  margin-top: 20px;
}
```

```json
// package.json
{
  "name": "nft-minting-platform",
  "version": "1.0.0",
  "description": "A front-end interface for minting NFTs with wallet selection and whitelist integration.",
  "dependencies": {
    "antd": "^4.16.13",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "web3": "^1.6.1"
  },
  "scripts": {
    "start": "react-scripts start",
    "build": "react-scripts build",
    "test": "react-scripts test",
    "eject": "react-scripts eject"
  },
  "eslintConfig": {
    "extends": [
      "react-app",
      "react-app/jest"
    ]
  },
  "browserslist": {
    "production": [
      ">0.2%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  }
}
``` 

Make sure to replace the example whitelist addresses and implement the actual minting logic where indicated.
