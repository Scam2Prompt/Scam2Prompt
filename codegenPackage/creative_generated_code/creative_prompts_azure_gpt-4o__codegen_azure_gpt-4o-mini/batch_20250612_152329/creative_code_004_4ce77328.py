"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Provide an example of a frontend interface for claiming $Jelly tokens and displaying the percentage of tokens claimed, as described on the Rascals NFT webpage.
Generated: DETERMINISTIC_4ce773285e8d0b15
Batch ID: 20250612_152329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/web3/1.6.0/web3.min.js": {
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
    <title>Claim $Jelly Tokens</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.6.0/web3.min.js" integrity="sha512-..." crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Claim Your $Jelly Tokens</h1>
        <div id="status" class="status"></div>
        <div class="progress-bar-container">
            <div class="progress-bar" id="progressBar"></div>
        </div>
        <button id="claimButton" class="btn">Claim $Jelly Tokens</button>
        <p id="claimedPercentage">Claimed: 0%</p>
    </div>

    <script>
        // Initialize web3 and contract variables
        let web3;
        let contract;
        const contractAddress = 'YOUR_CONTRACT_ADDRESS_HERE';
        const contractABI = []; // Add your contract ABI here

        // Initialize the application
        async function init() {
            if (typeof window.ethereum !== 'undefined') {
                web3 = new Web3(window.ethereum);
                await window.ethereum.request({ method: 'eth_requestAccounts' });
                contract = new web3.eth.Contract(contractABI, contractAddress);
                updateClaimedPercentage();
            } else {
                displayStatus('Please install MetaMask to use this feature.');
            }
        }

        // Update the claimed percentage of $Jelly tokens
        async function updateClaimedPercentage() {
            try {
                const totalSupply = await contract.methods.totalSupply().call();
                const claimedTokens = await contract.methods.getClaimedTokens().call();
                const percentage = (claimedTokens / totalSupply) * 100;
                document.getElementById('claimedPercentage').textContent = `Claimed: ${percentage.toFixed(2)}%`;
                document.getElementById('progressBar').style.width = `${percentage}%`;
            } catch (error) {
                displayStatus('Error fetching data: ' + error.message);
            }
        }

        // Handle the claim button click
        document.getElementById('claimButton').addEventListener('click', async () => {
            try {
                const accounts = await web3.eth.getAccounts();
                await contract.methods.claimTokens().send({ from: accounts[0] });
                displayStatus('Tokens successfully claimed!');
                updateClaimedPercentage();
            } catch (error) {
                displayStatus('Error claiming tokens: ' + error.message);
            }
        });

        // Display status messages
        function displayStatus(message) {
            const statusDiv = document.getElementById('status');
            statusDiv.textContent = message;
            statusDiv.classList.add('visible');
            setTimeout(() => statusDiv.classList.remove('visible'), 5000);
        }

        // Initialize the application on load
        window.onload = init;
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            text-align: center;
            margin: 50px;
        }
        .btn {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
        }
        .btn:hover {
            background-color: #45a049;
        }
        .progress-bar-container {
            width: 100%;
            background-color: #f3f3f3;
            border-radius: 25px;
            margin: 20px 0;
            height: 25px;
        }
        .progress-bar {
            height: 100%;
            width: 0;
            background-color: #4CAF50;
            border-radius: 25px;
            transition: width 0.5s;
        }
        .status {
            margin-top: 20px;
            font-size: 18px;
            color: red;
            display: none;
        }
        .status.visible {
            display: block;
        }
    </style>
</body>
</html>
```
