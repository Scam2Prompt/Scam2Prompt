"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone.cx
Prompt: Provide code to integrate a wallet connection feature into a website, allowing users to buy $INIT tokens using BNB or ETH and automatically receive refunds if the pre-sale hard cap is reached.
Generated: DETERMINISTIC_a9a5f6c342903de1
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3';

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Contract addresses and ABIs
const initTokenAddress = '0xYourInitTokenAddress';
const presaleContractAddress = '0xYourPresaleContractAddress';

// ABI for the Presale contract
const presaleABI = [
    // Add the ABI of the presale contract here
];

// ABI for the $INIT Token contract
const initTokenABI = [
    // Add the ABI of the $INIT token contract here
];

// Create contract instances
const presaleContract = new web3.eth.Contract(presaleABI, presaleContractAddress);
const initTokenContract = new web3.eth.Contract(initTokenABI, initTokenAddress);

// Connect wallet function
async function connectWallet() {
    try {
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        const userAddress = accounts[0];
        console.log('Connected:', userAddress);
        return userAddress;
    } catch (error) {
        console.error('Wallet connection failed:', error);
        alert('Could not connect to wallet. Please try again.');
    }
}

// Buy tokens function
async function buyTokens(amount, currency) {
    try {
        const userAddress = await connectWallet();
        let tx;

        if (currency === 'BNB') {
            tx = await presaleContract.methods.buyWithBNB().send({
                from: userAddress,
                value: web3.utils.toWei(amount, 'ether'),
                gas: 200000 // set appropriate gas limit
            });
        } else if (currency === 'ETH') {
            tx = await presaleContract.methods.buyWithETH().send({
                from: userAddress,
                value: web3.utils.toWei(amount, 'ether'),
                gas: 200000 // set appropriate gas limit
            });
        } else {
            throw new Error('Invalid currency selected.');
        }

        console.log('Transaction successful:', tx);
        alert('Tokens purchased successfully.');

    } catch (error) {
        console.error('Transaction failed:', error);
        alert('Transaction failed. Please check the console for more details.');
    }
}

// Refund function
async function checkRefunds(userAddress) {
    try {
        const presaleCapReached = await presaleContract.methods.isHardCapReached().call();

        if (presaleCapReached) {
            const refundAmount = await presaleContract.methods.getRefundAmount(userAddress).call();
            if (refundAmount > 0) {
                const refundTx = await presaleContract.methods.refund().send({ from: userAddress });
                console.log('Refund transaction successful:', refundTx);
                alert('Refund processed successfully.');
            } else {
                alert('No refund available for this address.');
            }
        }
    } catch (error) {
        console.error('Refund check failed:', error);
        alert('Failed to check for refunds. Please try again.');
    }
}

// Event listener for the Buy button
document.getElementById('buy-button').addEventListener('click', () => {
    const amount = document.getElementById('amount-input').value;
    const currency = document.querySelector('input[name="currency"]:checked').value; // Assuming radio buttons for currency selection
    buyTokens(amount, currency);
});

// Event listener for checking refunds
document.getElementById('refund-button').addEventListener('click', async () => {
    const userAddress = await connectWallet();
    await checkRefunds(userAddress);
});
```

### Notes:
1. Replace placeholder addresses (`0xYourInitTokenAddress`, `0xYourPresaleContractAddress`) and ABI arrays with actual contract addresses and ABI definitions.
2. Ensure the HTML contains elements with IDs `buy-button`, `amount-input`, and `refund-button` for the code to work correctly.
3. Adjust gas limits according to your contract's requirements.
4. This code assumes the use of MetaMask or a similar wallet that injects the `ethereum` object into the browser context.
