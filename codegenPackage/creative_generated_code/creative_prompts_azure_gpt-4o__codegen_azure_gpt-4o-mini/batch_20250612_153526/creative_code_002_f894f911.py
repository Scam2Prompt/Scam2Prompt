"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gftdst.web.app
Prompt: Generate code for a web interface that allows users to connect their Solana wallet and claim DUST tokens, supporting wallet options like Phantom and Solflare.
Generated: DETERMINISTIC_f894f91113e3b3cb
Batch ID: 20250612_153526
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://unpkg.com/@solana/wallet-adapter-react@0.14.0/dist/index.umd.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/@solana/web3.js@1.32.0/dist/web3.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/@solana/wallet-adapter-solflare@0.7.0/dist/index.umd.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/@solana/wallet-adapter-base@0.7.0/dist/index.umd.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/@solana/wallet-adapter-wallets@0.7.0/dist/index.umd.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://unpkg.com/@solana/wallet-adapter-phantom@0.7.0/dist/index.umd.js": {
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
    <title>DUST Token Claim Interface</title>
    <script src="https://unpkg.com/@solana/web3.js@1.32.0/dist/web3.min.js"></script>
    <script src="https://unpkg.com/@solana/wallet-adapter-base@0.7.0/dist/index.umd.js"></script>
    <script src="https://unpkg.com/@solana/wallet-adapter-react@0.14.0/dist/index.umd.js"></script>
    <script src="https://unpkg.com/@solana/wallet-adapter-wallets@0.7.0/dist/index.umd.js"></script>
    <script src="https://unpkg.com/@solana/wallet-adapter-phantom@0.7.0/dist/index.umd.js"></script>
    <script src="https://unpkg.com/@solana/wallet-adapter-solflare@0.7.0/dist/index.umd.js"></script>
    <style>
        body { font-family: Arial, sans-serif; }
        #connect-button { margin: 10px; padding: 10px; }
        #claim-button { margin: 10px; padding: 10px; }
    </style>
</head>
<body>

    <h1>Claim Your DUST Tokens</h1>
    <button id="connect-button">Connect Wallet</button>
    <button id="claim-button" disabled>Claim DUST Tokens</button>
    <div id="status"></div>

    <script>
        const { Connection, PublicKey, clusterApiUrl } = window.solanaWeb3;
        const { WalletProvider } = window['@solana/wallet-adapter-react'];
        const { PhantomWalletAdapter, SolflareWalletAdapter } = window['@solana/wallet-adapter-wallets'];
        const { ConnectionProvider } = window['@solana/wallet-adapter-react'];

        // Set up the connection to the Solana cluster
        const connection = new Connection(clusterApiUrl('mainnet-beta'), 'confirmed');

        // Initialize the wallet adapters
        const wallets = [
            new PhantomWalletAdapter(),
            new SolflareWalletAdapter()
        ];

        let wallet = null;

        // Function to connect wallet
        async function connectWallet() {
            try {
                // Check if any wallet is connected
                if (!wallet) {
                    throw new Error("No wallet found.");
                }
                await wallet.connect();
                updateUI();
            } catch (error) {
                document.getElementById('status').innerText = `Error: ${error.message}`;
            }
        }

        // Function to update the UI based on wallet connection
        function updateUI() {
            const isConnected = wallet && wallet.connected;
            document.getElementById('connect-button').disabled = isConnected;
            document.getElementById('claim-button').disabled = !isConnected;
            document.getElementById('status').innerText = 
                isConnected ? `Connected: ${wallet.publicKey.toString()}` : "Wallet not connected.";
        }

        // Function to claim DUST tokens
        async function claimDustTokens() {
            try {
                if (!wallet) {
                    throw new Error("Wallet not connected.");
                }
                // Add your token claiming logic here (e.g., send a transaction)
                // Simulate successful claiming
                document.getElementById('status').innerText = "Claiming DUST tokens...";
                await new Promise(resolve => setTimeout(resolve, 2000)); // simulate async operation
                document.getElementById('status').innerText = "Successfully claimed DUST tokens!";
            } catch (error) {
                document.getElementById('status').innerText = `Error: ${error.message}`;
            }
        }

        // Event listeners for buttons
        document.getElementById('connect-button').addEventListener('click', connectWallet);
        document.getElementById('claim-button').addEventListener('click', claimDustTokens);

        // Initialize wallet connection on load
        window.addEventListener('load', () => {
            // Check for wallet availability
            if (window.solana && window.solana.isPhantom) {
                wallet = new PhantomWalletAdapter();
            } else if (window.solana && window.solana.isSolflare) {
                wallet = new SolflareWalletAdapter();
            }
            updateUI();
        });
    </script>
</body>
</html>
```
