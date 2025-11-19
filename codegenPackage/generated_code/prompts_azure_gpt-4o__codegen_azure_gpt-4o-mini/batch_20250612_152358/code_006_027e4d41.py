"""
Generated Code Metadata:
========================
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Develop a smart contract that integrates the Enhanced T-Bill feature of USD0++ to ensure principal security and earn Pills during the pre-launch phase.
Generated: DETERMINISTIC_027e4d41898f6280
Batch ID: 20250612_152358
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

// Smart contract for Enhanced T-Bill feature integration
contract EnhancedTBill is Ownable {
    // State variables
    IERC20 public stableCoin; // The stablecoin used for T-Bill
    uint256 public principal; // Amount of principal secured
    uint256 public interestRate; // Interest rate for earning Pills
    uint256 public maturityDate; // Date when the T-Bill matures
    bool public isActive; // Status of the T-Bill

    // Events for logging
    event PrincipalDeposited(address indexed user, uint256 amount);
    event PillsEarned(address indexed user, uint256 amount);
    event TBillMatured(uint256 totalPills);

    // Constructor to initialize the contract
    constructor(IERC20 _stableCoin, uint256 _interestRate, uint256 _maturityDate) {
        stableCoin = _stableCoin;
        interestRate = _interestRate;
        maturityDate = _maturityDate;
        isActive = true;
    }

    // Function to deposit principal into the T-Bill
    function depositPrincipal(uint256 amount) external {
        require(isActive, "T-Bill is not active");
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer stablecoin from user to this contract
        stableCoin.transferFrom(msg.sender, address(this), amount);
        principal += amount;

        emit PrincipalDeposited(msg.sender, amount);
    }

    // Function to calculate and distribute Pills upon maturity
    function matureTBill() external onlyOwner {
        require(block.timestamp >= maturityDate, "T-Bill has not matured yet");
        require(isActive, "T-Bill is already matured");

        // Calculate total Pills earned
        uint256 totalPills = (principal * interestRate) / 100;

        // Mark the T-Bill as inactive
        isActive = false;

        // Emit event for matured T-Bill
        emit TBillMatured(totalPills);
    }

    // Function to withdraw principal and earned Pills
    function withdraw() external onlyOwner {
        require(!isActive, "T-Bill is still active");

        // Transfer the principal back to the owner
        stableCoin.transfer(msg.sender, principal);
        principal = 0; // Reset principal after withdrawal
    }

    // Function to get the current status of the T-Bill
    function getTBillStatus() external view returns (uint256, uint256, bool) {
        return (principal, interestRate, isActive);
    }
}
```
