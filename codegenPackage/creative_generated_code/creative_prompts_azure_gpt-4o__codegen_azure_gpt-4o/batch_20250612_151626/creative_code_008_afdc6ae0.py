"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogee1.pages.dev
Prompt: Create a liquidity provision smart contract for DOGE20 tokens on Uniswap, ensuring compliance with the roadmap's allocation of 10% of the token supply.
Generated: DETERMINISTIC_afdc6ae04b68d5b6
Batch ID: 20250612_151626
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

// Importing required interfaces and libraries from Uniswap and OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract LiquidityProvision is Ownable {
    // Address of the DOGE20 token
    IERC20 public doge20Token;

    // Address of the Uniswap V2 Router
    IUniswapV2Router02 public uniswapRouter;

    // Total token allocation for liquidity (10% of the token supply)
    uint256 public constant LIQUIDITY_ALLOCATION_PERCENT = 10;

    // Event emitted when liquidity is successfully added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor sets the token address and Uniswap router address
    constructor(address _doge20Token, address _uniswapRouter) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");

        doge20Token = IERC20(_doge20Token);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
    }

    /**
     * @dev Adds liquidity to Uniswap pool.
     * This function allocates 10% of the token supply as liquidity.
     * It requires the contract to have sufficient ETH and DOGE20 tokens.
     */
    function addLiquidity() external onlyOwner {
        // Calculate 10% of the total token supply
        uint256 totalSupply = doge20Token.totalSupply();
        uint256 liquidityTokens = (totalSupply * LIQUIDITY_ALLOCATION_PERCENT) / 100;

        // Ensure the contract has enough DOGE20 tokens to add liquidity
        require(
            doge20Token.balanceOf(address(this)) >= liquidityTokens,
            "Insufficient DOGE20 token balance for liquidity"
        );

        // Ensure the contract has sufficient ETH
        uint256 ethBalance = address(this).balance;
        require(ethBalance > 0, "Insufficient ETH balance for liquidity");

        // Approve Uniswap router to spend tokens
        doge20Token.approve(address(uniswapRouter), liquidityTokens);

        // Add liquidity to Uniswap
        // Amount of ETH paired with the tokens is passed from the contract balance
        (uint256 amountToken, uint256 amountETH, ) = uniswapRouter.addLiquidityETH{
            value: ethBalance
        }(
            address(doge20Token),
            liquidityTokens,
            0, // Minimum amount of DOGE20 desired (set to 0 for simplicity)
            0, // Minimum amount of ETH desired (set to 0 for simplicity)
            owner(), // Recipient of liquidity tokens (LP tokens)
            block.timestamp // Deadline for the transaction
        );

        // Emit event for successful liquidity addition
        emit LiquidityAdded(amountToken, amountETH);
    }

    /**
     * @dev Fallback function to receive ETH sent to the contract.
     */
    receive() external payable {}

    /**
     * @dev Emergency function to withdraw tokens or ETH from the contract.
     * Only callable by the contract owner.
     */
    function emergencyWithdraw(address _tokenAddress) external onlyOwner {
        if (_tokenAddress == address(0)) {
            // Withdraw ETH
            payable(owner()).transfer(address(this).balance);
        } else {
            // Withdraw tokens
            IERC20(_tokenAddress).transfer(
                owner(),
                IERC20(_tokenAddress).balanceOf(address(this))
            );
        }
    }
}
```
