"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycoded.pages.dev
Prompt: Explain how to handle incoming Ether in a Solidity contract, using the receive function from the OneinchSlippageBot as a reference.
Generated: DETERMINISTIC_7c801923f1927943
Batch ID: 20250612_164046
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
 * @title EtherReceiverContract
 * @dev A Solidity contract designed to handle incoming Ether using the `receive` function.
 */
contract EtherReceiverContract {
    // Event to log Ether received
    event EtherReceived(address indexed sender, uint256 amount);

    /**
     * @dev Emitted when Ether is received. This function is called when the contract
     *      receives Ether without any calldata.
     */
    receive() external payable {
        // Emit the EtherReceived event to log the sender and the amount received
        emit EtherReceived(msg.sender, msg.value);
    }

    /**
     * @dev Fallback function to handle calls with calldata that do not match any function signature.
     *      Includes error handling to ensure the fallback function does not accidentally execute logic.
     */
    fallback() external payable {
        require(msg.value > 0, "Fallback function only accepts Ether");
        emit EtherReceived(msg.sender, msg.value);
    }

    /**
     * @dev Function to retrieve the contract's Ether balance.
     * @return The balance of Ether held by the contract, in wei.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Withdraw Ether from the contract.
     * @param _to The recipient's address.
     * @param _amount The amount of Ether to withdraw, in wei.
     */
    function withdrawEther(address payable _to, uint256 _amount) external {
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(address(this).balance >= _amount, "Insufficient balance");

        // Transfer the Ether to the specified address
        _to.transfer(_amount);
    }
}
```
