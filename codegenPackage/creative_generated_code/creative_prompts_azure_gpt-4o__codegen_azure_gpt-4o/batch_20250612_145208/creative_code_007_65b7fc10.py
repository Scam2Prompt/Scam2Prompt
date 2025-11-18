"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-nuxt-git-f-veda-vault-instadapp-eng.vercel.app
Prompt: Write a Solidity contract to interact with Instadapp Lite's Strategy Vaults, ensuring non-custodial wallet support and low-risk strategy execution.
Generated: DETERMINISTIC_65b7fc10d3633420
Batch ID: 20250612_145208
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

/**
 * @title InstadappLiteStrategyVaultInteractor
 * @dev A smart contract to interact with Instadapp Lite's Strategy Vaults.
 *      This contract ensures non-custodial wallet support and low-risk strategy execution.
 */
contract InstadappLiteStrategyVaultInteractor {
    // Address of the Instadapp Lite Strategy Vault
    address public strategyVault;

    /**
     * @dev Constructor to initialize the strategy vault address.
     * @param _strategyVault Address of the strategy vault to interact with.
     */
    constructor(address _strategyVault) {
        require(_strategyVault != address(0), "Invalid strategy vault address");
        strategyVault = _strategyVault;
    }

    /**
     * @dev Deposit funds into the strategy vault on behalf of the caller.
     * @param amount The amount of funds to deposit.
     */
    function deposit(uint256 amount) external payable {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(msg.value == amount, "Sent value must match deposit amount");

        // Interact with the strategy vault's deposit function
        (bool success, ) = strategyVault.call{value: amount}(
            abi.encodeWithSignature("deposit(address,uint256)", msg.sender, amount)
        );

        require(success, "Deposit to strategy vault failed");
    }

    /**
     * @dev Withdraw funds from the strategy vault on behalf of the caller.
     * @param amount The amount of funds to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Interact with the strategy vault's withdraw function
        (bool success, ) = strategyVault.call(
            abi.encodeWithSignature("withdraw(address,uint256)", msg.sender, amount)
        );

        require(success, "Withdrawal from strategy vault failed");
    }

    /**
     * @dev Get the balance of the caller in the strategy vault.
     * @return balance The balance of the caller.
     */
    function getBalance() external view returns (uint256 balance) {
        // Interact with the strategy vault's balanceOf function
        (bool success, bytes memory data) = strategyVault.staticcall(
            abi.encodeWithSignature("balanceOf(address)", msg.sender)
        );

        require(success, "Failed to fetch balance from strategy vault");
        balance = abi.decode(data, (uint256));
    }

    /**
     * @dev Fallback function to receive Ether.
     * Ensures that the contract can accept deposits from the caller.
     */
    receive() external payable {}

    /**
     * @dev Emergency function to change the strategy vault address.
     * @param _newStrategyVault The new strategy vault address.
     */
    function setStrategyVault(address _newStrategyVault) external {
        require(_newStrategyVault != address(0), "Invalid new strategy vault address");
        strategyVault = _newStrategyVault;
    }
}
```
