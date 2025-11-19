"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://copycodegpt.pages.dev
Prompt: Explain how to implement the receive function in a Solidity contract for handling incoming Ether, as seen in the OneinchSlippageBot example.
Generated: DETERMINISTIC_9a80dc78041e1f55
Batch ID: 20250612_163156
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
 * @title EtherReceiver
 * @dev Contract that implements the `receive` function to handle incoming Ether.
 */
contract EtherReceiver {
    // Event to log received Ether
    event EtherReceived(address indexed sender, uint256 amount);

    /**
     * @dev The `receive` function is a special function in Solidity that is called
     * whenever the contract receives plain Ether without any calldata.
     * This is used to accept Ether sent directly to the contract.
     */
    receive() external payable {
        // Emit an event to log the details of the received Ether
        emit EtherReceived(msg.sender, msg.value);
    }

    /**
     * @dev Fallback function to handle unexpected calls with calldata.
     * It is recommended to include this for better contract robustness.
     * This fallback function does not accept Ether.
     */
    fallback() external {
        revert("Fallback function triggered: Call not supported");
    }

    /**
     * @dev Allows the owner of the contract to withdraw Ether stored in the contract.
     * This function can be updated to include access control mechanisms like Ownable.
     */
    function withdrawEther(address payable recipient) external {
        require(address(this).balance > 0, "No Ether available to withdraw");

        // Transfer contract balance to the recipient's address
        recipient.transfer(address(this).balance);
    }

    /**
     * @dev Returns the contract's current Ether balance.
     */
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
