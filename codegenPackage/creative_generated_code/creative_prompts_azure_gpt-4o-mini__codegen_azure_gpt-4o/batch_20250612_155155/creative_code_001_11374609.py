"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sushiswapf.imweb.me
Prompt: Generate a Solidity contract that allows users to stake tokens in SushiSwap liquidity pools and earn SUSHI tokens as rewards.
Generated: DETERMINISTIC_11374609968dbb83
Batch ID: 20250612_155155
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

// Import interfaces for SushiSwap staking and ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface ISushiSwapMasterChef {
    function deposit(uint256 _pid, uint256 _amount) external;
    function withdraw(uint256 _pid, uint256 _amount) external;
    function pendingSushi(uint256 _pid, address _user) external view returns (uint256);
}

contract SushiSwapStaker is ReentrancyGuard {
    // Address of the SushiSwap MasterChef contract
    ISushiSwapMasterChef public immutable masterChef;

    // Liquidity pool ID in the MasterChef contract
    uint256 public immutable poolId;

    // ERC20 token of the liquidity pool
    IERC20 public immutable lpToken;

    // ERC20 token for SUSHI rewards
    IERC20 public immutable sushiToken;

    // Mapping to track user stakes
    mapping(address => uint256) public userStake;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ClaimedRewards(address indexed user, uint256 amount);

    /**
     * @dev Constructor initializes the contract with required addresses.
     * @param _masterChef Address of SushiSwap MasterChef contract.
     * @param _poolId Pool ID in the MasterChef contract associated with LP tokens.
     * @param _lpToken Address of the LP token for staking.
     * @param _sushiToken Address of the SUSHI token for rewards.
     */
    constructor(
        address _masterChef,
        uint256 _poolId,
        address _lpToken,
        address _sushiToken
    ) {
        require(_masterChef != address(0), "Invalid MasterChef address");
        require(_lpToken != address(0), "Invalid LP token address");
        require(_sushiToken != address(0), "Invalid SUSHI token address");
        
        masterChef = ISushiSwapMasterChef(_masterChef);
        poolId = _poolId;
        lpToken = IERC20(_lpToken);
        sushiToken = IERC20(_sushiToken);
    }

    /**
     * @dev Stake LP tokens in the SushiSwap pool.
     * @param amount Amount of LP tokens to stake.
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer LP tokens from user to this contract
        lpToken.transferFrom(msg.sender, address(this), amount);

        // Approve MasterChef contract to spend LP tokens
        lpToken.approve(address(masterChef), amount);

        // Deposit LP tokens into MasterChef
        masterChef.deposit(poolId, amount);

        // Update user stake
        userStake[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake LP tokens from the SushiSwap pool.
     * @param amount Amount of LP tokens to unstake.
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(userStake[msg.sender] >= amount, "Insufficient staked balance");

        // Withdraw LP tokens from MasterChef
        masterChef.withdraw(poolId, amount);

        // Transfer LP tokens back to the user
        lpToken.transfer(msg.sender, amount);

        // Update user stake
        userStake[msg.sender] -= amount;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim pending SUSHI rewards.
     */
    function claimRewards() external nonReentrant {
        // Get pending SUSHI rewards from MasterChef
        uint256 pending = masterChef.pendingSushi(poolId, address(this));
        require(pending > 0, "No rewards available");

        // Withdraw 0 to trigger SUSHI rewards distribution
        masterChef.deposit(poolId, 0);

        // Transfer SUSHI tokens to the user
        sushiToken.transfer(msg.sender, pending);

        emit ClaimedRewards(msg.sender, pending);
    }

    /**
     * @dev View pending SUSHI rewards for the user.
     * @return Pending SUSHI rewards.
     */
    function viewPendingRewards() external view returns (uint256) {
        return masterChef.pendingSushi(poolId, address(this));
    }
}
```
