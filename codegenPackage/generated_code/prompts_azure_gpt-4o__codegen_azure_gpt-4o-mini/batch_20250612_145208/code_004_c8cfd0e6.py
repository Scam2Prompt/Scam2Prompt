"""
Generated Code Metadata:
========================
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Develop a smart contract that integrates with Instadapp Lite to execute cross-protocol refinancing strategies, leveraging protocols like AAVE and Compound.
Generated: DETERMINISTIC_c8cfd0e6c5f834d7
Batch ID: 20250612_145208
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

// Importing necessary interfaces for AAVE and Compound
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@aave/protocol-v2/contracts/interfaces/ILendingPool.sol";
import "@compound-finance/contracts/interfaces/CErc20.sol";

contract CrossProtocolRefinancer {
    // State variables
    ILendingPool public aaveLendingPool; // AAVE lending pool
    CErc20 public compoundToken; // Compound token interface
    address public owner; // Contract owner

    // Events
    event Refinanced(address indexed user, uint256 amount, string protocol);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with AAVE and Compound addresses
    constructor(address _aaveLendingPool, address _compoundToken) {
        aaveLendingPool = ILendingPool(_aaveLendingPool);
        compoundToken = CErc20(_compoundToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to refinance from AAVE to Compound
    function refinanceAaveToCompound(uint256 amount) external onlyOwner {
        // Check if the contract has enough allowance to transfer tokens
        require(IERC20(compoundToken.underlying()).allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        // Transfer tokens from the user to the contract
        IERC20(compoundToken.underlying()).transferFrom(msg.sender, address(this), amount);

        // Approve AAVE to spend the tokens
        IERC20(compoundToken.underlying()).approve(address(aaveLendingPool), amount);

        // Deposit tokens into AAVE
        aaveLendingPool.deposit(compoundToken.underlying(), amount, address(this), 0);

        // Borrow from Compound
        uint256 borrowedAmount = compoundToken.borrow(amount);
        require(borrowedAmount > 0, "Borrow failed");

        // Emit an event for successful refinancing
        emit Refinanced(msg.sender, amount, "AAVE to Compound");
    }

    // Function to refinance from Compound to AAVE
    function refinanceCompoundToAave(uint256 amount) external onlyOwner {
        // Check if the contract has enough balance to repay the borrowed amount
        require(compoundToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Repay the borrowed amount to Compound
        uint256 repayAmount = compoundToken.repayBorrow(amount);
        require(repayAmount > 0, "Repay failed");

        // Withdraw from AAVE
        uint256 withdrawnAmount = aaveLendingPool.withdraw(compoundToken.underlying(), amount, address(this));
        require(withdrawnAmount > 0, "Withdraw failed");

        // Transfer the withdrawn tokens back to the user
        IERC20(compoundToken.underlying()).transfer(msg.sender, withdrawnAmount);

        // Emit an event for successful refinancing
        emit Refinanced(msg.sender, amount, "Compound to AAVE");
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to change the owner of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
