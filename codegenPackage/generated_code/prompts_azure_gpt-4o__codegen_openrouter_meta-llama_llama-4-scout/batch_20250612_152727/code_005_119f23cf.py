"""
Generated Code Metadata:
========================
Original URL: https://synthethicdapp.pages.dev
Prompt: Write a smart contract for managing airdrops in a decentralized application, incorporating the synthetic protocol features described on the "Dapps Leading Synthetic Protocol" platform.
Generated: DETERMINISTIC_119f23cf3a3cc26c
Batch ID: 20250612_152727
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title AirdropManager Contract
 * @author [Your Name]
 * @notice Manages airdrops for a decentralized application
 */
contract AirdropManager is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Mapping of airdrop campaigns to their respective details
    mapping(address => AirdropCampaign) public airdropCampaigns;

    // Mapping of user claim status for each campaign
    mapping(address => mapping(address => bool)) public userClaims;

    /**
     * @dev Struct representing an airdrop campaign
     */
    struct AirdropCampaign {
        address token; // Token being airdropped
        uint256 totalAmount; // Total amount of tokens to be airdropped
        uint256 claimedAmount; // Amount of tokens already claimed
        uint256 startTime; // Start time of the campaign
        uint256 endTime; // End time of the campaign
        uint256 maxClaimPerUser; // Maximum amount that can be claimed per user
        address[] eligibleUsers; // List of eligible users for the campaign
    }

    /**
     * @dev Event emitted when a new airdrop campaign is created
     * @param campaignId ID of the new campaign
     * @param token Token being airdropped
     * @param totalAmount Total amount of tokens to be airdropped
     * @param startTime Start time of the campaign
     * @param endTime End time of the campaign
     * @param maxClaimPerUser Maximum amount that can be claimed per user
     */
    event NewCampaign(address indexed campaignId, address token, uint256 totalAmount, uint256 startTime, uint256 endTime, uint256 maxClaimPerUser);

    /**
     * @dev Event emitted when a user claims tokens from an airdrop campaign
     * @param campaignId ID of the campaign
     * @param user User claiming tokens
     * @param amount Amount of tokens claimed
     */
    event TokensClaimed(address indexed campaignId, address indexed user, uint256 amount);

    /**
     * @dev Creates a new airdrop campaign
     * @param _token Token being airdropped
     * @param _totalAmount Total amount of tokens to be airdropped
     * @param _startTime Start time of the campaign
     * @param _endTime End time of the campaign
     * @param _maxClaimPerUser Maximum amount that can be claimed per user
     * @param _eligibleUsers List of eligible users for the campaign
     */
    function createCampaign(address _token, uint256 _totalAmount, uint256 _startTime, uint256 _endTime, uint256 _maxClaimPerUser, address[] memory _eligibleUsers) public onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_totalAmount > 0, "Total amount must be greater than 0");
        require(_startTime < _endTime, "Invalid campaign duration");

        AirdropCampaign memory campaign;
        campaign.token = _token;
        campaign.totalAmount = _totalAmount;
        campaign.startTime = _startTime;
        campaign.endTime = _endTime;
        campaign.maxClaimPerUser = _maxClaimPerUser;
        campaign.eligibleUsers = _eligibleUsers;

        airdropCampaigns[_token] = campaign;

        emit NewCampaign(_token, _token, _totalAmount, _startTime, _endTime, _maxClaimPerUser);
    }

    /**
     * @dev Claims tokens from an airdrop campaign
     * @param _campaignId ID of the campaign
     * @param _amount Amount of tokens to claim
     */
    function claimTokens(address _campaignId, uint256 _amount) public nonReentrant {
        AirdropCampaign storage campaign = airdropCampaigns[_campaignId];
        require(campaign.token != address(0), "Campaign not found");
        require(campaign.startTime <= block.timestamp && block.timestamp <= campaign.endTime, "Campaign not active");
        require(userClaims[msg.sender][_campaignId] == false, "User has already claimed tokens");
        require(_amount > 0 && _amount <= campaign.maxClaimPerUser, "Invalid claim amount");

        // Check if user is eligible
        for (uint256 i = 0; i < campaign.eligibleUsers.length; i++) {
            if (campaign.eligibleUsers[i] == msg.sender) {
                // Update claimed amount and user claim status
                campaign.claimedAmount += _amount;
                userClaims[msg.sender][_campaignId] = true;

                // Transfer tokens to user
                IERC20(campaign.token).safeTransfer(msg.sender, _amount);

                emit TokensClaimed(_campaignId, msg.sender, _amount);

                return;
            }
        }

        revert("User is not eligible for this campaign");
    }

    /**
     * @dev Updates the eligible users for an airdrop campaign
     * @param _campaignId ID of the campaign
     * @param _newEligibleUsers New list of eligible users
     */
    function updateEligibleUsers(address _campaignId, address[] memory _newEligibleUsers) public onlyOwner {
        AirdropCampaign storage campaign = airdropCampaigns[_campaignId];
        require(campaign.token != address(0), "Campaign not found");

        campaign.eligibleUsers = _newEligibleUsers;
    }

    /**
     * @dev Withdraws remaining tokens from an airdrop campaign
     * @param _campaignId ID of the campaign
     */
    function withdrawRemainingTokens(address _campaignId) public onlyOwner nonReentrant {
        AirdropCampaign storage campaign = airdropCampaigns[_campaignId];
        require(campaign.token != address(0), "Campaign not found");

        uint256 remainingTokens = campaign.totalAmount - campaign.claimedAmount;
        IERC20(campaign.token).safeTransfer(msg.sender, remainingTokens);

        // Delete campaign
        delete airdropCampaigns[_campaignId];
    }
}
```
