"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimflockerztoken.pages.dev
Prompt: Create a smart contract in Solidity for staking $FLOCK tokens with a 342% APY, including functionality for claiming rewards and voting in a DAO.
Generated: DETERMINISTIC_c343b7c0675ec41c
Batch ID: 20250612_154010
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

// Importing the required OpenZeppelin contracts for ERC20 and Ownable
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FlockStaking is Ownable {
    // Staking structure to hold user information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already distributed to the user
        uint256 lastStakedAt; // Timestamp of the last stake
    }

    // Mapping of user addresses to their respective stakes
    mapping(address => Stake) public stakes;

    // The ERC20 token to be staked
    IERC20 public flockToken;

    // Annual Percentage Yield (APY) rate
    uint256 public constant APY = 342; // 342%
    uint256 public constant SECONDS_IN_A_YEAR = 365 days;

    // Total staked tokens
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the ERC20 token address
    constructor(address _flockToken) {
        flockToken = IERC20(_flockToken);
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than 0");
        
        // Update staking information
        Stake storage stakeInfo = stakes[msg.sender];
        if (stakeInfo.amount > 0) {
            // Calculate and distribute pending rewards before updating the stake
            uint256 pendingRewards = calculateRewards(msg.sender);
            stakeInfo.rewardDebt += pendingRewards;
        }

        // Transfer tokens from the user to the contract
        flockToken.transferFrom(msg.sender, address(this), _amount);

        // Update stake information
        stakeInfo.amount += _amount;
        stakeInfo.lastStakedAt = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens
    function withdraw(uint256 _amount) external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= _amount, "Insufficient staked amount");

        // Calculate rewards before withdrawing
        uint256 pendingRewards = calculateRewards(msg.sender);
        stakeInfo.rewardDebt += pendingRewards;

        // Update the stake amount
        stakeInfo.amount -= _amount;
        totalStaked -= _amount;

        // Transfer staked tokens back to the user
        flockToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        Stake storage stakeInfo = stakes[msg.sender];

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        // Reset user's reward debt
        stakeInfo.rewardDebt += pendingRewards;

        // Transfer rewards to the user
        flockToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to calculate the rewards for a user
    function calculateRewards(address _user) internal view returns (uint256) {
        Stake storage stakeInfo = stakes[_user];
        uint256 timeStaked = block.timestamp - stakeInfo.lastStakedAt;
        uint256 reward = (stakeInfo.amount * APY * timeStaked) / (100 * SECONDS_IN_A_YEAR);
        return reward - stakeInfo.rewardDebt;
    }

    // Function to get the user's stake information
    function getStakeInfo(address _user) external view returns (uint256 amount, uint256 rewards) {
        Stake storage stakeInfo = stakes[_user];
        uint256 pendingRewards = calculateRewards(_user);
        return (stakeInfo.amount, pendingRewards);
    }
}
```
