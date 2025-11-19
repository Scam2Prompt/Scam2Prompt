"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://outlaws.wtf
Prompt: Write a smart contract that manages bounty hunts and rewards for participants in the Outlaws.WTF digital storytelling experience.
Generated: DETERMINISTIC_49cedfe0aefb0ccf
Batch ID: 20250612_161616
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
 * @title BountyHuntManager
 * @dev This contract manages bounty hunts and rewards for participants
 * in the Outlaws.WTF digital storytelling experience.
 */
contract BountyHuntManager {
    // Struct to define a bounty hunt
    struct Bounty {
        string description;      // Description of the bounty hunt
        uint256 rewardAmount;    // Reward amount in wei
        address creator;         // Address of the bounty creator
        bool isCompleted;        // Flag to indicate if the bounty is completed
        address winner;          // Address of the bounty winner
    }

    // Mapping to store bounties by ID
    mapping(uint256 => Bounty) public bounties;

    // Counter to assign unique IDs to bounties
    uint256 private bountyCounter;

    // Event emitted when a new bounty is created
    event BountyCreated(
        uint256 bountyId,
        string description,
        uint256 rewardAmount,
        address indexed creator
    );

    // Event emitted when a bounty is completed
    event BountyCompleted(
        uint256 bountyId,
        address indexed winner,
        uint256 rewardAmount
    );

    // Modifier to check if the caller is the creator of a bounty
    modifier onlyCreator(uint256 bountyId) {
        require(
            msg.sender == bounties[bountyId].creator,
            "Caller is not the bounty creator"
        );
        _;
    }

    // Modifier to check if a bounty exists
    modifier bountyExists(uint256 bountyId) {
        require(
            bountyId < bountyCounter,
            "Bounty does not exist"
        );
        _;
    }

    /**
     * @dev Create a new bounty hunt.
     * @param description Description of the bounty hunt.
     */
    function createBounty(string calldata description) external payable {
        require(msg.value > 0, "Reward amount must be greater than 0");

        // Create a new bounty
        bounties[bountyCounter] = Bounty({
            description: description,
            rewardAmount: msg.value,
            creator: msg.sender,
            isCompleted: false,
            winner: address(0)
        });

        emit BountyCreated(bountyCounter, description, msg.value, msg.sender);

        // Increment bounty counter
        bountyCounter++;
    }

    /**
     * @dev Complete a bounty by selecting a winner.
     * @param bountyId ID of the bounty to complete.
     * @param winner Address of the bounty winner.
     */
    function completeBounty(uint256 bountyId, address winner)
        external
        bountyExists(bountyId)
        onlyCreator(bountyId)
    {
        Bounty storage bounty = bounties[bountyId];
        require(!bounty.isCompleted, "Bounty is already completed");

        // Mark bounty as completed and set the winner
        bounty.isCompleted = true;
        bounty.winner = winner;

        // Transfer reward to the winner
        (bool success, ) = winner.call{value: bounty.rewardAmount}("");
        require(success, "Reward transfer failed");

        emit BountyCompleted(bountyId, winner, bounty.rewardAmount);
    }

    /**
     * @dev Get details of a bounty.
     * @param bountyId ID of the bounty to retrieve.
     * @return Bounty details as a tuple.
     */
    function getBounty(uint256 bountyId)
        external
        view
        bountyExists(bountyId)
        returns (
            string memory description,
            uint256 rewardAmount,
            address creator,
            bool isCompleted,
            address winner
        )
    {
        Bounty memory bounty = bounties[bountyId];
        return (
            bounty.description,
            bounty.rewardAmount,
            bounty.creator,
            bounty.isCompleted,
            bounty.winner
        );
    }

    /**
     * @dev Get the total number of bounties created.
     * @return Total number of bounties.
     */
    function getTotalBounties() external view returns (uint256) {
        return bountyCounter;
    }

    /**
     * @dev Fallback function to prevent accidental Ether deposits.
     */
    fallback() external payable {
        revert("Use createBounty to deposit Ether");
    }

    /**
     * @dev Receive function to prevent accidental Ether deposits.
     */
    receive() external payable {
        revert("Use createBounty to deposit Ether");
    }
}
```
