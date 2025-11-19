"""
Generated Code Metadata:
========================
Original URL: https://green-bitcoins.pages.dev
Prompt: How can I implement a staking mechanism for the Green Bitcoin ($GBTC) token that allows users to earn exponential rewards and participate in weekly prediction challenges?
Generated: DETERMINISTIC_39df8a7483d68d73
Batch ID: 20250612_161617
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for security and standard token functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Green Bitcoin ($GBTC) token
contract GBTCStaking is Ownable {
    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
        uint256 rewards; // Accumulated rewards
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The $GBTC token contract
    IERC20 public gbtcToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate = 1e18; // 1 GBTC per second for simplicity

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to set the GBTC token address
    constructor(address _gbtcToken) {
        gbtcToken = IERC20(_gbtcToken);
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.balanceOf(msg.sender) >= amount, "Insufficient GBTC balance");

        // Transfer tokens from user to this contract
        gbtcToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        // Calculate the time difference since last stake
        uint256 timeStaked = block.timestamp - userStake.timestamp;
        return (userStake.amount * timeStaked * rewardRate) / 1e18; // Adjusting for reward rate
    }

    // Function to unstake tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        uint256 totalAmount = userStake.amount;

        // Reset user's stake information
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens and rewards back to the user
        gbtcToken.transfer(msg.sender, totalAmount);
        gbtcToken.transfer(msg.sender, rewards);

        emit Unstaked(msg.sender, totalAmount, rewards);
    }

    // Function to set a new reward rate (only owner can call)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(gbtcToken), "Cannot withdraw GBTC tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
