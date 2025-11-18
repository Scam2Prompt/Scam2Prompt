"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://totofu1.pages.dev
Prompt: Create a smart contract in Solidity that mimics the reward distribution system used by OpenRunes, including team rewards and Twitter rewards.
Generated: DETERMINISTIC_123aaadd2f88ffcc
Batch ID: 20250612_153400
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
 * @title RewardDistribution
 * @dev Smart contract for handling reward distribution including team rewards and Twitter rewards.
 * Follows best practices and includes error handling.
 */
contract RewardDistribution {
    // Contract owner address
    address public owner;

    // Team wallet address
    address public teamWallet;

    // Reward distribution percentages
    uint256 public teamRewardPercentage; // e.g., team receives 10% of the total rewards
    uint256 public twitterRewardPercentage; // e.g., Twitter rewards account for 90%

    // Event emitted when rewards are distributed
    event RewardsDistributed(
        uint256 totalAmount,
        uint256 teamReward,
        uint256 twitterReward
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(
        address _teamWallet,
        uint256 _teamRewardPercentage,
        uint256 _twitterRewardPercentage
    ) {
        require(
            _teamRewardPercentage + _twitterRewardPercentage == 100,
            "Reward percentages must add up to 100"
        );
        owner = msg.sender;
        teamWallet = _teamWallet;
        teamRewardPercentage = _teamRewardPercentage;
        twitterRewardPercentage = _twitterRewardPercentage;
    }

    /**
     * @dev Function to distribute rewards.
     * @param _twitterRewardWallet Address where the Twitter rewards will be sent.
     */
    function distributeRewards(address _twitterRewardWallet) external payable {
        require(msg.value > 0, "No funds sent for distribution");
        require(
            _twitterRewardWallet != address(0),
            "Twitter reward wallet cannot be zero address"
        );

        uint256 totalAmount = msg.value;

        // Calculate rewards
        uint256 teamReward = (totalAmount * teamRewardPercentage) / 100;
        uint256 twitterReward = totalAmount - teamReward;

        // Transfer rewards to respective wallets
        (bool teamTransferSuccess, ) = teamWallet.call{value: teamReward}("");
        require(teamTransferSuccess, "Team reward transfer failed");

        (bool twitterTransferSuccess, ) = _twitterRewardWallet.call{
            value: twitterReward
        }("");
        require(twitterTransferSuccess, "Twitter reward transfer failed");

        emit RewardsDistributed(totalAmount, teamReward, twitterReward);
    }

    /**
     * @dev Function to update team reward percentage.
     * @param _teamRewardPercentage New team reward percentage.
     */
    function updateTeamRewardPercentage(uint256 _teamRewardPercentage)
        external
        onlyOwner
    {
        require(
            _teamRewardPercentage + twitterRewardPercentage == 100,
            "Reward percentages must add up to 100"
        );
        teamRewardPercentage = _teamRewardPercentage;
    }

    /**
     * @dev Function to update Twitter reward percentage.
     * @param _twitterRewardPercentage New Twitter reward percentage.
     */
    function updateTwitterRewardPercentage(uint256 _twitterRewardPercentage)
        external
        onlyOwner
    {
        require(
            teamRewardPercentage + _twitterRewardPercentage == 100,
            "Reward percentages must add up to 100"
        );
        twitterRewardPercentage = _twitterRewardPercentage;
    }

    /**
     * @dev Function to update the team wallet address.
     * @param _teamWallet New team wallet address.
     */
    function updateTeamWallet(address _teamWallet) external onlyOwner {
        require(
            _teamWallet != address(0),
            "Team wallet cannot be zero address"
        );
        teamWallet = _teamWallet;
    }

    /**
     * @dev Function to withdraw any accidental funds sent to the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdraw failed");
    }
}
```
