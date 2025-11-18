"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lmeow-sushi.top
Prompt: Create a Solidity smart contract that integrates with SushiSwap’s staking pools to automate the staking and unstaking process for LMEOW tokens.
Generated: DETERMINISTIC_ca5abf773c9d69f7
Batch ID: 20250612_153916
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

// Importing OpenZeppelin's SafeERC20 for secure token transfers
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for SushiSwap's MasterChef contract (or similar staking pool contract)
interface ISushiSwapPool {
    function deposit(uint256 _pid, uint256 _amount) external;
    function withdraw(uint256 _pid, uint256 _amount) external;
    function pendingSushi(uint256 _pid, address _user) external view returns (uint256);
}

// Automated staking and unstaking contract for LMEOW tokens
contract LMEOWStakingAutomation is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Address of the LMEOW token
    IERC20 public immutable lmeowToken;

    // Address of the SushiSwap staking pool (MasterChef or equivalent)
    ISushiSwapPool public immutable sushiSwapPool;

    // Pool ID for the SushiSwap staking pool
    uint256 public immutable poolId;

    // Events for logging staking and unstaking actions
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _lmeowToken Address of the LMEOW token contract.
     * @param _sushiSwapPool Address of the SushiSwap staking pool contract.
     * @param _poolId Pool ID in the SushiSwap staking pool.
     */
    constructor(
        address _lmeowToken,
        address _sushiSwapPool,
        uint256 _poolId
    ) {
        require(_lmeowToken != address(0), "Invalid LMEOW token address");
        require(_sushiSwapPool != address(0), "Invalid SushiSwap pool address");

        lmeowToken = IERC20(_lmeowToken);
        sushiSwapPool = ISushiSwapPool(_sushiSwapPool);
        poolId = _poolId;
    }

    /**
     * @dev Stake LMEOW tokens into the SushiSwap pool.
     * @param _amount Amount of tokens to stake.
     */
    function stakeTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Transfer LMEOW tokens from the user to this contract
        lmeowToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Approve SushiSwap pool contract to spend LMEOW tokens
        lmeowToken.safeApprove(address(sushiSwapPool), _amount);

        // Deposit tokens into the staking pool
        sushiSwapPool.deposit(poolId, _amount);

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Unstake LMEOW tokens from the SushiSwap pool.
     * @param _amount Amount of tokens to unstake.
     */
    function unstakeTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than zero");

        // Withdraw tokens from the staking pool
        sushiSwapPool.withdraw(poolId, _amount);

        // Transfer LMEOW tokens back to the user
        lmeowToken.safeTransfer(msg.sender, _amount);

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending SUSHI rewards from the SushiSwap pool.
     */
    function claimRewards() external nonReentrant {
        // Check pending rewards from the staking pool
        uint256 pendingRewards = sushiSwapPool.pendingSushi(poolId, msg.sender);
        require(pendingRewards > 0, "No rewards available");

        // Withdraw rewards (typically involves calling `deposit` with _amount=0)
        sushiSwapPool.deposit(poolId, 0);

        // Emit event for claiming rewards
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Emergency withdrawal function to recover all staked tokens.
     * @notice Can only be called by the contract owner.
     */
    function emergencyWithdraw() external onlyOwner nonReentrant {
        sushiSwapPool.withdraw(poolId, type(uint256).max);
        uint256 contractBalance = lmeowToken.balanceOf(address(this));

        // Transfer all recovered tokens to the owner
        lmeowToken.safeTransfer(owner(), contractBalance);
    }
}
```
