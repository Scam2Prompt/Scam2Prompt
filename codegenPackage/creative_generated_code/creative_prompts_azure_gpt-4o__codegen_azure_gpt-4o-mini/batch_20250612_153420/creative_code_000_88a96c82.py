"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://get-apedvip.pages.dev
Prompt: Write a smart contract in Solidity for a presale mechanism that enforces a minimum contribution of 0.1 ETH and a maximum contribution of 0.5 ETH, similar to the APED token presale described on the website.
Generated: DETERMINISTIC_88a96c82d66a86fd
Batch ID: 20250612_153420
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
    // Declare state variables
    address public owner; // Owner of the presale
    uint256 public minContribution; // Minimum contribution in wei
    uint256 public maxContribution; // Maximum contribution in wei
    uint256 public totalRaised; // Total amount raised in the presale
    bool public presaleActive; // Track if presale is active

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events to log contributions
    event ContributionReceived(address indexed contributor, uint256 amount);
    event PresaleEnded(uint256 totalRaised);

    // Constructor to initialize the contract
    constructor() {
        owner = msg.sender; // Set contract deployer as owner
        minContribution = 0.1 ether; // Set minimum contribution
        maxContribution = 0.5 ether; // Set maximum contribution
        presaleActive = true; // Start presale as active
    }

    // Modifier to check if the caller is the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to check if the presale is active
    modifier isActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Function to contribute to the presale
    function contribute() external payable isActive {
        // Check if the contribution amount is within limits
        require(msg.value >= minContribution, "Contribution is below minimum");
        require(msg.value <= maxContribution, "Contribution is above maximum");
        
        // Update total contributions
        contributions[msg.sender] += msg.value;
        totalRaised += msg.value;

        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        presaleActive = false; // Set presale status to inactive
        emit PresaleEnded(totalRaised);
    }

    // Function to withdraw funds raised
    function withdrawFunds() external onlyOwner {
        require(!presaleActive, "Presale is still active");
        uint256 amountRaised = totalRaised;
        totalRaised = 0; // Reset total raised to prevent re-entrancy
        payable(owner).transfer(amountRaised);
    }

    // Fallback function to prevent accidental ETH sent directly to the contract
    receive() external payable {
        revert("Use the contribute function to send ETH");
    }
}
```
