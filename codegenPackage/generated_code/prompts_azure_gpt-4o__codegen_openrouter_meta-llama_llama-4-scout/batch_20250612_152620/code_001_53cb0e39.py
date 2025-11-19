"""
Generated Code Metadata:
========================
Original URL: https://scotty-ai.pages.dev
Prompt: Create a smart contract in Solidity that implements staking functionality for $SCOTTY tokens, including features like tracking staked balances, calculating rewards per ETH block, and allowing users to claim their rewards.
Generated: DETERMINISTIC_53cb0e397c94b0af
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @author [Your Name]
 * @notice A staking contract for $SCOTTY tokens.
 */
contract StakingContract is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debts
    mapping(address => uint256) public rewardDebts;

    // $SCOTTY token contract
    IERC20 public scottyToken;

    // Reward per ETH block
    uint256 public rewardPerBlock;

    // Total staked balance
    uint256 public totalStaked;

    // Last block number that reward was distributed
    uint256 public lastRewardBlock;

    // Reward distribution start block
    uint256 public startBlock;

    // Reward distribution end block
    uint256 public endBlock;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user claims rewards
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _scottyToken $SCOTTY token contract address
     * @param _rewardPerBlock Reward per ETH block
     * @param _startBlock Reward distribution start block
     * @param _endBlock Reward distribution end block
     */
    constructor(
        address _scottyToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) {
        require(_scottyToken != address(0), "Invalid token address");
        require(_rewardPerBlock > 0, "Reward per block must be greater than 0");
        require(_startBlock < _endBlock, "Invalid block range");

        scottyToken = IERC20(_scottyToken);
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
        lastRewardBlock = _startBlock;
    }

    /**
     * @notice Stake $SCOTTY tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(stakingBalances[msg.sender].add(_amount) >= 0, "Overflow");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);

        scottyToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $SCOTTY tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than 0");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staked balance");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        scottyToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external nonReentrant {
        uint256 _reward = getReward(msg.sender);
        require(_reward > 0, "No rewards to claim");

        rewardDebts[msg.sender] = rewardDebts[msg.sender].add(_reward);
        payable(msg.sender).transfer(_reward);

        emit RewardsClaimed(msg.sender, _reward);
    }

    /**
     * @notice Get user reward
     * @param _user User address
     * @return Reward amount
     */
    function getReward(address _user) public view returns (uint256) {
        uint256 _reward = 0;

        if (block.number > startBlock && block.number <= endBlock) {
            uint256 _lastRewardBlock = lastRewardBlock > startBlock ? lastRewardBlock : startBlock;
            uint256 _blocks = block.number.sub(_lastRewardBlock);

            _reward = totalStaked.mul(rewardPerBlock).mul(_blocks);
            _reward = _reward.div(1e18); // Assuming 18 decimals for reward token
        }

        return _reward.sub(rewardDebts[_user]);
    }

    /**
     * @notice Update last reward block and distribute rewards
     */
    function updateLastRewardBlock() internal {
        if (block.number > lastRewardBlock && totalStaked > 0) {
            uint256 _reward = rewardPerBlock.mul(block.number.sub(lastRewardBlock));
            _reward = _reward.mul(totalStaked).div(1e18); // Assuming 18 decimals for reward token

            // Distribute rewards to users ( implement your distribution logic here )
            // For simplicity, this example just updates the last reward block
            lastRewardBlock = block.number;
        }
    }
}
```
