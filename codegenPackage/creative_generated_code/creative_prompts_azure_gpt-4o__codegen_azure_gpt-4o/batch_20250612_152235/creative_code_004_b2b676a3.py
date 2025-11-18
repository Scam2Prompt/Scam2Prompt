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
    uint256 public constant CAP = 1000 ether; // Maximum cap for presale contributions
    uint256 public totalContributed; // Tracks total ETH contributed during the presale

    address public owner; // Address of the contract owner

    // Events
    event ContributionReceived(address indexed contributor, uint256 amount);

    // Constructor to set the owner of the contract
    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    // Fallback function to receive contributions
    receive() external payable {
        contribute();
    }

    // Function to handle ETH contributions
    function contribute() public payable {
        // Ensure the contribution does not exceed the cap
        require(msg.value > 0, "Contribution must be greater than 0");
        require(totalContributed + msg.value <= CAP, "Contribution exceeds the presale cap");

        // Update the total contributions
        totalContributed += msg.value;

        // Emit an event for the contribution
        emit ContributionReceived(msg.sender, msg.value);
    }

    // Function to withdraw funds by the owner
    function withdraw() external onlyOwner {
        // Transfer all funds to the owner
        payable(owner).transfer(address(this).balance);
    }

    // Function to check remaining contribution capacity
    function remainingCap() external view returns (uint256) {
        return CAP - totalContributed;
    }
}
```
