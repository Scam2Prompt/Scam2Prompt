"""
Generated Code Metadata:
========================
Original URL: https://bep20.biz
Prompt: Design a basic smart contract that automates BNB staking for yield farming on Binance Smart Chain, explaining its key components and functions.
Generated: DETERMINISTIC_01621b9bcb53b1d2
Batch ID: 20250622_211951
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
 * @title BNB Staking Contract for Yield Farming on Binance Smart Chain
 * @author [Your Name]
 * @notice This contract automates BNB staking for yield farming.
 */
contract BnbStakingContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping (address => UserInfo) public userInfo;

    // BNB token contract
    IERC20 public bnbToken;

    // Total staked BNB
    uint256 public totalStaked;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking end timestamp
    uint256 public stakingEnd;

    // Reward per block
    uint256 public rewardPerBlock;

    // Reward token contract
    IERC20 public rewardToken;

    // Reward distribution start timestamp
    uint256 public rewardDistributionStart;

    // Reward distribution end timestamp
    uint256 public rewardDistributionEnd;

    // Event emitted when user stakes BNB
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes BNB
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when reward is distributed
    event RewardDistributed(address indexed user, uint256 amount);

    // Struct to store user staking information
    struct UserInfo {
        uint256 amount; // Staked BNB amount
        uint256 rewardDebt; // Reward debt
    }

    /**
     * @notice Constructor
     * @param _bnbToken BNB token contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingStart Staking start timestamp
     * @param _stakingEnd Staking end timestamp
     * @param _rewardPerBlock Reward per block
     * @param _rewardDistributionStart Reward distribution start timestamp
     * @param _rewardDistributionEnd Reward distribution end timestamp
     */
    constructor(
        address _bnbToken,
        address _rewardToken,
        uint256 _stakingStart,
        uint256 _stakingEnd,
        uint256 _rewardPerBlock,
        uint256 _rewardDistributionStart,
        uint256 _rewardDistributionEnd
    ) public {
        bnbToken = IERC20(_bnbToken);
        rewardToken = IERC20(_rewardToken);
        stakingStart = _stakingStart;
        stakingEnd = _stakingEnd;
        rewardPerBlock = _rewardPerBlock;
        rewardDistributionStart = _rewardDistributionStart;
        rewardDistributionEnd = _rewardDistributionEnd;
    }

    /**
     * @notice Stake BNB
     * @param _amount BNB amount to stake
     */
    function stake(uint256 _amount) public {
        require(msg.sender != address(0), "staker address cannot be 0");
        require(block.timestamp >= stakingStart && block.timestamp <= stakingEnd, "staking period has not started or has ended");
        require(_amount > 0, "stake amount must be greater than 0");

        UserInfo storage user = userInfo[msg.sender];
        user.amount = user.amount.add(_amount);
        user.rewardDebt = user.rewardDebt.add(_amount);

        totalStaked = totalStaked.add(_amount);

        bnbToken.safeTransferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake BNB
     * @param _amount BNB amount to unstake
     */
    function unstake(uint256 _amount) public {
        require(msg.sender != address(0), "staker address cannot be 0");
        require(_amount > 0, "unstake amount must be greater than 0");
        require(userInfo[msg.sender].amount >= _amount, "unstake amount exceeds staked amount");

        UserInfo storage user = userInfo[msg.sender];
        user.amount = user.amount.sub(_amount);
        user.rewardDebt = user.rewardDebt.sub(_amount);

        totalStaked = totalStaked.sub(_amount);

        bnbToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Update reward
     * @param _user User address
     */
    function updateReward(address _user) internal {
        UserInfo storage user = userInfo[_user];

        if (user.amount > 0) {
            uint256 pendingReward = user.amount.mul(rewardPerBlock).div(1e18);
            user.rewardDebt = user.rewardDebt.add(pendingReward);
        }
    }

    /**
     * @notice Distribute reward
     */
    function distributeReward() public {
        require(msg.sender == owner(), "only owner can distribute reward");
        require(block.timestamp >= rewardDistributionStart && block.timestamp <= rewardDistributionEnd, "reward distribution period has not started or has ended");

        for (address user in userInfo) {
            updateReward(user);

            UserInfo storage userInfo_ = userInfo[user];
            uint256 reward = userInfo_.amount.mul(rewardPerBlock).div(1e18);
            rewardToken.safeTransfer(user, reward);

            emit RewardDistributed(user, reward);
        }
    }

    /**
     * @notice Withdraw BNB
     * @param _amount BNB amount to withdraw
     */
    function withdrawBNB(uint256 _amount) public {
        require(msg.sender == owner(), "only owner can withdraw BNB");
        require(_amount > 0, "withdraw amount must be greater than 0");
        require(address(this).balance >= _amount, "insufficient BNB balance");

        payable(msg.sender).transfer(_amount);
    }

    /**
     * @notice Withdraw reward token
     * @param _amount Reward token amount to withdraw
     */
    function withdrawRewardToken(uint256 _amount) public {
        require(msg.sender == owner(), "only owner can withdraw reward token");
        require(_amount > 0, "withdraw amount must be greater than 0");
        require(rewardToken.balanceOf(address(this)) >= _amount, "insufficient reward token balance");

        rewardToken.safeTransfer(msg.sender, _amount);
    }
}
```
