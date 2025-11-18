"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-virtuswap.pages.dev
Prompt: Write code to simulate a staking mechanism for a DeFi application, inspired by the Virtuswap staking functionality.
Generated: DETERMINISTIC_94bfced884177923
Batch ID: 20250612_152527
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title StakingContract
 * @dev This contract allows users to stake ERC20 tokens to earn rewards.
 */
contract StakingContract is Ownable {
    // Token being staked
    IERC20 public stakingToken;

    // Address of the reward token
    IERC20 public rewardToken;

    // Struct to represent each staker's info
    struct StakerInfo {
        uint256 amountStaked; // Amount of tokens staked
        uint256 rewardDebt;   // Accumulated rewards
    }

    // Mapping of stakers to their information
    mapping(address => StakerInfo) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Reward per block for staking
    uint256 public rewardPerBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to check if the user has staked
    modifier hasStaked(address _user) {
        require(stakers[_user].amountStaked > 0, "No tokens staked");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the staking token.
     * @param _rewardToken Address of the reward token.
     * @param _rewardPerBlock Reward amount for each block.
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _rewardPerBlock
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from the staker to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker's information
        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external hasStaked(msg.sender) {
        require(_amount > 0, "Amount must be greater than 0");
        require(_amount <= stakers[msg.sender].amountStaked, "Insufficient staked amount");

        // Update staker's information
        StakerInfo storage staker = stakers[msg.sender];
        staker.amountStaked -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the staker
        stakingToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
        
        // Optionally claim rewards when unstaking
        claimRewards();
    }

    /**
     * @dev Calculate and claim rewards for the staker.
     */
    function claimRewards() public hasStaked(msg.sender) {
        // Calculate rewards based on the amount staked and blocks passed
        uint256 rewards = stakers[msg.sender].amountStaked * rewardPerBlock; // Simplified reward calculation

        // Update reward debt
        stakers[msg.sender].rewardDebt += rewards;

        // Transfer rewards to the staker
        rewardToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev View function to get the amount of tokens staked by a user.
     * @param _user Address of the user.
     * @return Amount of tokens staked.
     */
    function getStakedAmount(address _user) external view returns (uint256) {
        return stakers[_user].amountStaked;
    }
}
```
