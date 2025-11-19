"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Generate code for a blockchain-based pledge system using Ethereum smart contracts, referencing the ETH Pledge concept.
Generated: DETERMINISTIC_03ed50a757f30331
Batch ID: 20250612_152600
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**PledgeSystem.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";

/**
 * @title PledgeSystem
 * @author [Your Name]
 * @notice A blockchain-based pledge system using Ethereum smart contracts.
 */
contract PledgeSystem {
    // Mapping of pledge campaigns
    mapping (address => PledgeCampaign) public campaigns;

    // Mapping of user pledges
    mapping (address => mapping (address => Pledge)) public userPledges;

    // Event emitted when a new campaign is created
    event NewCampaign(address indexed creator, address indexed campaign);

    // Event emitted when a user makes a pledge
    event PledgeMade(address indexed user, address indexed campaign, uint256 amount);

    // Event emitted when a pledge is cancelled
    event PledgeCancelled(address indexed user, address indexed campaign);

    // Event emitted when a campaign is ended
    event CampaignEnded(address indexed creator, address indexed campaign, bool success);

    /**
     * @dev Struct representing a pledge campaign
     */
    struct PledgeCampaign {
        address creator;
        string name;
        string description;
        uint256 goal;
        uint256 deadline;
        bool active;
        mapping (address => Pledge) pledges;
        uint256 totalPledged;
    }

    /**
     * @dev Struct representing a user's pledge
     */
    struct Pledge {
        uint256 amount;
        bool cancelled;
    }

    /**
     * @dev Creates a new pledge campaign
     * @param _name Name of the campaign
     * @param _description Description of the campaign
     * @param _goal Funding goal of the campaign
     * @param _deadline Deadline for the campaign
     */
    function createCampaign(string memory _name, string memory _description, uint256 _goal, uint256 _deadline) public {
        require(_goal > 0, "Goal must be greater than 0");
        require(_deadline > block.timestamp, "Deadline must be in the future");

        PledgeCampaign memory campaign;
        campaign.creator = msg.sender;
        campaign.name = _name;
        campaign.description = _description;
        campaign.goal = _goal;
        campaign.deadline = _deadline;
        campaign.active = true;

        campaigns[msg.sender] = campaign;

        emit NewCampaign(msg.sender, msg.sender);
    }

    /**
     * @dev Makes a pledge to a campaign
     * @param _campaign Address of the campaign
     * @param _amount Amount of the pledge
     */
    function makePledge(address _campaign, uint256 _amount) public {
        require(campaigns[_campaign].active, "Campaign is not active");
        require(_amount > 0, "Pledge amount must be greater than 0");

        PledgeCampaign storage campaign = campaigns[_campaign];
        require(campaign.creator != msg.sender, "Cannot pledge to your own campaign");

        userPledges[msg.sender][_campaign].amount = _amount;
        userPledges[msg.sender][_campaign].cancelled = false;

        campaign.pledges[msg.sender].amount = _amount;
        campaign.pledges[msg.sender].cancelled = false;

        campaign.totalPledged += _amount;

        emit PledgeMade(msg.sender, _campaign, _amount);
    }

    /**
     * @dev Cancels a pledge
     * @param _campaign Address of the campaign
     */
    function cancelPledge(address _campaign) public {
        require(userPledges[msg.sender][_campaign].amount > 0, "No pledge to cancel");

        PledgeCampaign storage campaign = campaigns[_campaign];
        Pledge storage pledge = userPledges[msg.sender][_campaign];

        require(!pledge.cancelled, "Pledge already cancelled");

        pledge.cancelled = true;
        campaign.totalPledged -= pledge.amount;

        emit PledgeCancelled(msg.sender, _campaign);
    }

    /**
     * @dev Ends a campaign
     * @param _campaign Address of the campaign
     */
    function endCampaign(address _campaign) public {
        require(campaigns[_campaign].creator == msg.sender, "Only the creator can end the campaign");
        require(campaigns[_campaign].deadline <= block.timestamp, "Campaign deadline has not passed");

        PledgeCampaign storage campaign = campaigns[_campaign];

        if (campaign.totalPledged >= campaign.goal) {
            // Campaign successful, distribute funds
            // ...
        } else {
            // Campaign failed, refund pledges
            for (address user in campaign.pledges) {
                if (!campaign.pledges[user].cancelled) {
                    // Refund pledge
                    // ...
                }
            }
        }

        campaign.active = false;

        emit CampaignEnded(msg.sender, _campaign, campaign.totalPledged >= campaign.goal);
    }
}
```

**PledgeSystem.test.js**
```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("PledgeSystem", function () {
    let pledgeSystem;

    beforeEach(async () => {
        const PledgeSystem = await ethers.getContractFactory("PledgeSystem");
        pledgeSystem = await PledgeSystem.deploy();
        await pledgeSystem.deployed();
    });

    it("Should create a new campaign", async () => {
        const name = "Test Campaign";
        const description = "This is a test campaign";
        const goal = 1000;
        const deadline = Math.floor(Date.now() / 1000) + 30 * 24 * 60 * 60;

        await pledgeSystem.createCampaign(name, description, goal, deadline);

        const campaign = await pledgeSystem.campaigns(pledgeSystem.address);
        expect(campaign.name).to.equal(name);
        expect(campaign.description).to.equal(description);
        expect(campaign.goal).to.equal(goal);
        expect(campaign.deadline).to.equal(deadline);
    });

    it("Should make a pledge to a campaign", async () => {
        const campaignAddress = pledgeSystem.address;
        const amount = 100;

        await pledgeSystem.makePledge(campaignAddress, amount);

        const pledge = await pledgeSystem.userPledges(pledgeSystem.address, campaignAddress);
        expect(pledge.amount).to.equal(amount);
    });

    it("Should cancel a pledge", async () => {
        const campaignAddress = pledgeSystem.address;
        const amount = 100;

        await pledgeSystem.makePledge(campaignAddress, amount);
        await pledgeSystem.cancelPledge(campaignAddress);

        const pledge = await pledgeSystem.userPledges(pledgeSystem.address, campaignAddress);
        expect(pledge.cancelled).to.equal(true);
    });

    it("Should end a campaign", async () => {
        const name = "Test Campaign";
        const description = "This is a test campaign";
        const goal = 1000;
        const deadline = Math.floor(Date.now() / 1000) + 30 * 24 * 60 * 60;

        await pledgeSystem.createCampaign(name, description, goal, deadline);

        const campaignAddress = pledgeSystem.address;
        const amount = 100;

        await pledgeSystem.makePledge(campaignAddress, amount);

        await ethers.provider.send("evm_increaseTime", [30 * 24 * 60 * 60]);
        await pledgeSystem.endCampaign(campaignAddress);

        const campaign = await pledgeSystem.campaigns(campaignAddress);
        expect(campaign.active).to.equal(false);
    });
});
```
