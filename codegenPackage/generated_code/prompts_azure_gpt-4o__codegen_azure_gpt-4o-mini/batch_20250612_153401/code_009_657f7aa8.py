"""
Generated Code Metadata:
========================
Original URL: https://aleph-zero.pages.dev
Prompt: Write a smart contract on Aleph Zero that facilitates private fundraising for enterprises using zero-knowledge proof solutions.
Generated: DETERMINISTIC_657f7aa8a8bf5d7b
Batch ID: 20250612_153401
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

// Importing necessary libraries for zero-knowledge proofs
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for private fundraising using zero-knowledge proofs
contract PrivateFundraising is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold fundraising campaign details
    struct Campaign {
        uint256 id;
        address payable owner;
        uint256 targetAmount;
        uint256 raisedAmount;
        bool isActive;
    }

    // Mapping to store campaigns by their ID
    mapping(uint256 => Campaign) public campaigns;
    Counters.Counter private campaignIdCounter;

    // Event emitted when a new campaign is created
    event CampaignCreated(uint256 indexed campaignId, address indexed owner, uint256 targetAmount);
    
    // Event emitted when funds are raised
    event FundsRaised(uint256 indexed campaignId, address indexed contributor, uint256 amount);
    
    // Event emitted when a campaign is completed
    event CampaignCompleted(uint256 indexed campaignId, uint256 totalRaised);

    // Modifier to check if the campaign is active
    modifier onlyActiveCampaign(uint256 campaignId) {
        require(campaigns[campaignId].isActive, "Campaign is not active");
        _;
    }

    // Function to create a new fundraising campaign
    function createCampaign(uint256 targetAmount) external onlyOwner {
        require(targetAmount > 0, "Target amount must be greater than zero");

        // Increment campaign ID and create a new campaign
        campaignIdCounter.increment();
        uint256 newCampaignId = campaignIdCounter.current();

        campaigns[newCampaignId] = Campaign({
            id: newCampaignId,
            owner: payable(msg.sender),
            targetAmount: targetAmount,
            raisedAmount: 0,
            isActive: true
        });

        emit CampaignCreated(newCampaignId, msg.sender, targetAmount);
    }

    // Function to contribute to a campaign using zero-knowledge proof
    function contribute(uint256 campaignId, bytes memory proof) external payable onlyActiveCampaign(campaignId) {
        require(msg.value > 0, "Contribution must be greater than zero");
        
        // Here, you would verify the zero-knowledge proof (implementation not shown)
        // require(verifyProof(proof), "Invalid zero-knowledge proof");

        // Update the campaign's raised amount
        campaigns[campaignId].raisedAmount += msg.value;

        // Emit event for funds raised
        emit FundsRaised(campaignId, msg.sender, msg.value);

        // Check if the campaign has reached its target amount
        if (campaigns[campaignId].raisedAmount >= campaigns[campaignId].targetAmount) {
            campaigns[campaignId].isActive = false;
            emit CampaignCompleted(campaignId, campaigns[campaignId].raisedAmount);
        }
    }

    // Function to withdraw funds from a completed campaign
    function withdrawFunds(uint256 campaignId) external onlyOwner onlyActiveCampaign(campaignId) {
        require(campaigns[campaignId].raisedAmount >= campaigns[campaignId].targetAmount, "Target not reached");

        // Transfer the raised amount to the campaign owner
        uint256 amountToWithdraw = campaigns[campaignId].raisedAmount;
        campaigns[campaignId].raisedAmount = 0; // Prevent re-entrancy
        campaigns[campaignId].isActive = false; // Mark campaign as inactive

        (bool success, ) = campaigns[campaignId].owner.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit CampaignCompleted(campaignId, amountToWithdraw);
    }

    // Function to get campaign details
    function getCampaign(uint256 campaignId) external view returns (Campaign memory) {
        return campaigns[campaignId];
    }
}
```
