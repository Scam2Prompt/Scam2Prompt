"""
Generated Code Metadata:
========================
Original URL: https://ton-spin.web.app
Prompt: Generate code for a web-based TON wallet connection interface that includes buttons for "FREE SPIN" and "CLAIM REWARD."
Generated: DETERMINISTIC_ea05b41f3714bef4
Batch ID: 20250612_153915
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
    <title>TON Wallet Interface</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
        }
        
        .container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 100%;
            max-width: 400px;
            text-align: center;
        }
        
        h1 {
            color: #0088cc;
            margin-bottom: 30px;
        }
        
        .wallet-status {
            margin-bottom: 20px;
            padding: 10px;
            border-radius: 5px;
            background-color: #f0f0f0;
        }
        
        .btn {
            background-color: #0088cc;
            color: white;
            border: none;
            padding: 12px 20px;
            margin: 10px 0;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: #006699;
        }
        
        .btn:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
        
        .btn-spin {
            background-color: #ff9900;
        }
        
        .btn-spin:hover {
            background-color: #e68a00;
        }
        
        .btn-claim {
            background-color: #00aa55;
        }
        
        .btn-claim:hover {
            background-color: #008844;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>TON Wallet</h1>
        
        <div class="wallet-status" id="walletStatus">
            Wallet not connected
        </div>
        
        <button class="btn" id="connectWalletBtn">
            Connect Wallet
        </button>
        
        <button class="btn btn-spin" id="freeSpinBtn" disabled>
            FREE SPIN
        </button>
        
        <button class="btn btn-claim" id="claimRewardBtn" disabled>
            CLAIM REWARD
        </button>
    </div>

    <script>
        // Check if TonWeb is available (for TON wallet integration)
        if (typeof window.ton === 'undefined') {
            console.warn('TON Wallet extension not detected');
        }

        document.addEventListener('DOMContentLoaded', function() {
            const walletStatus = document.getElementById('walletStatus');
            const connectWalletBtn = document.getElementById('connectWalletBtn');
            const freeSpinBtn = document.getElementById('freeSpinBtn');
            const claimRewardBtn = document.getElementById('claimRewardBtn');
            
            let isWalletConnected = false;
            let walletAddress = null;

            // Connect wallet button handler
            connectWalletBtn.addEventListener('click', async function() {
                try {
                    if (typeof window.ton === 'undefined') {
                        throw new Error('TON Wallet extension not found');
                    }
                    
                    // Request wallet connection
                    const accounts = await window.ton.send('ton_requestAccounts');
                    
                    if (accounts && accounts.length > 0) {
                        walletAddress = accounts[0];
                        isWalletConnected = true;
                        walletStatus.textContent = `Connected: ${walletAddress.substring(0, 6)}...${walletAddress.substring(walletAddress.length - 4)}`;
                        connectWalletBtn.textContent = 'Disconnect Wallet';
                        freeSpinBtn.disabled = false;
                        claimRewardBtn.disabled = false;
                    } else {
                        throw new Error('No accounts found');
                    }
                } catch (error) {
                    console.error('Wallet connection error:', error);
                    walletStatus.textContent = 'Connection failed: ' + error.message;
                }
            });

            // Free spin button handler
            freeSpinBtn.addEventListener('click', async function() {
                if (!isWalletConnected) return;
                
                try {
                    freeSpinBtn.disabled = true;
                    freeSpinBtn.textContent = 'Processing...';
                    
                    // Simulate API call for free spin
                    await new Promise(resolve => setTimeout(resolve, 1500));
                    
                    // In a real app, you would call your smart contract here
                    console.log('Free spin processed for address:', walletAddress);
                    alert('Free spin completed!');
                } catch (error) {
                    console.error('Free spin error:', error);
                    alert('Free spin failed: ' + error.message);
                } finally {
                    freeSpinBtn.disabled = false;
                    freeSpinBtn.textContent = 'FREE SPIN';
                }
            });

            // Claim reward button handler
            claimRewardBtn.addEventListener('click', async function() {
                if (!isWalletConnected) return;
                
                try {
                    claimRewardBtn.disabled = true;
                    claimRewardBtn.textContent = 'Processing...';
                    
                    // Simulate API call for claiming reward
                    await new Promise(resolve => setTimeout(resolve, 1500));
                    
                    // In a real app, you would call your smart contract here
                    console.log('Reward claimed for address:', walletAddress);
                    alert('Reward claimed successfully!');
                } catch (error) {
                    console.error('Claim reward error:', error);
                    alert('Claim reward failed: ' + error.message);
                } finally {
                    claimRewardBtn.disabled = false;
                    claimRewardBtn.textContent = 'CLAIM REWARD';
                }
            });
        });
    </script>
</body>
</html>
```
