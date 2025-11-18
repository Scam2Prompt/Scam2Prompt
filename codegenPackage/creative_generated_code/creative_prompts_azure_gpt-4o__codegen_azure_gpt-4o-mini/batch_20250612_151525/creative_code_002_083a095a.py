"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmnt.org
Prompt: Provide a smart contract example in Solidity for staking GMNTCoin that includes features like high APY rewards and daily profit generation, as described in the GMNT web3 staking platform.
Generated: DETERMINISTIC_083a095a8906d833
Batch ID: 20250612_151525
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

// Importing OpenZeppelin Contracts for safe mathematical operations
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract GMNTStaking is ReentrancyGuard {
    // Token being staked
    IERC20 public gmntToken;

    // User staking information
    struct Stake {
        uint256 amount;        // Amount of GMNT tokens staked
        uint256 rewardDebt;    // Rewards debt
        uint256 lastStakeTime; // Last time the user staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // Total tokens staked
    uint256 public totalStaked;

    // Annual Percentage Yield (APY) in basis points (10000 basis points = 100%)
    uint256 public constant APY_BASIS_POINTS = 1000; // 10%
    uint256 public constant SECONDS_IN_YEAR = 31536000; // Total seconds in a year

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the GMNT token
    constructor(IERC20 _gmntToken) {
        gmntToken = _gmntToken;
    }

    // Function to stake GMNT tokens
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        
        // Transfer GMNT tokens from the user to the contract
        gmntToken.transferFrom(msg.sender, address(this), _amount);

        // Update total staked
        totalStaked += _amount;

        // Calculate pending rewards if already staked
        if (stakes[msg.sender].amount > 0) {
            uint256 pendingRewards = calculateRewards(msg.sender);
            stakes[msg.sender].rewardDebt += pendingRewards;
        }

        // Update user stake information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].lastStakeTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake GMNT tokens and claim rewards
    function unstake(uint256 _amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        // Calculate pending rewards
        uint256 pendingRewards = calculateRewards(msg.sender);
        userStake.rewardDebt += pendingRewards;

        // Update the total staked amount
        userStake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer GMNT tokens back to the user
        gmntToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
        claimRewards(); // Automatically claim rewards after unstaking
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakedDuration = block.timestamp - userStake.lastStakeTime;
        uint256 rewardPerSecond = (userStake.amount * APY_BASIS_POINTS / 10000) / SECONDS_IN_YEAR;
        return rewardPerSecond * stakedDuration;
    }

    // Function to claim rewards
    function claimRewards() public nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        uint256 pendingRewards = calculateRewards(msg.sender) + userStake.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        // Reset reward debt after claiming
        userStake.rewardDebt = 0;
        userStake.lastStakeTime = block.timestamp;

        // Transfer the rewards to the user
        gmntToken.transfer(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Function to get user stake information
    function getUserStakeInfo(address _user) external view returns (uint256 amount, uint256 pendingRewards) {
        Stake storage userStake = stakes[_user];
        pendingRewards = calculateRewards(_user) + userStake.rewardDebt;
        return (userStake.amount, pendingRewards);
    }
}
```
