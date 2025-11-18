"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-unchained-on.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring compatibility with the platform's double staking rewards system.
Generated: DETERMINISTIC_b408f760b8ce8720
Batch ID: 20250612_153527
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
 * @dev Smart contract for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain.
 * @notice Supports double staking rewards system as per Pepe Unchained specifications.
 */
contract PEPUStaking {
    // Address of the $PEPU token contract
    IERC20 public pepuToken;

    // Struct for storing staking information
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 startTime;     // Timestamp when staking started
        uint256 reward;        // Accumulated reward
    }

    // Mapping to track stakes of each user
    mapping(address => Stake) private stakes;

    // Events for transparency and monitoring
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Reward rate per second (configured for double staking reward system)
    uint256 public rewardRate = 1e18; // Example: 1 $PEPU token per second per staked token (adjust as needed)

    // Constructor to initialize the contract with the $PEPU token address
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    /**
     * @dev Allows users to stake $PEPU tokens.
     * @param _amount Amount of $PEPU tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");

        // Update existing stake details (if any)
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            userStake.reward += calculateReward(msg.sender);
        }

        // Transfer tokens from the user to the contract
        pepuToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking details
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate final reward
        uint256 reward = calculateReward(msg.sender);
        uint256 amount = userStake.amount;

        // Reset staking details
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.reward = 0;

        // Transfer staked tokens and reward back to the user
        pepuToken.transfer(msg.sender, amount);
        pepuToken.transfer(msg.sender, reward);

        emit Unstaked(msg.sender, amount);
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows users to claim accumulated rewards without unstaking.
     */
    function claimReward() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked tokens found");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);

        // Transfer reward and update staking details
        pepuToken.transfer(msg.sender, reward);
        userStake.reward = 0;
        userStake.startTime = block.timestamp;

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the reward for a user based on staked amount and elapsed time.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 timeElapsed = block.timestamp - userStake.startTime;
        return userStake.reward + (userStake.amount * timeElapsed * rewardRate / 1e18);
    }

    /**
     * @dev Returns staking info for a user.
     * @param _user Address of the user.
     * @return amount Amount of $PEPU tokens staked.
     * @return reward Reward accumulated.
     * @return startTime Timestamp when staking began.
     */
    function getStakeInfo(address _user) external view returns (uint256 amount, uint256 reward, uint256 startTime) {
        Stake storage userStake = stakes[_user];
        amount = userStake.amount;
        reward = calculateReward(_user);
        startTime = userStake.startTime;
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
