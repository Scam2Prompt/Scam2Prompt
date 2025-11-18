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
 * @title HighTable Secret Deal Program
 * @dev This smart contract implements the HighTable Secret Deal Program as per Good Games Guild documentation.
 */
contract HighTableSecretDeal {
    // Structure to hold deal information
    struct Deal {
        uint256 id;
        address creator;
        address[] participants;
        uint256 rewards;
        bool isActive;
    }

    // State variables
    uint256 public nextDealId;
    mapping(uint256 => Deal) public deals; // Mapping of dealId to Deal
    mapping(address => uint256[]) public userDeals; // Mapping of user address to their deal IDs

    // Event to emit when a new deal is created
    event DealCreated(uint256 indexed dealId, address indexed creator, uint256 rewards);

    // Event to emit when a deal is completed
    event DealCompleted(uint256 indexed dealId);

    // Modifier to check if the deal is active
    modifier onlyActiveDeal(uint256 dealId) {
        require(deals[dealId].isActive, "Deal is not active");
        _;
    }

    /**
     * @dev Create a new deal
     * @param participants Array of addresses participating in the deal
     * @param rewards Amount of rewards for the deal
     */
    function createDeal(address[] memory participants, uint256 rewards) external {
        require(participants.length > 0, "Participants required");
        require(rewards > 0, "Rewards must be greater than 0");

        // Increment deal ID and create new deal
        uint256 dealId = nextDealId++;
        deals[dealId] = Deal(dealId, msg.sender, participants, rewards, true);
        userDeals[msg.sender].push(dealId);

        emit DealCreated(dealId, msg.sender, rewards);
    }

    /**
     * @dev Complete the deal, making it inactive
     * @param dealId ID of the deal to complete
     */
    function completeDeal(uint256 dealId) external onlyActiveDeal(dealId) {
        require(msg.sender == deals[dealId].creator, "Only creator can complete the deal");

        // Mark the deal as inactive
        deals[dealId].isActive = false;

        emit DealCompleted(dealId);
    }

    /**
     * @dev Retrieve deal information
     * @param dealId ID of the deal to retrieve
     * @return Deal The deal structure containing deal information
     */
    function getDeal(uint256 dealId) external view returns (Deal memory) {
        require(dealId < nextDealId, "Deal does not exist");
        return deals[dealId];
    }

    /**
     * @dev Get deals created by a specific user
     * @param user Address of the user
     * @return uint256[] Array of deal IDs created by the user
     */
    function getUserDeals(address user) external view returns (uint256[] memory) {
        return userDeals[user];
    }
}
```
