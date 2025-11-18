"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btcetfcoinn.pages.dev
Prompt: Write an Ethereum smart contract for staking BTCETF tokens, allowing users to lock tokens and earn rewards based on the total staked amount, as described in the BTCETF roadmap.
Generated: DETERMINISTIC_d1bad1b3396e866f
Batch ID: 20250612_152410
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

// Import the ERC20 interface for BTCETF token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// A staking contract for BTCETF tokens
contract BTCETFStaking is Ownable {
    // The ERC20 token to stake
    IERC20 public btcEftToken;

    // Struct to hold information about each user's staking
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Amount of rewards due based on previous stakes
        uint256 lastStakedTime; // Last time the user staked
    }

    // Mapping of user addresses to their stake information
    mapping(address => Stake) public stakes;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per second per staked token
    uint256 public rewardRate;

    // Event to emit when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event to emit when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event to emit when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the BTCETF token address and reward rate
    constructor(IERC20 _btcEftToken, uint256 _rewardRate) {
        btcEftToken = _btcEftToken;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(btcEftToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update user's stake and total staked
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.rewardDebt = pendingRewards(msg.sender);
        userStake.lastStakedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Update user's stake and total staked
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(btcEftToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = pendingRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");

        // Update reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(btcEftToken.transfer(msg.sender, rewards), "Token transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate pending rewards for a user
    function pendingRewards(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        return (userStake.amount * rewardRate * (block.timestamp - userStake.lastStakedTime)) / 1e18 + userStake.rewardDebt;
    }

    // Function to change the reward rate (only owner)
    function setRewardRate(uint256 _newRate) external onlyOwner {
        rewardRate = _newRate;
    }
}
```
