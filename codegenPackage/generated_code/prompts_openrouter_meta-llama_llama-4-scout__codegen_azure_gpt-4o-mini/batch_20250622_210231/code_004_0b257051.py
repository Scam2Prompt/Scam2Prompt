"""
Generated Code Metadata:
========================
Original URL: https://uniswap-widget-e94wzx722-toraverse.vercel.app
Prompt: Design a simple webpage that includes the Tegro Swap widget and allows users to connect via MetaMask or WalletConnect.
Generated: DETERMINISTIC_0b25705186b683ff
Batch ID: 20250622_210231
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/tegro-swap-widget.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@walletconnect/web3-provider/dist/umd/index.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tegro Swap Widget</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        #connectButton {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            transition: background-color 0.3s;
        }
        #connectButton:hover {
            background-color: #0056b3;
        }
        #widgetContainer {
            margin-top: 20px;
            display: none; /* Hidden until connected */
        }
    </style>
</head>
<body>

    <h1>Tegro Swap Widget</h1>
    <button id="connectButton">Connect Wallet</button>
    <div id="widgetContainer">
        <h2>Tegro Swap Widget</h2>
        <!-- Tegro Swap Widget will be embedded here -->
        <div id="tegroSwapWidget"></div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@walletconnect/web3-provider/dist/umd/index.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
    <script>
        // Initialize variables
        let web3;
        let provider;

        // Function to connect to MetaMask or WalletConnect
        async function connectWallet() {
            try {
                // Check if MetaMask is installed
                if (typeof window.ethereum !== 'undefined') {
                    // Request account access
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    web3 = new Web3(window.ethereum);
                    document.getElementById('widgetContainer').style.display = 'block';
                    initializeTegroSwap();
                } else {
                    // Fallback to WalletConnect
                    provider = new WalletConnectProvider.default({
                        infuraId: "YOUR_INFURA_ID" // Replace with your Infura ID
                    });

                    // Enable session (triggers QR Code modal)
                    await provider.enable();
                    web3 = new Web3(provider);
                    document.getElementById('widgetContainer').style.display = 'block';
                    initializeTegroSwap();
                }
            } catch (error) {
                console.error("Error connecting to wallet:", error);
                alert("Failed to connect wallet. Please try again.");
            }
        }

        // Function to initialize the Tegro Swap widget
        function initializeTegroSwap() {
            // Load the Tegro Swap widget (replace with actual Tegro Swap script)
            const script = document.createElement('script');
            script.src = "https://example.com/tegro-swap-widget.js"; // Replace with actual Tegro Swap widget URL
            script.onload = () => {
                // Initialize the widget after the script loads
                window.TegroSwap.init({
                    web3: web3,
                    container: document.getElementById('tegroSwapWidget')
                });
            };
            document.body.appendChild(script);
        }

        // Event listener for the connect button
        document.getElementById('connectButton').addEventListener('click', connectWallet);
    </script>
</body>
</html>
```
