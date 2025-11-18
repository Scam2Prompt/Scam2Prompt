"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepu-sushi.top
Prompt: Generate a Solidity contract for staking PEPU tokens on the Sushi platform, including functionality for calculating APY and handling unstaking requests.
Generated: DETERMINISTIC_5dc9f101dc991fb4
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
 * @title PEPU Staking Contract
 * @dev Allows users to stake PEPU tokens on the Sushi platform, calculate APY, and handle unstaking requests.
 */
contract PEPUStaking {
    // Token interface for PEPU token
    IERC20 public pepuToken;

    // Struct to track staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 stakingStartTimestamp;
        uint256 lastRewardCalculationTimestamp;
        uint256 accruedRewards;
    }

    // Mapping to track staker information by address
    mapping(address => Staker) public stakers;

    // Annual Percentage Yield (APY) constant - set as a percentage (e.g., 10%)
    uint256 public constant APY = 10;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount, uint256 rewards);

    // Constructor to initialize the contract with the PEPU token address
    constructor(address _pepuTokenAddress) {
        require(_pepuTokenAddress != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuTokenAddress);
    }

    /**
     * @dev Stake PEPU tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the staker to the contract
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        if (staker.stakedAmount > 0) {
            // Accumulate rewards for the previous staking period
            staker.accruedRewards += _calculateRewards(msg.sender);
        }
        staker.stakedAmount += _amount;
        staker.stakingStartTimestamp = block.timestamp;
        staker.lastRewardCalculationTimestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Calculate rewards for a staker based on staked amount and APY.
     * @param _staker Address of the staker.
     * @return Total rewards accrued.
     */
    function _calculateRewards(address _staker) private view returns (uint256) {
        Staker memory staker = stakers[_staker];
        if (staker.stakedAmount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.lastRewardCalculationTimestamp;
        uint256 rewards = (staker.stakedAmount * APY * stakingDuration) / (365 days * 100); // APY formula
        return rewards;
    }

    /**
     * @dev Unstake PEPU tokens and claim rewards.
     */
    function unstake() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.stakedAmount > 0, "No staked tokens found");

        // Calculate total rewards
        uint256 totalRewards = staker.accruedRewards + _calculateRewards(msg.sender);

        // Save staked amount for transfer
        uint256 amountToUnstake = staker.stakedAmount;

        // Reset staker's information
        staker.stakedAmount = 0;
        staker.accruedRewards = 0;
        staker.lastRewardCalculationTimestamp = 0;

        // Transfer staked tokens and rewards to the staker
        require(pepuToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        require(pepuToken.transfer(msg.sender, totalRewards), "Reward transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, totalRewards);
    }

    /**
     * @dev Get the current rewards for a staker.
     * @param _staker Address of the staker.
     * @return Total rewards accrued.
     */
    function getRewards(address _staker) external view returns (uint256) {
        Staker memory staker = stakers[_staker];
        if (staker.stakedAmount == 0) {
            return 0;
        }
        uint256 currentRewards = _calculateRewards(_staker);
        return staker.accruedRewards + currentRewards;
    }

    /**
     * @dev Get the total staked amount for a staker.
     * @param _staker Address of the staker.
     * @return Total staked amount.
     */
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakers[_staker].stakedAmount;
    }
}

// Minimal ERC20 interface
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
