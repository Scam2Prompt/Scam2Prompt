"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Create a smart contract in Solidity that implements a staking mechanism for $BRISE tokens, allowing users to earn $BEFE as rewards.
Generated: DETERMINISTIC_e44deb7f53787a49
Batch ID: 20250612_151906
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

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Struct to hold user staking details
    struct StakeInfo {
        uint256 amount; // Amount of $BRISE staked
        uint256 rewardDebt; // Accumulated rewards minus the amount already paid
        uint256 lastUpdated; // Last time the user staked or withdrawn
    }

    // Token addresses
    IERC20 public briseToken; // Address of the $BRISE token
    IERC20 public befeToken; // Address of the $BEFE token

    // Mapping to hold user stakes
    mapping(address => StakeInfo) public stakes;

    // Total staked amount
    uint256 public totalStaked;
    
    // Reward per staked token per second
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize token addresses and reward rate
    constructor(IERC20 _briseToken, IERC20 _befetToken, uint256 _rewardRate) {
        briseToken = _briseToken;
        befeToken = _befetToken;
        rewardRate = _rewardRate;
    }

    // Function to stake $BRISE tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");

        // Transfer $BRISE tokens from user to this contract
        briseToken.transferFrom(msg.sender, address(this), amount);
        
        // Update user's stake information
        StakeInfo storage stakeInfo = stakes[msg.sender];
        
        // Update total staked amount
        totalStaked += amount;

        // Calculate and update rewards before staking
        if (stakeInfo.amount > 0) {
            uint256 pendingReward = calculateReward(msg.sender);
            stakeInfo.rewardDebt += pendingReward;
        }

        stakeInfo.amount += amount;
        stakeInfo.lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked $BRISE tokens
    function withdraw(uint256 amount) external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount >= amount, "Insufficient staked balance");

        // Calculate and update rewards before withdrawal
        uint256 pendingReward = calculateReward(msg.sender);
        stakeInfo.rewardDebt += pendingReward;

        // Update user's staked amount
        stakeInfo.amount -= amount;
        totalStaked -= amount;

        // Transfer $BRISE tokens back to the user
        briseToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards in $BEFE tokens
    function claimRewards() external {
        uint256 pendingReward = calculateReward(msg.sender);
        require(pendingReward > 0, "No rewards to claim");

        StakeInfo storage stakeInfo = stakes[msg.sender];
        stakeInfo.rewardDebt += pendingReward;

        // Transfer $BEFE rewards to the user
        befeToken.transfer(msg.sender, pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    // Internal function to calculate pending rewards for a user
    function calculateReward(address user) internal view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[user];
        uint256 stakedDuration = block.timestamp - stakeInfo.lastUpdated;

        // Calculate the new reward since the last update
        return (stakeInfo.amount * rewardRate * stakedDuration) / 1e18 - stakeInfo.rewardDebt;
    }

    // Function to update reward rate (only owner)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to recover tokens sent to the contract by mistake
    function recoverTokens(IERC20 token, uint256 amount) external onlyOwner {
        token.transfer(msg.sender, amount);
    }
}
```
