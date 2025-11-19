"""
Generated Code Metadata:
========================
Original URL: https://ape-launchpad.vercel.app
Prompt: Design a simple web page using HTML, CSS, and JavaScript that allows users to connect their wallet and join the Ape Terminal community.
Generated: DETERMINISTIC_3dc7ac152bfc4e61
Batch ID: 20250622_210914
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
    <title>Ape Terminal Community</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        header {
            text-align: center;
            margin-bottom: 30px;
        }

        h1 {
            color: #4a4a4a;
            margin-bottom: 10px;
        }

        .description {
            color: #666;
            margin-bottom: 20px;
        }

        .wallet-section {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .wallet-btn {
            background-color: #6200ee;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .wallet-btn:hover {
            background-color: #3700b3;
        }

        .wallet-btn:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }

        .wallet-address {
            font-family: monospace;
            background-color: #f0f0f0;
            padding: 10px;
            border-radius: 5px;
            word-break: break-all;
            text-align: center;
            max-width: 100%;
        }

        .join-btn {
            background-color: #03dac6;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s;
            margin-top: 20px;
        }

        .join-btn:hover {
            background-color: #018786;
        }

        .join-btn:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }

        .status-message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
        }

        .success {
            background-color: #d4edda;
            color: #155724;
        }

        .error {
            background-color: #f8d7da;
            color: #721c24;
        }

        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Welcome to Ape Terminal</h1>
            <p class="description">Connect your wallet to join our community and access exclusive features.</p>
        </header>

        <div class="wallet-section">
            <button id="connectWalletBtn" class="wallet-btn">Connect Wallet</button>
            <div id="walletAddressContainer" class="hidden">
                <p>Connected Wallet:</p>
                <p id="walletAddress" class="wallet-address"></p>
            </div>
        </div>

        <div class="wallet-section">
            <button id="joinCommunityBtn" class="join-btn" disabled>Join Community</button>
        </div>

        <div id="statusMessage" class="status-message hidden"></div>
    </div>

    <script>
        // Check if Web3 is injected (MetaMask or similar)
        if (typeof window.ethereum !== 'undefined') {
            console.log('Web3 detected!');
        } else {
            alert('Please install MetaMask or another Web3 wallet to use this application!');
        }

        document.addEventListener('DOMContentLoaded', function() {
            const connectWalletBtn = document.getElementById('connectWalletBtn');
            const walletAddressContainer = document.getElementById('walletAddressContainer');
            const walletAddress = document.getElementById('walletAddress');
            const joinCommunityBtn = document.getElementById('joinCommunityBtn');
            const statusMessage = document.getElementById('statusMessage');

            let connectedAccount = null;

            // Connect wallet button handler
            connectWalletBtn.addEventListener('click', async function() {
                try {
                    // Request account access
                    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    connectedAccount = accounts[0];
                    
                    // Update UI
                    walletAddress.textContent = connectedAccount;
                    walletAddressContainer.classList.remove('hidden');
                    connectWalletBtn.disabled = true;
                    joinCommunityBtn.disabled = false;
                    
                    // Listen for account changes
                    window.ethereum.on('accountsChanged', function(accounts) {
                        if (accounts.length === 0) {
                            // Wallet disconnected
                            resetWalletState();
                        } else {
                            // Account changed
                            connectedAccount = accounts[0];
                            walletAddress.textContent = connectedAccount;
                        }
                    });
                    
                    showStatus('Wallet connected successfully!', 'success');
                } catch (error) {
                    console.error('Error connecting wallet:', error);
                    showStatus('Error connecting wallet: ' + error.message, 'error');
                }
            });

            // Join community button handler
            joinCommunityBtn.addEventListener('click', async function() {
                try {
                    // Simulate joining community (in a real app, this would call a smart contract)
                    showStatus('Successfully joined the Ape Terminal community!', 'success');
                    joinCommunityBtn.disabled = true;
                    
                    // In a real implementation, you might:
                    // 1. Call a smart contract function
                    // 2. Wait for transaction confirmation
                    // 3. Update UI based on success/failure
                    
                } catch (error) {
                    console.error('Error joining community:', error);
                    showStatus('Error joining community: ' + error.message, 'error');
                }
            });

            // Helper function to show status messages
            function showStatus(message, type) {
                statusMessage.textContent = message;
                statusMessage.className = `status-message ${type}`;
                statusMessage.classList.remove('hidden');
                
                // Hide after 5 seconds
                setTimeout(() => {
                    statusMessage.classList.add('hidden');
                }, 5000);
            }

            // Helper function to reset wallet state
            function resetWalletState() {
                connectedAccount = null;
                walletAddress.textContent = '';
                walletAddressContainer.classList.add('hidden');
                connectWalletBtn.disabled = false;
                joinCommunityBtn.disabled = true;
                showStatus('Wallet disconnected', 'error');
            }
        });
    </script>
</body>
</html>
```
