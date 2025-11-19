"""
Generated Code Metadata:
========================
Original URL: https://mindofpepetoken.network
Prompt: Create a smart contract in Solidity for staking $MIND tokens with dynamic APY rewards, ensuring compatibility with Ethereum-based wallets.
Generated: DETERMINISTIC_0e0905590dc23301
Batch ID: 20250612_153954
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MindStakingContract
 * @author [Your Name]
 * @notice A smart contract for staking $MIND tokens with dynamic APY rewards.
 */
contract MindStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // $MIND token contract
    IERC20 public mindToken;

    // Reward token contract (assuming $MIND for simplicity)
    IERC20 public rewardToken;

    // Dynamic APY reward rate (initial value, can be updated)
    uint256 public apyRewardRate;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last block number for reward distribution
    uint256 public lastRewardBlock;

    // Block number when the contract was deployed
    uint256 public deployBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardDistributed(address indexed user, uint256 amount);
    event ApyRewardRateUpdated(uint256 newRate);

    /**
     * @param _mindToken $MIND token contract address
     * @param _rewardToken Reward token contract address (assuming $MIND)
     * @param _apyRewardRate Initial APY reward rate (in percent)
     * @param _rewardPerBlock Initial reward per block
     */
    constructor(
        address _mindToken,
        address _rewardToken,
        uint256 _apyRewardRate,
        uint256 _rewardPerBlock
    ) public {
        mindToken = IERC20(_mindToken);
        rewardToken = IERC20(_rewardToken);
        apyRewardRate = _apyRewardRate;
        rewardPerBlock = _rewardPerBlock;
        deployBlock = block.number;
        lastRewardBlock = deployBlock;
    }

    /**
     * @dev Update APY reward rate
     * @param _newRate New APY reward rate (in percent)
     */
    function updateApyRewardRate(uint256 _newRate) public onlyOwner {
        apyRewardRate = _newRate;
        emit ApyRewardRateUpdated(_newRate);
    }

    /**
     * @dev Stake $MIND tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Invalid stake amount");

        // Transfer $MIND tokens to the contract
        mindToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance and reward debt
        if (stakingBalances[msg.sender] > 0) {
            _distributeReward(msg.sender);
        }

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        rewardDebt[msg.sender] = _getRewardDebt(msg.sender);
        totalStakingBalance = totalStakingBalance.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $MIND tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(_amount > 0, "Invalid unstake amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance and reward debt
        _distributeReward(msg.sender);

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        rewardDebt[msg.sender] = _getRewardDebt(msg.sender);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer $MIND tokens back to the user
        mindToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute reward to user
     * @param _user User address
     */
    function _distributeReward(address _user) internal {
        uint256 pendingReward = _getPendingReward(_user);
        if (pendingReward > 0) {
            rewardDebt[_user] = _getRewardDebt(_user);
            rewardToken.safeTransfer(_user, pendingReward);
            emit RewardDistributed(_user, pendingReward);
        }
    }

    /**
     * @dev Get user's pending reward
     * @param _user User address
     * @return Pending reward amount
     */
    function _getPendingReward(address _user) internal view returns (uint256) {
        uint256 userStakingBalance = stakingBalances[_user];
        if (userStakingBalance == 0) {
            return 0;
        }

        uint256 blocksSinceLastReward = block.number.sub(lastRewardBlock);
        uint256 reward = blocksSinceLastReward.mul(rewardPerBlock).mul(userStakingBalance).div(totalStakingBalance);

        // Apply APY reward rate
        reward = reward.add(reward.mul(apyRewardRate).div(100));

        return reward;
    }

    /**
     * @dev Get user's reward debt
     * @param _user User address
     * @return Reward debt amount
     */
    function _getRewardDebt(address _user) internal view returns (uint256) {
        return stakingBalances[_user].mul(block.number).div(deployBlock);
    }

    /**
     * @dev Update last reward block and distribute rewards
     */
    function _updateLastRewardBlock() internal {
        if (block.number > lastRewardBlock) {
            uint256 blocksSinceLastReward = block.number.sub(lastRewardBlock);
            uint256 totalReward = blocksSinceLastReward.mul(rewardPerBlock).mul(totalStakingBalance).div(totalStakingBalance);

            // Apply APY reward rate
            totalReward = totalReward.add(totalReward.mul(apyRewardRate).div(100));

            rewardToken.safeTransfer(msg.sender, totalReward);

            lastRewardBlock = block.number;
        }
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Function to claim reward
    function claimReward() public {
        _distributeReward(msg.sender);
        _updateLastRewardBlock();
    }
}
```
