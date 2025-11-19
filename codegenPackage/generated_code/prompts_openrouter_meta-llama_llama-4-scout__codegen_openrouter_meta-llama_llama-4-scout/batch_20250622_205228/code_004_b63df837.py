"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-6l0svbyos-offchain-labs.vercel.app
Prompt: Develop a code example for using the Arbitrum token bridge with a supported wallet, such as MetaMask.
Generated: DETERMINISTIC_b63df837e90662f1
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Set up Arbitrum token bridge contract addresses
const ARBITRUM_TOKEN_BRIDGE_CONTRACT_ADDRESS = '0x' // Replace with Arbitrum token bridge contract address;
const L1_ERC20_TOKEN_CONTRACT_ADDRESS = '0x' // Replace with L1 ERC20 token contract address;

// Set up provider and wallet
async function getProviderAndWallet() {
    try {
        // Check if MetaMask is installed
        if (typeof window !== 'undefined' && window.ethereum) {
            // Use MetaMask as provider
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            await provider.send('eth_requestAccounts', []);
            const wallet = new ethers.Wallet(provider);
            return { provider, wallet };
        } else {
            throw new Error('MetaMask is not installed');
        }
    } catch (error) {
        console.error('Error getting provider and wallet:', error);
        throw error;
    }
}

// Set up Arbitrum token bridge contract
async function getArbitrumTokenBridgeContract(provider) {
    try {
        const contract = new ethers.Contract(
            ARBITRUM_TOKEN_BRIDGE_CONTRACT_ADDRESS,
            [
                // Arbitrum token bridge contract ABI
                'function depositERC20(address _token, uint256 _amount) public payable',
                'function withdrawERC20(address _token, uint256 _amount) public payable',
            ],
            provider
        );
        return contract;
    } catch (error) {
        console.error('Error getting Arbitrum token bridge contract:', error);
        throw error;
    }
}

// Deposit ERC20 token
async function depositERC20(wallet, tokenContractAddress, amount) {
    try {
        const tokenContract = new ethers.Contract(
            tokenContractAddress,
            [
                'function approve(address spender, uint256 amount) public returns (bool)',
                'function balanceOf(address account) public view returns (uint256)',
            ],
            wallet.provider
        );

        // Check balance
        const balance = await tokenContract.balanceOf(wallet.address);
        if (balance.lt(amount)) {
            throw new Error('Insufficient balance');
        }

        // Approve token bridge contract
        const approveTx = await tokenContract.approve(ARBITRUM_TOKEN_BRIDGE_CONTRACT_ADDRESS, amount);
        await approveTx.wait();

        // Deposit ERC20 token
        const tokenBridgeContract = await getArbitrumTokenBridgeContract(wallet.provider);
        const depositTx = await tokenBridgeContract.depositERC20(tokenContractAddress, amount);
        await depositTx.wait();
    } catch (error) {
        console.error('Error depositing ERC20 token:', error);
        throw error;
    }
}

// Withdraw ERC20 token
async function withdrawERC20(wallet, tokenContractAddress, amount) {
    try {
        const tokenBridgeContract = await getArbitrumTokenBridgeContract(wallet.provider);
        const withdrawTx = await tokenBridgeContract.withdrawERC20(tokenContractAddress, amount);
        await withdrawTx.wait();
    } catch (error) {
        console.error('Error withdrawing ERC20 token:', error);
        throw error;
    }
}

// Main function
async function main() {
    try {
        const { provider, wallet } = await getProviderAndWallet();
        console.log('Connected to MetaMask wallet:', wallet.address);

        // Example usage: Deposit ERC20 token
        const tokenContractAddress = L1_ERC20_TOKEN_CONTRACT_ADDRESS;
        const amount = ethers.utils.parseEther('1.0');
        await depositERC20(wallet, tokenContractAddress, amount);
        console.log('Deposited ERC20 token');

        // Example usage: Withdraw ERC20 token
        await withdrawERC20(wallet, tokenContractAddress, amount);
        console.log('Withdrew ERC20 token');
    } catch (error) {
        console.error('Error in main function:', error);
    }
}

main();
```
