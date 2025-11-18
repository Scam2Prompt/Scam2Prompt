"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-claim.pages.dev
Prompt: Generate Solidity code for a smart contract that enables double staking rewards on the Pepe Unchained blockchain, as described in the $PEPU ecosystem.
Generated: DETERMINISTIC_9d5879a73b1773d8
Batch ID: 20250612_150119
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
 * @title DoubleStakingRewards
 * @dev A smart contract for double staking rewards on the Pepe Unchained blockchain
 * in the $PEPU ecosystem.
 */
contract DoubleStakingRewards {
    // Token interfaces
    IERC20 public stakingToken; // Token to be staked
    IERC20 public rewardToken1; // First reward token
    IERC20 public rewardToken2; // Second reward token

    // State variables
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total staked amount
    uint256 public rewardRate1; // Reward rate for the first reward token
    uint256 public rewardRate2; // Reward rate for the second reward token
    uint256 public lastUpdateTime; // Last time rewards were updated
    
    mapping(address => uint256) public stakedBalances; // Track staked balances
    mapping(address => uint256) public rewardBalances1; // Track earned rewards for token1
    mapping(address => uint256) public rewardBalances2; // Track earned rewards for token2

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward1, uint256 reward2);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateRewards(address account) {
        if (account != address(0)) {
            rewardBalances1[account] += _earned(account, rewardRate1);
            rewardBalances2[account] += _earned(account, rewardRate2);
        }
        lastUpdateTime = block.timestamp;
        _;
    }

    /**
     * @notice Constructor to initialize the contract.
     * @param _stakingToken Address of the staking token.
     * @param _rewardToken1 Address of the first reward token.
     * @param _rewardToken2 Address of the second reward token.
     * @param _rewardRate1 Reward rate for token1.
     * @param _rewardRate2 Reward rate for token2.
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken1,
        IERC20 _rewardToken2,
        uint256 _rewardRate1,
        uint256 _rewardRate2
    ) {
        owner = msg.sender;
        stakingToken = _stakingToken;
        rewardToken1 = _rewardToken1;
        rewardToken2 = _rewardToken2;
        rewardRate1 = _rewardRate1;
        rewardRate2 = _rewardRate2;
        lastUpdateTime = block.timestamp;
    }

    /**
     * @notice Stake tokens to earn rewards.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        stakingToken.transferFrom(msg.sender, address(this), amount);
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Withdraw staked tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance");
        stakedBalances[msg.sender] -= amount;
        totalStaked -= amount;
        stakingToken.transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @notice Claim earned rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 reward1 = rewardBalances1[msg.sender];
        uint256 reward2 = rewardBalances2[msg.sender];
        require(reward1 > 0 || reward2 > 0, "No rewards available");
        rewardBalances1[msg.sender] = 0;
        rewardBalances2[msg.sender] = 0;
        if (reward1 > 0) {
            rewardToken1.transfer(msg.sender, reward1);
        }
        if (reward2 > 0) {
            rewardToken2.transfer(msg.sender, reward2);
        }
        emit RewardsClaimed(msg.sender, reward1, reward2);
    }

    /**
     * @notice Calculate earned rewards for a user.
     * @param account The address of the user.
     * @param rate The reward rate to apply.
     * @return The amount of rewards earned.
     */
    function _earned(address account, uint256 rate) internal view returns (uint256) {
        return (stakedBalances[account] * rate * (block.timestamp - lastUpdateTime)) / 1e18;
    }

    /**
     * @notice Update reward rates.
     * @param _rewardRate1 New reward rate for token1.
     * @param _rewardRate2 New reward rate for token2.
     */
    function updateRewardRates(uint256 _rewardRate1, uint256 _rewardRate2) external onlyOwner {
        rewardRate1 = _rewardRate1;
        rewardRate2 = _rewardRate2;
    }

    /**
     * @notice Emergency withdrawal of tokens by the owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(owner, amount);
    }
}

/**
 * @dev Minimal interface for ERC20 functions used in the contract.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
