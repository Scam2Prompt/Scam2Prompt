"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.web.app
Prompt: Write a guide for deploying the DOGE20 liquidity pool on Uniswap, ensuring the allocation of 10% of the total token supply as described on the website.
Generated: DETERMINISTIC_4ffae1b3eee7e4cf
Batch ID: 20250612_152620
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

/**
 * @title DOGE20 Liquidity Pool Deployment
 * @dev This contract deploys a liquidity pool on Uniswap and allocates 10% of the total token supply to the pool.
 */

// Import ERC20 token standard interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// Interface for Uniswap Router
interface IUniswapV2Router02 {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);

    function WETH() external pure returns (address);
}

contract DOGE20LiquidityPool {
    IERC20 public immutable doge20Token; // Reference to DOGE20 token
    IUniswapV2Router02 public immutable uniswapRouter; // Reference to Uniswap Router

    address public immutable owner; // Contract owner
    uint256 public constant ALLOCATION_PERCENTAGE = 10; // Allocation percentage (10%)

    /**
     * @dev Initializes the contract with the DOGE20 token and Uniswap router addresses.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _uniswapRouter Address of the UniswapV2 Router contract.
     */
    constructor(address _doge20Token, address _uniswapRouter) {
        require(_doge20Token != address(0), "DOGE20 token address cannot be zero");
        require(_uniswapRouter != address(0), "Uniswap router address cannot be zero");

        doge20Token = IERC20(_doge20Token);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        owner = msg.sender;
    }

    /**
     * @dev Adds liquidity to the Uniswap pool by allocating 10% of the token supply.
     * @param ethAmount Amount of ETH to pair with the allocated DOGE20 tokens.
     */
    function addLiquidity(uint256 ethAmount) external payable {
        require(msg.sender == owner, "Only the owner can call this function");
        require(msg.value == ethAmount, "ETH amount mismatch");

        // Calculate 10% of the total DOGE20 token supply
        uint256 totalSupply = ERC20(address(doge20Token)).totalSupply();
        uint256 allocationAmount = (totalSupply * ALLOCATION_PERCENTAGE) / 100;

        // Transfer allocated DOGE20 tokens from owner to this contract
        require(
            doge20Token.transferFrom(msg.sender, address(this), allocationAmount),
            "Token transfer failed"
        );

        // Approve Uniswap router to spend DOGE20 tokens
        require(
            doge20Token.approve(address(uniswapRouter), allocationAmount),
            "Token approval failed"
        );

        // Add liquidity to the Uniswap pool
        uniswapRouter.addLiquidity{value: ethAmount}(
            address(doge20Token),
            uniswapRouter.WETH(),
            allocationAmount,
            ethAmount,
            0, // Minimum amount of DOGE20 tokens
            0, // Minimum amount of ETH
            msg.sender, // Recipient of liquidity tokens
            block.timestamp + 3600 // Deadline (1 hour)
        );
    }

    /**
     * @dev Allows the owner to withdraw any leftover ETH from the contract.
     */
    function withdrawETH() external {
        require(msg.sender == owner, "Only the owner can withdraw ETH");
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No ETH to withdraw");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw any leftover DOGE20 tokens from the contract.
     */
    function withdrawDOGE20() external {
        require(msg.sender == owner, "Only the owner can withdraw DOGE20 tokens");
        uint256 contractBalance = doge20Token.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        require(
            doge20Token.transfer(owner, contractBalance),
            "Token withdrawal failed"
        );
    }

    // Fallback function to accept ETH
    receive() external payable {}
}
```
