"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellydao.web.app
Prompt: Generate a script to implement staking functionality for $Jelly tokens, ensuring compatibility with the "Jelly Staking" utility mentioned on the JellyDAO site.
Generated: DETERMINISTIC_a0d21d0aef8d862e
Batch ID: 20250612_150545
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
 * @title JellyTokenStaking
 * @dev A contract for staking $Jelly tokens, compatible with Jelly Staking utility by JellyDAO.
 */
contract JellyTokenStaking {
    IERC20 public immutable jellyToken; // Reference to the $Jelly token
    address public owner; // Contract owner

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user address to their stake
    uint256 public rewardRatePerSecond; // Reward rate per second (adjustable by owner)

    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 oldRate, uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    constructor(IERC20 _jellyToken, uint256 _rewardRatePerSecond) {
        require(address(_jellyToken) != address(0), "Invalid token address");
        require(_rewardRatePerSecond > 0, "Reward rate must be greater than zero");

        jellyToken = _jellyToken;
        rewardRatePerSecond = _rewardRatePerSecond;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake $Jelly tokens.
     * @param _amount The amount of $Jelly tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(jellyToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(jellyToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance too low");

        // Transfer tokens from user to contract
        bool success = jellyToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Calculate any existing reward
        uint256 pendingReward = calculateReward(msg.sender);

        // Update the user's stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit stake event
        emit Staked(msg.sender, _amount, block.timestamp);

        // If there's a pending reward, transfer it to the user
        if (pendingReward > 0) {
            bool rewardTransfer = jellyToken.transfer(msg.sender, pendingReward);
            require(rewardTransfer, "Reward transfer failed");
        }
    }

    /**
     * @dev Allows a user to unstake their tokens along with rewards.
     */
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens to unstake");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Transfer staked amount and reward to user
        uint256 totalAmount = userStake.amount + reward;
        bool transferSuccess = jellyToken.transfer(msg.sender, totalAmount);
        require(transferSuccess, "Token transfer failed");

        // Reset the user's stake
        delete stakes[msg.sender];

        // Emit unstake event
        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculates the reward for a user based on their stake and staking duration.
     * @param _user The address of the user.
     * @return The calculated reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = stakingDuration * rewardRatePerSecond * userStake.amount / 1e18; // Reward is proportional to staked amount and duration
        return reward;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRate The new reward rate per second.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");

        uint256 oldRate = rewardRatePerSecond;
        rewardRatePerSecond = _newRate;

        emit RewardRateUpdated(oldRate, _newRate);
    }

    /**
     * @dev Allows the owner to withdraw any leftover tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(jellyToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        bool success = jellyToken.transfer(owner, _amount);
        require(success, "Token withdrawal failed");
    }
}

/**
 * @dev Minimal IERC20 interface for interacting with the $Jelly token.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function allowance(address owner, address spender) external view returns (uint256);
}
```
