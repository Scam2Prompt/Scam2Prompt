"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapps-syncz.web.app
Prompt: Create a smart contract for staking and claiming rewards using Layerium's governance features on Optimistic Rollup.
Generated: DETERMINISTIC_ce6e03b6812171e3
Batch ID: 20250612_150920
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
 * @title StakingContract
 * @dev A smart contract for staking tokens and claiming rewards using Layerium's governance features.
 */
contract StakingContract {
    // Token used for staking
    IERC20 public stakingToken;

    // Staking reward token
    IERC20 public rewardToken;

    // Governance address for Layerium
    address public governance;

    // Reward rate per second
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user addresses to their staked balances
    mapping(address => uint256) public stakedBalances;

    // Mapping of user addresses to their last update timestamp
    mapping(address => uint256) public lastUpdateTime;

    // Mapping of user addresses to their pending rewards
    mapping(address => uint256) public rewards;

    /**
     * @dev Modifier to ensure only the governance can call restricted functions.
     */
    modifier onlyGovernance() {
        require(msg.sender == governance, "Caller is not governance");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the staking token contract.
     * @param _rewardToken Address of the reward token contract.
     * @param _rewardRate Reward rate per second (in token units).
     * @param _governance Address of the governance.
     */
    constructor(
        IERC20 _stakingToken,
        IERC20 _rewardToken,
        uint256 _rewardRate,
        address _governance
    ) {
        stakingToken = _stakingToken;
        rewardToken = _rewardToken;
        rewardRate = _rewardRate;
        governance = _governance;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");
        updateReward(msg.sender);

        // Transfer staking tokens from the user to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update state variables
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;
    }

    /**
     * @dev Claim rewards accumulated from staking.
     */
    function claimRewards() external {
        updateReward(msg.sender);

        // Retrieve pending rewards
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset user's reward balance
        rewards[msg.sender] = 0;

        // Transfer reward tokens from the contract to the user
        rewardToken.transfer(msg.sender, reward);
    }

    /**
     * @dev Unstake tokens and optionally claim rewards.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake zero tokens");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");
        updateReward(msg.sender);

        // Update state variables
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer staking tokens back to the user
        stakingToken.transfer(msg.sender, _amount);
    }

    /**
     * @dev Update the reward variables for a user.
     * @param _user Address of the user.
     */
    function updateReward(address _user) internal {
        uint256 timeDifference = block.timestamp - lastUpdateTime[_user];
        if (timeDifference > 0) {
            rewards[_user] += (stakedBalances[_user] * rewardRate * timeDifference) / 1e18;
            lastUpdateTime[_user] = block.timestamp;
        }
    }

    /**
     * @dev Update the reward rate. Restricted to governance.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyGovernance {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdrawal by governance to recover tokens. Restricted to governance.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(IERC20 _token, uint256 _amount) external onlyGovernance {
        _token.transfer(governance, _amount);
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function balanceOf(address account) external view returns (uint256);
}
```
