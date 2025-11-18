"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-minter-delta.vercel.app
Prompt: Create a front-end interface for the Buildoors NFT minting platform that allows users to mint their "buildoor," earn `$BLD`, and view their level progression.
Generated: DETERMINISTIC_03f0bca31519e916
Batch ID: 20250612_151550
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js": {
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
    <title>Buildoors NFT Minting Platform</title>
    <!-- Link to CSS stylesheet -->
    <link rel="stylesheet" href="styles.css">
    <!-- Include Web3.js for Ethereum interactions -->
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
</head>
<body>
    <div id="app">
        <h1>Buildoors NFT Minting Platform</h1>
        
        <div id="minting-section">
            <h2>Mint Your Buildoor</h2>
            <button id="mint-button">Mint Buildoor</button>
            <p id="mint-status"></p>
        </div>
        
        <div id="earnings-section">
            <h2>Your Earnings</h2>
            <p id="bld-amount">Earned $BLD: 0</p>
        </div>
        
        <div id="level-section">
            <h2>Your Level Progression</h2>
            <p id="level-info">Current Level: 1</p>
        </div>
    </div>

    <script>
        // Initialize Web3 and contract details
        let web3;
        const contractAddress = '0xYourContractAddress'; // Replace with actual contract address
        const contractABI = []; // Replace with actual contract ABI

        // Main function to initialize the application
        async function init() {
            // Check if the browser is Ethereum-enabled
            if (typeof window.ethereum !== 'undefined') {
                web3 = new Web3(window.ethereum);
                try {
                    // Request account access if needed
                    await window.ethereum.request({ method: 'eth_requestAccounts' });
                    console.log('Ethereum account connected.');
                } catch (error) {
                    console.error('User denied account access', error);
                    document.getElementById('mint-status').innerText = 'Error: User denied account access.';
                }

                // Call functions to retrieve user earnings and level
                updateEarnings();
                updateLevel();
            } else {
                console.error('Ethereum browser extension not detected.');
                document.getElementById('mint-status').innerText = 'Error: Please install MetaMask or another Ethereum wallet.';
            }
        }

        // Function to mint a Buildoor
        async function mintBuildoor() {
            const contract = new web3.eth.Contract(contractABI, contractAddress);
            const accounts = await web3.eth.getAccounts();
            const account = accounts[0];

            try {
                const transaction = await contract.methods.mintBuildoor().send({ from: account });
                document.getElementById('mint-status').innerText = 'Mint successful! Transaction: ' + transaction.transactionHash;
                updateEarnings(); // Update earnings after minting
            } catch (error) {
                console.error('Minting failed', error);
                document.getElementById('mint-status').innerText = 'Error: Minting failed. Check console for details.';
            }
        }

        // Function to update user's earnings
        async function updateEarnings() {
            const contract = new web3.eth.Contract(contractABI, contractAddress);
            const accounts = await web3.eth.getAccounts();
            const account = accounts[0];

            try {
                const earnings = await contract.methods.getEarnings(account).call();
                document.getElementById('bld-amount').innerText = 'Earned $BLD: ' + earnings;
            } catch (error) {
                console.error('Failed to fetch earnings', error);
                document.getElementById('bld-amount').innerText = 'Error: Failed to fetch earnings.';
            }
        }

        // Function to update user's level
        async function updateLevel() {
            const contract = new web3.eth.Contract(contractABI, contractAddress);
            const accounts = await web3.eth.getAccounts();
            const account = accounts[0];

            try {
                const level = await contract.methods.getLevel(account).call();
                document.getElementById('level-info').innerText = 'Current Level: ' + level;
            } catch (error) {
                console.error('Failed to fetch level', error);
                document.getElementById('level-info').innerText = 'Error: Failed to fetch level.';
            }
        }

        // Event listener for mint button
        document.getElementById('mint-button').addEventListener('click', mintBuildoor);

        // Initialize the application on window load
        window.onload = init;
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset and body styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f0f0f0;
}

/* Center the application title */
#app {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Heading styles */
h1, h2 {
    color: #333;
}

/* Button styles */
button {
    padding: 10px 20px;
    background-color: #4CAF50; /* Green */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #45a049; /* Darker green */
}

/* Status message styles */
#mint-status, #bld-amount, #level-info {
    margin-top: 10px;
    color: #555;
}
```
