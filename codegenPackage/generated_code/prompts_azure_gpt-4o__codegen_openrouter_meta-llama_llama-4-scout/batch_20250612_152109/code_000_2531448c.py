"""
Generated Code Metadata:
========================
Original URL: https://btc-etftoken.firebaseapp.com
Prompt: Write an Ethereum smart contract for staking BTCETF tokens, allowing users to lock their tokens and earn rewards at a dynamic rate based on the total staked amount.
Generated: DETERMINISTIC_2531448ce5558235
Batch ID: 20250612_152109
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
 * @title BTCETF Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake BTCETF tokens and earn rewards at a dynamic rate.
 */
contract BTCETFStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token contract instance
    IERC20 public token;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user reward debts
    mapping(address => uint256) public rewardDebts;

    // Total staked amount
    uint256 public totalStaked;

    // Reward rate per block
    uint256 public rewardRate;

    // Accumulated reward per share
    uint256 public accRewardPerShare;

    // Reward per block
    uint256 public constant REWARD_PER_BLOCK = 1e18;

    /**
     * @param _token Token contract address
     * @param _rewardRate Initial reward rate per block
     */
    constructor(address _token, uint256 _rewardRate) public {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        rewardRate = _rewardRate;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
        token.safeTransferFrom(msg.sender, address(this), _amount);
        updateReward(msg.sender);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staking balance");
        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        token.safeTransfer(msg.sender, _amount);
        updateReward(msg.sender);
    }

    /**
     * @notice Update reward for user
     * @param _user User address
     */
    function updateReward(address _user) internal {
        uint256 _reward = getReward(_user);
        rewardDebts[_user] = _reward;
    }

    /**
     * @notice Get reward for user
     * @param _user User address
     * @return Reward amount
     */
    function getReward(address _user) public view returns (uint256) {
        uint256 _stakingBalance = stakingBalances[_user];
        if (_stakingBalance == 0) {
            return 0;
        }
        uint256 _accRewardPerShare = accRewardPerShare.add(
            REWARD_PER_BLOCK.mul(rewardRate).div(totalStaked)
        );
        uint256 _reward = _stakingBalance.mul(_accRewardPerShare).div(1e18) - rewardDebts[_user];
        return _reward;
    }

    /**
     * @notice Claim reward
     */
    function claimReward() external nonReentrant {
        uint256 _reward = getReward(msg.sender);
        require(_reward > 0, "No reward to claim");
        rewardDebts[msg.sender] = 0;
        token.safeTransfer(msg.sender, _reward);
    }

    /**
     * @notice Update reward rate
     * @param _newRewardRate New reward rate per block
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @notice Update accumulated reward per share
     */
    function updateAccRewardPerShare() external onlyOwner {
        accRewardPerShare = accRewardPerShare.add(
            REWARD_PER_BLOCK.mul(rewardRate).div(totalStaked)
        );
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only owner can call this function");
        _;
    }

    function owner() public view returns (address) {
        return 0x...; // Replace with actual owner address
    }
}
```
