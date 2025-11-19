"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoins20.pages.dev
Prompt: Generate a Solidity contract that implements a simple staking mechanism similar to DOGE20, allowing users to stake ERC-20 tokens and earn rewards over time.
Generated: DETERMINISTIC_5ecebe74b4aba351
Batch ID: 20250612_160853
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
 * @title StakingContract
 * @notice A simple staking mechanism for ERC-20 tokens
 * @dev Users can stake tokens to earn rewards over time.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // ERC-20 token used for staking
    IERC20 public stakingToken;

    // Reward rate per second (e.g., tokens rewarded per second of staking)
    uint256 public rewardRate;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Mapping of user addresses to their staked balance
    mapping(address => uint256) public balances;

    // Mapping of user addresses to their last reward claim timestamp
    mapping(address => uint256) public lastClaimed;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the staking token and reward rate.
     * @param _stakingToken Address of the ERC-20 token to be staked
     * @param _rewardRate Reward rate per second
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake tokens.
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update rewards before changing staked balance
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staked balance and total staked
        balances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update rewards before changing staked balance
        _updateRewards(msg.sender);

        // Update staked balance and total staked
        balances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 rewards = _calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update last claimed timestamp
        lastClaimed[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        require(
            stakingToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculates the rewards for a given user based on their staked balance and time since last claim.
     * @param _user Address of the user
     * @return The calculated rewards
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimed[_user];
        return balances[_user] * rewardRate * timeElapsed / 1 ether;
    }

    /**
     * @dev Updates the rewards for a given user without transferring them.
     * @param _user Address of the user
     */
    function _updateRewards(address _user) internal {
        if (lastClaimed[_user] == 0) {
            // Initialize last claimed timestamp the first time user interacts
            lastClaimed[_user] = block.timestamp;
        } else {
            uint256 rewards = _calculateRewards(_user);
            require(
                stakingToken.transfer(msg.sender, rewards),
                "Reward transferring failed during updating."
            );
        }
    }

    /**
     * @dev Allows the owner to change the reward rate.
     * @param _newRewardRate New reward rate per second
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
