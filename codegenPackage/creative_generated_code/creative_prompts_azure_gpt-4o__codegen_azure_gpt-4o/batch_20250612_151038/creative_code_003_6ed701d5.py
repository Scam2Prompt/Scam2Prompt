"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://or-22s.pages.dev
Prompt: Develop a function in Solidity to implement a rewards mechanism similar to the one described in the $ENTS tokenomics.
Generated: DETERMINISTIC_6ed701d5becc8b0b
Batch ID: 20250612_151038
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
 * @title RewardsSystem
 * @dev Implements a rewards mechanism inspired by $ENTS tokenomics.
 * Users can stake tokens and earn rewards over time.
 */

contract RewardsSystem {
    // State variables
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate per token staked, per second

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 lastUpdated; // Timestamp when rewards were last calculated
        uint256 rewardBalance; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Tracks stakes for each user

    // ERC20 Token Interface
    IERC20 public token;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract with reward rate and token address.
     * @param _rewardRate Reward rate per token per second.
     * @param _tokenAddress Address of the ERC20 token contract.
     */
    constructor(uint256 _rewardRate, address _tokenAddress) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before state changes
        _updateRewards(msg.sender);

        // Transfer tokens to the contract
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update stake amount
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw staked tokens.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(stakes[msg.sender].amount >= _amount, "Insufficient staked tokens");

        // Update rewards before state changes
        _updateRewards(msg.sender);

        // Update stake amount
        stakes[msg.sender].amount -= _amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].rewardBalance;
        require(reward > 0, "No rewards to claim");

        // Reset reward balance
        stakes[msg.sender].rewardBalance = 0;

        // Transfer rewards to the user
        require(token.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Updates accumulated rewards for a given user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage stakeData = stakes[_user];
        uint256 timeElapsed = block.timestamp - stakeData.lastUpdated;

        if (timeElapsed > 0) {
            uint256 newReward = (stakeData.amount * rewardRate * timeElapsed) / 1e18; // Assuming token has 18 decimals
            stakeData.rewardBalance += newReward;
            stakeData.lastUpdated = block.timestamp;
        }
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to recover tokens mistakenly sent to the contract.
     * @param _tokenAddress Address of the token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 recoverToken = IERC20(_tokenAddress);
        require(recoverToken.transfer(owner, _amount), "Token recovery failed");
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
