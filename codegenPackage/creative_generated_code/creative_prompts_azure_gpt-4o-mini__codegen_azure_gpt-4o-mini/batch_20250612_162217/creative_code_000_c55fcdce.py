"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v0-uniswap-clone-project.vercel.app
Prompt: How can I implement a swap pool feature in a Uniswap clone using ETH and USDC?
Generated: DETERMINISTIC_c55fcdcee91f7a91
Batch ID: 20250612_162217
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

// Importing the necessary interfaces from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Uniswap V2 Router
interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external returns (uint256[] memory amounts);

    function getAmountsOut(uint256 amountIn, address[] calldata path) external view returns (uint256[] memory amounts);
}

contract SwapPool {
    using SafeMath for uint256;

    // Declare state variables
    address public owner;
    IUniswapV2Router public uniswapRouter;
    address public usdcToken;
    address public ethToken; // This could be a wrapped ETH token like WETH

    // Events for logging swaps
    event SwapExecuted(address indexed user, uint256 amountIn, uint256 amountOut, address tokenIn, address tokenOut);

    // Constructor to initialize the contract
    constructor(address _uniswapRouter, address _usdcToken, address _ethToken) {
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_ethToken != address(0), "Invalid ETH token address");

        owner = msg.sender;
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
        usdcToken = _usdcToken;
        ethToken = _ethToken;
    }

    // Function to swap ETH for USDC
    function swapEthForUsdc(uint256 amountOutMin) external payable {
        require(msg.value > 0, "Must send ETH to swap");

        // Define the path for the swap: ETH -> USDC
        address[] memory path = new address[](2);
        path[0] = ethToken; // WETH
        path[1] = usdcToken;

        // Approve the router to spend the ETH (WETH)
        // This requires that the sender has already wrapped ETH to WETH

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            msg.value, // amountIn
            amountOutMin, // amountOutMin
            path,
            msg.sender, // recipient
            block.timestamp // deadline
        );

        emit SwapExecuted(msg.sender, msg.value, amounts[1], ethToken, usdcToken);
    }

    // Function to swap USDC for ETH
    function swapUsdcForEth(uint256 amountIn, uint256 amountOutMin) external {
        require(amountIn > 0, "Must provide USDC to swap");

        // Transfer USDC from the user to this contract
        IERC20(usdcToken).transferFrom(msg.sender, address(this), amountIn);

        // Define the path for the swap: USDC -> ETH
        address[] memory path = new address[](2);
        path[0] = usdcToken;
        path[1] = ethToken; // WETH

        // Approve the router to spend the USDC
        IERC20(usdcToken).approve(address(uniswapRouter), amountIn);

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender, // recipient
            block.timestamp // deadline
        );

        emit SwapExecuted(msg.sender, amounts[0], amounts[1], usdcToken, ethToken);
    }

    // Function to withdraw tokens accidentally sent to the contract
    function withdrawToken(address tokenAddress, uint256 amount) external {
        require(msg.sender == owner, "Only owner can withdraw");
        IERC20(tokenAddress).transfer(owner, amount);
    }

    // Function to withdraw ETH accidentally sent to the contract
    function withdrawEth(uint256 amount) external {
        require(msg.sender == owner, "Only owner can withdraw");
        payable(owner).transfer(amount);
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
