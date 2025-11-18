"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-in.web.app
Prompt: Generate code to integrate staking functionality for $MPEPE tokens into a DeFi liquidity pool, ensuring rewards are distributed automatically using audited smart contracts.
Generated: DETERMINISTIC_e2f55c74afd7143f
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a clean, well-documented, production-ready Solidity smart contract for staking $MPEPE tokens into a DeFi liquidity pool with automatic rewards distribution:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MPEPE Staking Contract
 * @dev This contract allows users to stake MPEPE tokens into a liquidity pool.
 * Rewards are distributed automatically based on staked amounts and duration.
 * Ensure $MPEPE token contract is ERC-20 compliant.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MPEPEStaking is Ownable, ReentrancyGuard {
    // $MPEPE token interface
    IERC20 public mpepeToken;

    // Struct to hold staking details
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt; // Tracks pending rewards already claimed
    }

    // Mapping to store stakers' data
    mapping(address => Stake) public stakes;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward rate per second (e.g., 10 tokens per second)
    uint256 public rewardRate;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with MPEPE token and reward rate.
     * @param _mpepeToken Address of the MPEPE token contract.
     * @param _rewardRate Reward rate per second (in MPEPE tokens).
     */
    constructor(address _mpepeToken, uint256 _rewardRate) {
        require(_mpepeToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        mpepeToken = IERC20(_mpepeToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to check if the caller has staked tokens.
     */
    modifier hasStake() {
        require(stakes[msg.sender].amount > 0, "No staked tokens");
        _;
    }

    /**
     * @dev Function to stake MPEPE tokens.
     * @param _amount Amount of MPEPE tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            mpepeToken.balanceOf(msg.sender) >= _amount,
            "Insufficient token balance"
        );

        // Transfer the staked tokens to the contract
        mpepeToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's stake data
        Stake storage userStake = stakes[msg.sender];
        userStake.rewardDebt += pendingRewards(msg.sender); // Update pending rewards
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;

        // Update global staked amount
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant hasStake {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;

        // Calculate total rewards
        uint256 totalRewards = pendingRewards(msg.sender);

        // Reset user stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.rewardDebt = 0;

        // Update global staked amount
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to user
        mpepeToken.transfer(msg.sender, stakedAmount);

        // Transfer rewards to user
        if (totalRewards > 0) {
            mpepeToken.transfer(msg.sender, totalRewards);
        }

        emit Unstaked(msg.sender, stakedAmount);
        emit RewardClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Function to claim rewards without unstaking.
     */
    function claimRewards() external nonReentrant hasStake {
        uint256 rewards = pendingRewards(msg.sender);

        require(rewards > 0, "No rewards to claim");

        // Update reward debt
        stakes[msg.sender].rewardDebt = 0;
        stakes[msg.sender].startTime = block.timestamp;

        // Transfer rewards to user
        mpepeToken.transfer(msg.sender, rewards);

        emit RewardClaimed(msg.sender, rewards);
    }

    /**
     * @dev Function to calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function pendingRewards(address _user) public view returns (uint256) {
        Stake memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp - userStake.startTime;
        uint256 totalReward = (elapsedTime * rewardRate * userStake.amount) /
            totalStaked;

        return totalReward - userStake.rewardDebt;
    }

    /**
     * @dev Function to update reward rate by the contract owner.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency function to withdraw tokens by the contract owner.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(
            mpepeToken.balanceOf(address(this)) >= _amount,
            "Insufficient contract token balance"
        );
        mpepeToken.transfer(owner(), _amount);
    }
}
```

### Key Features:
- Follows best practices for Solidity 0.8.x, including `ReentrancyGuard` for protection against reentrancy attacks.
- Uses OpenZeppelin's `Ownable` for administrative control.
- Handles staking, unstaking, and reward claiming functionality.
- Includes proper error handling and checks for invalid inputs.
- Supports reward rate updates and emergency withdrawals by the contract owner.

Make sure you thoroughly test this contract on testnet environments and go through proper auditing before deploying it in production.
