"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-pepecoin-io.pages.dev
Prompt: Write a Solidity smart contract for staking PepeCoin and earning BasedAI rewards. Include functionality for farming and bridging as described in the PepeOS staking application.
Generated: DETERMINISTIC_d0b074a009a42d4e
Batch ID: 20250612_145723
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
 * @title PepeCoin Staking Contract
 * @notice This contract allows users to stake PepeCoin and earn BasedAI rewards.
 * @dev Includes farming and bridging functionality for the PepeOS staking application.
 */
contract PepeCoinStaking {
    // State variables
    IERC20 public pepeCoin;  // PepeCoin token interface
    IERC20 public basedAI;   // BasedAI token interface
    mapping(address => uint256) public stakedAmount; // User's staked amounts
    mapping(address => uint256) public rewardDebt;   // User's reward debt
    uint256 public totalStaked;  // Total amount of PepeCoin staked
    uint256 public rewardPerToken; // Reward per token staked
    uint256 public constant REWARD_RATE = 1e18; // Reward rate

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Harvested(address indexed user, uint256 reward);

    // Constructor to initialize the contract with PepeCoin and BasedAI token addresses
    constructor(address _pepeCoin, address _basedAI) {
        pepeCoin = IERC20(_pepeCoin);
        basedAI = IERC20(_basedAI);
    }

    /**
     * @notice Stake PepeCoin tokens to earn BasedAI rewards.
     * @param amount The amount of PepeCoin to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Update reward for the user
        _updateReward(msg.sender);
        
        // Transfer PepeCoin to the contract
        pepeCoin.transferFrom(msg.sender, address(this), amount);

        // Update user's staked amount and total staked
        stakedAmount[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake PepeCoin tokens and withdraw rewards.
     * @param amount The amount of PepeCoin to unstake
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update reward for the user
        _updateReward(msg.sender);

        // Update user's staked amount and total staked
        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer PepeCoin back to the user
        pepeCoin.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Harvest BasedAI rewards earned by the user.
     */
    function harvest() external {
        _updateReward(msg.sender);
        uint256 reward = rewardDebt[msg.sender];
        
        require(reward > 0, "No rewards to harvest");
        
        // Reset user's reward debt and transfer BasedAI rewards
        rewardDebt[msg.sender] = 0;
        basedAI.transfer(msg.sender, reward);

        emit Harvested(msg.sender, reward);
    }

    /**
     * @notice Private function to update rewards for a user.
     * @param user The address of the user
     */
    function _updateReward(address user) private {
        // Calculate the new reward and update reward debt
        uint256 staked = stakedAmount[user];
        rewardDebt[user] += (staked * rewardPerToken) / 1e18; // Using fixed-point arithmetic
    }
    
    /**
     * @notice Function to claim rewards and perform bridging actions.
     * @dev This function is a placeholder for the bridging logic.
     */
    function bridge() external {
        // Placeholder for bridging logic
        require(totalStaked > 0, "No tokens staked to bridge");
        // Implement bridging logic here
    }

    /**
     * @notice Update reward rate (only owner can call).
     * @param newRate The new reward rate
     */
    function updateRewardRate(uint256 newRate) external onlyOwner {
        REWARD_RATE = newRate;
    }

    // Modifier to restrict function to contract owner
    modifier onlyOwner {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
