"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-manta-network.pages.dev
Prompt: Create a smart contract that facilitates staking $MANTA tokens and distributes rewards based on the Manta Network's staking mechanism.
Generated: DETERMINISTIC_7432640efc7bf90f
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a smart contract in Solidity that facilitates staking $MANTA tokens and rewards distribution:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin's ERC20 interface to interact with $MANTA token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MantaStaking {
    // MANTA token contract address
    IERC20 public mantaToken;

    // Reward rate per second
    uint256 public rewardRate;

    // Data structure to store staker information
    struct Staker {
        uint256 amountStaked; // Total amount staked by the user
        uint256 rewardDebt;   // Rewards already claimed
        uint256 lastStakeTime; // Timestamp of the last staking
    }

    // Mapping to track stakers' information
    mapping(address => Staker) public stakers;

    // Total amount of $MANTA tokens staked in the contract
    uint256 public totalStaked;

    // Owner of the contract
    address public owner;

    // Events for logging contract actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);

    // Modifier to restrict access to owner-specific functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Modifier to check if the caller has staked tokens
    modifier hasStaked() {
        require(stakers[msg.sender].amountStaked > 0, "No tokens staked");
        _;
    }

    // Constructor to initialize contract state
    constructor(IERC20 _mantaToken, uint256 _rewardRate) {
        mantaToken = _mantaToken;
        rewardRate = _rewardRate;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Stake $MANTA tokens in the contract
     * @param _amount Amount of $MANTA tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(
            mantaToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staker's information
        Staker storage staker = stakers[msg.sender];
        if (staker.amountStaked > 0) {
            // Accumulate pending rewards before updating stake
            uint256 pendingRewards = calculateRewards(msg.sender);
            staker.rewardDebt += pendingRewards;
        }

        staker.amountStaked += _amount;
        staker.lastStakeTime = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $MANTA tokens and claim rewards
     */
    function unstake() external hasStaked {
        // Calculate pending rewards
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = calculateRewards(msg.sender);
        uint256 totalRewards = pendingRewards + staker.rewardDebt;

        uint256 amountToUnstake = staker.amountStaked;

        // Update contract state
        totalStaked -= amountToUnstake;
        staker.amountStaked = 0;
        staker.rewardDebt = 0;

        // Transfer staked tokens and rewards back to the user
        require(mantaToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        require(mantaToken.transfer(msg.sender, totalRewards), "Rewards transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Claim rewards without unstaking
     */
    function claimRewards() external hasStaked {
        Staker storage staker = stakers[msg.sender];
        uint256 pendingRewards = calculateRewards(msg.sender);
        uint256 totalRewards = pendingRewards + staker.rewardDebt;

        // Update reward debt
        staker.rewardDebt = 0;
        staker.lastStakeTime = block.timestamp;

        // Transfer rewards to the user
        require(mantaToken.transfer(msg.sender, totalRewards), "Rewards transfer failed");

        emit RewardsClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculate pending rewards for a staker
     * @param _staker Address of the staker
     * @return Pending rewards
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        uint256 timeElapsed = block.timestamp - staker.lastStakeTime;
        uint256 pendingRewards = (staker.amountStaked * rewardRate * timeElapsed) / 1e18;
        return pendingRewards;
    }

    /**
     * @dev Update the reward rate (only callable by the owner)
     * @param _newRewardRate New reward rate per second
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }
}
```

This contract assumes the $MANTA token follows the ERC20 standard, and it uses OpenZeppelin's `IERC20` interface for interaction with the token. Token transfers are handled securely, and reward calculations ensure accuracy over time.
