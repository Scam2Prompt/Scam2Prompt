"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliche-iota.vercel.app
Prompt: Write code to integrate a "Connect Wallet" feature for a Web3 payment system using QR code scanning, as described on the cliche-iota.vercel.app website.
Generated: DETERMINISTIC_561e84517a32cd42
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import React, { useState } from 'react';
import Web3 from 'web3';
import QRCode from 'qrcode.react';
import WalletConnectProvider from '@walletconnect/web3-provider';

const ConnectWallet = () => {
  // Define state variables
  const [web3, setWeb3] = useState(null); // Web3 instance
  const [account, setAccount] = useState(null); // Connected wallet account
  const [qrCodeData, setQrCodeData] = useState(null); // QR Code data for WalletConnect
  const [errorMessage, setErrorMessage] = useState(null); // Error message

  // Function to initialize WalletConnect and generate QR code
  const connectWithWalletConnect = async () => {
    try {
      // Create WalletConnect Provider
      const provider = new WalletConnectProvider({
        infuraId: "YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
      });

      // Enable session (triggers QR Code modal)
      await provider.enable();

      // Create Web3 instance using WalletConnect Provider
      const web3Instance = new Web3(provider);

      // Get connected accounts
      const accounts = await web3Instance.eth.getAccounts();

      // Set state variables
      setWeb3(web3Instance);
      setAccount(accounts[0]);
      setErrorMessage(null); // Clear any previous errors

      // Handle disconnection
      provider.on("disconnect", () => {
        setWeb3(null);
        setAccount(null);
        setQrCodeData(null);
        setErrorMessage("Disconnected from wallet.");
      });
    } catch (error) {
      setErrorMessage("Failed to connect wallet: " + error.message);
    }
  };

  // Function to handle manual wallet disconnection
  const disconnectWallet = () => {
    if (web3 && web3.currentProvider && web3.currentProvider.close) {
      web3.currentProvider.close();
    }
    setWeb3(null);
    setAccount(null);
    setQrCodeData(null);
    setErrorMessage("Wallet disconnected.");
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", padding: "20px" }}>
      <h1>Connect Wallet</h1>
      {/* Display connected account */}
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
          <button onClick={disconnectWallet} style={{ margin: "10px 0" }}>
            Disconnect Wallet
          </button>
        </div>
      ) : (
        <div>
          <button onClick={connectWithWalletConnect} style={{ margin: "10px 0" }}>
            Connect with WalletConnect
          </button>
          {qrCodeData && (
            <div>
              <h3>Scan the QR Code below with your wallet:</h3>
              <QRCode value={qrCodeData} />
            </div>
          )}
        </div>
      )}

      {/* Display error messages */}
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
    </div>
  );
};

export default ConnectWallet;
```

**Note**: Replace `"YOUR_INFURA_PROJECT_ID"` with your actual Infura project ID for the code to work correctly. Ensure you have the necessary dependencies installed (`react`, `web3`, `qrcode.react`, and `@walletconnect/web3-provider`).
