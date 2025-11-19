"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Create a simple trading strategy using Synthetix Perps and Polynomial's smart wallet, allowing users to access up to 50x leverage on various markets.
Generated: DETERMINISTIC_8b32320a9e185d95
Batch ID: 20250622_205111
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

/**
 * @title LeverageTradingStrategy
 * @dev A simple trading strategy using Synthetix Perps and Polynomial's smart wallet.
 * Allows users to access up to 50x leverage on various markets.
 */
interface ISynthetixPerps {
    function openPosition(
        bytes32 marketKey,
        int256 sizeDelta,
        uint256 leverage
    ) external returns (bool);

    function closePosition(bytes32 marketKey) external returns (bool);
}

interface IPolynomialSmartWallet {
    function deposit() external payable;

    function withdraw(uint256 amount) external;

    function getBalance() external view returns (uint256);
}

contract LeverageTradingStrategy {
    ISynthetixPerps public synthetixPerps;
    IPolynomialSmartWallet public polynomialWallet;

    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    event PositionOpened(bytes32 indexed marketKey, int256 sizeDelta, uint256 leverage);
    event PositionClosed(bytes32 indexed marketKey);
    event FundsDeposited(uint256 amount);
    event FundsWithdrawn(uint256 amount);

    /**
     * @dev Constructor to initialize the contract with Synthetix Perps and Polynomial Wallet addresses.
     * @param _synthetixPerps Address of the Synthetix Perps contract.
     * @param _polynomialWallet Address of the Polynomial Smart Wallet contract.
     */
    constructor(address _synthetixPerps, address _polynomialWallet) {
        require(_synthetixPerps != address(0), "Invalid Synthetix Perps address");
        require(_polynomialWallet != address(0), "Invalid Polynomial Wallet address");

        synthetixPerps = ISynthetixPerps(_synthetixPerps);
        polynomialWallet = IPolynomialSmartWallet(_polynomialWallet);
        owner = msg.sender;
    }

    /**
     * @dev Deposit funds into the Polynomial Smart Wallet.
     */
    function depositFunds() external payable onlyOwner {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        polynomialWallet.deposit{value: msg.value}();
        emit FundsDeposited(msg.value);
    }

    /**
     * @dev Withdraw funds from the Polynomial Smart Wallet.
     * @param amount Amount to withdraw.
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        polynomialWallet.withdraw(amount);
        emit FundsWithdrawn(amount);
    }

    /**
     * @dev Open a leveraged position on a specific market.
     * @param marketKey The key of the market to trade on.
     * @param sizeDelta The size of the position (positive for long, negative for short).
     * @param leverage The leverage multiplier (up to 50x).
     */
    function openPosition(
        bytes32 marketKey,
        int256 sizeDelta,
        uint256 leverage
    ) external onlyOwner {
        require(leverage > 0 && leverage <= 50, "Leverage must be between 1x and 50x");
        require(sizeDelta != 0, "Size delta must not be zero");

        bool success = synthetixPerps.openPosition(marketKey, sizeDelta, leverage);
        require(success, "Failed to open position");

        emit PositionOpened(marketKey, sizeDelta, leverage);
    }

    /**
     * @dev Close an open position on a specific market.
     * @param marketKey The key of the market to close the position on.
     */
    function closePosition(bytes32 marketKey) external onlyOwner {
        bool success = synthetixPerps.closePosition(marketKey);
        require(success, "Failed to close position");

        emit PositionClosed(marketKey);
    }

    /**
     * @dev Get the current balance of the Polynomial Smart Wallet.
     * @return The balance of the wallet.
     */
    function getWalletBalance() external view returns (uint256) {
        return polynomialWallet.getBalance();
    }
}
```
