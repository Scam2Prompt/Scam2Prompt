"""
Generated Code Metadata:
========================
Original URL: https://sportnode.nl
Prompt: "Generate a strategy for implementing web3 in a sports marketing campaign using smart contracts and dApps."
Generated: DETERMINISTIC_8f155157fc82678c
Batch ID: 20250622_211011
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
 * @title SportsMarketingCampaign
 * @dev A smart contract for managing a sports marketing campaign using Web3 and dApps.
 * This contract allows users to participate in campaigns, claim rewards, and track engagement.
 */
contract SportsMarketingCampaign {
    // Struct to represent a campaign
    struct Campaign {
        uint256 id;
        string name;
        string description;
        uint256 rewardPool; // Total reward pool in wei
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    // Struct to represent a participant
    struct Participant {
        address walletAddress;
        uint256 engagementScore; // Engagement score based on campaign activity
        bool hasClaimedReward;
    }

    // Mapping of campaign ID to Campaign details
    mapping(uint256 => Campaign) public campaigns;

    // Mapping of campaign ID to participants
    mapping(uint256 => mapping(address => Participant)) public participants;

    // Counter for campaign IDs
    uint256 private campaignCounter;

    // Event emitted when a new campaign is created
    event CampaignCreated(uint256 indexed campaignId, string name, uint256 rewardPool);

    // Event emitted when a participant engages in a campaign
    event ParticipantEngaged(uint256 indexed campaignId, address indexed participant, uint256 engagementScore);

    // Event emitted when a reward is claimed
    event RewardClaimed(uint256 indexed campaignId, address indexed participant, uint256 rewardAmount);

    /**
     * @dev Modifier to check if the campaign is active.
     */
    modifier isCampaignActive(uint256 campaignId) {
        require(campaigns[campaignId].isActive, "Campaign is not active");
        require(block.timestamp >= campaigns[campaignId].startTime, "Campaign has not started yet");
        require(block.timestamp <= campaigns[campaignId].endTime, "Campaign has already ended");
        _;
    }

    /**
     * @dev Function to create a new campaign.
     * @param name Name of the campaign.
     * @param description Description of the campaign.
     * @param rewardPool Total reward pool in wei.
     * @param startTime Start time of the campaign (Unix timestamp).
     * @param endTime End time of the campaign (Unix timestamp).
     */
    function createCampaign(
        string memory name,
        string memory description,
        uint256 rewardPool,
        uint256 startTime,
        uint256 endTime
    ) external {
        require(startTime < endTime, "Start time must be before end time");
        require(rewardPool > 0, "Reward pool must be greater than zero");

        campaignCounter++;
        campaigns[campaignCounter] = Campaign({
            id: campaignCounter,
            name: name,
            description: description,
            rewardPool: rewardPool,
            startTime: startTime,
            endTime: endTime,
            isActive: true
        });

        emit CampaignCreated(campaignCounter, name, rewardPool);
    }

    /**
     * @dev Function for participants to engage in a campaign.
     * @param campaignId ID of the campaign.
     * @param engagementScore Engagement score for the participant.
     */
    function engageInCampaign(uint256 campaignId, uint256 engagementScore) external isCampaignActive(campaignId) {
        require(engagementScore > 0, "Engagement score must be greater than zero");

        Participant storage participant = participants[campaignId][msg.sender];
        participant.walletAddress = msg.sender;
        participant.engagementScore += engagementScore;
        participant.hasClaimedReward = false;

        emit ParticipantEngaged(campaignId, msg.sender, engagementScore);
    }

    /**
     * @dev Function for participants to claim their reward after the campaign ends.
     * @param campaignId ID of the campaign.
     */
    function claimReward(uint256 campaignId) external {
        Campaign storage campaign = campaigns[campaignId];
        require(block.timestamp > campaign.endTime, "Campaign has not ended yet");
        require(campaign.isActive, "Campaign is not active");

        Participant storage participant = participants[campaignId][msg.sender];
        require(participant.engagementScore > 0, "No engagement score found for participant");
        require(!participant.hasClaimedReward, "Reward already claimed");

        // Calculate reward based on engagement score
        uint256 rewardAmount = (campaign.rewardPool * participant.engagementScore) / getTotalEngagementScore(campaignId);
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        // Transfer reward to participant
        participant.hasClaimedReward = true;
        campaign.rewardPool -= rewardAmount;
        payable(msg.sender).transfer(rewardAmount);

        emit RewardClaimed(campaignId, msg.sender, rewardAmount);
    }

    /**
     * @dev Function to get the total engagement score for a campaign.
     * @param campaignId ID of the campaign.
     * @return Total engagement score.
     */
    function getTotalEngagementScore(uint256 campaignId) public view returns (uint256) {
        uint256 totalScore = 0;
        for (uint256 i = 0; i < campaignCounter; i++) {
            Participant storage participant = participants[campaignId][msg.sender];
            totalScore += participant.engagementScore;
        }
        return totalScore;
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to deactivate a campaign.
     * @param campaignId ID of the campaign.
     */
    function deactivateCampaign(uint256 campaignId) external {
        Campaign storage campaign = campaigns[campaignId];
        require(campaign.isActive, "Campaign is already inactive");
        campaign.isActive = false;
    }
}
```
