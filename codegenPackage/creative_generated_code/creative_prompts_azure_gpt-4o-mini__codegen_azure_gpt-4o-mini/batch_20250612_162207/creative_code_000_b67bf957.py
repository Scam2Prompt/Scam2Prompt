"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-dogecoin20-io.pages.dev
Prompt: How can I implement a staking mechanism for an ERC-20 token like DOGE20 to distribute rewards over a two-year period?
Generated: DETERMINISTIC_b67bf957b2aeca4b
Batch ID: 20250612_162207
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

// Importing the IERC20 interface to interact with the ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for an ERC20 token
contract StakingContract is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp when staked
        uint256 rewards;      // Accumulated rewards
    }

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    // Total rewards pool
    uint256 public totalRewards;
    // Duration for staking rewards distribution (2 years in seconds)
    uint256 constant public STAKING_DURATION = 63072000; // 60 * 60 * 24 * 365 * 2

    // Constructor to initialize the staking token
    constructor(IERC20 _stakingToken) {
        stakingToken = _stakingToken;
    }

    // Stake tokens into the contract
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Withdraw staked tokens along with rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No staked amount found");

        // Calculate rewards based on staking duration
        uint256 rewards = calculateRewards(userStake.amount, userStake.timestamp);
        userStake.rewards += rewards;

        // Transfer staked amount and rewards back to the user
        require(stakingToken.transfer(msg.sender, userStake.amount), "Transfer failed");
        require(stakingToken.transfer(msg.sender, userStake.rewards), "Transfer failed");

        // Reset user's stake information
        userStake.amount = 0;
        userStake.rewards = 0;

        emit Withdrawn(msg.sender, userStake.amount, rewards);
    }

    // Calculate rewards based on the staked amount and staking time
    function calculateRewards(uint256 _amount, uint256 _timestamp) internal view returns (uint256) {
        // Here we can define the reward rate (e.g., 10% per year)
        uint256 rewardRate = 10; // 10% yearly
        uint256 stakingTime = block.timestamp - _timestamp;

        // Calculate rewards based on the formula: rewards = (amount * rate * time) / (365 days)
        return (_amount * rewardRate * stakingTime) / (365 days * 100);
    }

    // Function to set total rewards (owner can adjust this if needed)
    function setTotalRewards(uint256 _totalRewards) external onlyOwner {
        totalRewards = _totalRewards;
    }

    // Function to withdraw accidental ERC20 token transfers (only for owner)
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token != stakingToken, "Cannot withdraw staking token");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
