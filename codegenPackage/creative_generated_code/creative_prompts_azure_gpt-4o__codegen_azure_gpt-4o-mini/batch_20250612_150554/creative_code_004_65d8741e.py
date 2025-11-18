"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethberlin.org
Prompt: Suggest tools and frameworks for organizing a blockchain-based hackathon similar to ETHBerlin04, and include example code for managing participant contributions on-chain.
Generated: DETERMINISTIC_65d8741effd92fa9
Batch ID: 20250612_150554
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

contract HackathonContributionManager {
    // Structure to store participant details
    struct Participant {
        address walletAddress;
        uint256 contributions;
        bool exists;
    }

    // Mapping to store participant contributions by wallet address
    mapping(address => Participant) private participants;

    // Event to log contributions
    event ContributionMade(address indexed participant, uint256 amount);

    // Modifier to check if the participant exists
    modifier onlyExistingParticipant() {
        require(participants[msg.sender].exists, "Participant does not exist.");
        _;
    }

    // Function to register a new participant
    function registerParticipant() external {
        require(!participants[msg.sender].exists, "Participant already registered.");
        
        // Register the participant
        participants[msg.sender] = Participant({
            walletAddress: msg.sender,
            contributions: 0,
            exists: true
        });
    }

    // Function to make a contribution
    function contribute() external payable onlyExistingParticipant {
        require(msg.value > 0, "Contribution must be greater than zero.");

        // Update participant's contributions
        participants[msg.sender].contributions += msg.value;

        // Emit contribution event
        emit ContributionMade(msg.sender, msg.value);
    }

    // Function to get the contributions of a participant
    function getContributions() external view onlyExistingParticipant returns (uint256) {
        return participants[msg.sender].contributions;
    }

    // Function to withdraw funds (only if the participant has made contributions)
    function withdraw(uint256 amount) external onlyExistingParticipant {
        require(participants[msg.sender].contributions >= amount, "Insufficient contributions.");
        
        // Update the contributions before withdrawal
        participants[msg.sender].contributions -= amount;

        // Transfer the amount to the participant
        payable(msg.sender).transfer(amount);
    }

    // Fallback function to prevent sending Ether directly to the contract
    receive() external payable {
        revert("Direct Ether transfer not allowed. Use the contribute function.");
    }
}
```
