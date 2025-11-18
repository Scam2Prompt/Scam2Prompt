"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-in.pages.dev
Prompt: Create a tutorial for integrating Green Bitcoin's staking mechanics into a decentralized application (dApp) using Ethereum's blockchain and smart contract functionality.
Generated: DETERMINISTIC_30d1b2932a29fb08
Batch ID: 20250612_152924
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
 * @title GreenBitcoinStaking
 * @dev This contract implements staking mechanics for Green Bitcoin on the Ethereum blockchain.
 * Users can stake ETH, earn rewards, and withdraw their staked amount.
 */
contract GreenBitcoinStaking {
    // State variables
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total ETH staked in the contract
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5% annualized)

    struct Stake {
        uint256 amount; // Amount staked by the user
        uint256 timestamp; // Timestamp when the stake was made
    }

    mapping(address => Stake) public stakes; // Mapping to track user stakes
    mapping(address => uint256) public rewards; // Mapping to track user rewards

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor
    constructor(uint256 _rewardRate) {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake ETH in the contract.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Calculate pending rewards for the user before updating the stake
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            rewards[msg.sender] += pendingReward;
        }

        // Update the user's stake
        stakes[msg.sender].amount += msg.value;
        stakes[msg.sender].timestamp = block.timestamp;

        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Allows users to withdraw their staked amount along with rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount to withdraw");

        uint256 reward = calculateReward(msg.sender) + rewards[msg.sender];
        uint256 amountToWithdraw = userStake.amount;

        // Reset user's stake and rewards
        userStake.amount = 0;
        rewards[msg.sender] = 0;
        totalStaked -= amountToWithdraw;

        // Transfer staked amount and rewards back to the user
        payable(msg.sender).transfer(amountToWithdraw + reward);

        emit Withdrawn(msg.sender, amountToWithdraw, reward);
    }

    /**
     * @dev Updates the reward rate. Restricted to the owner.
     * @param _newRate The new reward rate.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRate;

        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Calculates the reward for a user based on their staked amount and time.
     * @param _user The address of the user.
     * @return The calculated reward.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (365 days * 100);

        return reward;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct transfers not allowed. Use stake function.");
    }
}
```

### Notes:
This contract satisfies best practices for Solidity development, including:
- Proper error handling.
- Clear modularization of logic.
- Safe transfer of Ether using `payable(msg.sender).transfer`.
- Documentation for all functions and variables.
