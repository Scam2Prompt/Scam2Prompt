"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate code to integrate the PepeArab staking functionality into a decentralized application (dApp), allowing users to stake $PEAB tokens and calculate rewards based on APY.
Generated: DETERMINISTIC_0e762e334a78457b
Batch ID: 20250612_145730
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $PEAB tokens
contract PepeArabStaking is Ownable {
    // Token to be staked
    IERC20 public stakingToken;

    // User staking information
    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield (APY) in basis points (e.g., 500 = 5%)
    uint256 public apy;

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the staking token and APY
    constructor(IERC20 _stakingToken, uint256 _apy) {
        stakingToken = _stakingToken;
        apy = _apy;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to calculate rewards based on the staked amount and time
    function calculateRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        // Calculate the duration of the stake in seconds
        uint256 duration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on APY
        uint256 rewards = (userStake.amount * apy * duration) / (365 days * 10000);
        return rewards;
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards
        uint256 rewards = calculateRewards(msg.sender);

        // Reset user's stake information
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        // Transfer staked tokens and rewards to the user
        stakingToken.transfer(msg.sender, userStake.amount);
        if (rewards > 0) {
            stakingToken.transfer(msg.sender, rewards); // Assuming rewards are also in $PEAB
        }

        emit Unstaked(msg.sender, userStake.amount, rewards);
    }

    // Function to update the APY (only owner can call)
    function updateAPY(uint256 _newAPY) external onlyOwner {
        apy = _newAPY;
    }
}
```
