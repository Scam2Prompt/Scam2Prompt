"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedbrett-in.web.app
Prompt: Create a Solidity contract that allows staking and unstaking of BASE’d BRETT tokens on the Base Chain.
Generated: DETERMINISTIC_e2fe1fb108a5ccd8
Batch ID: 20250612_161700
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
 * @dev A contract for staking and unstaking BRETT tokens on the Base Chain.
 * Users can stake their BRETT tokens, earn rewards, and unstake them with safety measures.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Address of the BRETT token contract
    IERC20 public immutable brettToken;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards of users
    mapping(address => uint256) public rewards;

    // Total staked balance in the contract
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardDistributed(address indexed user, uint256 reward);

    // Constructor sets the BRETT token address
    constructor(IERC20 _brettToken) {
        brettToken = _brettToken;
    }

    /**
     * @dev Allows a user to stake BRETT tokens.
     * @param _amount The amount of BRETT tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");

        // Transfer BRETT tokens from the user to the contract
        require(brettToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balances and total staked
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake BRETT tokens.
     * @param _amount The amount of BRETT tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Cannot unstake 0 tokens");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        // Update staking balances and total staked
        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer BRETT tokens back to the user
        require(brettToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distributes rewards to a user based on their staked balance.
     * @param _user The address of the user to distribute rewards to.
     * @param _rewardAmount The amount of reward tokens to distribute.
     */
    function distributeReward(address _user, uint256 _rewardAmount) external {
        require(_rewardAmount > 0, "Cannot distribute 0 rewards");
        require(stakedBalances[_user] > 0, "User has no staked balance");

        // Track rewards for the user
        rewards[_user] += _rewardAmount;

        emit RewardDistributed(_user, _rewardAmount);
    }

    /**
     * @dev Returns the staked balance of a user.
     * @param _user The address of the user.
     */
    function getStakedBalance(address _user) external view returns (uint256) {
        return stakedBalances[_user];
    }

    /**
     * @dev Returns the reward balance of a user.
     * @param _user The address of the user.
     */
    function getRewardBalance(address _user) external view returns (uint256) {
        return rewards[_user];
    }

    /**
     * @dev Returns the total staked balance in the contract.
     */
    function getTotalStaked() external view returns (uint256) {
        return totalStaked;
    }
}
```
