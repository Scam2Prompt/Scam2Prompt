"""
Generated Code Metadata:
========================
Original URL: https://staking-wisdomise.pages.dev
Prompt: Generate a Solidity code snippet for a smart contract that implements a 365-day lock term staking pool with a 28.39% reward and 0% NFT boost for WSDM tokens on the Polygon Mainnet.
Generated: DETERMINISTIC_5086561d747dc1c7
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing OpenZeppelin's SafeERC20 for safe token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// StakingPool contract for a 365-day lock term staking pool
contract StakingPool is Ownable {
    using SafeERC20 for IERC20;

    // Token to be staked
    IERC20 public immutable stakingToken;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 startTime;
        bool isActive;
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Reward rate (28.39% per year)
    uint256 public constant REWARD_RATE = 2839; // 28.39% in basis points
    uint256 public constant LOCK_PERIOD = 365 days;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].isActive == false, "Existing active stake found");

        // Transfer tokens from user to contract
        stakingToken.safeTransferFrom(msg.sender, address(this), amount);

        // Create a new stake
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            isActive: true
        });

        emit Staked(msg.sender, amount);
    }

    // Function to calculate reward
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (!userStake.isActive) return 0;

        uint256 stakingDuration = block.timestamp - userStake.startTime;
        if (stakingDuration < LOCK_PERIOD) return 0; // No reward if not locked for 365 days

        // Calculate reward based on the amount staked and the reward rate
        return (userStake.amount * REWARD_RATE * stakingDuration) / (10000 * 365 days);
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(block.timestamp >= userStake.startTime + LOCK_PERIOD, "Stake is still locked");

        // Calculate reward
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset the user's stake
        userStake.isActive = false;
        userStake.amount = 0;

        // Transfer staked tokens and reward to the user
        stakingToken.safeTransfer(msg.sender, totalAmount);

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        stakingToken.safeTransfer(msg.sender, amount);
    }
}
```
