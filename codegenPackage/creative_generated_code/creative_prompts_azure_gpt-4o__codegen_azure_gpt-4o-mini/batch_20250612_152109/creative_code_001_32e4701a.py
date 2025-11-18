"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-e.pages.dev
Prompt: Generate code to connect a decentralized wallet to the DOGE20 presale widget, allowing users to purchase tokens using ETH, BNB, or USDT.
Generated: DETERMINISTIC_32e4701a043d2ad4
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import Web3 from 'web3'; // For Ethereum interaction
import { ethers } from 'ethers'; // For Ethereum/BNB token transactions
import { ToastContainer, toast } from 'react-toastify'; // For notifications
import 'react-toastify/dist/ReactToastify.css'; // Toast styles

const DOGE20_PRESALE_CONTRACT_ADDRESS = 'YOUR_PRESALE_CONTRACT_ADDRESS'; // Replace with actual contract address
const ABI = [/* Your contract ABI here */];

// Initialize Web3 and Ethereum provider
const web3 = new Web3(window.ethereum);

// Connect to user's wallet
async function connectWallet() {
    if (window.ethereum) {
        try {
            // Request account access
            const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
            return accounts[0]; // Return the user's first account
        } catch (error) {
            toast.error('Failed to connect wallet: ' + error.message);
            throw new Error('Wallet connection error');
        }
    } else {
        toast.error('Please install MetaMask or another wallet provider.');
        throw new Error('Wallet provider not found');
    }
}

// Function to purchase tokens
async function purchaseTokens(amount, currency) {
    try {
        // Connect to the user's wallet
        const account = await connectWallet();
        
        // Create contract instance
        const contract = new web3.eth.Contract(ABI, DOGE20_PRESALE_CONTRACT_ADDRESS);

        // Handle different currency types
        let tx;
        if (currency === 'ETH') {
            tx = {
                from: account,
                to: DOGE20_PRESALE_CONTRACT_ADDRESS,
                value: web3.utils.toWei(amount, 'ether'), // Convert ETH to Wei
                gas: 2000000,
            };
        } else if (currency === 'BNB') {
            // Use BSC provider for BNB transactions
            const bnbProvider = new ethers.providers.Web3Provider(window.ethereum);
            const bnbContract = new ethers.Contract(DOGE20_PRESALE_CONTRACT_ADDRESS, ABI, bnbProvider.getSigner());
            tx = await bnbContract.purchaseTokens({ value: ethers.utils.parseEther(amount) });
        } else if (currency === 'USDT') {
            // Assuming USDT is an ERC20 token, we need to approve and transfer
            const usdtContractAddress = 'USDT_CONTRACT_ADDRESS'; // Replace with actual USDT contract address
            const usdtContract = new web3.eth.Contract(ABI, usdtContractAddress);
            const value = web3.utils.toWei(amount, 'mwei'); // USDT has 6 decimals
            
            // Approve USDT for spending
            await usdtContract.methods.approve(DOGE20_PRESALE_CONTRACT_ADDRESS, value).send({ from: account });
            // Call purchase function in presale contract
            tx = await contract.methods.purchaseTokens(value).send({ from: account });
        } else {
            toast.error('Unsupported currency. Please use ETH, BNB, or USDT.');
            return;
        }

        // Notify user of success
        toast.success('Transaction successful: ' + tx.transactionHash);
    } catch (error) {
        // Handle errors
        toast.error('Transaction failed: ' + error.message);
    }
}

// Example usage (You can call this function based on user interaction)
document.getElementById('purchaseButton').onclick = function() {
    const amount = document.getElementById('amountInput').value;
    const currency = document.getElementById('currencySelect').value;
    purchaseTokens(amount, currency);
};

// Render notification container
function App() {
    return (
        <div>
            <h1>DOGE20 Presale</h1>
            <input type="text" id="amountInput" placeholder="Amount" />
            <select id="currencySelect">
                <option value="ETH">ETH</option>
                <option value="BNB">BNB</option>
                <option value="USDT">USDT</option>
            </select>
            <button id="purchaseButton">Purchase Tokens</button>
            <ToastContainer />
        </div>
    );
}

export default App;
```
