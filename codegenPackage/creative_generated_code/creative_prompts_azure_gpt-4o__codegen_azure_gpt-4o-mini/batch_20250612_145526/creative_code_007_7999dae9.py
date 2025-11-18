"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://catcoinhq.com
Prompt: Develop a smart contract in Solidity to enable users to swap Catcoin ($CAT) for Ethereum (ETH) or Binance Coin (BNB) directly on-chain.
Generated: DETERMINISTIC_7999dae96925ec98
Batch ID: 20250612_145526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function swapExactTokensForETH(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);

    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

// Smart contract for the Catcoin swap
contract CatcoinSwap {
    // Address of the Catcoin token
    address public catcoinAddress;
    // Instance of the Uniswap router
    IUniswapV2Router public uniswapRouter;

    // Event emitted on successful swap
    event SwapExecuted(address indexed user, uint amountIn, address indexed tokenOut, uint amountOut);

    // Constructor to initialize the contract with Catcoin address and Uniswap router
    constructor(address _catcoinAddress, address _uniswapRouter) {
        catcoinAddress = _catcoinAddress;
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
    }

    // Function to swap Catcoin for ETH
    function swapCatcoinForETH(uint amountIn, uint amountOutMin, uint deadline) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");
        
        // Transfer Catcoin from user to this contract
        IERC20(catcoinAddress).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend Catcoin
        IERC20(catcoinAddress).approve(address(uniswapRouter), amountIn);

        // Path for swap (Catcoin -> WETH -> ETH)
        address[] memory path = new address[](2);
        path[0] = catcoinAddress;
        path[1] = uniswapRouter.WETH();

        // Execute the swap
        uniswapRouter.swapExactTokensForETH(amountIn, amountOutMin, path, msg.sender, deadline);

        // Emit event
        emit SwapExecuted(msg.sender, amountIn, address(0), amountOutMin);
    }

    // Function to swap Catcoin for BNB
    function swapCatcoinForBNB(uint amountIn, uint amountOutMin, uint deadline) external {
        require(amountIn > 0, "Amount must be greater than 0");
        require(deadline >= block.timestamp, "Deadline has passed");
        
        // Transfer Catcoin from user to this contract
        IERC20(catcoinAddress).transferFrom(msg.sender, address(this), amountIn);

        // Approve the Uniswap router to spend Catcoin
        IERC20(catcoinAddress).approve(address(uniswapRouter), amountIn);

        // Path for swap (Catcoin -> BNB)
        address[] memory path = new address[](2);
        path[0] = catcoinAddress;
        path[1] = address(0); // Assuming the address for BNB is known

        // Execute the swap
        uniswapRouter.swapExactTokensForTokens(amountIn, amountOutMin, path, msg.sender, deadline);

        // Emit event
        emit SwapExecuted(msg.sender, amountIn, address(0), amountOutMin);
    }
}
```

Make sure to replace the placeholder for the Binance Coin (BNB) address in the path with the actual contract address if needed, as the BNB address differs between networks.
