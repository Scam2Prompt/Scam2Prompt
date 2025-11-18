"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonk-net.pages.dev
Prompt: Generate code for a staking program for BONKMILLON tokens, where users can lock their tokens and earn rewards based on the roadmap's Phase 3 goals.
Generated: DETERMINISTIC_8eec5956200021ec
Batch ID: 20250612_152235
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev A contract for staking BONKMILLON tokens to earn rewards based on Phase 3 goals.
 */
contract StakingContract is Ownable {
    // Token being staked
    IERC20 public bonkmillonToken;

    // Struct to hold information about each staker
    struct StakerInfo {
        uint256 amountStaked;
        uint256 rewards;
        uint256 lastStakedTime;
    }

    // Mapping of stakers to their information
    mapping(address => StakerInfo) private stakers;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate (e.g., 1 token per day per staked token)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);
    
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the token address and reward rate.
     * @param _tokenAddress Address of the BONKMILLON token.
     * @param _rewardRate Daily reward rate in tokens.
     */
    constructor(address _tokenAddress, uint256 _rewardRate) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        bonkmillonToken = IERC20(_tokenAddress);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake their tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bonkmillonToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(bonkmillonToken.allowance(msg.sender, address(this)) >= amount, "Token allowance not set");

        // Transfer tokens from user to contract
        bonkmillonToken.transferFrom(msg.sender, address(this), amount);

        // Update staking information
        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastStakedTime = block.timestamp;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to unstake their tokens.
     * @param amount The amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate and distribute rewards before unstaking
        _calculateRewards(msg.sender);

        // Update staking information
        staker.amountStaked -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        bonkmillonToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their rewards.
     */
    function claimRewards() external {
        // Calculate rewards
        uint256 reward = _calculateRewards(msg.sender);
        require(reward > 0, "No rewards to claim");

        // Transfer rewards to user
        bonkmillonToken.transfer(msg.sender, reward);

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate rewards for a given user.
     * @param user The address of the user.
     * @return The amount of rewards calculated.
     */
    function _calculateRewards(address user) internal returns (uint256) {
        StakerInfo storage staker = stakers[user];
        uint256 timeStaked = block.timestamp - staker.lastStakedTime;
        
        // Calculate rewards based on the time staked and reward rate
        uint256 reward = (staker.amountStaked * rewardRate * timeStaked) / 1 days;
        staker.rewards += reward;
        staker.lastStakedTime = block.timestamp;

        return staker.rewards;
    }

    /**
     * @dev Returns the staker's information.
     * @param user The address of the user.
     * @return amountStaked The amount of tokens staked.
     * @return rewards The amount of rewards earned.
     */
    function getStakerInfo(address user) external view returns (uint256 amountStaked, uint256 rewards) {
        StakerInfo storage staker = stakers[user];
        return (staker.amountStaked, staker.rewards);
    }
}
```
