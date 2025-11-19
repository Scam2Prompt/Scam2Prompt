"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://support-metamask-helps.bravesites.com
Prompt: What are the advantages of using MetaMask for managing ETH and ERC-20 tokens in a dApp environment?
Generated: DETERMINISTIC_30d1c239e8346ce6
Batch ID: 20250612_162701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
import Web3 from 'web3';

// Instantiate Web3 with MetaMask's provider
const web3 = new Web3(window.ethereum);

async function connectMetaMask() {
    try {
        // Request account access if needed
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('MetaMask connected');
    } catch (error) {
        console.error('User denied account access or there was an error:', error);
    }
}

async function getETHBalance(address) {
    try {
        // Get balance in Wei
        const balanceWei = await web3.eth.getBalance(address);
        // Convert Wei to Ether
        return web3.utils.fromWei(balanceWei, 'ether');
    } catch (error) {
        console.error('Error fetching ETH balance:', error);
        throw new Error('Could not fetch ETH balance');
    }
}

async function getERC20TokenBalance(tokenAddress, walletAddress) {
    try {
        // ERC20 Token ABI for balanceOf function
        const tokenABI = [
            {
                "constant": true,
                "inputs": [{ "name": "_owner", "type": "address" }],
                "name": "balanceOf",
                "outputs": [{ "name": "balance", "type": "uint256" }],
                "payable": false,
                "stateMutability": "view",
                "type": "function"
            }
        ];

        // Create contract instance
        const tokenContract = new web3.eth.Contract(tokenABI, tokenAddress);
        // Fetch balance
        const balance = await tokenContract.methods.balanceOf(walletAddress).call();
        // Convert balance to a readable format
        return web3.utils.fromWei(balance, 'ether');
    } catch (error) {
        console.error('Error fetching ERC-20 token balance:', error);
        throw new Error('Could not fetch ERC-20 token balance');
    }
}

// Example usage
(async () => {
    await connectMetaMask();

    const userAddress = (await web3.eth.getAccounts())[0]; // Get connected user's address
    console.log(`Connected Address: ${userAddress}`);

    const ethBalance = await getETHBalance(userAddress);
    console.log(`ETH Balance: ${ethBalance} ETH`);

    const tokenAddress = '0xYourTokenAddressHere'; // Replace with actual token address
    const erc20Balance = await getERC20TokenBalance(tokenAddress, userAddress);
    console.log(`ERC-20 Token Balance: ${erc20Balance} Tokens`);
})();
```
