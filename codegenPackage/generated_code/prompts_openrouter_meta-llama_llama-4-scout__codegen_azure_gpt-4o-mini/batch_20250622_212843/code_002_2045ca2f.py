"""
Generated Code Metadata:
========================
Original URL: https://hypurrfiapp.com
Prompt: "Generate a code example for borrowing from HypurrFi's isolated markets using a smart contract."
Generated: DETERMINISTIC_2045ca2ff6a1b29b
Batch ID: 20250622_212843
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
import "@openzeppelin/contracts/access/Ownable.sol";

// HypurrFi interface for borrowing from isolated markets
interface IHypurrFi {
    function borrow(uint256 amount) external;
    function repay(uint256 amount) external;
}

contract HypurrFiBorrowing is Ownable {
    // State variables
    IHypurrFi public hypurrFi; // Instance of the HypurrFi contract
    IERC20 public collateralToken; // Token used as collateral
    IERC20 public debtToken; // Token to be borrowed

    // Events for logging
    event Borrowed(address indexed borrower, uint256 amount);
    event Repaid(address indexed borrower, uint256 amount);

    // Constructor to initialize the contract with HypurrFi and token addresses
    constructor(address _hypurrFi, address _collateralToken, address _debtToken) {
        hypurrFi = IHypurrFi(_hypurrFi);
        collateralToken = IERC20(_collateralToken);
        debtToken = IERC20(_debtToken);
    }

    // Function to borrow tokens from HypurrFi
    function borrowTokens(uint256 amount) external onlyOwner {
        // Ensure the amount to borrow is greater than zero
        require(amount > 0, "Borrow amount must be greater than zero");

        // Call the borrow function from HypurrFi
        hypurrFi.borrow(amount);

        // Emit an event for borrowing
        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed tokens
    function repayTokens(uint256 amount) external onlyOwner {
        // Ensure the amount to repay is greater than zero
        require(amount > 0, "Repay amount must be greater than zero");

        // Transfer the debt tokens from the contract to the HypurrFi contract
        require(debtToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Call the repay function from HypurrFi
        hypurrFi.repay(amount);

        // Emit an event for repayment
        emit Repaid(msg.sender, amount);
    }

    // Function to withdraw collateral tokens (if needed)
    function withdrawCollateral(uint256 amount) external onlyOwner {
        // Ensure the amount to withdraw is greater than zero
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Transfer collateral tokens back to the owner
        require(collateralToken.transfer(msg.sender, amount), "Transfer failed");
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
