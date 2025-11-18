"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kenduinu-an.web.app
Prompt: Write a smart contract in Solidity for staking $KENDU tokens as described in the Kendu Inu ecosystem, ensuring users can lock their tokens for rewards and withdraw them after a specified period.
Generated: DETERMINISTIC_37c08c563ab22756
Batch ID: 20250612_153812
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

// Importing the ERC20 interface to interact with the KENDU token contract
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for KENDU tokens
contract KenduStaking {
    // Declare state variables
    IERC20 public kenduToken; // KENDU token contract address
    uint256 public rewardRate; // Reward rate per block
    uint256 public lockDuration; // Duration for which tokens need to be locked
    address public owner; // Contract owner

    // Struct to hold user stake information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
        uint256 rewards; // Rewards accumulated
    }

    // Mapping to track stakes by user address
    mapping(address => Stake) public stakes;

    // Event to log staking actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(IERC20 _kenduToken, uint256 _rewardRate, uint256 _lockDuration) {
        kenduToken = _kenduToken;
        rewardRate = _rewardRate;
        lockDuration = _lockDuration;
        owner = msg.sender; // Set the contract creator as the owner
    }

    // Function to stake KENDU tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(kenduToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked KENDU tokens and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.timestamp + lockDuration, "Tokens are still locked");

        // Calculate accumulated rewards
        uint256 rewards = calculateRewards(msg.sender);
        userStake.rewards += rewards; // Update user's rewards

        // Transfer back staked tokens and rewards
        require(kenduToken.transfer(msg.sender, userStake.amount), "Transfer failed");
        require(kenduToken.transfer(msg.sender, userStake.rewards), "Transfer failed");

        // Reset user's stake information
        userStake.amount = 0;
        userStake.rewards = 0;

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;
        uint256 blocksStaked = block.timestamp - userStake.timestamp;
        return (blocksStaked * rewardRate * userStake.amount) / 1e18; // Adjust reward calculation
    }

    // Function to change the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to change the lock duration (only owner)
    function setLockDuration(uint256 _lockDuration) external onlyOwner {
        lockDuration = _lockDuration;
    }

    // Function to withdraw contract balance (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(owner, amount), "Transfer failed");
    }
}
```
