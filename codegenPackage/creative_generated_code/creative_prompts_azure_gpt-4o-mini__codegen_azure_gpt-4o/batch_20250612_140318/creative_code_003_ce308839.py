"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appi-uniswap.info
Prompt: Provide an example of how to execute a swap on Uniswap using JavaScript and its SDK.
Generated: DETERMINISTIC_ce30883934388be7
Batch ID: 20250612_140318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies from Uniswap SDK and ethers.js
const { Token, TokenAmount, Pair, Trade, Route, TradeType, Fetcher, Percent } = require('@uniswap/sdk');
const { ethers } = require('ethers');

// Define async function to perform token swap
async function swapTokens() {
  try {
    // Define the network and provider
    const chainId = 1; // Mainnet
    const provider = new ethers.providers.InfuraProvider(chainId, 'YOUR_INFURA_PROJECT_ID');

    // Define the token details (example: swapping WETH to DAI)
    const WETH = new Token(chainId, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', 18, 'WETH', 'Wrapped Ether');
    const DAI = new Token(chainId, '0x6B175474E89094C44Da98b954EedeAC495271d0F', 18, 'DAI', 'Dai Stablecoin');

    // Fetch the pair data from Uniswap
    const pair = await Fetcher.fetchPairData(WETH, DAI, provider);

    // Create a route for the trade
    const route = new Route([pair], WETH);

    // Define the amount to trade (example: 0.1 WETH to DAI)
    const amountIn = ethers.utils.parseUnits('0.1', WETH.decimals);
    const trade = new Trade(route, new TokenAmount(WETH, amountIn.toString()), TradeType.EXACT_INPUT);

    // Define slippage tolerance (example: 0.5%)
    const slippageTolerance = new Percent('50', '10000'); // 0.5%

    // Calculate the minimum amount out
    const amountOutMin = trade.minimumAmountOut(slippageTolerance).raw;

    // Define the recipient of swapped tokens
    const recipient = 'YOUR_WALLET_ADDRESS';

    // Define the deadline for the trade (example: 20 minutes from now)
    const deadline = Math.floor(Date.now() / 1000) + 60 * 20;

    // Create the Uniswap Router contract instance
    const uniswapRouterAddress = '0xE592427A0AEce92De3Edee1F18E0157C05861564'; // Uniswap V3 Router
    const uniswapRouterABI = [
      'function swapExactTokensForTokens(uint amountIn, uint amountOutMin, address[] calldata path, address to, uint deadline) external returns (uint[] memory amounts',
    ];
    const router = new ethers.Contract(uniswapRouterAddress, uniswapRouterABI, provider);

    // Approve the router to spend WETH tokens
    const signer = provider.getSigner();
    const wethContract = new ethers.Contract(WETH.address, ['function approve(address spender, uint amount) external returns (bool)'], signer);
    await wethContract.approve(uniswapRouterAddress, amountIn);

    // Execute the swap
    const path = [WETH.address, DAI.address];
    const tx = await router.swapExactTokensForTokens(
      amountIn,
      amountOutMin.toString(),
      path,
      recipient,
      deadline,
      { gasLimit: ethers.utils.hexlify(1000000) } // Provide adequate gas limit
    );

    // Wait for the transaction to be confirmed
    const receipt = await tx.wait();
    console.log('Swap executed successfully:', receipt);
  } catch (error) {
    console.error('Error executing swap:', error);
  }
}

// Call the swapTokens function
swapTokens();
```

> Note: Replace `YOUR_INFURA_PROJECT_ID` and `YOUR_WALLET_ADDRESS` with actual values. Always ensure token approvals and network configurations are correct.
