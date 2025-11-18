"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrettoken.web.app
Prompt: Write Solidity code to implement a staking mechanism for the BRETT token within the BASE chain ecosystem.
Generated: DETERMINISTIC_81a0994f47fb9de1
Batch ID: 20250612_152710
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
 * @title Staking Contract for BRETT Token
 * @dev A simple staking mechanism for the BRETT token on the BASE chain ecosystem.
 */
contract BrettTokenStaking {
    // State variables
    IERC20 public brettToken; // ERC20 token contract interface
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of BRETT tokens staked

    struct StakerInfo {
        uint256 amount; // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt for reward calculations
        uint256 lastClaimTime; // Last time rewards were claimed
    }

    mapping(address => StakerInfo) public stakers; // Mapping of staker addresses to staker info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @dev Constructor to set the BRETT token and reward rate.
     * @param _brettToken Address of the BRETT token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _brettToken, uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        brettToken = _brettToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake BRETT tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Update staker's rewards before changing stake amount
        StakerInfo storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        // Transfer tokens from staker to contract
        require(brettToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker info
        staker.amount += _amount;
        staker.lastClaimTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BRETT tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amount >= _amount, "Unstake amount exceeds staked balance");

        // Update staker's rewards before changing stake amount
        _updateRewards(msg.sender);

        // Deduct staked amount
        staker.amount -= _amount;
        staker.lastClaimTime = block.timestamp;

        totalStaked -= _amount;

        // Transfer tokens back to staker
        require(brettToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        StakerInfo storage staker = stakers[msg.sender];

        uint256 rewardAmount = staker.rewardDebt;
        require(rewardAmount > 0, "No rewards to claim");

        staker.rewardDebt = 0; // Reset reward debt
        staker.lastClaimTime = block.timestamp;

        // Transfer rewards to staker
        require(brettToken.transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param _staker Address of the staker.
     */
    function _updateRewards(address _staker) internal {
        StakerInfo storage staker = stakers[_staker];
        if (staker.amount > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastClaimTime;
            uint256 newRewards = staker.amount * rewardRate * timeElapsed;

            // Accumulate rewards in rewardDebt
            staker.rewardDebt += newRewards;
        }
    }

    /**
     * @dev Retrieve the current reward balance for a staker.
     * @param _staker Address of the staker.
     * @return Reward balance.
     */
    function getPendingRewards(address _staker) external view returns (uint256) {
        StakerInfo storage staker = stakers[_staker];
        if (staker.amount > 0) {
            uint256 timeElapsed = block.timestamp - staker.lastClaimTime;
            uint256 newRewards = staker.amount * rewardRate * timeElapsed;
            return staker.rewardDebt + newRewards;
        }
        return 0;
    }
}

/**
 * @dev Minimal interface of an ERC20 token contract for token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
