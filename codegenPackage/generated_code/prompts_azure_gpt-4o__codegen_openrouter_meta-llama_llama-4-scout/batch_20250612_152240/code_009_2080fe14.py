"""
Generated Code Metadata:
========================
Original URL: https://bamboomeme.pages.dev
Prompt: Create a Solidity contract for a meme token that includes a community reward system, inspired by `$BAMBOO`'s claim reward feature.
Generated: DETERMINISTIC_2080fe14c5693ec8
Batch ID: 20250612_152240
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MemeToken
 * @author [Your Name]
 * @notice A meme token with a community reward system.
 */
contract MemeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user claim rewards
    mapping(address => uint256) private _claimRewards;

    // Mapping of user community contributions
    mapping(address => uint256) private _communityContributions;

    // Total community contributions
    uint256 private _totalCommunityContributions;

    // Reward per contribution
    uint256 public rewardPerContribution;

    // Contribution threshold for reward claim
    uint256 public contributionThreshold;

    /**
     * @notice Constructor for MemeToken.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param rewardPerContribution_ The reward per contribution.
     * @param contributionThreshold_ The contribution threshold for reward claim.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 rewardPerContribution_,
        uint256 contributionThreshold_
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        rewardPerContribution = rewardPerContribution_;
        contributionThreshold = contributionThreshold_;
    }

    /**
     * @notice Contribute to the community and earn rewards.
     * @param amount The amount to contribute.
     */
    function contribute(uint256 amount) external nonReentrant {
        require(amount > 0, "Contribution amount must be greater than 0");

        _communityContributions[msg.sender] = _communityContributions[msg.sender].add(amount);
        _totalCommunityContributions = _totalCommunityContributions.add(amount);

        // Check if contribution threshold is met for reward claim
        if (_communityContributions[msg.sender] >= contributionThreshold) {
            _claimRewards[msg.sender] = _claimRewards[msg.sender].add(rewardPerContribution);
        }

        emit Contribution(msg.sender, amount);
    }

    /**
     * @notice Claim reward.
     */
    function claimReward() external nonReentrant {
        require(_claimRewards[msg.sender] > 0, "No reward to claim");

        uint256 reward = _claimRewards[msg.sender];
        _claimRewards[msg.sender] = 0;

        _mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Get user claim reward.
     * @param user The user's address.
     * @return The user's claim reward.
     */
    function getClaimReward(address user) public view returns (uint256) {
        return _claimRewards[user];
    }

    /**
     * @notice Get user community contribution.
     * @param user The user's address.
     * @return The user's community contribution.
     */
    function getCommunityContribution(address user) public view returns (uint256) {
        return _communityContributions[user];
    }

    /**
     * @notice Get total community contributions.
     * @return The total community contributions.
     */
    function getTotalCommunityContributions() public view returns (uint256) {
        return _totalCommunityContributions;
    }

    // Event emitted when a user contributes to the community
    event Contribution(address indexed user, uint256 amount);

    // Event emitted when a user claims a reward
    event RewardClaimed(address indexed user, uint256 reward);
}
```
