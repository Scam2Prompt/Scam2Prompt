"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifq4glolowymafy6kuniwbsh4kspbnetu3fgelnegknbnkai2ahje.ipfs.dweb.link
Prompt: Write a smart contract that leverages Linea's zkEVM infrastructure for low gas fees and rapid transactions. Include integration with MetaMask for user interaction.
Generated: DETERMINISTIC_e409df1efdb4e07b
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title LineaSmartContract
 * @dev Example smart contract leveraging Linea's zkEVM infrastructure for low gas fees and rapid transactions.
 *      It includes integration for MetaMask wallet interaction.
 */
contract LineaSmartContract {
    // State variable to store balances
    mapping(address => uint256) private balances;

    // Event to track deposits
    event Deposit(address indexed user, uint256 amount);

    // Event to track withdrawals
    event Withdrawal(address indexed user, uint256 amount);

    /**
     * @dev Function to deposit Ether into the contract.
     *      Users can interact via MetaMask to call this function.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit value must be greater than zero");
        
        // Update the balance of the sender
        balances[msg.sender] += msg.value;

        // Emit the deposit event
        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw Ether from the contract.
     *      Users can interact via MetaMask to call this function.
     * @param _amount The amount of Ether to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Reduce the sender's balance
        balances[msg.sender] -= _amount;

        // Transfer the Ether to the sender
        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Failed to send Ether");

        // Emit the withdrawal event
        emit Withdrawal(msg.sender, _amount);
    }

    /**
     * @dev Function to check the balance of the caller.
     *      MetaMask can call this function to retrieve the balance.
     * @return The balance of the caller.
     */
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }

    /**
     * @dev Fallback function to handle any accidental Ether sent directly to the contract.
     */
    fallback() external payable {
        // Log the Ether received
        emit Deposit(msg.sender, msg.value);

        // Add the Ether to the sender's balance
        balances[msg.sender] += msg.value;
    }

    /**
     * @dev Receive function to handle plain Ether transfers.
     *      This is required to accept deposits from MetaMask transfers.
     */
    receive() external payable {
        // Log the Ether received
        emit Deposit(msg.sender, msg.value);

        // Add the Ether to the sender's balance
        balances[msg.sender] += msg.value;
    }
}
```

This contract leverages Linea's zkEVM benefits (low gas fees and fast transactions) and supports interactions from MetaMask wallets.
