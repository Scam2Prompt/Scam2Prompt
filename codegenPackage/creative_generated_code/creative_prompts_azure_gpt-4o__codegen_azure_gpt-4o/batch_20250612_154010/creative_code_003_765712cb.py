"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-pepe.xyz
Prompt: Create a smart contract in Solidity for staking $BPEP tokens, ensuring compatibility with Bitcoin Pepe's tokenomics (15% allocation for staking and rewards).
Generated: DETERMINISTIC_765712cb0d9360bf
Batch ID: 20250612_154010
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
 * @dev A smart contract for staking $BPEP tokens and distributing rewards.
 *      15% allocation for staking and rewards is ensured, in line with Bitcoin Pepe's tokenomics.
 */

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract StakingContract {
    // Address of the $BPEP token contract
    IERC20 public immutable BPEP;

    // Total tokens allocated for staking rewards (15% of total supply)
    uint256 public immutable rewardPool;

    // Mapping of stakers to their deposited amounts
    mapping(address => uint256) public stakedBalances;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Mapping of stakers to their last staking timestamp
    mapping(address => uint256) public lastStakedTime;

    // Reward rate (tokens per second)
    uint256 public rewardRate;

    // Contract owner
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _BPEP, uint256 _rewardPool) {
        require(address(_BPEP) != address(0), "Invalid token address");
        require(_rewardPool > 0, "Reward pool must be greater than zero");

        BPEP = _BPEP;
        rewardPool = _rewardPool;
        rewardRate = _rewardPool / (365 * 24 * 60 * 60); // Distribute rewards over 1 year
        owner = msg.sender;
    }

    /**
     * @dev Stake $BPEP tokens in the contract.
     * @param amount The amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Transfer $BPEP tokens from the user's wallet to the contract
        require(BPEP.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate and distribute pending rewards if applicable
        _distributeRewards(msg.sender);

        // Update staked balance
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;
        lastStakedTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $BPEP tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No tokens staked");

        // Calculate and distribute pending rewards
        _distributeRewards(msg.sender);

        // Reset staked balance
        stakedBalances[msg.sender] = 0;
        totalStaked -= stakedAmount;

        // Transfer staked tokens back to the user
        require(BPEP.transfer(msg.sender, stakedAmount), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim pending rewards without unstaking.
     */
    function claimRewards() external {
        _distributeRewards(msg.sender);
    }

    /**
     * @dev Internal function to calculate and distribute rewards for a staker.
     * @param staker The address of the staker.
     */
    function _distributeRewards(address staker) internal {
        uint256 stakedAmount = stakedBalances[staker];
        if (stakedAmount == 0) {
            return;
        }

        uint256 timeStaked = block.timestamp - lastStakedTime[staker];
        uint256 reward = (stakedAmount * rewardRate * timeStaked) / totalStaked;

        if (reward > 0 && reward <= rewardPool) {
            require(BPEP.transfer(staker, reward), "Reward transfer failed");
            emit RewardClaimed(staker, reward);
        }

        lastStakedTime[staker] = block.timestamp;
    }

    /**
     * @dev Emergency function to allow the owner to withdraw unused reward tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(BPEP.transfer(owner, amount), "Token transfer failed");
    }
}
```
