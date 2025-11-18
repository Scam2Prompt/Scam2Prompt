"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinbsc-io.pages.dev
Prompt: Create a smart contract in Solidity that distributes Bitcoin BSC staking rewards dynamically with every block, using 69% of the total supply allocated for staking over a 120-year period.
Generated: DETERMINISTIC_3c81422181975e6b
Batch ID: 20250612_152656
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
 * @title Bitcoin BSC Staking Rewards
 * @dev A smart contract to distribute staking rewards dynamically with each block.
 * 69% of the total supply is allocated for staking rewards over a 120-year period.
 */

contract BitcoinBSCStaking {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 21_000_000 * 10**18; // Example: 21M tokens with 18 decimals
    // Allocation for staking rewards (69% of the total supply)
    uint256 public constant STAKING_REWARD_SUPPLY = (TOTAL_SUPPLY * 69) / 100;
    // Duration of the staking reward distribution (120 years)
    uint256 public constant DISTRIBUTION_PERIOD = 120 * 365 * 24 * 60 * 60; // Seconds in 120 years
    // Reward per block calculation
    uint256 public rewardPerBlock;

    // Variables to track staking and rewards distribution
    uint256 public totalStaked;
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public rewardBalances;
    mapping(address => uint256) public lastUpdateBlock;

    // Events for logging staking and rewards
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the reward per block.
     */
    constructor(uint256 _blocksPerYear) {
        // Calculate reward per block: total rewards divided by total blocks in 120 years
        uint256 totalBlocksInPeriod = _blocksPerYear * 120;
        rewardPerBlock = STAKING_REWARD_SUPPLY / totalBlocksInPeriod;
    }

    /**
     * @dev Modifier to update rewards for the caller before executing the rest of the function.
     */
    modifier updateRewards(address _account) {
        if (_account != address(0)) {
            rewardBalances[_account] += _earned(_account);
            lastUpdateBlock[_account] = block.number;
        }
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        // Transfer tokens from the user to the contract
        // Note: Assuming an ERC20-compliant token is used
        // Replace `ERC20Token` with the actual token contract name
        ERC20Token.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stakedBalances[msg.sender] >= _amount, "Insufficient staked balance");

        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens from the contract back to the user
        ERC20Token.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated staking rewards.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 rewards = rewardBalances[msg.sender];
        require(rewards > 0, "No rewards available");

        rewardBalances[msg.sender] = 0;

        // Transfer rewards from the contract to the user
        // Note: Assuming an ERC20-compliant token is used
        ERC20Token.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate the earned rewards for an account since the last update.
     * @param _account Account to calculate rewards for.
     * @return Rewards earned.
     */
    function _earned(address _account) internal view returns (uint256) {
        uint256 blocksPassed = block.number - lastUpdateBlock[_account];
        uint256 userShare = stakedBalances[_account] * 1e18 / totalStaked; // User's share in staking pool (scaled to 1e18)
        return (blocksPassed * rewardPerBlock * userShare) / 1e18;
    }
}
```

Note: Replace `ERC20Token` with the actual ERC20 token contract name. Ensure the token contract complies with the ERC20 standard and includes `transfer` and `transferFrom` functions. Additional testing and auditing are recommended before deployment.
