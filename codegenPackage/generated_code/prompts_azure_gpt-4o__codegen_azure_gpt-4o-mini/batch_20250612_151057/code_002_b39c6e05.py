"""
Generated Code Metadata:
========================
Original URL: https://roost-cys.pages.dev
Prompt: Create a Solidity smart contract that distributes funds from the $ROOST presale according to the specified breakdown: 50% to liquidity pools and 50% for expenses, development, and distribution.
Generated: DETERMINISTIC_b39c6e05f4dfdc38
Batch ID: 20250612_151057
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract RoostPresaleDistributor is Ownable {
    // Address of the $ROOST token
    IERC20 public roostToken;

    // Events for logging fund distribution
    event FundsDistributed(uint256 liquidityAmount, uint256 expensesAmount);

    // Constructor to set the $ROOST token address
    constructor(address _roostToken) {
        require(_roostToken != address(0), "Invalid token address");
        roostToken = IERC20(_roostToken);
    }

    // Function to distribute funds from the presale
    function distributeFunds(uint256 totalAmount) external onlyOwner {
        require(totalAmount > 0, "Total amount must be greater than zero");
        require(roostToken.balanceOf(address(this)) >= totalAmount, "Insufficient funds in contract");

        // Calculate the amounts for liquidity and expenses
        uint256 liquidityAmount = totalAmount / 2; // 50% for liquidity
        uint256 expensesAmount = totalAmount - liquidityAmount; // 50% for expenses

        // Transfer funds to liquidity pool (replace with actual liquidity pool address)
        // For demonstration, we will just emit an event instead of transferring
        // address liquidityPool = <LIQUIDITY_POOL_ADDRESS>;
        // roostToken.transfer(liquidityPool, liquidityAmount);

        // Transfer funds for expenses (replace with actual expenses address)
        // address expensesAddress = <EXPENSES_ADDRESS>;
        // roostToken.transfer(expensesAddress, expensesAmount);

        // Emit event for logging
        emit FundsDistributed(liquidityAmount, expensesAmount);
    }

    // Function to withdraw any ERC20 tokens accidentally sent to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(roostToken), "Cannot withdraw $ROOST tokens");
        IERC20(tokenAddress).transfer(owner(), amount);
    }

    // Function to withdraw Ether from the contract (if any)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
