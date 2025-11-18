"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularitydaoai-launchpad.pages.dev
Prompt: Develop a Solidity-based refund mechanism for Gold and Diamond tier participants in SingularityDAO's token sale, as described in the refund policy.
Generated: DETERMINISTIC_6525a9b77481d075
Batch ID: 20250612_153606
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

contract SingularityDAOTokenSale {
    // Constants for tier levels
    enum Tier { None, Gold, Diamond }

    // User struct to store participant details
    struct Participant {
        uint256 amountPaid; // Amount paid by the participant
        Tier tier; // Tier of the participant
        bool refunded; // Refund status
    }

    // Mapping to store participants' information
    mapping(address => Participant) public participants;

    // Total amount raised in the token sale
    uint256 public totalRaised;

    // Event to log refunds
    event RefundIssued(address indexed participant, uint256 amount);

    // Constructor to initialize the contract
    constructor() {
        totalRaised = 0; // Initialize total raised
    }

    // Function to participate in the token sale
    function participate(Tier tier) external payable {
        require(msg.value > 0, "Must send ETH to participate");
        require(tier == Tier.Gold || tier == Tier.Diamond, "Invalid tier");

        // Initialize or update participant
        Participant storage participant = participants[msg.sender];
        require(participant.amountPaid == 0, "Already participated");

        participant.amountPaid = msg.value;
        participant.tier = tier;
        totalRaised += msg.value;
    }

    // Refund mechanism for eligible participants
    function refund() external {
        Participant storage participant = participants[msg.sender];
        require(participant.amountPaid > 0, "No funds to refund");
        require(!participant.refunded, "Already refunded");
        require(participant.tier == Tier.Gold || participant.tier == Tier.Diamond, "Not eligible for refund");

        // Update refund status to prevent re-entrancy
        participant.refunded = true;

        // Transfer funds back to the participant
        (bool success, ) = msg.sender.call{value: participant.amountPaid}("");
        require(success, "Refund transfer failed");

        // Emit refund event
        emit RefundIssued(msg.sender, participant.amountPaid);
    }

    // Fallback function to receive ETH
    receive() external payable {
        // This function allows the contract to receive ETH
    }

    // Function to check the contract's balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
