"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://botcodesrc.pages.dev
Prompt: Write a Solidity contract that uses the `receive()` function to accept Ether payments and integrates with Uniswap for liquidity operations, as described in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_d9f2f360cb381277
Batch ID: 20250612_151343
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

// Import necessary Uniswap interfaces
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract EtherLiquidityManager {
    // State variables
    address public owner;
    IUniswapV2Router02 public uniswapRouter;
    address public WETH; // Wrapped Ether token address

    // Events
    event ReceivedEther(address indexed sender, uint256 amount);
    event LiquidityAdded(uint256 tokenAmount, uint256 etherAmount);
    event LiquidityRemoved(uint256 liquidity, uint256 tokenAmount, uint256 etherAmount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Constructor to set the Uniswap router address and owner
    constructor(address _uniswapRouterAddress) {
        require(_uniswapRouterAddress != address(0), "Invalid Uniswap router address");
        owner = msg.sender;
        uniswapRouter = IUniswapV2Router02(_uniswapRouterAddress);
        WETH = uniswapRouter.WETH();
    }

    // receive() function to accept Ether payments
    receive() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }

    // Function to provide liquidity to a Uniswap pair (token paired with WETH)
    function addLiquidity(address token, uint256 tokenAmount) external payable onlyOwner {
        require(token != address(0), "Invalid token address");
        require(msg.value > 0, "Ether amount must be greater than zero");

        // Approve Uniswap router to spend the token
        IERC20(token).approve(address(uniswapRouter), tokenAmount);

        // Add liquidity
        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = uniswapRouter.addLiquidityETH{value: msg.value}(
            token,
            tokenAmount,
            0, // Minimum amount of tokens
            0, // Minimum amount of ETH
            owner, // Recipient of the liquidity tokens
            block.timestamp // Deadline for the transaction
        );

        emit LiquidityAdded(amountToken, amountETH);
    }

    // Function to remove liquidity from a Uniswap pair (token paired with WETH)
    function removeLiquidity(address token, uint256 liquidity) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(liquidity > 0, "Liquidity amount must be greater than zero");

        address pair = IUniswapV2Factory(uniswapRouter.factory()).getPair(token, WETH);
        require(pair != address(0), "Pair does not exist");

        // Approve Uniswap router to spend liquidity tokens
        IERC20(pair).approve(address(uniswapRouter), liquidity);

        // Remove liquidity
        (uint256 amountToken, uint256 amountETH) = uniswapRouter.removeLiquidityETH(
            token,
            liquidity,
            0, // Minimum amount of tokens
            0, // Minimum amount of ETH
            owner, // Recipient of the withdrawn tokens and ETH
            block.timestamp // Deadline for the transaction
        );

        emit LiquidityRemoved(liquidity, amountToken, amountETH);
    }

    // Function to withdraw Ether from the contract
    function withdrawEther(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = owner.call{value: amount}("");
        require(success, "Ether withdrawal failed");
    }

    // Function to withdraw ERC20 tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient token balance");
        IERC20(token).transfer(owner, amount);
    }

    // Function to update the Uniswap router address
    function updateUniswapRouter(address _uniswapRouterAddress) external onlyOwner {
        require(_uniswapRouterAddress != address(0), "Invalid Uniswap router address");
        uniswapRouter = IUniswapV2Router02(_uniswapRouterAddress);
        WETH = uniswapRouter.WETH();
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
