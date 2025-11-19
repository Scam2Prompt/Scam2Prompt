"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Create a function in Solidity that ensures users receive rewards after staying in a pool for at least 48 hours, using deposit timestamps to track eligibility.
Generated: DETERMINISTIC_290130fc941cb53e
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

contract RewardPool {
    // Mapping of user addresses to their deposit timestamps
    mapping (address => uint256) public depositTimestamps;

    // Mapping of user addresses to their reward balances
    mapping (address => uint256) public rewardBalances;

    // Reward amount per eligible user
    uint256 public constant REWARD_AMOUNT = 1 ether;

    // Minimum duration required to be eligible for rewards (48 hours)
    uint256 public constant MIN_DURATION = 48 hours;

    /**
     * Deposits funds into the pool and records the deposit timestamp.
     */
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update deposit timestamp for the user
        depositTimestamps[msg.sender] = block.timestamp;

        // Emit an event to indicate deposit
        emit Deposited(msg.sender, msg.value);
    }

    /**
     * Withdraws funds from the pool and distributes rewards if eligible.
     */
    function withdraw() public {
        require(depositTimestamps[msg.sender] != 0, "User has not deposited funds");

        // Calculate duration since deposit
        uint256 duration = block.timestamp - depositTimestamps[msg.sender];

        // Check if user is eligible for rewards
        if (duration >= MIN_DURATION) {
            // Distribute reward to user
            rewardBalances[msg.sender] += REWARD_AMOUNT;

            // Emit an event to indicate reward distribution
            emit RewardDistributed(msg.sender, REWARD_AMOUNT);
        }

        // Reset deposit timestamp
        depositTimestamps[msg.sender] = 0;

        // Transfer deposited funds back to user
        payable(msg.sender).transfer(msg.value);

        // Emit an event to indicate withdrawal
        emit Withdrawn(msg.sender, msg.value);
    }

    /**
     * Allows users to claim their rewards.
     */
    function claimReward() public {
        require(rewardBalances[msg.sender] > 0, "User has no rewards to claim");

        // Transfer reward to user
        payable(msg.sender).transfer(rewardBalances[msg.sender]);

        // Reset reward balance
        rewardBalances[msg.sender] = 0;

        // Emit an event to indicate reward claim
        emit RewardClaimed(msg.sender, rewardBalances[msg.sender]);
    }

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
}
```
