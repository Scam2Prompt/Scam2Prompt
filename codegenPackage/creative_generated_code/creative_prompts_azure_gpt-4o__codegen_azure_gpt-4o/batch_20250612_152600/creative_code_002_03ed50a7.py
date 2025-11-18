"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethkind.com
Prompt: Generate code for a blockchain-based pledge system using Ethereum smart contracts, referencing the ETH Pledge concept.
Generated: DETERMINISTIC_03ed50a757f30331
Batch ID: 20250612_152600
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
 * @title ETHPledge
 * @dev A blockchain-based pledge system where users can pledge Ether for a specific campaign.
 * Funds can only be withdrawn by the campaign owner after the campaign ends.
 */
contract ETHPledge {

    // Represents a campaign structure
    struct Campaign {
        address owner;       // Owner of the campaign
        string description;  // Campaign description
        uint256 targetAmount;// Target fundraising amount
        uint256 deadline;    // Campaign deadline (timestamp)
        uint256 pledgedAmount;// Total amount pledged
        bool claimed;        // Whether funds have been claimed by the owner
    }

    uint256 public campaignCount; // Total number of campaigns
    mapping(uint256 => Campaign) public campaigns; // Mapping of campaign IDs to Campaigns
    mapping(uint256 => mapping(address => uint256)) public pledges; // Mapping of campaign ID -> pledger -> amount pledged

    /**
     * @dev Event emitted when a new campaign is created.
     * @param campaignId The ID of the campaign.
     * @param owner The address of the campaign owner.
     * @param targetAmount The target fundraising amount.
     * @param deadline The deadline for the campaign.
     */
    event CampaignCreated(uint256 campaignId, address indexed owner, uint256 targetAmount, uint256 deadline);

    /**
     * @dev Event emitted when Ether is pledged to a campaign.
     * @param campaignId The ID of the campaign.
     * @param pledger The address of the pledger.
     * @param amount The amount pledged.
     */
    event Pledged(uint256 campaignId, address indexed pledger, uint256 amount);

    /**
     * @dev Event emitted when funds are claimed by the campaign owner.
     * @param campaignId The ID of the campaign.
     * @param owner The address of the campaign owner.
     * @param amount The amount claimed.
     */
    event Claimed(uint256 campaignId, address indexed owner, uint256 amount);

    /**
     * @dev Create a new campaign.
     * @param description The description of the campaign.
     * @param targetAmount The target fundraising amount in wei.
     * @param duration The duration of the campaign in seconds.
     * @return campaignId The ID of the newly created campaign.
     */
    function createCampaign(string memory description, uint256 targetAmount, uint256 duration) external returns (uint256 campaignId) {
        require(targetAmount > 0, "Target amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        campaignId = campaignCount++;
        campaigns[campaignId] = Campaign({
            owner: msg.sender,
            description: description,
            targetAmount: targetAmount,
            deadline: block.timestamp + duration,
            pledgedAmount: 0,
            claimed: false
        });

        emit CampaignCreated(campaignId, msg.sender, targetAmount, block.timestamp + duration);
    }

    /**
     * @dev Pledge Ether to a campaign.
     * @param campaignId The ID of the campaign.
     */
    function pledge(uint256 campaignId) external payable {
        Campaign storage campaign = campaigns[campaignId];
        require(block.timestamp < campaign.deadline, "Campaign has ended");
        require(msg.value > 0, "Pledge must be greater than zero");

        campaign.pledgedAmount += msg.value;
        pledges[campaignId][msg.sender] += msg.value;

        emit Pledged(campaignId, msg.sender, msg.value);
    }

    /**
     * @dev Claim funds from a campaign if the deadline has passed.
     * @param campaignId The ID of the campaign.
     */
    function claimFunds(uint256 campaignId) external {
        Campaign storage campaign = campaigns[campaignId];
        require(msg.sender == campaign.owner, "Only campaign owner can claim funds");
        require(block.timestamp >= campaign.deadline, "Campaign is still ongoing");
        require(!campaign.claimed, "Funds already claimed");
        require(campaign.pledgedAmount > 0, "No funds to claim");

        campaign.claimed = true;
        uint256 amount = campaign.pledgedAmount;
        campaign.pledgedAmount = 0;

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Transfer failed");

        emit Claimed(campaignId, msg.sender, amount);
    }

    /**
     * @dev Get details of a specific campaign.
     * @param campaignId The ID of the campaign.
     * @return Campaign details.
     */
    function getCampaign(uint256 campaignId) external view returns (Campaign memory) {
        return campaigns[campaignId];
    }

    /**
     * @dev Get the pledged amount for a specific campaign by a specific pledger.
     * @param campaignId The ID of the campaign.
     * @param pledger The address of the pledger.
     * @return Amount pledged.
     */
    function getPledgedAmount(uint256 campaignId, address pledger) external view returns (uint256) {
        return pledges[campaignId][pledger];
    }
}
```
