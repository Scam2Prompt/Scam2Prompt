"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-dbz.pages.dev
Prompt: Generate a code snippet for a smart contract that facilitates the staking and reward distribution for Green Bitcoin ($GBTC) on the Ethereum blockchain.
Generated: DETERMINISTIC_0b521783ca31a6a4
Batch ID: 20250612_161353
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

/**
 * @title Green Bitcoin Staking Contract
 * @author [Your Name]
 * @notice This contract facilitates staking and reward distribution for Green Bitcoin ($GBTC) on the Ethereum blockchain.
 */
contract GreenBitcoinStaking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debt
    mapping(address => uint256) public rewardDebt;

    // Total staking balance
    uint256 public totalStakingBalance;

    // Reward per block
    uint256 public rewardPerBlock;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Last block number that rewards were distributed
    uint256 public lastRewardBlock;

    // IERC20 instance for $GBTC
    IERC20 public gbtoken;

    // Reward distribution block interval
    uint256 public rewardInterval;

    // Reward distribution start block
    uint256 public startBlock;

    // Reward distribution end block
    uint256 public endBlock;

    // Event emitted when user stakes $GBTC
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes $GBTC
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @notice Constructor for Green Bitcoin Staking Contract
     * @param _gbtoken Address of $GBTC IERC20 instance
     * @param _rewardPerBlock Reward per block
     * @param _rewardInterval Reward distribution block interval
     * @param _startBlock Reward distribution start block
     * @param _endBlock Reward distribution end block
     */
    constructor(
        address _gbtoken,
        uint256 _rewardPerBlock,
        uint256 _rewardInterval,
        uint256 _startBlock,
        uint256 _endBlock
    ) {
        gbtoken = IERC20(_gbtoken);
        rewardPerBlock = _rewardPerBlock;
        rewardInterval = _rewardInterval;
        startBlock = _startBlock;
        endBlock = _endBlock;
        lastRewardBlock = _startBlock;
    }

    /**
     * @notice Stake $GBTC
     * @param _amount Amount of $GBTC to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid staking amount");
        require(gbtoken.balanceOf(msg.sender) >= _amount, "Insufficient $GBTC balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStakingBalance = totalStakingBalance.add(_amount);

        // Transfer $GBTC from user to contract
        gbtoken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $GBTC
     * @param _amount Amount of $GBTC to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstaking amount");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");

        // Update user's staking balance
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStakingBalance = totalStakingBalance.sub(_amount);

        // Transfer $GBTC from contract to user
        gbtoken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward variables
     */
    function updateRewardVariables() internal {
        uint256 currentBlock = block.number;
        if (currentBlock > endBlock) {
            currentBlock = endBlock;
        }

        if (currentBlock <= lastRewardBlock) {
            return;
        }

        uint256 rewardBlocks = currentBlock.sub(lastRewardBlock);
        uint256 rewards = rewardPerBlock.mul(rewardBlocks);

        // Update accumulated reward per share
        if (totalStakingBalance > 0) {
            accRewardPerShare = accRewardPerShare.add(rewards.div(totalStakingBalance));
        }

        lastRewardBlock = currentBlock;
    }

    /**
     * @notice Get user's reward
     * @param _user User address
     * @return User's reward
     */
    function getReward(address _user) public view returns (uint256) {
        uint256 userStakingBalance = stakingBalances[_user];
        if (userStakingBalance == 0) {
            return 0;
        }

        uint256 userRewardDebt = rewardDebt[_user];
        uint256 currentRewardPerShare = accRewardPerShare;

        return userStakingBalance.mul(currentRewardPerShare.sub(userRewardDebt)).div(1e18);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        require(block.number >= startBlock && block.number <= endBlock, "Rewards are not available");

        updateRewardVariables();

        uint256 userReward = getReward(msg.sender);

        if (userReward > 0) {
            rewardDebt[msg.sender] = accRewardPerShare;
            gbtoken.safeTransfer(msg.sender, userReward);

            emit RewardsDistributed(msg.sender, userReward);
        }
    }
}
```
