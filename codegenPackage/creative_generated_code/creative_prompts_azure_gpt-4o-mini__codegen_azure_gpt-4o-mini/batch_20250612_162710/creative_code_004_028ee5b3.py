"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.arteratoken.lucaageadesign.com
Prompt: Describe the process of swapping ETH for Artera Token on Uniswap, including any specific settings or configurations needed in MetaMask.
Generated: DETERMINISTIC_028ee5b3aef29ae3
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
import { Token, ChainId, TokenAmount, Pair, Route, Trade, TradeType, Fetcher, Percent } from '@uniswap/sdk';

// Initialize Web3 instance
const web3 = new Web3(window.ethereum);

// MetaMask integration to request account access
async function connectMetaMask() {
    if (window.ethereum) {
        try {
            // Request account access
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            console.log('MetaMask connected');
        } catch (error) {
            // Handle error if user denies access
            console.error('User denied account access', error);
        }
    } else {
        console.error('MetaMask is not installed');
    }
}

// Function to swap ETH for Artera Token on Uniswap
async function swapETHForArteraToken(amountInEth, arteraTokenAddress) {
    try {
        // Get the user's address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];

        // Initialize provider and wallet
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();

        // Fetch the ETH and Artera Token details
        const ethToken = new Token(ChainId.MAINNET, ethers.constants.AddressZero, 18);
        const arteraToken = new Token(ChainId.MAINNET, arteraTokenAddress, 18);

        // Fetch pair and route for the swap
        const pair = await Fetcher.fetchPairData(ethToken, arteraToken);
        const route = new Route([pair], ethToken);
        
        // Create a trade object and calculate slippage
        const trade = new Trade(route, new TokenAmount(ethToken, ethers.utils.parseUnits(amountInEth.toString(), 18)), TradeType.EXACT_INPUT);
        const slippageTolerance = new Percent('50', '10000'); // 0.50%
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).toFixed();

        // Prepare the transaction
        const tx = {
            from: userAddress,
            to: pair.liquidityToken.address,
            value: ethers.utils.parseEther(amountInEth.toString()),
            gas: 2000000,
            data: trade.swapCallParameters({ slippageTolerance, recipient: userAddress, deadline: Math.floor(Date.now() / 1000) + 60 * 20 }).data,
        };

        // Send the transaction
        const txResponse = await signer.sendTransaction(tx);
        console.log('Transaction Response:', txResponse);
        
        // Wait for the transaction to be confirmed
        await txResponse.wait();
        console.log('Transaction confirmed:', txResponse.hash);
        
    } catch (error) {
        // Handle errors during the swap process
        console.error('Error swapping ETH for Artera Token:', error);
    }
}

// Usage example
(async () => {
    await connectMetaMask();
    const amountInEth = 0.1; // Amount of ETH to swap
    const arteraTokenAddress = '0xYourArteraTokenAddressHere'; // Replace with the actual Artera Token address
    await swapETHForArteraToken(amountInEth, arteraTokenAddress);
})();
```
