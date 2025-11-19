"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainbitcoinbsc.pages.dev
Prompt: Generate an example of how to implement a smart contract for staking BTCBSC tokens based on the information provided on the Bitcoin BSC site.
Generated: DETERMINISTIC_8a8a94e2810a0e37
Batch ID: 20250612_160946
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

// Import the ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for staking BTCBSC tokens
contract StakingContract is Ownable {
    // Struct to hold staking details for each user
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 timestamp;     // Time when tokens were staked
    }

    // Mapping of user addresses to their staking details
    mapping(address => Stake) public stakes;
    
    // Token being staked
    IERC20 public stakingToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the token to be staked
    constructor(address _stakingToken) {
        require(_stakingToken != address(0), "Invalid token address");
        stakingToken = IERC20(_stakingToken);
    }

    // Function for users to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(stakingToken.allowance(msg.sender, address(this)) >= amount, "Token allowance required");

        // Transfer tokens from the user to this contract
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Emit the Staked event
        emit Staked(msg.sender, amount);
    }

    // Function for users to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];

        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update user's stake
        userStake.amount -= amount;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, amount);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, amount);
    }

    // Function to check the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Optional: Function to check the staking duration (in seconds)
    function stakingDuration(address user) external view returns (uint256) {
        if (stakes[user].amount == 0) return 0;
        return block.timestamp - stakes[user].timestamp;
    }
}
```
