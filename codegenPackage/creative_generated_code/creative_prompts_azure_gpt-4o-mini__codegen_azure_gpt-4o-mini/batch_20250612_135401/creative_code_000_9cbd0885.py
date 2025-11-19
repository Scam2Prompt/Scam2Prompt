"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-lupqrbm0k-uniswap.vercel.app
Prompt: How can I enable JavaScript to use the Uniswap interface effectively?
Generated: DETERMINISTIC_9cbd088515e42773
Batch ID: 20250612_135401
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
import { ChainId, Token, Fetcher, Route, Trade, TokenAmount, TradeType, Percent } from '@uniswap/sdk';

// Initialize Web3
const web3 = new Web3(window.ethereum);

// Request account access if needed
async function enableEthereum() {
    try {
        // Request access to the user's Ethereum account
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        console.log("Ethereum enabled");
    } catch (error) {
        console.error("User denied account access or error occurred:", error);
    }
}

// Function to fetch token details and create a trade route
async function getTradeDetails(tokenAddress, amountIn, slippage = 0.5) {
    try {
        // Define the token (Example: DAI)
        const token = await Fetcher.fetchTokenData(ChainId.MAINNET, tokenAddress);

        // Fetch the pair data
        const pair = await Fetcher.fetchPairData(token, WETH[ChainId.MAINNET]);

        // Create a route for the trade
        const route = new Route([pair], WETH[ChainId.MAINNET]);

        // Create a trade based on the input amount
        const trade = new Trade(route, new TokenAmount(token, amountIn), TradeType.EXACT_INPUT);

        // Calculate the slippage tolerance
        const slippageTolerance = new Percent(slippage.toString(), '100');

        // Prepare the trade parameters
        const amountOutMin = trade.minimumAmountOut(slippageTolerance).toFixed();
        const path = [token.address, WETH[ChainId.MAINNET].address];
        const to = await web3.eth.getAccounts()[0]; // Use the first account
        const deadline = Math.floor(Date.now() / 1000) + 60 * 20; // 20 minutes from the current time

        return { amountOutMin, path, to, deadline };
    } catch (error) {
        console.error("Error fetching trade details:", error);
    }
}

// Function to execute the trade
async function executeTrade(tokenAddress, amountIn) {
    try {
        const { amountOutMin, path, to, deadline } = await getTradeDetails(tokenAddress, amountIn);

        // Construct the transaction parameters
        const transactionParameters = {
            to: UNISWAP_ROUTER_ADDRESS, // Replace with Uniswap Router address
            from: to,
            data: web3.eth.abi.encodeFunctionCall({
                name: 'swapExactTokensForETH',
                type: 'function',
                inputs: [
                    { type: 'uint256', name: 'amountIn' },
                    { type: 'uint256', name: 'amountOutMin' },
                    { type: 'address[]', name: 'path' },
                    { type: 'address', name: 'to' },
                    { type: 'uint256', name: 'deadline' }
                ]
            }, [amountIn, amountOutMin, path, to, deadline]),
            gas: '200000',
        };

        // Send the transaction
        const txHash = await web3.eth.sendTransaction(transactionParameters);
        console.log("Transaction successful with hash:", txHash);
    } catch (error) {
        console.error("Error executing the trade:", error);
    }
}

// Example usage
(async () => {
    await enableEthereum();
    const tokenAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F'; // DAI example address
    const amountIn = web3.utils.toWei('1', 'ether'); // Amount of DAI to swap
    await executeTrade(tokenAddress, amountIn);
})();
```

**Note:** Replace `UNISWAP_ROUTER_ADDRESS` with the actual address of the Uniswap Router on the desired network. Ensure that the user has sufficient tokens and ETH for the transaction.
