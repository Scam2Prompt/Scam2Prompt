"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-erc20.vip
Prompt: Create a JavaScript snippet to check if JavaScript is enabled in the browser before initializing a DeFi ERC-20 token interface.
Generated: DETERMINISTIC_aafdf6c44878c0dc
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Check if JavaScript is enabled by setting a variable in the body
document.documentElement.className = "js-enabled"; // Add a class to indicate JS is enabled

// Function to initialize the DeFi ERC-20 token interface
function initializeDeFiTokenInterface() {
    try {
        // Assuming web3 is included and available globally
        if (typeof window.ethereum === 'undefined') {
            throw new Error('Ethereum provider not found. Please install MetaMask or another web3 wallet.');
        }

        // Initialize web3
        const web3 = new Web3(window.ethereum);

        // Request account access if needed
        window.ethereum.request({ method: 'eth_requestAccounts' })
            .then(accounts => {
                console.log('Connected account:', accounts[0]);
                // You can initialize your ERC-20 token interface here
                // For example, create a contract instance:
                const contractAddress = 'YOUR_CONTRACT_ADDRESS';
                const abi = []; // Replace with your contract's ABI
                const contract = new web3.eth.Contract(abi, contractAddress);

                // Example function call on the contract
                contract.methods.totalSupply().call()
                    .then(supply => {
                        console.log('Total Supply:', supply);
                    })
                    .catch(error => {
                        console.error('Error calling totalSupply:', error);
                    });
            })
            .catch(error => {
                console.error('User denied account access or error occurred:', error);
            });
    } catch (error) {
        console.error('Error initializing DeFi token interface:', error);
    }
}

// Document ready event to check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', () => {
    if (document.documentElement.classList.contains('js-enabled')) {
        initializeDeFiTokenInterface();
    } else {
        console.warn('JavaScript is not enabled!');
    }
});
```
