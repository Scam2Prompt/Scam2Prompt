"""
Generated Code Metadata:
========================
Original URL: https://testingmeow2lol.com
Prompt: Develop a smart contract code (in Solidity) for staking $WEPE tokens and earning rewards, considering the token's address (0xccB365D2e11aE4D6d74715c680f56cf58bF4bF10) and supply (200,000,000,000 $WEPE).
Generated: DETERMINISTIC_ee53eaffde5db022
Batch ID: 20250622_211941
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

// Importing the ERC20 interface for interacting with the $WEPE token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $WEPE token
contract WEPEStaking is Ownable {
    // Address of the $WEPE token
    IERC20 public wepeToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping to track user stakes
    mapping(address => Stake) public stakes;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate (e.g., 1% per week)
    uint256 public rewardRate = 100; // Reward rate in basis points (1% = 100)

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the $WEPE token address
    constructor(address _wepeTokenAddress) {
        require(_wepeTokenAddress != address(0), "Invalid token address");
        wepeToken = IERC20(_wepeTokenAddress);
    }

    // Function to stake $WEPE tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(wepeToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        wepeToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        // Update total staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens and rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards based on the time staked
        uint256 reward = calculateReward(msg.sender);

        // Update total staked amount
        totalStaked -= userStake.amount;

        // Reset user's stake
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;

        // Transfer staked tokens and rewards to user
        wepeToken.transfer(msg.sender, amountToWithdraw + reward);

        emit Withdrawn(msg.sender, amountToWithdraw, reward);
    }

    // Function to calculate rewards for a user
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0) return 0;

        // Calculate the duration for which the tokens have been staked
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate reward based on the staking duration and reward rate
        uint256 reward = (userStake.amount * rewardRate * stakingDuration) / (1 weeks * 10000);
        return reward;
    }

    // Function to update the reward rate (only owner can call)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRate;
    }

    // Function to recover tokens sent to the contract by mistake
    function recoverTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(wepeToken), "Cannot recover staked token");
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }
}
```
