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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title InSPIRIT Smart Contract
 * @author [Your Name]
 * @notice This contract allows users to lock up SPIRIT tokens to receive a share of revenue from DEX swaps.
 */
contract InSPIRIT {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user locked token balances
    mapping (address => uint256) public lockedBalances;

    // Mapping of user revenue shares
    mapping (address => uint256) public revenueShares;

    // Total locked token balance
    uint256 public totalLockedBalance;

    // Total revenue share
    uint256 public totalRevenueShare;

    // SPIRIT token contract
    IERC20 public spiritToken;

    // DEX swap revenue address
    address public revenueAddress;

    /**
     * @notice Constructor
     * @param _spiritToken SPIRIT token contract address
     * @param _revenueAddress DEX swap revenue address
     */
    constructor(address _spiritToken, address _revenueAddress) public {
        spiritToken = IERC20(_spiritToken);
        revenueAddress = _revenueAddress;
    }

    /**
     * @notice Lock up SPIRIT tokens to receive a share of revenue from DEX swaps
     * @param _amount Amount of SPIRIT tokens to lock up
     */
    function lockUpTokens(uint256 _amount) public {
        require(_amount > 0, "Invalid amount");
        require(spiritToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Transfer tokens to contract
        spiritToken.safeTransferFrom(msg.sender, address(this), _amount);

        // Update locked balance and revenue share
        lockedBalances[msg.sender] = lockedBalances[msg.sender].add(_amount);
        totalLockedBalance = totalLockedBalance.add(_amount);
        revenueShares[msg.sender] = revenueShares[msg.sender].add(_amount);
        totalRevenueShare = totalRevenueShare.add(_amount);
    }

    /**
     * @notice Unlock SPIRIT tokens
     */
    function unlockTokens() public {
        require(lockedBalances[msg.sender] > 0, "No locked balance");

        // Calculate revenue share
        uint256 revenueShare = lockedBalances[msg.sender].mul(totalRevenueShare).div(totalLockedBalance);

        // Transfer revenue share to user
        spiritToken.safeTransfer(msg.sender, revenueShare);

        // Reset locked balance and revenue share
        lockedBalances[msg.sender] = 0;
        revenueShares[msg.sender] = 0;
    }

    /**
     * @notice Add DEX swap revenue
     * @param _amount Amount of revenue to add
     */
    function addRevenue(uint256 _amount) public {
        require(msg.sender == revenueAddress, "Unauthorized");
        require(_amount > 0, "Invalid amount");

        // Transfer revenue to contract
        spiritToken.safeTransferFrom(revenueAddress, address(this), _amount);

        // Distribute revenue to users
        distributeRevenue(_amount);
    }

    /**
     * @notice Distribute revenue to users
     * @param _amount Amount of revenue to distribute
     */
    function distributeRevenue(uint256 _amount) internal {
        // Calculate distribution ratio
        uint256 distributionRatio = _amount.mul(100).div(totalRevenueShare);

        // Distribute revenue to users
        for (address user in revenueShares) {
            uint256 userRevenue = revenueShares[user].mul(distributionRatio).div(100);
            spiritToken.safeTransfer(user, userRevenue);
        }
    }
}
```
