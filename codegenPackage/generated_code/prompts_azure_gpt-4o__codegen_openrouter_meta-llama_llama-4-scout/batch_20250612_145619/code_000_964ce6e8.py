"""
Generated Code Metadata:
========================
Original URL: https://ethphb.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledge system, ensuring compatibility with the features described on ETH Pledge.
Generated: DETERMINISTIC_964ce6e85490bea2
Batch ID: 20250612_145619
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title PledgeSystem
 * @author [Your Name]
 * @notice Ethereum-based pledge system
 */
contract PledgeSystem is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of pledgers to their pledge information
    mapping (address => Pledger) public pledgers;

    // Mapping of campaigns to their information
    mapping (address => Campaign) public campaigns;

    // Mapping of campaign IDs to their existence
    mapping (uint256 => bool) public campaignExists;

    // Event emitted when a new campaign is created
    event NewCampaign(address indexed creator, uint256 indexed campaignId);

    // Event emitted when a pledger makes a pledge
    event PledgeMade(address indexed pledger, uint256 indexed campaignId, uint256 amount);

    // Event emitted when a campaign is completed
    event CampaignCompleted(uint256 indexed campaignId);

    // Event emitted when a campaign is cancelled
    event CampaignCancelled(uint256 indexed campaignId);

    // Struct to represent a pledger
    struct Pledger {
        uint256 pledgeAmount;
        bool hasPledged;
    }

    // Struct to represent a campaign
    struct Campaign {
        address creator;
        uint256 goal;
        uint256 pledged;
        uint256 deadline;
        bool isActive;
        bool isCompleted;
    }

    // Create a new campaign
    function createCampaign(uint256 _goal, uint256 _deadline) public {
        require(_goal > 0, "Goal must be greater than 0");
        require(_deadline > block.timestamp, "Deadline must be in the future");

        uint256 campaignId = uint256(keccak256(abi.encodePacked(msg.sender, _goal, _deadline)));

        require(!campaignExists[campaignId], "Campaign already exists");

        campaigns[address(this)] = Campaign(
            msg.sender,
            _goal,
            0,
            _deadline,
            true,
            false
        );

        campaignExists[campaignId] = true;

        emit NewCampaign(msg.sender, campaignId);
    }

    // Make a pledge to a campaign
    function makePledge(uint256 _campaignId, uint256 _amount) public {
        Campaign storage campaign = campaigns[address(this)];
        require(campaign.isActive, "Campaign is not active");
        require(campaign.deadline > block.timestamp, "Campaign deadline has passed");
        require(_amount > 0, "Pledge amount must be greater than 0");

        Pledger storage pledger = pledgers[msg.sender];
        if (pledger.hasPledged) {
            pledger.pledgeAmount = pledger.pledgeAmount.add(_amount);
        } else {
            pledger.pledgeAmount = _amount;
            pledger.hasPledged = true;
        }

        campaign.pledged = campaign.pledged.add(_amount);

        emit PledgeMade(msg.sender, _campaignId, _amount);

        // Check if campaign goal is reached
        if (campaign.pledged >= campaign.goal) {
            campaign.isActive = false;
            campaign.isCompleted = true;

            emit CampaignCompleted(_campaignId);
        }
    }

    // Cancel a campaign
    function cancelCampaign(uint256 _campaignId) public {
        Campaign storage campaign = campaigns[address(this)];
        require(campaign.creator == msg.sender, "Only the creator can cancel the campaign");
        require(campaign.isActive, "Campaign is not active");

        campaign.isActive = false;

        emit CampaignCancelled(_campaignId);
    }

    // Withdraw pledge
    function withdrawPledge(uint256 _campaignId) public {
        Pledger storage pledger = pledgers[msg.sender];
        require(pledger.hasPledged, "Pledger has not made a pledge");

        Campaign storage campaign = campaigns[address(this)];
        require(!campaign.isActive, "Campaign is still active");

        uint256 amount = pledger.pledgeAmount;
        pledger.pledgeAmount = 0;
        pledger.hasPledged = false;

        // Transfer pledge amount to pledger
        IERC20(0x...).safeTransfer(msg.sender, amount);
    }

    // Claim pledge
    function claimPledge(uint256 _campaignId) public {
        Campaign storage campaign = campaigns[address(this)];
        require(campaign.creator == msg.sender, "Only the creator can claim the pledge");
        require(campaign.isCompleted, "Campaign is not completed");

        uint256 amount = campaign.pledged;
        campaign.pledged = 0;

        // Transfer pledge amount to creator
        IERC20(0x...).safeTransfer(msg.sender, amount);
    }
}
```
