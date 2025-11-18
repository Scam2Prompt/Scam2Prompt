"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mestken.top
Prompt: Create a smart contract example that interacts with MetaMask for token transactions, ensuring the user retains control over their private keys.
Generated: DETERMINISTIC_4d4178737428cdf6
Batch ID: 20250612_153854
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

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A simple ERC20 token contract that allows minting and transferring of tokens
contract MyToken is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }

    // Function to mint new tokens, can only be called by the owner
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MetaMask Token Interaction</title>
    <script src="https://cdn.jsdelivr.net/npm/web3/dist/web3.min.js"></script>
</head>
<body>
    <h1>Interact with MyToken</h1>
    <button id="connectButton">Connect MetaMask</button>
    <button id="sendButton" disabled>Send Tokens</button>

    <script>
        const tokenContractAddress = 'YOUR_CONTRACT_ADDRESS_HERE'; // Replace with deployed contract address
        const tokenABI = [ /* ABI goes here */ ];

        let web3;
        let accounts;
        let tokenContract;

        // Connect to MetaMask and initialize web3
        async function connectMetaMask() {
            if (window.ethereum) {
                web3 = new Web3(window.ethereum);
                try {
                    // Request account access
                    accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
                    document.getElementById('sendButton').disabled = false;
                    console.log('Connected:', accounts[0]);
                } catch (error) {
                    console.error("User denied account access");
                }
            } else {
                alert("Please install MetaMask!");
            }
        }

        // Function to send tokens
        async function sendTokens() {
            const amount = web3.utils.toWei('1', 'ether'); // Amount to send (1 token)

            tokenContract = new web3.eth.Contract(tokenABI, tokenContractAddress);
            try {
                const receipt = await tokenContract.methods.transfer('RECIPIENT_ADDRESS_HERE', amount)
                    .send({ from: accounts[0] });
                console.log('Transaction successful', receipt);
            } catch (error) {
                console.error('Transaction failed', error);
            }
        }

        // Event listeners for buttons
        document.getElementById('connectButton').addEventListener('click', connectMetaMask);
        document.getElementById('sendButton').addEventListener('click', sendTokens);
    </script>
</body>
</html>
```

Make sure to replace `YOUR_CONTRACT_ADDRESS_HERE` with the actual deployed contract address and provide the ABI in the `tokenABI` variable. Also, replace `'RECIPIENT_ADDRESS_HERE'` with the actual recipient's address.
