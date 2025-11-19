"""
Generated Code Metadata:
========================
Original URL: https://e1-9n2.pages.dev
Prompt: Build a front-end interface using HTML and JavaScript to allow users to mint up to a maximum number of NFTs per transaction, as specified by the smart contract.
Generated: DETERMINISTIC_3032b1768255a75c
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Minting Interface</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input[type="number"] {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
        .status {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
        }
        .success {
            background-color: #dff0d8;
            color: #3c763d;
        }
        .error {
            background-color: #f2dede;
            color: #a94442;
        }
        .info {
            background-color: #d9edf7;
            color: #31708f;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NFT Minting Interface</h1>
        
        <div class="form-group">
            <label for="walletAddress">Wallet Address:</label>
            <input type="text" id="walletAddress" placeholder="0x..." disabled>
        </div>
        
        <div class="form-group">
            <label for="mintAmount">Number of NFTs to Mint (Max: <span id="maxMint">5</span>):</label>
            <input type="number" id="mintAmount" min="1" max="5" value="1">
        </div>
        
        <div class="form-group">
            <button id="connectWallet">Connect Wallet</button>
            <button id="mintButton" disabled>Mint NFTs</button>
        </div>
        
        <div id="statusMessage" class="status" style="display: none;"></div>
    </div>

    <script>
        // Global variables
        let maxMintPerTx = 5; // Default value, should be fetched from contract
        let connectedWallet = null;

        // DOM elements
        const walletAddressInput = document.getElementById('walletAddress');
        const mintAmountInput = document.getElementById('mintAmount');
        const maxMintSpan = document.getElementById('maxMint');
        const connectWalletBtn = document.getElementById('connectWallet');
        const mintButton = document.getElementById('mintButton');
        const statusMessage = document.getElementById('statusMessage');

        // Initialize the app
        document.addEventListener('DOMContentLoaded', () => {
            // Set max attribute on input based on contract limit
            mintAmountInput.max = maxMintPerTx;
            maxMintSpan.textContent = maxMintPerTx;
            
            // Add event listeners
            connectWalletBtn.addEventListener('click', connectWallet);
            mintButton.addEventListener('click', mintNFTs);
            mintAmountInput.addEventListener('change', validateMintAmount);
        });

        // Connect wallet function
        async function connectWallet() {
            try {
                // Check if MetaMask is installed
                if (typeof window.ethereum === 'undefined') {
                    showStatus('Please install MetaMask to use this dApp.', 'error');
                    return;
                }

                // Request account access
                const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                connectedWallet = accounts[0];
                
                // Update UI
                walletAddressInput.value = connectedWallet;
                connectWalletBtn.textContent = 'Connected';
                connectWalletBtn.disabled = true;
                mintButton.disabled = false;
                
                showStatus('Wallet connected successfully!', 'success');
                
                // Listen for account changes
                window.ethereum.on('accountsChanged', (newAccounts) => {
                    if (newAccounts.length === 0) {
                        // Wallet disconnected
                        walletDisconnected();
                    } else {
                        // Account changed
                        connectedWallet = newAccounts[0];
                        walletAddressInput.value = connectedWallet;
                        showStatus('Account changed.', 'info');
                    }
                });
                
                // TODO: Fetch maxMintPerTx from contract here
                // maxMintPerTx = await getMaxMintPerTx();
                // mintAmountInput.max = maxMintPerTx;
                // maxMintSpan.textContent = maxMintPerTx;
                
            } catch (error) {
                console.error('Error connecting wallet:', error);
                showStatus('Error connecting wallet: ' + error.message, 'error');
            }
        }

        // Handle wallet disconnection
        function walletDisconnected() {
            connectedWallet = null;
            walletAddressInput.value = '';
            connectWalletBtn.textContent = 'Connect Wallet';
            connectWalletBtn.disabled = false;
            mintButton.disabled = true;
            showStatus('Wallet disconnected.', 'info');
        }

        // Validate mint amount input
        function validateMintAmount() {
            const amount = parseInt(mintAmountInput.value);
            
            if (isNaN(amount) || amount < 1) {
                mintAmountInput.value = 1;
            } else if (amount > maxMintPerTx) {
                mintAmountInput.value = maxMintPerTx;
                showStatus(`Maximum ${maxMintPerTx} NFTs per transaction.`, 'info');
            }
        }

        // Mint NFTs function
        async function mintNFTs() {
            if (!connectedWallet) {
                showStatus('Please connect your wallet first.', 'error');
                return;
            }
            
            const amount = parseInt(mintAmountInput.value);
            
            if (isNaN(amount) || amount < 1 || amount > maxMintPerTx) {
                showStatus('Invalid mint amount.', 'error');
                return;
            }
            
            try {
                mintButton.disabled = true;
                showStatus(`Minting ${amount} NFT(s)...`, 'info');
                
                // TODO: Replace with actual contract interaction
                // const tx = await nftContract.methods.mint(amount).send({ from: connectedWallet });
                // showStatus(`Successfully minted ${amount} NFT(s)! Transaction hash: ${tx.transactionHash}`, 'success');
                
                // Simulate contract call for demo purposes
                await new Promise(resolve => setTimeout(resolve, 2000));
                showStatus(`Successfully minted ${amount} NFT(s)! (Demo)`, 'success');
                
            } catch (error) {
                console.error('Error minting NFTs:', error);
                showStatus('Error minting NFTs: ' + error.message, 'error');
            } finally {
                mintButton.disabled = false;
            }
        }

        // Show status message
        function showStatus(message, type) {
            statusMessage.textContent = message;
            statusMessage.className = 'status ' + type;
            statusMessage.style.display = 'block';
            
            // Auto-hide success messages after 5 seconds
            if (type === 'success') {
                setTimeout(() => {
                    statusMessage.style.display = 'none';
                }, 5000);
            }
        }
    </script>
</body>
</html>
```
