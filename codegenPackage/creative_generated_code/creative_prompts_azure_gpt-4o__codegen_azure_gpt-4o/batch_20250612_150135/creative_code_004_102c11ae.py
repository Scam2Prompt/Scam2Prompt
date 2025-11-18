"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vivalalibertadproject.com
Prompt: Provide a step-by-step guide to integrate the $LIBRA token into a crowdfunding platform, ensuring efficient and decentralized funding for Argentine startups and educational initiatives.
Generated: DETERMINISTIC_102c11aeb52e0e7c
Batch ID: 20250612_150135
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
 * @title CrowdfundingPlatform
 * @dev A decentralized crowdfunding platform that integrates the $LIBRA token for funding Argentine startups and educational initiatives.
 */
contract CrowdfundingPlatform {
    // Struct to represent a crowdfunding campaign
    struct Campaign {
        address payable creator;    // Address of the campaign creator
        string title;               // Title of the campaign
        string description;         // Description of the campaign
        uint256 goal;               // Funding goal in $LIBRA tokens
        uint256 deadline;           // Deadline for the campaign
        uint256 fundsRaised;        // Total funds raised in $LIBRA tokens
        bool completed;             // Whether the campaign is completed
    }

    // State variables
    address public libraTokenAddress;     // The $LIBRA token contract address
    Campaign[] public campaigns;          // List of all campaigns

    // Events
    event CampaignCreated(uint256 campaignId, address creator, uint256 goal, uint256 deadline);
    event DonationReceived(uint256 campaignId, address donor, uint256 amount);
    event CampaignCompleted(uint256 campaignId);

    /**
     * @dev Constructor to initialize the $LIBRA token address.
     * @param _libraTokenAddress Address of the deployed $LIBRA token contract.
     */
    constructor(address _libraTokenAddress) {
        require(_libraTokenAddress != address(0), "Invalid token address");
        libraTokenAddress = _libraTokenAddress;
    }

    /**
     * @dev Function to create a new crowdfunding campaign.
     * @param _title Title of the campaign.
     * @param _description Description of the campaign.
     * @param _goal Funding goal in $LIBRA tokens.
     * @param _duration Duration of the campaign in seconds from the current time.
     */
    function createCampaign(
        string memory _title,
        string memory _description,
        uint256 _goal,
        uint256 _duration
    ) external {
        require(_goal > 0, "Goal must be greater than zero");
        require(_duration > 0, "Duration must be greater than zero");

        uint256 deadline = block.timestamp + _duration;

        campaigns.push(
            Campaign({
                creator: payable(msg.sender),
                title: _title,
                description: _description,
                goal: _goal,
                deadline: deadline,
                fundsRaised: 0,
                completed: false
            })
        );

        emit CampaignCreated(campaigns.length - 1, msg.sender, _goal, deadline);
    }

    /**
     * @dev Function to donate $LIBRA tokens to a campaign.
     * @param _campaignId ID of the campaign to donate to.
     * @param _amount Amount of $LIBRA tokens to donate.
     */
    function donate(uint256 _campaignId, uint256 _amount) external {
        require(_campaignId < campaigns.length, "Invalid campaign ID");
        Campaign storage campaign = campaigns[_campaignId];
        require(block.timestamp < campaign.deadline, "Campaign has expired");
        require(!campaign.completed, "Campaign is already completed");
        require(_amount > 0, "Donation amount must be greater than zero");

        // Transfer $LIBRA tokens from donor to the contract
        IERC20(libraTokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Update campaign funds raised
        campaign.fundsRaised += _amount;

        emit DonationReceived(_campaignId, msg.sender, _amount);
    }

    /**
     * @dev Function to complete a campaign if the funding goal is reached.
     * @param _campaignId ID of the campaign to complete.
     */
    function completeCampaign(uint256 _campaignId) external {
        require(_campaignId < campaigns.length, "Invalid campaign ID");
        Campaign storage campaign = campaigns[_campaignId];
        require(block.timestamp >= campaign.deadline, "Campaign is still active");
        require(!campaign.completed, "Campaign is already completed");
        require(campaign.fundsRaised >= campaign.goal, "Funding goal not met");

        // Transfer raised funds to the campaign creator
        IERC20(libraTokenAddress).transfer(campaign.creator, campaign.fundsRaised);

        // Mark campaign as completed
        campaign.completed = true;

        emit CampaignCompleted(_campaignId);
    }

    /**
     * @dev Fetch the total number of campaigns.
     * @return Total number of campaigns.
     */
    function getCampaignCount() external view returns (uint256) {
        return campaigns.length;
    }
}

// Interface for the $LIBRA token contract (ERC20 standard)
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
