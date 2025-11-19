"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddysunversity.com
Prompt: Create a Solidity smart contract that allows users to stake $DADDY tokens and earn rewards based on their holdings.
Generated: DETERMINISTIC_a1637c71fada9b6f
Batch ID: 20250612_163338
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
 * @title DaddyTokenStaking
 * @dev Staking contract for $DADDY token allowing users to stake their tokens and earn rewards.
 * The contract calculates rewards based on the length and amount of the stake.
 */
contract DaddyTokenStaking {
    // State variables
    IERC20 public immutable daddyToken; // Reference to the $DADDY token contract
    uint256 public rewardRate; // Reward rate per second per token staked
    address public owner; // Owner of the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when the stake was created
        uint256 rewardEarned; // Reward earned but not claimed
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stake information

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateReward(address user) {
        Stake storage stake = stakes[user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.timestamp;
            stake.rewardEarned += (stake.amount * rewardRate * timeElapsed) / 1e18;
            stake.timestamp = block.timestamp;
        }
        _;
    }

    // Constructor
    constructor(IERC20 _daddyToken, uint256 _rewardRate) {
        require(address(_daddyToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        daddyToken = _daddyToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows users to stake $DADDY tokens.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user to the contract
        daddyToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        Stake storage stake = stakes[msg.sender];
        stake.amount += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     */
    function withdraw() external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No tokens staked");

        uint256 amount = stake.amount;
        stake.amount = 0;

        // Transfer tokens back to the user
        daddyToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their accumulated rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 reward = stake.rewardEarned;
        require(reward > 0, "No rewards to claim");

        stake.rewardEarned = 0;

        // Transfer rewards to the user
        daddyToken.transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param newRewardRate The new reward rate.
     */
    function updateRewardRate(uint256 newRewardRate) external onlyOwner {
        require(newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = newRewardRate;
    }

    /**
     * @dev Emergency function to allow the owner to recover tokens mistakenly sent to the contract.
     * @param tokenAddress The address of the token to recover.
     * @param amount The amount of tokens to recover.
     */
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        IERC20(token = IERC20(tokenAddress);
        token.transfer(owner, amount);
    // Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
