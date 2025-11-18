"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Write a smart contract in Solidity that implements staking functionality for Moonboots DAO, allowing users to earn ecosystem rewards based on their $MBDAO token holdings.
Generated: DETERMINISTIC_f78ce849adecf356
Batch ID: 20250612_150552
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Moonboots DAO token
interface IMBDAO is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for Moonboots DAO
contract MoonbootsStaking is Ownable {
    // Struct to represent each staker's information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardsEarned;
        uint256 lastClaimedTime;
    }

    // Mapping of each staker's address to their staking information
    mapping(address => Staker) private stakers;

    // The MBDAO token used for staking
    IMBDAO public mbdaoToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when a user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws their stake
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the staking contract with the MBDAO token and reward rate
    constructor(IMBDAO _mbdaoToken, uint256 _rewardRate) {
        mbdaoToken = _mbdaoToken;
        rewardRate = _rewardRate;
    }

    // Function to stake MBDAO tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the tokens from the user to the contract
        mbdaoToken.transferFrom(msg.sender, address(this), amount);

        // Update the staker's information
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked += amount;
        staker.lastClaimedTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Calculate rewards before withdrawal
        _updateRewards(msg.sender);

        // Update the staker's amount staked
        staker.amountStaked -= amount;

        // Transfer the tokens back to the user
        mbdaoToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);
    }

    // Internal function to calculate and distribute rewards
    function _updateRewards(address stakerAddress) internal {
        Staker storage staker = stakers[stakerAddress];
        uint256 timeStaked = block.timestamp - staker.lastClaimedTime;
        uint256 rewards = (staker.amountStaked * rewardRate * timeStaked) / 1e18;

        // Update rewards and last claimed time
        staker.rewardsEarned += rewards;
        staker.lastClaimedTime = block.timestamp;

        // Mint and transfer the rewards to the user
        if (rewards > 0) {
            mbdaoToken.mint(stakerAddress, rewards);
            emit RewardsClaimed(stakerAddress, rewards);
        }
    }

    // Function to get staker information
    function getStakerInfo(address stakerAddress) external view returns (uint256 stakedAmount, uint256 rewardsEarned, uint256 lastClaimed) {
        Staker memory staker = stakers[stakerAddress];
        return (staker.amountStaked, staker.rewardsEarned, staker.lastClaimedTime);
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
