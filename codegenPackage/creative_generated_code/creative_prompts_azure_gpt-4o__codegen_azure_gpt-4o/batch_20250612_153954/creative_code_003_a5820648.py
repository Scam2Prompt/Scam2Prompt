"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upshift.fi
Prompt: Write a smart contract in Solidity that incorporates Upshift Finance's rewards boost mechanism (e.g., 1.25x upUSDC PT Boost) for users who participate in voting.
Generated: DETERMINISTIC_a5820648d9acdd11
Batch ID: 20250612_153954
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
 * @title UpshiftRewardsBoost
 * @dev A smart contract to implement Upshift Finance's rewards boost mechanism for users who participate in voting.
 */
contract UpshiftRewardsBoost {
    // Owner of the contract
    address public owner;

    // Token address for reward distribution (e.g., upUSDC PT)
    address public rewardToken;

    // Boost multiplier (e.g., 1.25x)
    uint256 public boostMultiplier = 125; // Represented as 1.25x * 100 for precision

    // Voting participation record
    mapping(address => bool) public hasVoted;

    // Rewards mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Event for reward distribution
    event RewardDistributed(address indexed user, uint256 originalReward, uint256 boostedReward);

    // Event for voting participation
    event UserVoted(address indexed user);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the initial owner and reward token address.
     * @param _rewardToken Address of the reward token contract.
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid reward token address");
        owner = msg.sender;
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function for users to record their voting participation.
     */
    function recordVote() external {
        require(!hasVoted[msg.sender], "User has already voted");
        hasVoted[msg.sender] = true;

        emit UserVoted(msg.sender);
    }

    /**
     * @dev Function to distribute rewards to users.
     * @param users Array of user addresses to distribute rewards to.
     * @param originalRewards Array of original reward amounts corresponding to each user.
     */
    function distributeRewards(address[] calldata users, uint256[] calldata originalRewards) external onlyOwner {
        require(users.length == originalRewards.length, "Input arrays length mismatch");

        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            uint256 originalReward = originalRewards[i];
            require(originalReward > 0, "Invalid reward amount");

            uint256 boostedReward = originalReward;

            // Apply boost if user has voted
            if (hasVoted[user]) {
                boostedReward = (originalReward * boostMultiplier) / 100;
            }

            rewards[user] += boostedReward;

            emit RewardDistributed(user, originalReward, boostedReward);

            // Transfer tokens (assuming rewardToken implements ERC20 standard)
            require(
                IERC20(rewardToken).transfer(user, boostedReward),
                "Token transfer failed"
            );
        }
    }

    /**
     * @dev Function to update the boost multiplier.
     * @param _boostMultiplier New boost multiplier (e.g., 1.25x should be passed as 125).
     */
    function updateBoostMultiplier(uint256 _boostMultiplier) external onlyOwner {
        require(_boostMultiplier > 100, "Boost multiplier must be greater than 1x (100)");
        boostMultiplier = _boostMultiplier;
    }

    /**
     * @dev Function to update the reward token address.
     * @param _rewardToken New reward token address.
     */
    function updateRewardToken(address _rewardToken) external onlyOwner {
        require(_rewardToken != address(0), "Invalid reward token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Interface for ERC20 token standard.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }
}
```
