"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validsocs.pages.dev
Prompt: Describe the process of staking and harvesting assets in a DApp, including any relevant code implementations mentioned on the site.
Generated: DETERMINISTIC_900f732ce78678b2
Batch ID: 20250612_162828
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
 * @title StakingDApp
 * @dev A smart contract for staking and harvesting assets in a decentralized application (DApp).
 */
contract StakingDApp {
    // Struct to hold staker information
    struct Staker {
        uint256 amountStaked; // Amount of tokens staked
        uint256 lastStakeTime; // Timestamp of the last stake
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of address to staker information
    mapping(address => Staker) public stakers;

    // Reward per second per token staked
    uint256 public rewardRate = 1e18; // Example reward rate (can be set dynamically)

    // Token contract interface
    IERC20 public stakingToken;

    // Event emitted when tokens are staked
    event Staked(address indexed staker, uint256 amount);

    // Event emitted when rewards are harvested
    event Harvested(address indexed staker, uint256 reward);

    // Constructor to set the staking token
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    /**
     * @dev Stake tokens into the DApp.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards before changing stake balance
        _updateRewards(msg.sender);

        // Transfer tokens from the staker to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker's data
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Harvest accumulated rewards.
     */
    function harvest() external {
        _updateRewards(msg.sender);

        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.rewards;

        require(reward > 0, "No rewards available");

        // Reset rewards
        staker.rewards = 0;

        // Transfer rewards to the staker
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit Harvested(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param _staker The address of the staker.
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        if (staker.amountStaked > 0) {
            uint256 timeStaked = block.timestamp - staker.lastStakeTime;
            uint256 newRewards = timeStaked * staker.amountStaked * rewardRate / 1e18; // Calculate rewards
            staker.rewards += newRewards;
        }
        staker.lastStakeTime = block.timestamp; // Update last stake time
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
