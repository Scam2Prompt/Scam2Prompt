"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Create a Solidity smart contract for implementing the HighTable Secret Deal Program, using the key features described in the Good Games Guild documentation.
Generated: DETERMINISTIC_18003293dc81789d
Batch ID: 20250612_153820
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

/**
 * @title HighTableSecretDealProgram
 * @dev This contract implements the HighTable Secret Deal Program as described in the Good Games Guild documentation.
 * Features include registering deals, managing deal participants, and securely handling funds.
 */
contract HighTableSecretDealProgram {
    // Struct to represent a deal
    struct Deal {
        uint256 id; // Unique identifier for the deal
        string description; // Description of the deal
        uint256 amount; // Amount involved in the deal (in wei)
        address creator; // Address of the deal creator
        address participant; // Address of the participant in the deal
        bool isCompleted; // Status of the deal (completed or not)
    }

    // Mapping to store deals by their ID
    mapping(uint256 => Deal) private deals;

    // Counter to generate unique deal IDs
    uint256 private dealCounter;

    // Events to notify about contract activities
    event DealCreated(uint256 indexed id, address indexed creator, string description, uint256 amount);
    event ParticipantAssigned(uint256 indexed id, address indexed participant);
    event DealCompleted(uint256 indexed id);

    /**
     * @dev Modifier to ensure the caller is the creator of the deal.
     * @param _dealId ID of the deal.
     */
    modifier onlyCreator(uint256 _dealId) {
        require(deals[_dealId].creator == msg.sender, "Caller is not the creator of the deal");
        _;
    }

    /**
     * @dev Modifier to ensure the caller is the participant of the deal.
     * @param _dealId ID of the deal.
     */
    modifier onlyParticipant(uint256 _dealId) {
        require(deals[_dealId].participant == msg.sender, "Caller is not the participant of the deal");
        _;
    }

    /**
     * @dev Function to create a new deal.
     * @param _description Description of the deal.
     * @param _amount Amount involved in the deal (in wei).
     */
    function createDeal(string memory _description, uint256 _amount) external payable {
        require(msg.value == _amount, "Sent value must match the deal amount");
        require(_amount > 0, "Deal amount must be greater than zero");

        // Increment deal counter to generate unique ID
        dealCounter++;

        // Create and store the new deal
        deals[dealCounter] = Deal({
            id: dealCounter,
            description: _description,
            amount: _amount,
            creator: msg.sender,
            participant: address(0), // No participant assigned initially
            isCompleted: false
        });

        // Emit event to notify deal creation
        emit DealCreated(dealCounter, msg.sender, _description, _amount);
    }

    /**
     * @dev Function to assign a participant to a deal.
     * @param _dealId ID of the deal.
     * @param _participant Address of the participant to be assigned.
     */
    function assignParticipant(uint256 _dealId, address _participant) external onlyCreator(_dealId) {
        require(_participant != address(0), "Participant address cannot be zero");
        require(deals[_dealId].participant == address(0), "Participant already assigned");

        // Assign the participant
        deals[_dealId].participant = _participant;

        // Emit event to notify participant assignment
        emit ParticipantAssigned(_dealId, _participant);
    }

    /**
     * @dev Function to mark a deal as completed and transfer funds to the participant.
     * @param _dealId ID of the deal.
     */
    function completeDeal(uint256 _dealId) external onlyParticipant(_dealId) {
        Deal storage deal = deals[_dealId];
        require(!deal.isCompleted, "Deal is already completed");

        // Mark the deal as completed
        deal.isCompleted = true;

        // Transfer funds to the participant
        payable(deal.participant).transfer(deal.amount);

        // Emit event to notify deal completion
        emit DealCompleted(_dealId);
    }

    /**
     * @dev Function to get details of a deal.
     * @param _dealId ID of the deal.
     * @return Deal details.
     */
    function getDeal(uint256 _dealId) external view returns (Deal memory) {
        require(deals[_dealId].creator != address(0), "Deal does not exist");
        return deals[_dealId];
    }
}
```
