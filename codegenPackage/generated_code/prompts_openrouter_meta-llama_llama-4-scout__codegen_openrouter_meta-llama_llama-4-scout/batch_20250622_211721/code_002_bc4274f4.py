"""
Generated Code Metadata:
========================
Original URL: https://sentai-tokenapp.pages.dev
Prompt: Generate a smart contract code for a token staking platform that includes features like staking, unstaking, and claiming rewards on the Sentai Token network.
Generated: DETERMINISTIC_bc4274f426ebc770
Batch ID: 20250622_211721
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Sentai Token Staking Contract
 * @author [Your Name]
 * @notice This contract provides staking, unstaking, and claiming rewards functionality for Sentai Token.
 */
contract SentaiTokenStaking is Ownable {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => Staker) public stakers;

    // Sentai Token contract instance
    IERC20 public sentaiToken;

    // Reward token contract instance
    IERC20 public rewardToken;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Struct representing a staker's information
     */
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardsEarned;
        uint256 lastClaimedBlock;
    }

    /**
     * @dev Constructor for SentaiTokenStaking contract
     * @param _sentaiToken Address of Sentai Token contract
     * @param _rewardToken Address of reward token contract
     * @param _stakingStart Staking start timestamp
     * @param _stakingEnd Staking end timestamp
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _sentaiToken,
        address _rewardToken,
        uint256 _stakingStart,
        uint256 _stakingEnd,
        uint256 _rewardPerBlock
    ) public {
        require(_sentaiToken != address(0), "Sentai Token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingStart < _stakingEnd, "Staking start timestamp must be less than staking end timestamp");

        sentaiToken = IERC20(_sentaiToken);
        rewardToken = IERC20(_rewardToken);
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake Sentai Tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(stakingStart <= block.timestamp && block.timestamp <= stakingEnd, "Staking period has not started or has ended");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(sentaiToken.balanceOf(msg.sender) >= _amount, "Insufficient Sentai Token balance");

        // Transfer tokens from staker to contract
        sentaiToken.transferFrom(msg.sender, address(this), _amount);

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake Sentai Tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(stakers[msg.sender].stakedAmount >= _amount, "Unstaking amount exceeds staked amount");
        require(_amount > 0, "Unstaking amount must be greater than zero");

        // Update staker information
        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        // Transfer tokens from contract to staker
        sentaiToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(stakers[msg.sender].stakedAmount > 0, "Staker has no staked tokens");

        // Calculate rewards earned
        uint256 rewardsEarned = calculateRewards(msg.sender);

        // Update staker rewards earned
        stakers[msg.sender].rewardsEarned = stakers[msg.sender].rewardsEarned.add(rewardsEarned);
        stakers[msg.sender].lastClaimedBlock = block.number;

        // Transfer rewards to staker
        rewardToken.transfer(msg.sender, rewardsEarned);

        emit RewardsClaimed(msg.sender, rewardsEarned);
    }

    /**
     * @dev Calculate rewards earned by a staker
     * @param _staker Address of staker
     * @return Rewards earned by staker
     */
    function calculateRewards(address _staker) internal view returns (uint256) {
        uint256 stakedBlocks = block.number.sub(stakers[_staker].lastClaimedBlock);
        uint256 rewardsEarned = stakedBlocks.mul(rewardPerBlock).mul(stakers[_staker].stakedAmount).div(totalStaked);

        return rewardsEarned;
    }

    /**
     * @dev Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @dev Withdraw tokens from contract
     * @param _token Address of token to withdraw
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) public onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
