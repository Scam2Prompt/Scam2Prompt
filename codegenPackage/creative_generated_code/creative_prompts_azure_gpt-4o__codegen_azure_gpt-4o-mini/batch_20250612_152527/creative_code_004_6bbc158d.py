"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nettensor-5u5.pages.dev
Prompt: Create a smart contract in Solidity that interacts with Net Tensor's App Chain and utilizes $NAO tokens for staking and claiming rewards.
Generated: DETERMINISTIC_6bbc158d498d412c
Batch ID: 20250612_152527
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

// Import interfaces and contracts required for the ERC20 token and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title NAOStaking
 * @dev A smart contract for staking $NAO tokens and claiming rewards.
 */
contract NAOStaking is Ownable {
    // The IERC20 interface for $NAO Token
    IERC20 public naoToken;

    // Structure to hold user staking data
    struct UserStake {
        uint256 amount;         // Amount of tokens staked
        uint256 rewards;        // Accumulated rewards
        uint256 lastUpdated;    // Last update timestamp
    }

    // Mapping from user address to their stake data
    mapping(address => UserStake) public stakes;

    // Total amount of $NAO tokens staked
    uint256 public totalStaked;

    // Reward rate per staked token per second
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the NAO token address and reward rate
     * @param _naoToken Address of the $NAO token contract
     * @param _rewardRate Reward rate per staked token per second
     */
    constructor(address _naoToken, uint256 _rewardRate) {
        require(_naoToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        
        naoToken = IERC20(_naoToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake $NAO tokens in the contract
     * @param amount Amount of $NAO tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");
        
        // Update user's rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        require(naoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user's stake data
        stakes[msg.sender].amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $NAO tokens from the contract
     * @param amount Amount of $NAO tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");
        
        // Update user's rewards before unstaking
        _updateRewards(msg.sender);

        // Adjust user's stake data
        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;

        // Transfer tokens back to the user
        require(naoToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateRewards(msg.sender);

        uint256 rewardAmount = stakes[msg.sender].rewards;
        require(rewardAmount > 0, "No rewards to claim");

        // Reset rewards to zero
        stakes[msg.sender].rewards = 0;

        // Transfer rewards to the user
        require(naoToken.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Internal function to update user's rewards based on the time elapsed
     * @param user Address of the user
     */
    function _updateRewards(address user) internal {
        UserStake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            // Calculate time elapsed since last update
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            // Update rewards based on the elapsed time
            userStake.rewards += (userStake.amount * rewardRate * timeElapsed);
        }
        // Update last updated timestamp
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev View function to get the total rewards of a user
     * @param user Address of the user
     * @return Total rewards available for the user
     */
    function getRewards(address user) external view returns (uint256) {
        UserStake storage userStake = stakes[user];
        uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
        uint256 pendingRewards = (userStake.amount * rewardRate * timeElapsed) + userStake.rewards;
        return pendingRewards;
    }
}
```
