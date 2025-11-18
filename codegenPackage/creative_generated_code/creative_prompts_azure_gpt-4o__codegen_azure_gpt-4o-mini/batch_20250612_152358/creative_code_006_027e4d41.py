"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidfgwggshi5syqnklufswynx2u6rumuvgp4jl6n4lbqsolbeshdga.ipfs.dweb.link
Prompt: Develop a smart contract that integrates the Enhanced T-Bill feature of USD0++ to ensure principal security and earn Pills during the pre-launch phase.
Generated: DETERMINISTIC_027e4d41898f6280
Batch ID: 20250612_152358
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for Enhanced T-Bill integration
contract EnhancedTBill is Ownable {
    // State variables
    IERC20 public stableCoin; // The ERC20 token representing stable coin (e.g., USDC)
    uint256 public totalInvested; // Total amount invested in the T-Bill
    uint256 public interestRate; // Interest rate for T-Bills
    mapping(address => uint256) public investments; // Mapping of user investments
    mapping(address => uint256) public earnedPills; // Mapping of earned Pills for users

    // Events for logging
    event Invested(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event InterestRateUpdated(uint256 newInterestRate);

    // Constructor to set the stable coin address and initial interest rate
    constructor(IERC20 _stableCoin, uint256 _initialInterestRate) {
        stableCoin = _stableCoin;
        interestRate = _initialInterestRate;
    }

    // Function to invest in T-Bills
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        require(stableCoin.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        totalInvested += amount;
        investments[msg.sender] += amount;

        // Emit investment event
        emit Invested(msg.sender, amount);
    }

    // Function to calculate and distribute earned Pills
    function distributePills() external {
        require(totalInvested > 0, "No investments to distribute Pills");

        uint256 earned = (totalInvested * interestRate) / 100;
        earnedPills[msg.sender] += earned; // Assume the user is the caller for simplicity

        // Emit an event for earning Pills
        emit Invested(msg.sender, earned);
    }

    // Function to withdraw investment and earned Pills
    function withdraw(uint256 amount) external {
        require(investments[msg.sender] >= amount, "Insufficient balance to withdraw");

        investments[msg.sender] -= amount;
        totalInvested -= amount;
        require(stableCoin.transfer(msg.sender, amount), "Transfer failed");

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Owner function to update interest rate
    function updateInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than zero");
        interestRate = newRate;

        // Emit interest rate update event
        emit InterestRateUpdated(newRate);
    }

    // Function to view the balance of earned Pills
    function viewPillsBalance() external view returns (uint256) {
        return earnedPills[msg.sender];
    }
}
```
