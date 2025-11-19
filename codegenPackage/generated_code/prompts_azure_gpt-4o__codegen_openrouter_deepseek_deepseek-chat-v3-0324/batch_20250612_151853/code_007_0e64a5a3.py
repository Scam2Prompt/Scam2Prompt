"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-feat-optimism-subgraph-venus-protocol.vercel.app
Prompt: Write a Solidity smart contract that interacts with the Venus Protocol to deposit assets and track interest accrual.
Generated: DETERMINISTIC_0e64a5a396388ef3
Batch ID: 20250612_151853
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
import "./IVToken.sol";
import "./IVenusComptroller.sol";

contract VenusYieldTracker {
    using SafeERC20 for IERC20;

    // Venus Comptroller address
    IVenusComptroller public immutable comptroller;
    
    // Mapping to track user deposits (user => underlying => amount)
    mapping(address => mapping(address => uint256)) public userDeposits;
    
    // Mapping to track vToken addresses (underlying => vToken)
    mapping(address => address) public vTokens;

    event Deposit(address indexed user, address indexed underlying, uint256 amount);
    event Withdraw(address indexed user, address indexed underlying, uint256 amount);
    event InterestAccrued(address indexed user, address indexed underlying, uint256 interest);

    constructor(address _comptroller) {
        require(_comptroller != address(0), "Invalid comptroller address");
        comptroller = IVenusComptroller(_comptroller);
    }

    /**
     * @dev Set vToken address for an underlying asset
     * @param underlying Address of the underlying asset
     * @param vToken Address of the corresponding vToken
     */
    function setVToken(address underlying, address vToken) external {
        require(underlying != address(0), "Invalid underlying address");
        require(vToken != address(0), "Invalid vToken address");
        vTokens[underlying] = vToken;
    }

    /**
     * @dev Deposit underlying asset into Venus Protocol
     * @param underlying Address of the underlying asset to deposit
     * @param amount Amount to deposit
     */
    function deposit(address underlying, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        address vToken = vTokens[underlying];
        require(vToken != address(0), "vToken not set for this asset");

        // Transfer underlying tokens from user to this contract
        IERC20(underlying).safeTransferFrom(msg.sender, address(this), amount);

        // Approve vToken to spend underlying
        IERC20(underlying).approve(vToken, amount);

        // Mint vTokens
        uint256 result = IVToken(vToken).mint(amount);
        require(result == 0, "Mint failed");

        // Update user deposits
        userDeposits[msg.sender][underlying] += amount;

        emit Deposit(msg.sender, underlying, amount);
    }

    /**
     * @dev Withdraw underlying asset from Venus Protocol
     * @param underlying Address of the underlying asset to withdraw
     * @param amount Amount to withdraw
     */
    function withdraw(address underlying, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        address vToken = vTokens[underlying];
        require(vToken != address(0), "vToken not set for this asset");
        require(userDeposits[msg.sender][underlying] >= amount, "Insufficient balance");

        // Redeem underlying from vToken
        uint256 result = IVToken(vToken).redeemUnderlying(amount);
        require(result == 0, "Redeem failed");

        // Transfer underlying tokens to user
        IERC20(underlying).safeTransfer(msg.sender, amount);

        // Update user deposits
        userDeposits[msg.sender][underlying] -= amount;

        emit Withdraw(msg.sender, underlying, amount);
    }

    /**
     * @dev Calculate accrued interest for a user's deposit
     * @param user Address of the user
     * @param underlying Address of the underlying asset
     * @return interest Amount of interest accrued
     */
    function calculateInterest(address user, address underlying) public view returns (uint256 interest) {
        address vToken = vTokens[underlying];
        require(vToken != address(0), "vToken not set for this asset");
        
        uint256 initialDeposit = userDeposits[user][underlying];
        if (initialDeposit == 0) return 0;

        // Get current vToken balance
        uint256 currentVTokenBalance = IVToken(vToken).balanceOf(address(this));
        
        // Calculate exchange rate
        uint256 exchangeRate = IVToken(vToken).exchangeRateCurrent();
        
        // Calculate current underlying value
        uint256 currentUnderlyingValue = (currentVTokenBalance * exchangeRate) / 1e18;
        
        // Calculate interest
        if (currentUnderlyingValue > initialDeposit) {
            interest = currentUnderlyingValue - initialDeposit;
        } else {
            interest = 0;
        }
    }

    /**
     * @dev Claim accrued interest for a user's deposit
     * @param underlying Address of the underlying asset
     */
    function claimInterest(address underlying) external {
        uint256 interest = calculateInterest(msg.sender, underlying);
        require(interest > 0, "No interest to claim");

        address vToken = vTokens[underlying];
        require(vToken != address(0), "vToken not set for this asset");

        // Redeem interest
        uint256 result = IVToken(vToken).redeemUnderlying(interest);
        require(result == 0, "Redeem failed");

        // Transfer interest to user
        IERC20(underlying).safeTransfer(msg.sender, interest);

        emit InterestAccrued(msg.sender, underlying, interest);
    }

    /**
     * @dev Emergency function to withdraw all funds from a vToken
     * @param vToken Address of the vToken
     */
    function emergencyWithdraw(address vToken) external {
        require(vToken != address(0), "Invalid vToken address");
        
        // Redeem all vTokens
        uint256 vTokenBalance = IVToken(vToken).balanceOf(address(this));
        uint256 result = IVToken(vToken).redeem(vTokenBalance);
        require(result == 0, "Redeem failed");
        
        // Transfer underlying to owner (this contract)
        address underlying = IVToken(vToken).underlying();
        uint256 underlyingBalance = IERC20(underlying).balanceOf(address(this));
        IERC20(underlying).safeTransfer(msg.sender, underlyingBalance);
    }
}

interface IVToken {
    function mint(uint256 mintAmount) external returns (uint256);
    function redeem(uint256 redeemTokens) external returns (uint256);
    function redeemUnderlying(uint256 redeemAmount) external returns (uint256);
    function balanceOf(address owner) external view returns (uint256);
    function exchangeRateCurrent() external view returns (uint256);
    function underlying() external view returns (address);
}

interface IVenusComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint256[] memory);
    function exitMarket(address vToken) external returns (uint256);
}
```
