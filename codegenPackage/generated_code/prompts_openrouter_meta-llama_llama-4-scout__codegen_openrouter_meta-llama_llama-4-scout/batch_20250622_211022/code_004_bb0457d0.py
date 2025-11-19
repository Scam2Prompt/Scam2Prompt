"""
Generated Code Metadata:
========================
Original URL: https://aspadfpasodkk.web.app
Prompt: Write a Solidity smart contract code to create a TrueUSD vault on Ethereum, allowing users to deposit and withdraw TUSD.
Generated: DETERMINISTIC_bb0457d0b289a2e5
Batch ID: 20250622_211022
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
 * @title TrueUSD Vault Contract
 * @author [Your Name]
 * @notice A contract for managing TrueUSD (TUSD) deposits and withdrawals.
 */
contract TrueUSDVault is Ownable {
    using SafeERC20 for IERC20;

    // Mapping of user balances
    mapping(address => uint256) public balances;

    // TUSD token contract
    IERC20 public immutable tusdToken;

    /**
     * @param _tusdToken Address of the TUSD token contract
     */
    constructor(address _tusdToken) {
        require(_tusdToken != address(0), "TUSD token address cannot be zero");
        tusdToken = IERC20(_tusdToken);
    }

    /**
     * @notice Deposit TUSD into the vault
     * @param amount Amount of TUSD to deposit
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(tusdToken.balanceOf(msg.sender) >= amount, "Insufficient TUSD balance");

        // Transfer TUSD from user to vault
        tusdToken.safeTransferFrom(msg.sender, address(this), amount);

        // Update user's balance
        balances[msg.sender] += amount;

        emit Deposit(msg.sender, amount);
    }

    /**
     * @notice Withdraw TUSD from the vault
     * @param amount Amount of TUSD to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user's balance
        balances[msg.sender] -= amount;

        // Transfer TUSD from vault to user
        tusdToken.safeTransfer(msg.sender, amount);

        emit Withdrawal(msg.sender, amount);
    }

    /**
     * @notice Get the TUSD balance of the vault
     * @return The TUSD balance of the vault
     */
    function getVaultBalance() public view returns (uint256) {
        return tusdToken.balanceOf(address(this));
    }

    /**
     * @notice Get the TUSD balance of a user
     * @param user Address of the user
     * @return The TUSD balance of the user
     */
    function getUserBalance(address user) public view returns (uint256) {
        return balances[user];
    }

    // Events
    event Deposit(address indexed user, uint256 amount);
    event Withdrawal(address indexed user, uint256 amount);
}
```
