"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ackinacki-air.live
Prompt: Create a smart contract on the Acki Nacki blockchain that utilizes the $SHELL gas token for stable transaction fees.
Generated: DETERMINISTIC_9d4bc9b84afccc33
Batch ID: 20250612_151219
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

// Import required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AckiNackiSmartContract
 * @dev A simple smart contract that utilizes the $SHELL token for gas fees on the Acki Nacki blockchain.
 */
contract AckiNackiSmartContract is Ownable {
    // State variable to hold the address of the $SHELL token contract
    IERC20 public shellToken;

    // Events to log transactions and interactions
    event TransactionExecuted(address indexed sender, uint256 amount);

    /**
     * @dev Constructor to set the $SHELL token address.
     * @param _shellToken The address of the $SHELL token contract.
     */
    constructor(address _shellToken) {
        require(_shellToken != address(0), "Invalid token address");
        shellToken = IERC20(_shellToken);
    }

    /**
     * @dev Function to execute a transaction using $SHELL tokens.
     * @param amount The amount of $SHELL tokens to use for the transaction.
     */
    function executeTransaction(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(shellToken.balanceOf(msg.sender) >= amount, "Insufficient $SHELL balance");

        // Transfer $SHELL tokens from sender to this contract
        require(shellToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Emit transaction event
        emit TransactionExecuted(msg.sender, amount);
    }

    /**
     * @dev Function for the owner to withdraw $SHELL tokens from the contract.
     * @param amount The amount of $SHELL tokens to withdraw.
     */
    function withdrawShellTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(shellToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer $SHELL tokens from this contract to the owner
        require(shellToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Function to check the balance of $SHELL tokens held by the contract.
     * @return The balance of $SHELL tokens.
     */
    function checkShellTokenBalance() external view returns (uint256) {
        return shellToken.balanceOf(address(this));
    }
}
```
