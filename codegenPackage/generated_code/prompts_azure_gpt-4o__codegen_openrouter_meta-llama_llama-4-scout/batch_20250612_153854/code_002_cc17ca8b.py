"""
Generated Code Metadata:
========================
Original URL: https://airdrop-carv.vercel.app
Prompt: Generate Solidity code for a smart contract that facilitates staking $CARV tokens and tracks governance participation.
Generated: DETERMINISTIC_cc17ca8b21cd7253
Batch ID: 20250612_153854
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CarvStakingContract
 * @author [Your Name]
 * @notice A smart contract for staking $CARV tokens and tracking governance participation.
 */
contract CarvStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of staker addresses to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of staker addresses to their governance participation status
    mapping(address => bool) public governanceParticipants;

    // $CARV token contract
    IERC20 public carvToken;

    // Total staked $CARV tokens
    uint256 public totalStaked;

    // Staking start timestamp
    uint256 public stakingStartTime;

    // Staking end timestamp
    uint256 public stakingEndTime;

    // Reward per block
    uint256 public rewardPerBlock;

    // Event emitted when a user stakes $CARV tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes $CARV tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user participates in governance
    event ParticipatedInGovernance(address indexed user);

    // Event emitted when reward is claimed
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @param _carvToken $CARV token contract address
     * @param _stakingStartTime Staking start timestamp
     * @param _stakingEndTime Staking end timestamp
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _carvToken,
        uint256 _stakingStartTime,
        uint256 _stakingEndTime,
        uint256 _rewardPerBlock
    ) {
        require(_carvToken != address(0), "Invalid $CARV token contract address");
        require(_stakingStartTime > block.timestamp, "Staking start time must be in the future");
        require(_stakingEndTime > _stakingStartTime, "Staking end time must be after staking start time");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");

        carvToken = IERC20(_carvToken);
        stakingStartTime = _stakingStartTime;
        stakingEndTime = _stakingEndTime;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake $CARV tokens
     * @param _amount Amount of $CARV tokens to stake
     */
    function stake(uint256 _amount) external {
        require(stakingStartTime <= block.timestamp && block.timestamp <= stakingEndTime, "Staking period has not started or has ended");
        require(_amount > 0, "Stake amount must be greater than 0");
        require(carvToken.balanceOf(msg.sender) >= _amount, "Insufficient $CARV token balance");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.rewardDebt = staker.rewardDebt.add(_amount);

        totalStaked = totalStaked.add(_amount);

        carvToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $CARV tokens
     * @param _amount Amount of $CARV tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(stakingEndTime <= block.timestamp, "Staking period has not ended");
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked $CARV tokens");

        Staker storage staker = stakers[msg.sender];
        staker.stakedAmount = staker.stakedAmount.sub(_amount);
        staker.rewardDebt = staker.rewardDebt.sub(_amount);

        totalStaked = totalStaked.sub(_amount);

        carvToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Participate in governance
     */
    function participateInGovernance() external {
        require(stakers[msg.sender].stakedAmount > 0, "You must have staked $CARV tokens to participate in governance");
        require(!governanceParticipants[msg.sender], "You have already participated in governance");

        governanceParticipants[msg.sender] = true;

        emit ParticipatedInGovernance(msg.sender);
    }

    /**
     * @dev Claim reward
     */
    function claimReward() external {
        require(stakers[msg.sender].stakedAmount > 0, "You must have staked $CARV tokens to claim reward");

        Staker storage staker = stakers[msg.sender];
        uint256 reward = staker.stakedAmount.mul(rewardPerBlock).div(1e18);
        staker.rewardDebt = staker.rewardDebt.sub(reward);

        carvToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Struct for staker information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    /**
     * @dev Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        require(_newRewardPerBlock > 0, "Reward per block must be greater than 0");

        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @dev Withdraw $CARV tokens from the contract
     * @param _amount Amount of $CARV tokens to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(carvToken.balanceOf(address(this)) >= _amount, "Insufficient $CARV token balance in the contract");

        carvToken.safeTransfer(msg.sender, _amount);
    }
}
```
