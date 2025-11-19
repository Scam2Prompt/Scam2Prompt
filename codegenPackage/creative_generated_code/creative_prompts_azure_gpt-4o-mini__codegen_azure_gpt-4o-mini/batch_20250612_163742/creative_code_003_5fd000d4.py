"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-in.pages.dev
Prompt: Provide an example of how to implement a staking mechanism for $WAI tokens in a decentralized application.
Generated: DETERMINISTIC_5fd000d4c5365258
Batch ID: 20250612_163742
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

// Importing ERC20 interface for interaction with $WAI token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $WAI tokens
contract StakingContract is Ownable {
    // Token to be staked
    IERC20 public waiToken;

    // Struct to hold staking information for each staker
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Time when the tokens were staked
    }

    // Mapping to track stakes of each address
    mapping(address => Stake) public stakes;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the token address
    constructor(address _waiToken) {
        require(_waiToken != address(0), "Invalid token address");
        waiToken = IERC20(_waiToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(waiToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer $WAI tokens from the user to this contract
        waiToken.transferFrom(msg.sender, address(this), _amount);

        // Update the staker's information
        Stake storage stakeInfo = stakes[msg.sender];
        stakeInfo.amount += _amount;
        stakeInfo.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= _amount, "Insufficient staked amount");

        // Update the staker's information
        stakeInfo.amount -= _amount;

        // Transfer the $WAI tokens back to the user
        waiToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards (example mechanism, can be modified)
    function calculateRewards(address _staker) public view returns (uint256) {
        Stake storage stakeInfo = stakes[_staker];
        // Example: reward 1 token for every 1 token staked per day
        return (stakeInfo.amount * (block.timestamp - stakeInfo.timestamp)) / 1 days;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Transfer rewards to the user
        waiToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address _staker) external view returns (uint256) {
        return stakes[_staker].amount;
    }
}
```
