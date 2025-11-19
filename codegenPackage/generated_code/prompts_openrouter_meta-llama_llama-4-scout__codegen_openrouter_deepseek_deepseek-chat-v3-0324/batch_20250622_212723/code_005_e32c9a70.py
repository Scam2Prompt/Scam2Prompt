"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: "Create a staking mechanism for WMTx that allocates rewards to node operators and World Mobile products, using a non-custodial vault for secure management."
Generated: DETERMINISTIC_e32c9a700aabe66d
Batch ID: 20250622_212723
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
import "@openzeppelin/contracts/access/Ownable.sol";

contract WMTxStaking is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    struct Stake {
        uint256 amount;
        uint256 stakedAt;
        uint256 lastClaimed;
    }

    IERC20 public immutable wmtxToken;
    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public rewardPool;
    uint256 public constant REWARD_DURATION = 30 days;
    uint256 public constant NODE_OPERATOR_SHARE = 70; // 70%
    uint256 public constant PRODUCT_SHARE = 30; // 30%

    address public nodeOperatorPool;
    address public productPool;

    mapping(address => Stake) public stakes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event RewardPoolFunded(uint256 amount);
    event RewardRateUpdated(uint256 newRate);
    event PoolsUpdated(address nodeOperatorPool, address productPool);

    constructor(
        address _wmtxToken,
        address _nodeOperatorPool,
        address _productPool,
        uint256 _initialRewardRate
    ) {
        require(_wmtxToken != address(0), "Invalid token address");
        require(_nodeOperatorPool != address(0), "Invalid node operator pool");
        require(_productPool != address(0), "Invalid product pool");

        wmtxToken = IERC20(_wmtxToken);
        nodeOperatorPool = _nodeOperatorPool;
        productPool = _productPool;
        rewardRate = _initialRewardRate;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        Stake storage userStake = stakes[msg.sender];
        if (userStake.amount > 0) {
            _claimRewards(msg.sender);
        }

        wmtxToken.safeTransferFrom(msg.sender, address(this), amount);
        userStake.amount += amount;
        userStake.stakedAt = block.timestamp;
        userStake.lastClaimed = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");
        
        _claimRewards(msg.sender);

        userStake.amount -= amount;
        totalStaked -= amount;
        wmtxToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external nonReentrant {
        _claimRewards(msg.sender);
    }

    function _claimRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) return;

        uint256 reward = calculateReward(user);
        if (reward == 0) return;

        userStake.lastClaimed = block.timestamp;

        uint256 nodeOperatorReward = (reward * NODE_OPERATOR_SHARE) / 100;
        uint256 productReward = (reward * PRODUCT_SHARE) / 100;

        wmtxToken.safeTransfer(nodeOperatorPool, nodeOperatorReward);
        wmtxToken.safeTransfer(productPool, productReward);

        emit RewardClaimed(user, reward);
    }

    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 timeElapsed = block.timestamp - userStake.lastClaimed;
        uint256 reward = (userStake.amount * rewardRate * timeElapsed) / (100 * REWARD_DURATION);
        return reward;
    }

    function fundRewardPool(uint256 amount) external onlyOwner {
        wmtxToken.safeTransferFrom(msg.sender, address(this), amount);
        rewardPool += amount;
        emit RewardPoolFunded(amount);
    }

    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than 0");
        rewardRate = newRate;
        emit RewardRateUpdated(newRate);
    }

    function updatePools(address _nodeOperatorPool, address _productPool) external onlyOwner {
        require(_nodeOperatorPool != address(0), "Invalid node operator pool");
        require(_productPool != address(0), "Invalid product pool");
        
        nodeOperatorPool = _nodeOperatorPool;
        productPool = _productPool;
        emit PoolsUpdated(_nodeOperatorPool, _productPool);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = wmtxToken.balanceOf(address(this));
        wmtxToken.safeTransfer(owner(), balance);
    }
}
```
