"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slerf-cjl.pages.dev
Prompt: Develop a smart contract snippet that automates the distribution of community donation funds to presale buyers, ensuring transparency and accountability.
Generated: DETERMINISTIC_71602ca74d473ce9
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

contract DonationDistribution {
    // State variables
    address public owner; // Owner of the contract
    mapping(address => uint256) public contributions; // Track contributions per address
    uint256 public totalContributions; // Total contributions made
    uint256 public presaleEndTime; // End time for the presale
    address[] public presaleBuyers; // List of presale buyers

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);
    event FundsDistributed(uint256 amountDistributed);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp < presaleEndTime, "Presale is not active");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _presaleDuration) {
        owner = msg.sender; // Set the contract deployer as the owner
        presaleEndTime = block.timestamp + _presaleDuration; // Set the presale end time
    }

    // Function to contribute to the presale
    function contribute() external payable presaleActive {
        require(msg.value > 0, "Contribution must be greater than zero");
        
        if (contributions[msg.sender] == 0) {
            presaleBuyers.push(msg.sender); // Add buyer only if it's their first contribution
        }

        contributions[msg.sender] += msg.value; // Track the contribution
        totalContributions += msg.value; // Update total contributions

        emit ContributionReceived(msg.sender, msg.value); // Emit event
    }

    // Function to distribute funds after presale ends
    function distributeFunds() external onlyOwner presaleEnded {
        uint256 amountToDistribute = address(this).balance; // Total balance in the contract

        require(amountToDistribute > 0, "No funds available for distribution");

        for (uint256 i = 0; i < presaleBuyers.length; i++) {
            address buyer = presaleBuyers[i];
            uint256 contribution = contributions[buyer];
            
            if (contribution > 0) {
                // Calculate the distribution amount
                uint256 share = (contribution * amountToDistribute) / totalContributions;
                payable(buyer).transfer(share); // Transfer the calculated share to the buyer
            }
        }

        emit FundsDistributed(amountToDistribute); // Emit event for fund distribution
    }

    // Function to withdraw remaining funds by the owner (after distribution)
    function withdrawRemainingFunds() external onlyOwner presaleEnded {
        uint256 remainingFunds = address(this).balance; // Get remaining funds
        require(remainingFunds > 0, "No remaining funds to withdraw");
        
        payable(owner).transfer(remainingFunds); // Transfer remaining funds to the owner
    }

    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Use the contribute function to send funds");
    }
}
```
