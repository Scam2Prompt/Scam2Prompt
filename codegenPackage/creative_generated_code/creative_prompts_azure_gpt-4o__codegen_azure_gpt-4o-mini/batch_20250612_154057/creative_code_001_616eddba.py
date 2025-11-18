"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-savcr.com
Prompt: Generate code to create a custom transaction using DeFi Saver's Recipe Creator that combines flash loans and token swaps across multiple protocols.
Generated: DETERMINISTIC_616eddbab430506e
Batch ID: 20250612_154057
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPool.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPoolAddressesProvider.sol";

contract CustomTransaction is Ownable {
    // Addresses for the Uniswap router and Aave lending pool provider
    IUniswapV2Router02 public immutable uniswapRouter;
    ILendingPoolAddressesProvider public immutable aaveProvider;
    
    // Event to log transaction success
    event TransactionExecuted(address indexed user, uint256 amountIn, uint256 amountOut);

    // Constructor to set the router and lending pool provider addresses
    constructor(address _uniswapRouter, address _aaveProvider) {
        uniswapRouter = IUniswapV2Router02(_uniswapRouter);
        aaveProvider = ILendingPoolAddressesProvider(_aaveProvider);
    }

    // Function to execute a custom transaction that combines flash loans and swaps
    function executeTransaction(
        address[] calldata tokens,
        uint256 amount,
        address swapTo,
        uint256 minAmountOut
    ) external onlyOwner {
        // Validate input parameters
        require(tokens.length >= 2, "At least two tokens required");
        require(amount > 0, "Amount must be greater than zero");

        // Obtain the lending pool
        ILendingPool lendingPool = ILendingPool(aaveProvider.getLendingPool());

        // Request a flash loan from Aave
        lendingPool.flashLoan(
            address(this),
            tokens[0],
            amount,
            ""
        );
    }

    // Callback function to execute after receiving the flash loan
    function executeFlashLoan(
        address sender,
        address token,
        uint256 amount,
        uint256 fee,
        bytes calldata params
    ) external {
        require(msg.sender == address(aaveProvider.getLendingPool()), "Only Aave can call this function");
        
        // Approve the Uniswap router to spend the token
        IERC20(token).approve(address(uniswapRouter), amount);

        // Swap the token using Uniswap
        address[] memory path = new address[](2);
        path[0] = token;
        path[1] = tokens[1]; // Swap to the next token in the path

        uniswapRouter.swapExactTokensForTokens(
            amount,
            minAmountOut,
            path,
            address(this),
            block.timestamp
        );

        // Repay the flash loan
        uint256 totalRepayment = amount + fee;
        IERC20(token).approve(address(lendingPool), totalRepayment);
        lendingPool.repay(token, totalRepayment, 1, address(this));

        emit TransactionExecuted(msg.sender, amount, minAmountOut);
    }

    // Allow the contract to receive ETH
    receive() external payable {}
}
```
