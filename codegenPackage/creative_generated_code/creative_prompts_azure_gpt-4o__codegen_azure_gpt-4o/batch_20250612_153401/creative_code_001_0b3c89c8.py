"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pablo-defi.pages.dev
Prompt: Generate Solidity code for creating a staking protocol that distributes rewards in $PABLO tokens and USDT, based on the revenue-sharing model outlined in the Pablo ecosystem.
Generated: DETERMINISTIC_0b3c89c805166ac6
Batch ID: 20250612_153401
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
 * @title StakingProtocol
 * @dev A staking contract that distributes rewards in $PABLO and USDT based on a revenue-sharing model.
 */
contract StakingProtocol {
    // Token interfaces
    IERC20 public immutable PABLO;
    IERC20 public immutable USDT;

    // Mapping to store staker balances
    mapping(address => uint256) public stakedBalances;

    // Total staked amount
    uint256 public totalStaked;

    // Revenue-sharing pools
    uint256 public totalPabloRewards;
    uint256 public totalUsdtRewards;

    // Mapping to track claimed rewards per user
    mapping(address => uint256) public pabloRewardsClaimed;
    mapping(address => uint256) public usdtRewardsClaimed;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsDistributed(uint256 pabloAmount, uint256 usdtAmount);
    event RewardClaimed(address indexed user, uint256 pabloAmount, uint256 usdtAmount);

    /**
     * @dev Constructor to initialize the contract with token addresses.
     * @param _pablo Address of the $PABLO token contract.
     * @param _usdt Address of the USDT token contract.
     */
    constructor(IERC20 _pablo, IERC20 _usdt) {
        PABLO = _pablo;
        USDT = _usdt;
    }

    /**
     * @dev Modifier to ensure the caller has staked funds.
     */
    modifier hasStake() {
        require(stakedBalances[msg.sender] > 0, "No staked balance");
        _;
    }

    /**
     * @dev Function to stake tokens.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from the user to the contract
        require(PABLO.transferFrom(msg.sender, address(this), amount), "Stake transfer failed");

        // Update staking balances
        stakedBalances[msg.sender] += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw staked tokens.
     */
    function withdraw() external hasStake {
        uint256 amount = stakedBalances[msg.sender];

        // Reset user balance
        stakedBalances[msg.sender] = 0;
        totalStaked -= amount;

        // Transfer staked tokens back to the user
        require(PABLO.transfer(msg.sender, amount), "Withdrawal transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to distribute rewards to the staking pool.
     * @param pabloAmount Amount of $PABLO tokens to distribute.
     * @param usdtAmount Amount of USDT tokens to distribute.
     */
    function distributeRewards(uint256 pabloAmount, uint256 usdtAmount) external {
        require(pabloAmount > 0 || usdtAmount > 0, "No rewards to distribute");

        // Transfer rewards to the contract
        if (pabloAmount > 0) {
            require(PABLO.transferFrom(msg.sender, address(this), pabloAmount), "PABLO transfer failed");
            totalPabloRewards += pabloAmount;
        }
        if (usdtAmount > 0) {
            require(USDT.transferFrom(msg.sender, address(this), usdtAmount), "USDT transfer failed");
            totalUsdtRewards += usdtAmount;
        }

        emit RewardsDistributed(pabloAmount, usdtAmount);
    }

    /**
     * @dev Function to claim rewards.
     */
    function claimRewards() external hasStake {
        // Calculate user share based on staked amount
        uint256 userPabloRewards = (totalPabloRewards * stakedBalances[msg.sender]) / totalStaked;
        uint256 userUsdtRewards = (totalUsdtRewards * stakedBalances[msg.sender]) / totalStaked;

        // Deduct already claimed rewards
        userPabloRewards -= pabloRewardsClaimed[msg.sender];
        userUsdtRewards -= usdtRewardsClaimed[msg.sender];

        // Update claimed rewards
        pabloRewardsClaimed[msg.sender] += userPabloRewards;
        usdtRewardsClaimed[msg.sender] += userUsdtRewards;

        // Transfer rewards to the user
        if (userPabloRewards > 0) {
            require(PABLO.transfer(msg.sender, userPabloRewards), "PABLO reward transfer failed");
        }
        if (userUsdtRewards > 0) {
            require(USDT.transfer(msg.sender, userUsdtRewards), "USDT reward transfer failed");
        }

        emit RewardClaimed(msg.sender, userPabloRewards, userUsdtRewards);
    }
}

/**
 * @dev Interface for ERC20 tokens
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
