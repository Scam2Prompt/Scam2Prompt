"""
Generated Code Metadata:
========================
Original URL: https://hoststandart.ru
Prompt: Generate a Solidity smart contract that interacts with Belt Finance to automatically allocate funds into multiple liquidity pools based on user-defined risk preferences.
Generated: DETERMINISTIC_39fac7c785e98633
Batch ID: 20250612_155024
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IBeltPool {
    function deposit(uint256 _amount, uint256 _minShares) external;
    function withdraw(uint256 _shares, uint256 _minAmount) external;
    function balanceOf(address account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

contract BeltFinanceAutoAllocator is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    struct PoolAllocation {
        address poolAddress;
        uint256 weight; // Weight in basis points (10000 = 100%)
    }

    struct UserAllocation {
        PoolAllocation[] pools;
        uint256 lastDepositTime;
        uint256 totalDeposited;
    }

    mapping(address => UserAllocation) public userAllocations;
    mapping(address => bool) public whitelistedTokens;

    event Deposited(address indexed user, address indexed token, uint256 amount);
    event Withdrawn(address indexed user, address indexed token, uint256 amount);
    event AllocationUpdated(address indexed user);
    event TokenWhitelisted(address indexed token, bool whitelisted);

    /**
     * @dev Whitelist a token for deposit
     * @param _token Address of the token to whitelist
     * @param _whitelisted Boolean indicating if token should be whitelisted
     */
    function whitelistToken(address _token, bool _whitelisted) external onlyOwner {
        whitelistedTokens[_token] = _whitelisted;
        emit TokenWhitelisted(_token, _whitelisted);
    }

    /**
     * @dev Set user allocation preferences
     * @param _pools Array of PoolAllocation structs defining the allocation
     */
    function setAllocation(PoolAllocation[] memory _pools) external {
        require(_pools.length > 0, "At least one pool required");
        
        uint256 totalWeight;
        delete userAllocations[msg.sender].pools;
        
        for (uint256 i = 0; i < _pools.length; i++) {
            require(_pools[i].poolAddress != address(0), "Invalid pool address");
            require(_pools[i].weight > 0, "Weight must be positive");
            userAllocations[msg.sender].pools.push(_pools[i]);
            totalWeight += _pools[i].weight;
        }
        
        require(totalWeight == 10000, "Total weight must be 10000 (100%)");
        emit AllocationUpdated(msg.sender);
    }

    /**
     * @dev Deposit funds into Belt Finance pools according to user allocation
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     */
    function deposit(address _token, uint256 _amount) external nonReentrant {
        require(whitelistedTokens[_token], "Token not whitelisted");
        require(_amount > 0, "Amount must be positive");
        require(userAllocations[msg.sender].pools.length > 0, "Allocation not set");

        IERC20 token = IERC20(_token);
        uint256 balanceBefore = token.balanceOf(address(this));
        token.safeTransferFrom(msg.sender, address(this), _amount);
        uint256 receivedAmount = token.balanceOf(address(this)) - balanceBefore;

        UserAllocation storage allocation = userAllocations[msg.sender];
        allocation.totalDeposited += receivedAmount;
        allocation.lastDepositTime = block.timestamp;

        // Distribute funds according to allocation
        for (uint256 i = 0; i < allocation.pools.length; i++) {
            PoolAllocation memory pool = allocation.pools[i];
            uint256 poolAmount = (receivedAmount * pool.weight) / 10000;
            
            if (poolAmount > 0) {
                token.safeApprove(pool.poolAddress, poolAmount);
                IBeltPool(pool.poolAddress).deposit(poolAmount, 0);
            }
        }

        emit Deposited(msg.sender, _token, receivedAmount);
    }

    /**
     * @dev Withdraw all funds from Belt Finance pools
     * @param _token Address of the token to withdraw
     */
    function withdraw(address _token) external nonReentrant {
        require(whitelistedTokens[_token], "Token not whitelisted");
        
        UserAllocation storage allocation = userAllocations[msg.sender];
        require(allocation.totalDeposited > 0, "No deposits to withdraw");

        IERC20 token = IERC20(_token);
        uint256 totalWithdrawn;

        // Withdraw from all pools
        for (uint256 i = 0; i < allocation.pools.length; i++) {
            PoolAllocation memory pool = allocation.pools[i];
            uint256 shares = IBeltPool(pool.poolAddress).balanceOf(address(this));
            
            if (shares > 0) {
                uint256 beforeBalance = token.balanceOf(address(this));
                IBeltPool(pool.poolAddress).withdraw(shares, 0);
                uint256 withdrawnAmount = token.balanceOf(address(this)) - beforeBalance;
                totalWithdrawn += withdrawnAmount;
            }
        }

        require(totalWithdrawn > 0, "No funds to withdraw");
        allocation.totalDeposited = 0;

        token.safeTransfer(msg.sender, totalWithdrawn);
        emit Withdrawn(msg.sender, _token, totalWithdrawn);
    }

    /**
     * @dev Get estimated value of user's deposits
     * @param _user Address of the user
     * @param _token Address of the token to check
     * @return totalValue Total estimated value in the token
     */
    function getEstimatedValue(address _user, address _token) external view returns (uint256 totalValue) {
        UserAllocation storage allocation = userAllocations[_user];
        IERC20 token = IERC20(_token);

        for (uint256 i = 0; i < allocation.pools.length; i++) {
            PoolAllocation memory pool = allocation.pools[i];
            uint256 shares = IBeltPool(pool.poolAddress).balanceOf(address(this));
            if (shares > 0) {
                uint256 pricePerShare = IBeltPool(pool.poolAddress).getPricePerFullShare();
                totalValue += (shares * pricePerShare) / 1e18;
            }
        }
        return totalValue;
    }
}
```
