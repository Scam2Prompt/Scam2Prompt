"""
Generated Code Metadata:
========================
Original URL: https://everyworld4.pages.dev
Prompt: How can I implement a web3 rewarded ads discovery protocol similar to Everyworld that allows users to earn points and win rewards for environmental charities?
Generated: DETERMINISTIC_9a9c43930ef46b8f
Batch ID: 20250612_161224
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract EcoRewardProtocol is Ownable, ReentrancyGuard {
    // Structs
    struct AdCampaign {
        address advertiser;
        uint256 budget;
        uint256 rewardPerView;
        uint256 totalViews;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    struct User {
        uint256 points;
        uint256 lastInteraction;
        address chosenCharity;
    }

    // State variables
    mapping(uint256 => AdCampaign) public adCampaigns;
    mapping(address => User) public users;
    mapping(address => bool) public approvedCharities;
    address[] public charityList;
    
    uint256 public campaignCounter;
    uint256 public cooldownPeriod = 1 hours;
    IERC20 public rewardToken;

    // Events
    event CampaignCreated(
        uint256 indexed campaignId,
        address indexed advertiser,
        uint256 budget,
        uint256 rewardPerView
    );
    event AdViewed(
        uint256 indexed campaignId,
        address indexed user,
        uint256 reward
    );
    event RewardClaimed(
        address indexed user,
        address indexed charity,
        uint256 amount
    );
    event CharityAdded(address indexed charity);
    event CharityRemoved(address indexed charity);

    // Constructor
    constructor(address _rewardToken) {
        rewardToken = IERC20(_rewardToken);
    }

    // Modifiers
    modifier validCampaign(uint256 _campaignId) {
        require(_campaignId < campaignCounter, "Invalid campaign ID");
        require(adCampaigns[_campaignId].isActive, "Campaign not active");
        require(
            block.timestamp >= adCampaigns[_campaignId].startTime,
            "Campaign not started"
        );
        require(
            block.timestamp <= adCampaigns[_campaignId].endTime,
            "Campaign ended"
        );
        _;
    }

    // Admin functions
    function addCharity(address _charity) external onlyOwner {
        require(!approvedCharities[_charity], "Charity already added");
        approvedCharities[_charity] = true;
        charityList.push(_charity);
        emit CharityAdded(_charity);
    }

    function removeCharity(address _charity) external onlyOwner {
        require(approvedCharities[_charity], "Charity not found");
        approvedCharities[_charity] = false;
        emit CharityRemoved(_charity);
    }

    function setCooldownPeriod(uint256 _cooldown) external onlyOwner {
        cooldownPeriod = _cooldown;
    }

    // Advertiser functions
    function createCampaign(
        uint256 _budget,
        uint256 _rewardPerView,
        uint256 _duration
    ) external {
        require(_budget > 0, "Budget must be positive");
        require(_rewardPerView > 0, "Reward must be positive");
        require(
            rewardToken.transferFrom(msg.sender, address(this), _budget),
            "Token transfer failed"
        );

        uint256 campaignId = campaignCounter++;
        adCampaigns[campaignId] = AdCampaign({
            advertiser: msg.sender,
            budget: _budget,
            rewardPerView: _rewardPerView,
            totalViews: 0,
            startTime: block.timestamp,
            endTime: block.timestamp + _duration,
            isActive: true
        });

        emit CampaignCreated(campaignId, msg.sender, _budget, _rewardPerView);
    }

    function endCampaign(uint256 _campaignId) external {
        require(_campaignId < campaignCounter, "Invalid campaign ID");
        require(
            msg.sender == adCampaigns[_campaignId].advertiser,
            "Only advertiser can end campaign"
        );
        require(adCampaigns[_campaignId].isActive, "Campaign already ended");

        adCampaigns[_campaignId].isActive = false;
        uint256 remainingBudget = adCampaigns[_campaignId].budget -
            (adCampaigns[_campaignId].totalViews * adCampaigns[_campaignId].rewardPerView);

        if (remainingBudget > 0) {
            rewardToken.transfer(
                adCampaigns[_campaignId].advertiser,
                remainingBudget
            );
        }
    }

    // User functions
    function viewAd(uint256 _campaignId) external validCampaign(_campaignId) nonReentrant {
        User storage user = users[msg.sender];
        AdCampaign storage campaign = adCampaigns[_campaignId];

        require(
            block.timestamp >= user.lastInteraction + cooldownPeriod,
            "Cooldown period not passed"
        );

        uint256 reward = campaign.rewardPerView;
        require(campaign.budget >= reward, "Campaign budget exhausted");

        campaign.budget -= reward;
        campaign.totalViews += 1;
        user.points += reward;
        user.lastInteraction = block.timestamp;

        emit AdViewed(_campaignId, msg.sender, reward);
    }

    function selectCharity(address _charity) external {
        require(approvedCharities[_charity], "Charity not approved");
        users[msg.sender].chosenCharity = _charity;
    }

    function claimRewards() external nonReentrant {
        User storage user = users[msg.sender];
        require(user.points > 0, "No rewards to claim");
        require(user.chosenCharity != address(0), "No charity selected");

        uint256 rewardAmount = user.points;
        user.points = 0;

        require(
            rewardToken.transfer(user.chosenCharity, rewardAmount),
            "Token transfer failed"
        );

        emit RewardClaimed(msg.sender, user.chosenCharity, rewardAmount);
    }

    // View functions
    function getActiveCampaigns() external view returns (uint256[] memory) {
        uint256 count = 0;
        for (uint256 i = 0; i < campaignCounter; i++) {
            if (
                adCampaigns[i].isActive &&
                block.timestamp >= adCampaigns[i].startTime &&
                block.timestamp <= adCampaigns[i].endTime
            ) {
                count++;
            }
        }

        uint256[] memory activeCampaigns = new uint256[](count);
        uint256 index = 0;
        for (uint256 i = 0; i < campaignCounter; i++) {
            if (
                adCampaigns[i].isActive &&
                block.timestamp >= adCampaigns[i].startTime &&
                block.timestamp <= adCampaigns[i].endTime
            ) {
                activeCampaigns[index] = i;
                index++;
            }
        }
        return activeCampaigns;
    }

    function getCharityList() external view returns (address[] memory) {
        return charityList;
    }
}
```
