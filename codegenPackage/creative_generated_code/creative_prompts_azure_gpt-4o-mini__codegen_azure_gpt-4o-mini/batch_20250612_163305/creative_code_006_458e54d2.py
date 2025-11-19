"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinsbsc.pages.dev
Prompt: Write a Solidity contract that manages the staking rewards for BTCBSC holders, ensuring daily payouts in line with the Bitcoin block schedule.
Generated: DETERMINISTIC_458e54d2b97e260b
Batch ID: 20250612_163305
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

// Interface for the ERC20 token (BTCBSC)
interface IERC20 {
    function transfer(address to, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Staking contract for BTCBSC holders
contract BTCBSCStaking {
    // Struct to hold information about each staker
    struct Staker {
        uint256 amountStaked; // Amount of BTCBSC staked
        uint256 lastClaimed;  // Timestamp of the last reward claim
    }

    // Mapping to track stakers
    mapping(address => Staker) public stakers;

    // Rewards per block (adjust this value according to your rewards plan)
    uint256 public rewardsPerBlock = 10 * 10**18; // 10 BTCBSC rewards per block (example)

    // Reference to the BTCBSC token contract
    IERC20 public btcBscToken;

    // The total rewards distributed
    uint256 public totalRewards;

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed staker, uint256 amount);

    // Constructor to set the BTCBSC token address
    constructor(address _btcBscToken) {
        require(_btcBscToken != address(0), "Invalid token address");
        btcBscToken = IERC20(_btcBscToken);
    }

    // Function to stake BTCBSC tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(btcBscToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer the tokens to the contract
        btcBscToken.transfer(address(this), _amount);

        // Update staker information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        staker.lastClaimed = block.timestamp;

        totalRewards += _amount; // Increment total rewards

        // Emit an event for the stake action
    }

    // Function to claim staking rewards
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "No staked amount found");

        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update the last claimed timestamp
        staker.lastClaimed = block.timestamp;

        // Transfer rewards to the staker
        require(btcBscToken.transfer(msg.sender, rewards), "Transfer failed");
        
        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards based on the staking amount and time
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 blocksPassed = (block.timestamp - staker.lastClaimed) / 86400; // Days passed
        return (staker.amountStaked * rewardsPerBlock * blocksPassed) / 10**18; // Calculate rewards
    }

    // Function to get the staker's information
    function getStakerInfo(address _staker) external view returns (uint256 amountStaked, uint256 lastClaimed) {
        Staker storage staker = stakers[_staker];
        return (staker.amountStaked, staker.lastClaimed);
    }
}
```
