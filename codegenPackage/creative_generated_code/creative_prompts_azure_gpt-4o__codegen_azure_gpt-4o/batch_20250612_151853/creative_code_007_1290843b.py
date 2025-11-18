"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doggodao.web.app
Prompt: Develop a front-end interface for a Solana-based web app that allows users to mint $DOGGO tokens directly from their connected wallets.
Generated: DETERMINISTIC_1290843b2811c635
Batch ID: 20250612_151853
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@solana/web3.js@1.73.0/lib/index.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@solana/wallet-adapter-react@0.17.1/lib/index.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@solana/wallet-adapter-base@0.9.7/lib/index.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/@solana/wallet-adapter-wallets@0.9.2/lib/index.min.js": {
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
    <title>Mint $DOGGO Tokens</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/@solana/web3.js@1.73.0/lib/index.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@solana/wallet-adapter-wallets@0.9.2/lib/index.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@solana/wallet-adapter-react@0.17.1/lib/index.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@solana/wallet-adapter-base@0.9.7/lib/index.min.js"></script>
</head>

<body>
    <div class="container mt-5">
        <h1 class="text-center">Mint $DOGGO Tokens</h1>
        <div class="text-center mt-4">
            <button id="connect-wallet-btn" class="btn btn-primary">Connect Wallet</button>
            <button id="mint-doggo-btn" class="btn btn-success mt-3" disabled>Mint $DOGGO Tokens</button>
        </div>
        <div id="status-message" class="text-center mt-3"></div>
    </div>

    <script>
        // Constants
        const MINT_ADDRESS = "DOGGO_MINT_ADDRESS"; // Replace with actual mint address for $DOGGO tokens
        const MINT_AMOUNT = 1; // Number of tokens to mint

        // Variables
        let wallet = null;

        // DOM Elements
        const connectWalletBtn = document.getElementById('connect-wallet-btn');
        const mintDoggoBtn = document.getElementById('mint-doggo-btn');
        const statusMessage = document.getElementById('status-message');

        // Function to display status messages
        const displayMessage = (message, isError = false) => {
            statusMessage.textContent = message;
            statusMessage.style.color = isError ? 'red' : 'green';
        };

        // Function to connect wallet
        const connectWallet = async () => {
            try {
                const solana = window.solana;
                if (!solana || !solana.isPhantom) {
                    displayMessage('Phantom Wallet is not installed!', true);
                    return;
                }

                const walletConnection = await solana.connect();
                wallet = walletConnection.publicKey.toString();
                displayMessage(`Connected Wallet: ${wallet}`);
                mintDoggoBtn.disabled = false; // Enable mint button after wallet is connected
            } catch (error) {
                displayMessage('Error connecting wallet: ' + error.message, true);
            }
        };

        // Function to mint $DOGGO tokens
        const mintDoggoTokens = async () => {
            try {
                if (!wallet) {
                    displayMessage('Please connect your wallet first!', true);
                    return;
                }

                // Establish a connection to the Solana blockchain
                const connection = new solanaWeb3.Connection(solanaWeb3.clusterApiUrl('devnet'), 'confirmed');

                // Create a transaction to mint tokens
                const transaction = new solanaWeb3.Transaction().add(
                    new solanaWeb3.SystemProgram.transfer({
                        fromPubkey: wallet,
                        toPubkey: MINT_ADDRESS,
                        lamports: solanaWeb3.LAMPORTS_PER_SOL * MINT_AMOUNT, // Convert SOL to lamports
                    })
                );

                // Serialize and sign the transaction
                const { signature } = await window.solana.signAndSendTransaction(transaction);
                await connection.confirmTransaction(signature, 'confirmed');

                displayMessage('Successfully minted $DOGGO tokens!');
            } catch (error) {
                displayMessage('Error minting tokens: ' + error.message, true);
            }
        };

        // Event listeners
        connectWalletBtn.addEventListener('click', connectWallet);
        mintDoggoBtn.addEventListener('click', mintDoggoTokens);
    </script>
</body>

</html>
```
