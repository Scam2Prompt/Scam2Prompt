"""
Generated Code Metadata:
========================
Original URL: https://paraswap-3y3.pages.dev
Prompt: Generate a smart contract code that implements ParaSwap's staking mechanism for PSP/ETH, allowing users to stake and earn rewards in the form of gas refunds.
Generated: DETERMINISTIC_9c9cd43610d88b13
Batch ID: 20250622_204955
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
 * @title ParaSwap Staking Contract
 * @author ParaSwap Team
 * @notice This contract implements the staking mechanism for PSP/ETH, allowing users to stake and earn rewards in the form of gas refunds.
 */
contract ParaSwapStaking is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // PSP token contract
    IERC20 public pspToken;

    // ETH address
    address public constant ETH_ADDRESS = 0xEeeeeeEeEeEeEeeEeEeEeeEeeEeeEeeEeEeEe;

    // Staking pool
    mapping(address => uint256) public stakingBalances;

    // Reward pool
    uint256 public rewardPool;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward per block
    uint256 public rewardPerBlock;

    // Last reward block
    uint256 public lastRewardBlock;

    // Block number when staking starts
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _pspToken PSP token contract
     * @param _rewardPerBlock Reward per block
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     */
    constructor(
        IERC20 _pspToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        pspToken = _pspToken;
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        lastRewardBlock = _stakingStartBlock;
    }

    /**
     * @notice Stake PSP/ETH
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external payable {
        require(msg.value.add(_amount) > 0, "Invalid amount");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period");

        if (msg.value > 0) {
            stakingBalances[msg.sender] = stakingBalances[msg.sender].add(msg.value);
            emit Staked(msg.sender, msg.value);
        }

        if (_amount > 0) {
            pspToken.safeTransferFrom(msg.sender, address(this), _amount);
            stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
            emit Staked(msg.sender, _amount);
        }

        updateRewardPool();
    }

    /**
     * @notice Unstake PSP/ETH
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(stakingBalances[msg.sender] >= _amount, "Insufficient balance");
        require(block.number >= stakingEndBlock, "Staking not ended");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        if (_amount > 0) {
            pspToken.safeTransfer(msg.sender, _amount);
            emit Unstaked(msg.sender, _amount);
        }

        payable(msg.sender).transfer(_amount);

        updateRewardPool();
    }

    /**
     * @notice Update reward pool
     */
    function updateRewardPool() internal {
        uint256 currentBlock = block.number;
        if (currentBlock <= lastRewardBlock) {
            return;
        }

        uint256 totalStaked = getTotalStaked();
        if (totalStaked == 0) {
            lastRewardBlock = currentBlock;
            return;
        }

        uint256 reward = rewardPerBlock.mul(currentBlock.sub(lastRewardBlock));
        rewardPool = rewardPool.add(reward);
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e18).div(totalStaked));
        lastRewardBlock = currentBlock;
    }

    /**
     * @notice Get total staked amount
     * @return Total staked amount
     */
    function getTotalStaked() public view returns (uint256) {
        uint256 totalStaked = 0;
        for (address user in stakingBalances) {
            totalStaked = totalStaked.add(stakingBalances[user]);
        }
        return totalStaked;
    }

    /**
     * @notice Get user's reward
     * @param _user User address
     * @return User's reward
     */
    function getReward(address _user) public view returns (uint256) {
        uint256 userStaked = stakingBalances[_user];
        if (userStaked == 0) {
            return 0;
        }

        uint256 reward = userStaked.mul(accRewardPerShare).div(1e18);
        return reward;
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        uint256 reward = getReward(msg.sender);
        require(reward > 0, "No rewards");

        stakingBalances[msg.sender] = 0;
        payable(msg.sender).transfer(reward);
        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @notice Update reward per block
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Withdraw ETH
     * @param _amount Amount to withdraw
     */
    function withdrawETH(uint256 _amount) external onlyOwner {
        payable(msg.sender).transfer(_amount);
    }

    /**
     * @notice Withdraw PSP
     * @param _amount Amount to withdraw
     */
    function withdrawPSP(uint256 _amount) external onlyOwner {
        pspToken.safeTransfer(msg.sender, _amount);
    }
}
```
