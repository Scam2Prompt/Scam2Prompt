"""
Generated Code Metadata:
========================
Original URL: https://9aa9e9cd.dapp-a9y.pages.dev
Prompt: How can I implement a bug bounty program for my Web3 application based on the guidelines from HatsFinance?
Generated: DETERMINISTIC_a07197bded04f852
Batch ID: 20250612_163243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity implementation for a simple bug bounty program inspired by HatsFinance best practices:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Web3 Bug Bounty Program
 * @notice This contract implements a bug bounty program following security best practices
 * @dev Inherits from Ownable, ReentrancyGuard for security
 */
contract Web3BugBounty is Ownable, ReentrancyGuard {
    enum Severity { Low, Medium, High, Critical }
    
    struct Bounty {
        uint256 amount;
        bool paid;
        address submitter;
        string description;
        Severity severity;
        uint256 submissionTime;
    }

    // Bounty rewards by severity level
    mapping(Severity => uint256) public rewardTiers;
    // Active bounties
    Bounty[] public bounties;
    // Supported ERC20 token for rewards
    IERC20 public rewardToken;

    event BountySubmitted(uint256 indexed bountyId, address submitter, Severity severity);
    event BountyPaid(uint256 indexed bountyId, address submitter, uint256 amount);
    event RewardTokenChanged(address newToken);
    event RewardTiersUpdated();

    /**
     * @dev Constructor sets initial reward tiers and token
     * @param _rewardToken Address of ERC20 token used for rewards
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Token address cannot be zero");
        rewardToken = IERC20(_rewardToken);
        
        // Set initial reward tiers (amounts in token decimals)
        rewardTiers[Severity.Low] = 100 * 10**18;         // 100 tokens
        rewardTiers[Severity.Medium] = 500 * 10**18;      // 500 tokens
        rewardTiers[Severity.High] = 2000 * 10**18;       // 2000 tokens
        rewardTiers[Severity.Critical] = 10000 * 10**18;  // 10000 tokens
    }

    /**
     * @notice Submit a bug report
     * @param _description Detailed description of the bug
     * @param _severity Severity level of the bug
     * @return bountyId ID of the created bounty
     */
    function submitBounty(string calldata _description, Severity _severity) external returns (uint256 bountyId) {
        require(bytes(_description).length > 0, "Description cannot be empty");
        
        uint256 rewardAmount = rewardTiers[_severity];
        require(rewardAmount > 0, "Invalid severity level");
        
        bountyId = bounties.length;
        bounties.push(Bounty({
            amount: rewardAmount,
            paid: false,
            submitter: msg.sender,
            description: _description,
            severity: _severity,
            submissionTime: block.timestamp
        }));
        
        emit BountySubmitted(bountyId, msg.sender, _severity);
        return bountyId;
    }

    /**
     * @notice Approve and payout a bounty
     * @dev Only owner can call this function
     * @param _bountyId ID of the bounty to payout
     */
    function approveAndPayBounty(uint256 _bountyId) external onlyOwner nonReentrant {
        require(_bountyId < bounties.length, "Invalid bounty ID");
        Bounty storage bounty = bounties[_bountyId];
        require(!bounty.paid, "Bounty already paid");
        
        uint256 amount = bounty.amount;
        require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        bounty.paid = true;
        require(rewardToken.transfer(bounty.submitter, amount), "Token transfer failed");
        
        emit BountyPaid(_bountyId, bounty.submitter, amount);
    }

    /**
     * @notice Update reward tiers
     * @dev Only owner can call this function
     * @param _low Low severity reward amount
     * @param _medium Medium severity reward amount
     * @param _high High severity reward amount
     * @param _critical Critical severity reward amount
     */
    function updateRewardTiers(
        uint256 _low,
        uint256 _medium,
        uint256 _high,
        uint256 _critical
    ) external onlyOwner {
        rewardTiers[Severity.Low] = _low;
        rewardTiers[Severity.Medium] = _medium;
        rewardTiers[Severity.High] = _high;
        rewardTiers[Severity.Critical] = _critical;
        emit RewardTiersUpdated();
    }

    /**
     * @notice Change the reward token
     * @dev Only owner can call this function
     * @param _newToken Address of the new ERC20 token
     */
    function setRewardToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Token address cannot be zero");
        rewardToken = IERC20(_newToken);
        emit RewardTokenChanged(_newToken);
    }

    /**
     * @notice Withdraw funds from contract
     * @dev Only owner can call this function
     * @param _amount Amount to withdraw
     */
    function withdrawFunds(uint256 _amount) external onlyOwner nonReentrant {
        require(rewardToken.transfer(owner(), _amount), "Token transfer failed");
    }

    /**
     * @notice Get total bounties count
     * @return count Total bounties submitted
     */
    function getBountiesCount() external view returns (uint256 count) {
        return bounties.length;
    }

    /**
     * @notice Get contract token balance
     * @return balance Current token balance of contract
     */
    function getContractBalance() external view returns (uint256 balance) {
        return rewardToken.balanceOf(address(this));
    }
}
```
