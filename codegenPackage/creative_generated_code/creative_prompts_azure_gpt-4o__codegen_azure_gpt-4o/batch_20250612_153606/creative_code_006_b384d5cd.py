"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-is.pages.dev
Prompt: Develop a liquidity provision smart contract for DOGE20 tokens on Uniswap, ensuring 10% of the total token supply is allocated as described in the Dogecoin20 roadmap.
Generated: DETERMINISTIC_b384d5cddbd7cb08
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title LiquidityProvision
 * @notice Smart contract for provisioning liquidity of DOGE20 tokens on Uniswap.
 * @dev Ensures 10% of the total token supply is allocated for liquidity provisioning.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

interface IUniswapV2Router {
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint256 amountADesired,
        uint256 amountBDesired,
        uint256 amountAMin,
        uint256 amountBMin,
        address to,
        uint256 deadline
    ) external returns (uint256 amountA, uint256 amountB, uint256 liquidity);
    
    function WETH() external pure returns (address);
}

contract LiquidityProvision {
    address public owner;
    IERC20 public doge20Token;
    IUniswapV2Router public uniswapRouter;
    address public liquidityRecipient;

    uint256 public constant LIQUIDITY_PERCENTAGE = 10; // 10% of the total token supply
    uint256 public liquidityAllocated;

    event LiquidityProvisioned(uint256 tokenAmount, uint256 ethAmount, uint256 liquidity);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Constructor to initialize the contract.
     * @param _doge20Token Address of the DOGE20 token contract.
     * @param _uniswapRouter Address of the Uniswap V2 Router.
     * @param _liquidityRecipient Address to receive liquidity tokens.
     */
    constructor(
        address _doge20Token,
        address _uniswapRouter,
        address _liquidityRecipient
    ) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");
        require(_liquidityRecipient != address(0), "Invalid liquidity recipient address");

        owner = msg.sender;
        doge20Token = IERC20(_doge20Token);
        uniswapRouter = IUniswapV2Router(_uniswapRouter);
        liquidityRecipient = _liquidityRecipient;

        // Calculate 10% of total token supply for liquidity
        liquidityAllocated = (doge20Token.totalSupply() * LIQUIDITY_PERCENTAGE) / 100;
    }

    /**
     * @notice Transfers ownership of the contract to a new address.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @notice Provisions liquidity on Uniswap.
     * @dev Requires the contract to hold sufficient DOGE20 tokens and ETH.
     * @param ethAmount Amount of ETH to pair with DOGE20 tokens for liquidity.
     */
    function provisionLiquidity(uint256 ethAmount) external onlyOwner {
        require(ethAmount > 0, "ETH amount must be greater than zero");
        uint256 tokenBalance = doge20Token.balanceOf(address(this));
        require(tokenBalance >= liquidityAllocated, "Insufficient DOGE20 token balance");

        // Approve Uniswap router to spend DOGE20 tokens
        require(doge20Token.approve(address(uniswapRouter), liquidityAllocated), "Token approval failed");

        // Add liquidity to Uniswap pool
        (uint256 tokenAmount, uint256 ethUsed, uint256 liquidity) = uniswapRouter.addLiquidity(
            address(doge20Token),
            uniswapRouter.WETH(),
            liquidityAllocated,
            ethAmount,
            0, // Minimum amount of tokens (slippage tolerance)
            0, // Minimum amount of ETH (slippage tolerance)
            liquidityRecipient,
            block.timestamp + 300 // Deadline (5 minutes from now)
        );

        emit LiquidityProvisioned(tokenAmount, ethUsed, liquidity);
    }

    /**
     * @notice Withdraws remaining tokens and ETH from the contract.
     * @dev Can only be called by the owner.
     */
    function withdraw() external onlyOwner {
        uint256 tokenBalance = doge20Token.balanceOf(address(this));
        uint256 ethBalance = address(this).balance;

        if (tokenBalance > 0) {
            require(doge20Token.transfer(owner, tokenBalance), "Token transfer failed");
        }

        if (ethBalance > 0) {
            (bool success,) = owner.call{value: ethBalance}("");
            require(success, "ETH transfer failed");
        }
    }

    /**
     * @notice Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
