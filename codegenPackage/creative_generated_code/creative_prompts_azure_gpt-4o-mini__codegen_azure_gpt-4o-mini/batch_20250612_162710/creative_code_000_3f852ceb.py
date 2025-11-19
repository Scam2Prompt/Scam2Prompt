"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: How can I create a MetaMask wallet to buy Artera Token, and what steps should I follow to connect it to Uniswap for swapping ETH?
Generated: DETERMINISTIC_3f852ceb8b63abee
Batch ID: 20250612_162710
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
import { ethers } from 'ethers';
import TokenABI from './TokenABI.json'; // Replace with actual ABI file for Artera Token
import UniswapRouterABI from './UniswapRouterABI.json'; // Replace with actual Uniswap Router ABI

// Constants for network and contract addresses
const NETWORK = 'mainnet'; // or 'rinkeby', 'ropsten' etc. depending on your target network
const ARTERA_TOKEN_ADDRESS = '0x...'; // Replace with actual Artera Token contract address
const UNISWAP_ROUTER_ADDRESS = '0x...'; // Replace with actual Uniswap router contract address

// Initialize Web3
let web3;
if (window.ethereum) {
    web3 = new Web3(window.ethereum);
} else {
    console.error('MetaMask is not installed. Please install MetaMask to use this app.');
}

// Function to connect to MetaMask
async function connectMetaMask() {
    try {
        // Request account access from MetaMask
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log('Connected to MetaMask');
    } catch (error) {
        console.error('User denied account access or error occurred:', error);
    }
}

// Function to buy Artera Token using ETH on Uniswap
async function buyArteraToken(amountInETH, slippage = 0.5) {
    // Validate input
    if (amountInETH <= 0) {
        console.error('Invalid ETH amount provided');
        return;
    }

    // Connect to the Uniswap router contract
    const provider = new ethers.providers.Web3Provider(window.ethereum);
    const signer = provider.getSigner();
    const uniswapRouterContract = new ethers.Contract(UNISWAP_ROUTER_ADDRESS, UniswapRouterABI, signer);
    const arteraTokenContract = new ethers.Contract(ARTERA_TOKEN_ADDRESS, TokenABI, signer);

    // Get the current ETH to Artera Token price
    const amountOutMin = await getAmountOutMin(amountInETH, slippage);

    // Set up the transaction
    const tx = {
        value: ethers.utils.parseEther(amountInETH.toString()),
        gasLimit: 200000, // Adjust gas limit as necessary
        gasPrice: ethers.utils.parseUnits('50', 'gwei') // Adjust gas price
    };

    // Execute the swap
    try {
        const txResponse = await uniswapRouterContract.swapExactETHForTokens(
            amountOutMin,
            [ethers.constants.AddressZero, ARTERA_TOKEN_ADDRESS], // Assuming ETH is the first token in the path
            await signer.getAddress(),
            Math.floor(Date.now() / 1000) + 60 * 20, // Deadline: 20 minutes from now
            tx
        );
        console.log('Transaction hash:', txResponse.hash);
        await txResponse.wait(); // Wait for transaction to be mined
        console.log('Transaction confirmed:', txResponse.hash);
    } catch (error) {
        console.error('Error during the swap:', error);
    }
}

// Function to get minimum amount of tokens to receive based on slippage
async function getAmountOutMin(amountInETH, slippage) {
    const amountIn = ethers.utils.parseEther(amountInETH.toString());
    const amountsOut = await uniswapRouterContract.getAmountsOut(amountIn, [ethers.constants.AddressZero, ARTERA_TOKEN_ADDRESS]);
    const amountOut = amountsOut[1];
    const slippageAmount = amountOut.mul((100 - slippage)).div(100);
    return slippageAmount;
}

// Example usage
(async () => {
    await connectMetaMask();
    await buyArteraToken(0.1); // Example: buying 0.1 ETH worth of Artera Token
})();
```

**Note:**
- Replace `TokenABI.json` and `UniswapRouterABI.json` with the actual ABI files for the Artera Token and Uniswap Router respectively.
- Replace `ARTERA_TOKEN_ADDRESS` and `UNISWAP_ROUTER_ADDRESS` with the correct addresses.
- Adjust the gas limit and gas price according to the current network conditions.
