"""
Generated Code Metadata:
========================
Original URL: https://copycoded.pages.dev
Prompt: Generate a Solidity smart contract that uses a Migrator and Exchange libraries to interact with Uniswap V2.
Generated: DETERMINISTIC_b2030dede90648d0
Batch ID: 20250622_204938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

contract UniswapMigrator {
    // State variables
    IUniswapV2Router02 public uniswapRouter;
    IUniswapV2Factory public uniswapFactory;
    address public owner;

    // Events
    event TokensMigrated(address indexed token, uint256 amountIn, uint256 amountOut);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with Uniswap router and factory addresses
    constructor(address _router, address _factory) {
        uniswapRouter = IUniswapV2Router02(_router);
        uniswapFactory = IUniswapV2Factory(_factory);
        owner = msg.sender;
    }

    // Function to migrate tokens from one Uniswap pair to another
    function migrateTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 minAmountOut,
        address to,
        uint256 deadline
    ) external onlyOwner {
        // Transfer tokens from the owner to this contract
        require(IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn), "Transfer failed");

        // Approve the Uniswap router to spend the tokens
        require(IERC20(tokenIn).approve(address(uniswapRouter), amountIn), "Approval failed");

        // Perform the swap on Uniswap
        address[] memory path = new address[](2);
        path[0] = tokenIn;
        path[1] = tokenOut;

        uint256[] memory amounts = uniswapRouter.swapExactTokensForTokens(
            amountIn,
            minAmountOut,
            path,
            to,
            deadline
        );

        // Emit an event for the migration
        emit TokensMigrated(tokenIn, amounts[0], amounts[1]);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).transfer(msg.sender, amount), "Withdrawal failed");
    }

    // Function to set a new Uniswap router address (if needed)
    function setRouter(address _router) external onlyOwner {
        uniswapRouter = IUniswapV2Router02(_router);
    }

    // Function to set a new Uniswap factory address (if needed)
    function setFactory(address _factory) external onlyOwner {
        uniswapFactory = IUniswapV2Factory(_factory);
    }
}
```
