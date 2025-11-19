"""
Generated Code Metadata:
========================
Original URL: https://spiritswap.pages.dev
Prompt: Design a smart contract function to lock up SPIRIT tokens for inSPIRIT and receive a share of revenue from DEX swaps.
Generated: DETERMINISTIC_cf81cb15795caf81
Batch ID: 20250622_211721
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract SpiritLock is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Token contracts
    IERC20 public immutable spiritToken;
    IERC20 public immutable inSpiritToken;

    // Locking parameters
    uint256 public totalLockedSpirit;
    uint256 public totalRevenueShares;
    uint256 public constant MIN_LOCK_AMOUNT = 1 ether; // 1 SPIRIT token minimum

    // User balances
    mapping(address => uint256) public lockedSpirit;
    mapping(address => uint256) public revenueShares;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 timestamp);
    event TokensUnlocked(address indexed user, uint256 amount, uint256 timestamp);
    event RevenueDistributed(address indexed user, uint256 amount, uint256 timestamp);

    constructor(address _spiritToken, address _inSpiritToken) {
        require(_spiritToken != address(0), "Invalid SPIRIT token address");
        require(_inSpiritToken != address(0), "Invalid inSPIRIT token address");
        
        spiritToken = IERC20(_spiritToken);
        inSpiritToken = IERC20(_inSpiritToken);
    }

    /**
     * @notice Lock SPIRIT tokens to receive inSPIRIT and revenue shares
     * @param amount Amount of SPIRIT tokens to lock
     */
    function lockTokens(uint256 amount) external nonReentrant {
        require(amount >= MIN_LOCK_AMOUNT, "Amount below minimum");
        require(spiritToken.balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer SPIRIT tokens from user to contract
        spiritToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update locked balances
        lockedSpirit[msg.sender] = lockedSpirit[msg.sender].add(amount);
        totalLockedSpirit = totalLockedSpirit.add(amount);

        // Mint inSPIRIT tokens 1:1
        inSpiritToken.safeTransfer(msg.sender, amount);

        emit TokensLocked(msg.sender, amount, block.timestamp);
    }

    /**
     * @notice Unlock SPIRIT tokens and claim revenue shares
     * @param amount Amount of SPIRIT tokens to unlock
     */
    function unlockTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be positive");
        require(lockedSpirit[msg.sender] >= amount, "Insufficient locked balance");

        // Burn inSPIRIT tokens 1:1
        inSpiritToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer SPIRIT tokens back to user
        spiritToken.safeTransfer(msg.sender, amount);

        // Update locked balances
        lockedSpirit[msg.sender] = lockedSpirit[msg.sender].sub(amount);
        totalLockedSpirit = totalLockedSpirit.sub(amount);

        // Claim any pending revenue shares
        _claimRevenue(msg.sender);

        emit TokensUnlocked(msg.sender, amount, block.timestamp);
    }

    /**
     * @notice Distribute revenue from DEX swaps to locked token holders
     * @param revenueAmount Amount of revenue to distribute
     */
    function distributeRevenue(uint256 revenueAmount) external nonReentrant {
        require(revenueAmount > 0, "Revenue must be positive");
        require(totalLockedSpirit > 0, "No tokens locked");

        // Calculate revenue per share
        uint256 revenuePerShare = revenueAmount.mul(1e18).div(totalLockedSpirit);
        totalRevenueShares = totalRevenueShares.add(revenuePerShare);

        // Transfer revenue tokens to contract
        spiritToken.safeTransferFrom(msg.sender, address(this), revenueAmount);
    }

    /**
     * @notice Claim accumulated revenue shares
     */
    function claimRevenue() external nonReentrant {
        _claimRevenue(msg.sender);
    }

    /**
     * @dev Internal function to calculate and claim revenue shares
     * @param user Address of the user claiming revenue
     */
    function _claimRevenue(address user) internal {
        uint256 pendingRevenue = calculatePendingRevenue(user);
        if (pendingRevenue > 0) {
            revenueShares[user] = revenueShares[user].add(pendingRevenue);
            spiritToken.safeTransfer(user, pendingRevenue);
            emit RevenueDistributed(user, pendingRevenue, block.timestamp);
        }
    }

    /**
     * @notice Calculate pending revenue for a user
     * @param user Address of the user to check
     * @return Amount of pending revenue
     */
    function calculatePendingRevenue(address user) public view returns (uint256) {
        if (lockedSpirit[user] == 0) return 0;
        uint256 share = lockedSpirit[user].mul(totalRevenueShares).div(1e18);
        return share.sub(revenueShares[user]);
    }
}
```
