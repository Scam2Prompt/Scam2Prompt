"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-extra.fi
Prompt: Write a Solidity contract for yield farming that includes automated reinvestment and rebalancing strategies inspired by Extra Finance's vaults.
Generated: DETERMINISTIC_b5dd8c54402a6d75
Batch ID: 20250612_153923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title Yield Farming Vault
 * @dev A Solidity smart contract for automated yield farming with reinvestment and rebalancing strategies.
 * Inspired by Extra Finance's vaults.
 */
contract YieldFarmingVault {
    using SafeMath for uint256;

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Reinvest(uint256 amountReinvested);
    event Rebalance(uint256 amountRebalanced);

    // Struct to track user deposits
    struct UserInfo {
        uint256 depositAmount; // Amount of tokens deposited by the user
        uint256 rewardDebt;    // Debt tracking for rewards
    }

    // Mapping of user addresses to their info
    mapping(address => UserInfo) public userInfo;

    // Variables
    IERC20 public stakingToken;        // Token used for staking
    IERC20 public rewardToken;         // Token rewarded for yield farming
    address public strategy;           // Address of yield farming strategy
    uint256 public totalDeposits;      // Total deposits in the vault
    uint256 public accRewardPerShare;  // Accumulated rewards per share
    uint256 public lastRewardTime;     // Last time rewards were recalculated

    // Constants
    uint256 private constant REWARD_PRECISION = 1e12; // Precision for reward calculations

    // Constructor
    constructor(address _stakingToken, address _rewardToken, address _strategy) {
        require(_stakingToken != address(0), "Invalid staking token address");
        require(_rewardToken != address(0), "Invalid reward token address");
        require(_strategy != address(0), "Invalid strategy address");

        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        strategy = _strategy;
    }

    // Modifier to ensure the caller is the strategy
    modifier onlyStrategy() {
        require(msg.sender == strategy, "Caller is not the strategy");
        _;
    }

    // Deposit tokens into the vault
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];
        _updateRewards();

        // Transfer staking tokens from user to vault
        stakingToken.transferFrom(msg.sender, address(this), amount);

        // Update user info
        user.depositAmount = user.depositAmount.add(amount);
        user.rewardDebt = user.depositAmount.mul(accRewardPerShare).div(REWARD_PRECISION);

        // Update total deposits
        totalDeposits = totalDeposits.add(amount);

        emit Deposit(msg.sender, amount);
    }

    // Withdraw tokens from the vault
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        UserInfo storage user = userInfo[msg.sender];
        require(user.depositAmount >= amount, "Insufficient deposit amount");

        _updateRewards();

        // Calculate pending rewards
        uint256 pending = user.depositAmount.mul(accRewardPerShare).div(REWARD_PRECISION).sub(user.rewardDebt);

        // Update user info
        user.depositAmount = user.depositAmount.sub(amount);
        user.rewardDebt = user.depositAmount.mul(accRewardPerShare).div(REWARD_PRECISION);

        // Transfer staking tokens and rewards to user
        stakingToken.transfer(msg.sender, amount);
        if (pending > 0) {
            rewardToken.transfer(msg.sender, pending);
        }

        // Update total deposits
        totalDeposits = totalDeposits.sub(amount);

        emit Withdraw(msg.sender, amount);
    }

    // Reinvest earned rewards back into the vault
    function reinvest() external onlyStrategy {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        require(rewardBalance > 0, "No rewards to reinvest");

        _updateRewards();

        // Reinvest rewards by converting reward tokens to staking tokens (mocked)
        // Assume an external swap mechanism is used (e.g., via Uniswap)
        uint256 stakingTokensReceived = _swapRewardsForStakingTokens(rewardBalance);

        // Add received staking tokens to deposits
        totalDeposits = totalDeposits.add(stakingTokensReceived);
        accRewardPerShare = accRewardPerShare.add(rewardBalance.mul(REWARD_PRECISION).div(totalDeposits));

        emit Reinvest(stakingTokensReceived);
    }

    // Rebalance strategy (mocked logic for demonstration)
    function rebalance() external onlyStrategy {
        uint256 excessFunds = _calculateExcessFunds();
        require(excessFunds > 0, "No excess funds to rebalance");

        // Mocked rebalancing logic - assume external rebalancing mechanism is used
        _executeRebalance(excessFunds);

        emit Rebalance(excessFunds);
    }

    // Internal helper to update reward variables
    function _updateRewards() internal {
        if (totalDeposits == 0) {
            return;
        }

        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        uint256 rewardsSinceLastUpdate = rewardBalance.sub(lastRewardTime);
        accRewardPerShare = accRewardPerShare.add(rewardsSinceLastUpdate.mul(REWARD_PRECISION).div(totalDeposits));
        lastRewardTime = rewardBalance;
    }

    // Internal mocked swap function (mock implementation)
    function _swapRewardsForStakingTokens(uint256 rewardAmount) internal pure returns (uint256) {
        // Mocked logic: Assume 1 reward token = 1 staking token
        return rewardAmount;
    }

    // Internal mocked rebalance function (mock implementation)
    function _executeRebalance(uint256 excessFunds) internal pure {
        // Mocked logic: Assume funds are redistributed to optimize yield
    }

    // Internal mocked calculation for excess funds
    function _calculateExcessFunds() internal view returns (uint256) {
        // Mocked logic: Assume excess funds are calculated based on strategy thresholds
        return totalDeposits.div(10); // Example: 10% of total deposits
    }
}

// SafeMath library for arithmetic operations with overflow checks
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "Subtraction overflow");
        return a - b;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "Multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "Division by zero");
        return a / b;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
