"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-hotfix-zksync-bridge-limits-venus-protocol.vercel.app
Prompt: How can I integrate the Venus Protocol into a DeFi application, and what are the benefits of using its algorithmic money market features?
Generated: DETERMINISTIC_7594af8285aa1126
Batch ID: 20250622_205230
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

// Import Venus Protocol interfaces
import {IVToken} from "./interfaces/IVToken.sol";
import {IComptroller} from "./interfaces/IComptroller.sol";
import {IPriceOracle} from "./interfaces/IPriceOracle.sol";

contract VenusIntegration {
    IComptroller public comptroller;
    IPriceOracle public priceOracle;

    // Initialize with Venus Comptroller address
    constructor(address _comptroller, address _priceOracle) {
        comptroller = IComptroller(_comptroller);
        priceOracle = IPriceOracle(_priceOracle);
    }

    /**
     * @notice Enter Venus markets to enable borrowing
     * @param vTokens Array of vToken addresses to enter
     */
    function enterMarkets(address[] calldata vTokens) external returns (uint[] memory) {
        return comptroller.enterMarkets(vTokens);
    }

    /**
     * @notice Supply assets to Venus Protocol
     * @param vToken Address of the vToken contract
     * @param amount Amount of underlying to supply
     */
    function supply(address vToken, uint amount) external {
        IVToken(vToken).mint(amount);
    }

    /**
     * @notice Borrow assets from Venus Protocol
     * @param vToken Address of the vToken to borrow
     * @param amount Amount to borrow
     */
    function borrow(address vToken, uint amount) external {
        IVToken(vToken).borrow(amount);
    }

    /**
     * @notice Repay borrowed assets
     * @param vToken Address of the vToken to repay
     * @param amount Amount to repay
     */
    function repayBorrow(address vToken, uint amount) external {
        IVToken(vToken).repayBorrow(amount);
    }

    /**
     * @notice Redeem supplied assets
     * @param vToken Address of the vToken to redeem
     * @param amount Amount of vTokens to redeem
     */
    function redeem(address vToken, uint amount) external {
        IVToken(vToken).redeem(amount);
    }

    /**
     * @notice Get account liquidity in USD
     * @param account User address
     * @return (error code, liquidity, shortfall)
     */
    function getAccountLiquidity(address account) external view returns (uint, uint, uint) {
        return comptroller.getAccountLiquidity(account);
    }

    /**
     * @notice Get the underlying asset price from Venus Oracle
     * @param vToken vToken address
     * @return Price in USD (scaled by 1e18)
     */
    function getUnderlyingPrice(address vToken) external view returns (uint) {
        return priceOracle.getUnderlyingPrice(vToken);
    }

    /**
     * @notice Check if a market is listed in Venus
     * @param vToken vToken address to check
     * @return Whether the market is listed
     */
    function isMarketListed(address vToken) external view returns (bool) {
        return comptroller.markets(vToken).isListed;
    }
}

// File: interfaces/IVToken.sol
interface IVToken {
    function mint(uint mintAmount) external returns (uint);
    function redeem(uint redeemTokens) external returns (uint);
    function borrow(uint borrowAmount) external returns (uint);
    function repayBorrow(uint repayAmount) external returns (uint);
    function balanceOf(address owner) external view returns (uint);
    function borrowBalanceCurrent(address account) external returns (uint);
    function exchangeRateCurrent() external returns (uint);
}

// File: interfaces/IComptroller.sol
interface IComptroller {
    function enterMarkets(address[] calldata vTokens) external returns (uint[] memory);
    function exitMarket(address vToken) external returns (uint);
    function getAccountLiquidity(address account) external view returns (uint, uint, uint);
    function markets(address vToken) external view returns (bool isListed, uint collateralFactorMantissa);
}

// File: interfaces/IPriceOracle.sol
interface IPriceOracle {
    function getUnderlyingPrice(address vToken) external view returns (uint);
}
```
