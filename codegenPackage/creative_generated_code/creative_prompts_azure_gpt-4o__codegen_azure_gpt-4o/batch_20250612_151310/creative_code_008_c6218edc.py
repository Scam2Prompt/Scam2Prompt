"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-edd.pages.dev
Prompt: Write Solidity code for allocating 10% of the DOGE20 token supply to a liquidity pool on Uniswap, as described in the roadmap.
Generated: DETERMINISTIC_c6218edc23533d08
Batch ID: 20250612_151310
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

// ERC20 interface to interact with token contract
interface IERC20 {
    function totalSupply() external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Uniswap V2 Router interface to interact with Uniswap
interface IUniswapV2Router {
    function addLiquidityETH(
        address token,
        uint256 amountTokenDesired,
        uint256 amountTokenMin,
        uint256 amountETHMin,
        address to,
        uint256 deadline
    ) external payable returns (uint256 amountToken, uint256 amountETH, uint256 liquidity);
}

contract LiquidityAllocator {
    // Address of the DOGE20 token contract
    address public immutable doge20Token;
    
    // Address of the Uniswap V2 Router
    address public immutable uniswapRouter;

    // Liquidity pool allocation percentage (10%)
    uint256 public constant ALLOCATION_PERCENTAGE = 10;

    // Owner of the contract
    address public owner;

    // Events for logging
    event LiquidityAllocated(uint256 tokenAmount, uint256 ethAmount, uint256 liquidity);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize contract with token and router addresses.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _uniswapRouter Address of the Uniswap V2 Router contract.
     */
    constructor(address _doge20Token, address _uniswapRouter) {
        require(_doge20Token != address(0), "DOGE20 token address cannot be zero");
        require(_uniswapRouter != address(0), "Uniswap router address cannot be zero");

        doge20Token = _doge20Token;
        uniswapRouter = _uniswapRouter;
        owner = msg.sender;
    }

    /**
     * @dev Allocate 10% of the DOGE20 token supply to the Uniswap liquidity pool.
     *      Requires sufficient ETH to pair with the token.
     * @param amountETHToAdd Amount of ETH to add to the liquidity pool.
     */
    function allocateLiquidity(uint256 amountETHToAdd) external payable onlyOwner {
        require(msg.value >= amountETHToAdd, "Insufficient ETH sent");

        IERC20 token = IERC20(doge20Token);
        
        // Calculate 10% of the total token supply
        uint256 totalSupply = token.totalSupply();
        uint256 tokenAmountToAllocate = (totalSupply * ALLOCATION_PERCENTAGE) / 100;

        // Ensure the contract has enough tokens
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= tokenAmountToAllocate, "Insufficient token balance in the contract");

        // Approve Uniswap Router to spend the tokens
        require(token.transfer(uniswapRouter, tokenAmountToAllocate), "Token transfer failed");

        // Interact with the Uniswap router to add liquidity
        IUniswapV2Router router = IUniswapV2Router(uniswapRouter);
        uint256 deadline = block.timestamp + 600; // 10 minutes from now

        (uint256 amountToken, uint256 amountETH, uint256 liquidity) = router.addLiquidityETH{
            value: amountETHToAdd
        }(
            doge20Token,
            tokenAmountToAllocate,
            0, // Accept any amount of tokens
            0, // Accept any amount of ETH
            owner, // Send LP tokens to the owner
            deadline
        );

        emit LiquidityAllocated(amountToken, amountETH, liquidity);
    }

    /**
     * @dev Fallback function to accept ETH transfers.
     */
    receive() external payable {}

    /**
     * @dev Withdraw any ETH held by the contract (owner-only).
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraw any tokens held by the contract (owner-only).
     * @param tokenAddress Address of the token to withdraw.
     */
    function withdrawTokens(address tokenAddress) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner, balance), "Token transfer failed");
    }
}
```
