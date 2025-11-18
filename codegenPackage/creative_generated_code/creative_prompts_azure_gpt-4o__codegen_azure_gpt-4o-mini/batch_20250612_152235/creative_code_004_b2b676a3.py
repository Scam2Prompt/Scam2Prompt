"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiexkodjd2izwx6r53x5g4q54yhqmiifywanhuecvkkdn2yyxq3rpu.ipfs.dweb.link
Prompt: Write a Solidity function that tracks the total ETH contributed during the presale and ensures it does not exceed the cap of 1000 ETH.
Generated: DETERMINISTIC_b2b676a3bc98499b
Batch ID: 20250612_152235
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

contract Presale {
    // State variables
    uint256 public totalContributions; // Total ETH contributed during the presale
    uint256 public constant CAP = 1000 ether; // Presale cap of 1000 ETH
    address public owner; // Owner of the presale contract

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event CapExceeded(address indexed contributor, uint256 attemptedAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Function to contribute ETH to the presale
    function contribute() external payable {
        // Check if contribution is valid and does not exceed cap
        require(msg.value > 0, "Contribution must be greater than 0");
        require(totalContributions + msg.value <= CAP, "Contribution exceeds cap");

        // Update total contributions
        totalContributions += msg.value;

        // Emit contribution event
        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to withdraw funds by the owner
    function withdraw() external onlyOwner {
        require(totalContributions > 0, "No funds to withdraw");

        // Transfer all funds to the owner
        payable(owner).transfer(totalContributions);
        totalContributions = 0; // Reset total contributions after withdrawal
    }

    // Function to get the current total contributions
    function getTotalContributions() external view returns (uint256) {
        return totalContributions;
    }
}
```
