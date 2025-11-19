"""
Generated Code Metadata:
========================
Original URL: https://plasma-otc-ui.pages.dev
Prompt: Generate a smart contract code for a deal creation platform using Plasma, incorporating terms and conditions as specified in the dApp.
Generated: DETERMINISTIC_6d879b14df4d558d
Batch ID: 20250622_212059
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

/**
 * @title DealCreationPlatform
 * @dev A smart contract for creating and managing deals with terms and conditions in a decentralized application (dApp).
 *      This contract uses Plasma principles for scalability and security.
 */
contract DealCreationPlatform {
    // Struct to represent a deal
    struct Deal {
        uint256 id; // Unique identifier for the deal
        address creator; // Address of the deal creator
        address participant; // Address of the deal participant
        string terms; // Terms and conditions of the deal
        uint256 amount; // Amount involved in the deal
        bool isAccepted; // Status of the deal acceptance
        bool isCompleted; // Status of the deal completion
    }

    // State variables
    uint256 private dealCounter; // Counter for deal IDs
    mapping(uint256 => Deal) private deals; // Mapping of deal IDs to Deal structs
    mapping(address => uint256[]) private userDeals; // Mapping of user addresses to their deal IDs

    // Events
    event DealCreated(uint256 indexed dealId, address indexed creator, address indexed participant, string terms, uint256 amount);
    event DealAccepted(uint256 indexed dealId, address indexed participant);
    event DealCompleted(uint256 indexed dealId);

    // Modifier to check if the caller is the deal creator
    modifier onlyCreator(uint256 dealId) {
        require(deals[dealId].creator == msg.sender, "Caller is not the deal creator");
        _;
    }

    // Modifier to check if the caller is the deal participant
    modifier onlyParticipant(uint256 dealId) {
        require(deals[dealId].participant == msg.sender, "Caller is not the deal participant");
        _;
    }

    /**
     * @dev Create a new deal.
     * @param participant Address of the participant in the deal.
     * @param terms Terms and conditions of the deal.
     * @param amount Amount involved in the deal.
     */
    function createDeal(address participant, string memory terms, uint256 amount) external {
        require(participant != address(0), "Invalid participant address");
        require(amount > 0, "Amount must be greater than zero");

        dealCounter++;
        uint256 dealId = dealCounter;

        deals[dealId] = Deal({
            id: dealId,
            creator: msg.sender,
            participant: participant,
            terms: terms,
            amount: amount,
            isAccepted: false,
            isCompleted: false
        });

        userDeals[msg.sender].push(dealId);
        userDeals[participant].push(dealId);

        emit DealCreated(dealId, msg.sender, participant, terms, amount);
    }

    /**
     * @dev Accept a deal.
     * @param dealId ID of the deal to accept.
     */
    function acceptDeal(uint256 dealId) external onlyParticipant(dealId) {
        Deal storage deal = deals[dealId];
        require(!deal.isAccepted, "Deal already accepted");
        require(!deal.isCompleted, "Deal already completed");

        deal.isAccepted = true;

        emit DealAccepted(dealId, msg.sender);
    }

    /**
     * @dev Complete a deal.
     * @param dealId ID of the deal to complete.
     */
    function completeDeal(uint256 dealId) external onlyCreator(dealId) {
        Deal storage deal = deals[dealId];
        require(deal.isAccepted, "Deal not yet accepted");
        require(!deal.isCompleted, "Deal already completed");

        deal.isCompleted = true;

        emit DealCompleted(dealId);
    }

    /**
     * @dev Get details of a deal.
     * @param dealId ID of the deal to retrieve.
     * @return Deal details.
     */
    function getDeal(uint256 dealId) external view returns (Deal memory) {
        require(deals[dealId].id != 0, "Deal does not exist");
        return deals[dealId];
    }

    /**
     * @dev Get all deals created or participated in by a user.
     * @param user Address of the user.
     * @return Array of deal IDs.
     */
    function getUserDeals(address user) external view returns (uint256[] memory) {
        return userDeals[user];
    }
}
```
