"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Design a smart contract for staking and rewarding WCT tokens on the WalletConnect Network, considering scalability and decentralization.
Generated: DETERMINISTIC_a90c28741c0714d9
Batch ID: 20250622_205139
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WCTStaking is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Struct to represent a staker's information
    struct Staker {
        uint256 amount;         // Amount of tokens staked
        uint256 rewardDebt;     // Reward debt for accounting
        uint256 lastStakeTime;  // Last stake timestamp
    }

    // The WCT token contract
    IERC20 public immutable wctToken;

    // Reward token (could be same as staking token)
    IERC20 public immutable rewardToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward parameters
    uint256 public rewardRate;          // Reward tokens per second
    uint256 public lastUpdateTime;      // Last time reward was calculated
    uint256 public rewardPerTokenStored; // Accumulated rewards per token

    // Staking parameters
    uint256 public minStakeAmount;      // Minimum stake amount
    uint256 public lockDuration;        // Duration tokens are locked after staking (in seconds)

    // Mapping of stakers
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakeAmountUpdated(uint256 newAmount);
    event LockDurationUpdated(uint256 newDuration);

    constructor(
        address _wctToken,
        address _rewardToken,
        uint256 _rewardRate,
        uint256 _minStakeAmount,
        uint256 _lockDuration
    ) {
        require(_wctToken != address(0), "WCT token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");

        wctToken = IERC20(_wctToken);
        rewardToken = IERC20(_rewardToken);
        rewardRate = _rewardRate;
        minStakeAmount = _minStakeAmount;
        lockDuration = _lockDuration;
        lastUpdateTime = block.timestamp;
    }

    // Update reward calculations
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            stakers[account].rewardDebt = earned(account);
        }
        _;
    }

    // Get the last applicable time for reward calculation
    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    // Calculate reward per token
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored + (
            (lastTimeRewardApplicable() - lastUpdateTime) * rewardRate * 1e18 / totalStaked
        );
    }

    // Calculate earned rewards for an account
    function earned(address account) public view returns (uint256) {
        return stakers[account].amount * (rewardPerToken() - stakers[account].rewardDebt) / 1e18;
    }

    // Stake WCT tokens
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(wctToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakers[msg.sender].amount > 0) {
            _claimReward();
        }

        wctToken.safeTransferFrom(msg.sender, address(this), amount);
        stakers[msg.sender].amount += amount;
        stakers[msg.sender].lastStakeTime = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Withdraw staked tokens
    function withdraw(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(stakers[msg.sender].amount >= amount, "Insufficient staked balance");
        require(block.timestamp >= stakers[msg.sender].lastStakeTime + lockDuration, "Tokens are locked");

        _claimReward();

        stakers[msg.sender].amount -= amount;
        totalStaked -= amount;
        wctToken.safeTransfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    // Claim rewards
    function claimReward() external nonReentrant updateReward(msg.sender) {
        _claimReward();
    }

    // Internal function to claim rewards
    function _claimReward() internal {
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            stakers[msg.sender].rewardDebt = rewardPerToken();
            rewardToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    // Admin functions
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
        emit RewardRateUpdated(_rewardRate);
    }

    function setMinStakeAmount(uint256 _minStakeAmount) external onlyOwner {
        minStakeAmount = _minStakeAmount;
        emit MinStakeAmountUpdated(_minStakeAmount);
    }

    function setLockDuration(uint256 _lockDuration) external onlyOwner {
        lockDuration = _lockDuration;
        emit LockDurationUpdated(_lockDuration);
    }

    // Emergency function to recover ERC20 tokens
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(wctToken), "Cannot withdraw staking token");
        IERC20(tokenAddress).safeTransfer(owner(), amount);
    }
}
```
