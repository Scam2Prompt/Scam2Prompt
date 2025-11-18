"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-app.pages.dev
Prompt: Develop a Solidity smart contract that automates the distribution of BTCMTX staking rewards based on the amount of tokens staked and the duration of staking.
Generated: DETERMINISTIC_f782d94cf5181f1c
Batch ID: 20250612_153420
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

// Importing OpenZeppelin's Ownable contract for access control
import "@openzeppelin/contracts/access/Ownable.sol";
// Importing the SafeMath library to ensure safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the ERC20 token (BTCMTX) to interact with its functions
interface IBTCMTX {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BTCMTXStakingRewards is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // When the stake was created
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;
    // Address of the BTCMTX token
    IBTCMTX public btcmtxToken;
    // Reward rate per token per second
    uint256 public rewardRate;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);
    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with the BTCMTX token and reward rate
    constructor(IBTCMTX _btcmtxToken, uint256 _rewardRate) {
        btcmtxToken = _btcmtxToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(btcmtxToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        require(btcmtxToken.transfer(address(this), amount), "Token transfer failed");
        
        // Update the user's stake
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw stakes and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stakes found");

        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount.add(reward);

        // Reset user's stake
        userStake.amount = 0;

        // Transfer the total amount (stake + reward) to the user
        require(btcmtxToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount);
        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate rewards based on the staked amount and duration
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 duration = block.timestamp.sub(userStake.startTime);
        return userStake.amount.mul(duration).mul(rewardRate).div(1e18); // Assuming rewardRate is scaled by 1e18 for precision
    }

    // Admin function to update the reward rate
    function setRewardRate(uint256 newRewardRate) external onlyOwner {
        rewardRate = newRewardRate;
    }

    // Function to check the stake of a user
    function getStake(address user) external view returns (uint256 amount, uint256 duration, uint256 reward) {
        amount = stakes[user].amount;
        duration = block.timestamp.sub(stakes[user].startTime);
        reward = calculateReward(user);
    }
}
```
