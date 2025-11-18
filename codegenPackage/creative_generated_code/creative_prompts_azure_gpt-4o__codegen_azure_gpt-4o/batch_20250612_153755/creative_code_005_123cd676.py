"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-mystenlabs-dapp-integration.vercel.app
Prompt: Provide an example of a front-end implementation for a dApp that includes "Connect Wallet" functionality for the Sui blockchain, as seen on the Sui Games Testnet.
Generated: DETERMINISTIC_123cd6767e6a479e
Batch ID: 20250612_153755
URLs Found: 8
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-core": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@mysten/wallet-standard": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-react": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-all-wallets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/react@17/umd/react.production.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/react-dom@17/umd/react-dom.production.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-react-ui/styles.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@babel/standalone/babel.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sui dApp - Connect Wallet</title>
  <script src="https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-all-wallets"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-core"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-react"></script>
  <script src="https://cdn.jsdelivr.net/npm/@mysten/wallet-standard"></script>
  <script src="https://cdn.jsdelivr.net/npm/react@17/umd/react.production.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/react-dom@17/umd/react-dom.production.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/@babel/standalone/babel.min.js"></script>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@mysten/wallet-adapter-react-ui/styles.css">
</head>
<body>
  <div id="root"></div>

  <script type="text/babel">
    const { useEffect, useState } = React;
    const { WalletProvider, useWallet } = mysten.walletAdapterReact;
    const { WalletStandardWalletAdapter } = mysten.walletAdapterCore;
    const { WalletAdapterStandard } = mysten.walletStandard;
    const wallets = [
      new WalletStandardWalletAdapter(),
    ];

    const App = () => {
      const { connect, disconnect, connected, wallets, select } = useWallet();
      const [selectedWallet, setSelectedWallet] = useState(null);

      useEffect(() => {
        // Automatically select a wallet if one is already connected
        if (connected && wallets.length > 0) {
          setSelectedWallet(wallets[0]);
        }
      }, [connected, wallets]);

      const handleConnect = async () => {
        try {
          if (!selectedWallet) {
            alert("Please select a wallet first.");
            return;
          }

          await connect(selectedWallet);
          alert("Wallet connected successfully.");
        } catch (error) {
          console.error("Error connecting wallet:", error);
          alert("Failed to connect wallet.");
        }
      };

      const handleDisconnect = async () => {
        try {
          await disconnect();
          alert("Wallet disconnected successfully.");
        } catch (error) {
          console.error("Error disconnecting wallet:", error);
          alert("Failed to disconnect wallet.");
        }
      };

      return (
        <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
          <h1>Sui dApp - Connect Wallet</h1>
          <div style={{ marginBottom: "20px" }}>
            <label htmlFor="wallet-select">Select Wallet:</label>
            <select
              id="wallet-select"
              value={selectedWallet ? selectedWallet.name : ""}
              onChange={(e) => {
                const wallet = wallets.find((w) => w.name === e.target.value);
                setSelectedWallet(wallet);
                select(wallet);
              }}
            >
              <option value="" disabled>Select Wallet</option>
              {wallets.map((wallet, idx) => (
                <option key={idx} value={wallet.name}>
                  {wallet.name}
                </option>
              ))}
            </select>
          </div>
          <div>
            <button
              onClick={handleConnect}
              disabled={connected || !selectedWallet}
              style={{
                padding: "10px 20px",
                marginRight: "10px",
                cursor: connected ? "not-allowed" : "pointer",
              }}
            >
              {connected ? "Connected" : "Connect Wallet"}
            </button>
            <button
              onClick={handleDisconnect}
              disabled={!connected}
              style={{
                padding: "10px 20px",
                cursor: connected ? "pointer" : "not-allowed",
              }}
            >
              Disconnect Wallet
            </button>
          </div>
          {connected && (
            <div style={{ marginTop: "20px", color: "green" }}>
              <p><strong>Wallet Connected:</strong></p>
              <p>Wallet Name: {selectedWallet.name}</p>
            </div>
          )}
        </div>
      );
    };

    ReactDOM.render(
      <WalletProvider wallets={wallets}>
        <App />
      </WalletProvider>,
      document.getElementById("root")
    );
  </script>
</body>
</html>
```
