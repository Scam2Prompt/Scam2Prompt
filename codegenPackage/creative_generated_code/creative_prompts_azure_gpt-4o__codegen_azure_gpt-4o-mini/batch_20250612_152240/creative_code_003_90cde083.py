"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appbitcoinminetrixclaim.pages.dev
Prompt: Provide code examples for burning non-transferable ERC-20 mining credits to increase Bitcoin cloud mining power, as described in the Bitcoin Minetrix platform.
Generated: DETERMINISTIC_90cde08316bd2fea
Batch ID: 20250612_152240
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BitcoinMinetrix {
    // Declare the variables
    IERC20 public miningCredits; // ERC-20 token for mining credits
    uint256 public cloudMiningPower; // Total cloud mining power

    // Event to emit when credits are burned
    event CreditsBurned(address indexed user, uint256 amount, uint256 newPower);

    // Constructor to initialize the contract with mining credit token address
    constructor(address _miningCredits) {
        require(_miningCredits != address(0), "Invalid token address");
        miningCredits = IERC20(_miningCredits);
    }

    // Function to burn non-transferable ERC-20 mining credits
    function burnCredits(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Check if the user has enough credits
        uint256 balance = miningCredits.balanceOf(msg.sender);
        require(balance >= amount, "Insufficient credits");

        // Burn the credits (in this case, we just ‘transfer’ to address(0))
        bool success = miningCredits.transfer(address(0), amount);
        require(success, "Burn failed");

        // Increase cloud mining power based on the amount burned
        cloudMiningPower += amount; // Example logic, adjust as needed

        // Emit the event for tracking
        emit CreditsBurned(msg.sender, amount, cloudMiningPower);
    }

    // Function to get current cloud mining power
    function getCloudMiningPower() external view returns (uint256) {
        return cloudMiningPower;
    }
}
```
