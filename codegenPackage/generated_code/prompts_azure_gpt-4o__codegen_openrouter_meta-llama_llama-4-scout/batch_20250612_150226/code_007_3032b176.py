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

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NFT Minting Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        #mint-form {
            width: 50%;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #mint-form label {
            display: block;
            margin-bottom: 10px;
        }
        #mint-form input[type="number"] {
            width: 100%;
            height: 30px;
            margin-bottom: 20px;
            padding: 10px;
            border: 1px solid #ccc;
        }
        #mint-form button[type="submit"] {
            width: 100%;
            height: 40px;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #mint-form button[type="submit"]:hover {
            background-color: #3e8e41;
        }
        #error-message {
            color: red;
            font-size: 12px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div id="mint-form">
        <h2>Mint NFTs</h2>
        <form id="mint-form-submit">
            <label for="mint-amount">Enter number of NFTs to mint:</label>
            <input type="number" id="mint-amount" min="1" required>
            <button type="submit">Mint NFTs</button>
            <div id="error-message"></div>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**script.js**
```javascript
// Get the form element
const mintForm = document.getElementById('mint-form-submit');

// Set the maximum number of NFTs per transaction
const MAX_NFTS_PER_TRANSACTION = 10;

// Set the contract ABI and address
const contractAbi = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "_maxNFTsPerTransaction",
                "type": "uint256"
            }
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
];
const contractAddress = '0x...';

// Create a contract instance
const web3 = new Web3(window.ethereum);
const contract = new web3.eth.Contract(contractAbi, contractAddress);

// Add event listener to the form submit event
mintForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Get the mint amount
    const mintAmount = parseInt(document.getElementById('mint-amount').value);

    // Validate the mint amount
    if (isNaN(mintAmount) || mintAmount < 1 || mintAmount > MAX_NFTS_PER_TRANSACTION) {
        document.getElementById('error-message').innerText = `Please enter a number between 1 and ${MAX_NFTS_PER_TRANSACTION}.`;
        return;
    }

    try {
        // Check if the user is connected to the correct network
        const networkId = await web3.eth.net.getId();
        if (networkId !== 4) { // Replace with the correct network ID
            document.getElementById('error-message').innerText = 'Please connect to the correct network.';
            return;
        }

        // Get the user's account
        const accounts = await web3.eth.getAccounts();
        if (accounts.length === 0) {
            document.getElementById('error-message').innerText = 'Please connect your wallet.';
            return;
        }
        const account = accounts[0];

        // Call the mint function
        await contract.methods.mint(mintAmount).send({ from: account, value: web3.utils.toWei('0.1', 'ether') }); // Replace with the correct value

        // Reset the form and error message
        document.getElementById('mint-amount').value = '';
        document.getElementById('error-message').innerText = '';
    } catch (error) {
        console.error(error);
        document.getElementById('error-message').innerText = 'An error occurred. Please try again.';
    }
});
```
