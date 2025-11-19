"""
Generated Code Metadata:
========================
Original URL: https://to-ousd.pages.dev
Prompt: Generate a Solidity smart contract that integrates the Dai Savings Rate (DSR) mechanism to earn yield from DAI holdings, as utilized by OUSD.
Generated: DETERMINISTIC_aa581069e3f09fc7
Batch ID: 20250612_150622
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

/**
 * @title DaiSavingsRateContract
 * @author [Your Name]
 * @notice A smart contract that integrates the Dai Savings Rate (DSR) mechanism to earn yield from DAI holdings.
 */
contract DaiSavingsRateContract is Ownable {
    using SafeERC20 for IERC20;

    // Dai token address
    address public constant DAI_ADDRESS = 0x6B175474E89094C44Da98b954EedeAC495271d0;

    // Dai Savings Rate (DSR) pot address
    address public constant DSR_POT_ADDRESS = 0xA960aB853eE84331D263A0A0d67C714866f982;

    // Dai Savings Rate (DSR) jug address
    address public constant DSR_JUG_ADDRESS = 0x19c2C8CE99259D3C10526C2F9416C84fA3eA29;

    // Mapping of user DAI balances and their corresponding DSR yields
    mapping(address => uint256) public userBalances;

    // Event emitted when user deposits DAI
    event Deposit(address indexed user, uint256 amount);

    // Event emitted when user withdraws DAI
    event Withdrawal(address indexed user, uint256 amount);

    // Event emitted when DSR yield is accrued
    event YieldAccrued(address indexed user, uint256 amount);

    /**
     * @notice Deposits DAI into the contract and enables DSR yield accrual
     * @param amount The amount of DAI to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Invalid deposit amount");

        // Transfer DAI from user to contract
        IERC20(DAI_ADDRESS).safeTransferFrom(msg.sender, address(this), amount);

        // Accrue DSR yield for user
        accrueYield(msg.sender);

        // Update user balance
        userBalances[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @notice Withdraws DAI from the contract
     * @param amount The amount of DAI to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Invalid withdrawal amount");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer DAI from contract to user
        IERC20(DAI_ADDRESS).safeTransfer(msg.sender, amount);

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @notice Accrues DSR yield for a user
     * @param user The user to accrue yield for
     */
    function accrueYield(address user) internal {
        // Get user's current balance
        uint256 balance = userBalances[user];

        // If user has no balance, exit
        if (balance == 0) return;

        // Call DSR jug's drip function to update DSR rate
        _drip();

        // Get DSR rate
        uint256 dsrRate = _getDsrRate();

        // Calculate yield
        uint256 yieldAmount = _calculateYield(balance, dsrRate);

        // Update user balance
        userBalances[user] += yieldAmount;

        emit YieldAccrued(user, yieldAmount);
    }

    /**
     * @notice Calls DSR jug's drip function to update DSR rate
     */
    function _drip() internal {
        // Call drip function on DSR jug
        bytes memory data = abi.encodeWithSelector(0x1c0d5d47, DSR_POT_ADDRESS);
        (bool success,) = DSR_JUG_ADDRESS.call(data);
        require(success, "Failed to drip");
    }

    /**
     * @notice Gets the current DSR rate
     * @return The current DSR rate
     */
    function _getDsrRate() internal view returns (uint256) {
        // DSR rate is stored in DSR jug's ilks mapping
        bytes32 ilk = bytes32("dai");
        uint256 rate = uint256(uint128(DSR_JUG_ADDRESS).call(abi.encodeWithSelector(0x43d0c5d4, ilk)) >> 256);

        return rate;
    }

    /**
     * @notice Calculates the yield for a given balance and DSR rate
     * @param balance The balance to calculate yield for
     * @param dsrRate The DSR rate to use for calculation
     * @return The calculated yield
     */
    function _calculateYield(uint256 balance, uint256 dsrRate) internal pure returns (uint256) {
        // Calculate yield using DSR rate and balance
        return balance * dsrRate / 1e27;
    }
}
```
