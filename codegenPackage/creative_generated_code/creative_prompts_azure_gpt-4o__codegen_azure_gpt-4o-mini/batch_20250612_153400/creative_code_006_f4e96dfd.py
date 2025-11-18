"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-dogecoin20.pages.dev
Prompt: Generate code for adding liquidity to Uniswap for DOGE20 tokens, allocating 10% of the total token supply as described in the roadmap.
Generated: DETERMINISTIC_f4e96dfd35cbc7eb
Batch ID: 20250612_153400
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

// Importing necessary interfaces and libraries
import "@uniswap/v3-periphery/contracts/interfaces/INonfungiblePositionManager.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityManager is Ownable {
    INonfungiblePositionManager public positionManager;
    IERC20 public doge20Token;

    // Constants
    uint256 public constant LIQUIDITY_PERCENTAGE = 10; // 10% of total supply

    // Event for liquidity addition
    event LiquidityAdded(uint256 tokenId, uint256 liquidity);

    constructor(address _positionManager, address _doge20Token) {
        positionManager = INonfungiblePositionManager(_positionManager);
        doge20Token = IERC20(_doge20Token);
    }

    /**
     * @dev Adds liquidity to Uniswap for DOGE20 tokens.
     * @param amount The amount of DOGE20 tokens to add as liquidity.
     * @param token0 The address of the first token of the pair (DOGE20).
     * @param token1 The address of the second token of the pair (ETH or another token).
     * @param fee The pool fee for Uniswap.
     * @param recipient The recipient of the minted liquidity position.
     * @param deadline The timestamp by which the transaction must be confirmed.
     */
    function addLiquidity(
        uint256 amount,
        address token0,
        address token1,
        uint24 fee,
        address recipient,
        uint256 deadline
    ) external onlyOwner returns (uint256 tokenId, uint256 liquidity) {
        // Validate input parameters
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");

        // Calculate total supply and 10% allocation
        uint256 totalSupply = doge20Token.totalSupply();
        uint256 allocation = (totalSupply * LIQUIDITY_PERCENTAGE) / 100;

        // Ensure that the requested amount does not exceed the allocated amount
        require(amount <= allocation, "Amount exceeds allocated liquidity");

        // Transfer DOGE20 tokens from owner to the contract
        require(doge20Token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Approve the position manager to spend the DOGE20 tokens
        require(doge20Token.approve(address(positionManager), amount), "Approval failed");

        // Adding liquidity to Uniswap
        (tokenId, liquidity) = positionManager.mint(
            INonfungiblePositionManager.MintParams({
                token0: token0,
                token1: token1,
                fee: fee,
                tickLower: -887220, // Example tick values, should be set based on pair
                tickUpper: 887220,
                amount0Desired: amount,
                amount1Desired: 0, // Change as needed for the pair
                amount0Min: 0,
                amount1Min: 0,
                recipient: recipient,
                deadline: deadline
            })
        );

        emit LiquidityAdded(tokenId, liquidity);
    }

    /**
     * @dev Withdraw unspent DOGE20 tokens from the contract.
     * @param to The address to send the tokens to.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        
        uint256 contractBalance = doge20Token.balanceOf(address(this));
        require(amount <= contractBalance, "Insufficient balance");

        // Transfer the specified amount of DOGE20 tokens
        require(doge20Token.transfer(to, amount), "Transfer failed");
    }
}
```
