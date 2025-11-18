"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dodgecoiin20.pages.dev
Prompt: Generate Solidity code for a liquidity provision mechanism that allocates 10% of the DOGE20 token supply to Uniswap, ensuring early liquidity for trading.
Generated: DETERMINISTIC_423e334ff0e611c9
Batch ID: 20250612_153526
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";

contract Doge20LiquidityProvision {
    using SafeERC20 for IERC20;

    // Constants
    uint256 public constant LIQUIDITY_PERCENTAGE = 10; // 10%
    address public immutable owner;
    IERC20 public immutable doge20Token;
    IUniswapV2Router02 public immutable uniswapRouter;
    address public immutable uniswapPair;

    // Events
    event LiquidityProvided(uint256 tokenAmount, uint256 ethAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the token, router, and owner
    constructor(address _doge20Token, address _uniswapRouter) {
        require(_doge20Token != address(0), "Invalid DOGE20 token address");
        require(_uniswapRouter != address(0), "Invalid Uniswap router address");

        owner = msg.sender;
        doge20Token = IERC20(_doge20Token);
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);

        // Create Uniswap pair for DOGE20 and ETH
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory())
            .createPair(_doge20Token, uniswapRouter.WETH());
    }

    // Function to provide liquidity to Uniswap
    function provideLiquidity(uint256 tokenSupply) external onlyOwner {
        // Calculate the amount of tokens to allocate for liquidity
        uint256 tokenAmount = (tokenSupply * LIQUIDITY_PERCENTAGE) / 100;

        // Transfer tokens to the contract
        doge20Token.safeTransferFrom(msg.sender, address(this), tokenAmount);

        // Approve the router to spend the tokens
        doge20Token.safeApprove(address(uniswapRouter), tokenAmount);

        // Add liquidity to Uniswap
        (uint256 amountToken, uint256 amountETH, ) = uniswapRouter.addLiquidityETH{
            value: address(this).balance
        }(
            address(doge20Token),
            tokenAmount,
            0, // slippage is unavoidable
            0, // slippage is unavoidable
            owner, // recipient of the liquidity tokens
            block.timestamp
        );

        emit LiquidityProvided(amountToken, amountETH);
    }

    // Receive function to allow the contract to receive ETH
    receive() external payable {}
    
    // Fallback function
    fallback() external payable {}
}
```
