"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-dapp.pages.dev
Prompt: Explain how to implement the anyCall feature in a smart contract for cross-chain transactions using Multichain.
Generated: DETERMINISTIC_0af1a15af530a9ec
Batch ID: 20250612_163500
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

interface IMultichain {
    function anyCall(
        address target,
        bytes calldata data,
        uint256 value,
        uint256 chainId
    ) external payable;
}

/**
 * @title CrossChainTransaction
 * @dev This contract enables cross-chain transactions using the anyCall feature of Multichain.
 */
contract CrossChainTransaction is Ownable {
    IMultichain public multichain;

    // Event to emit when a cross-chain transaction is initiated
    event CrossChainTransactionInitiated(
        address indexed target,
        bytes data,
        uint256 value,
        uint256 chainId
    );

    // Constructor to set the Multichain contract address
    constructor(address _multichainAddress) {
        require(_multichainAddress != address(0), "Invalid Multichain address");
        multichain = IMultichain(_multichainAddress);
    }

    /**
     * @dev Initiates a cross-chain transaction using the anyCall feature.
     * @param target The address of the contract to which the function call will be sent.
     * @param data The encoded function call data.
     * @param value The amount of native currency to send with the call.
     * @param chainId The target chain ID for the transaction.
     */
    function initiateCrossChainTransaction(
        address target,
        bytes calldata data,
        uint256 value,
        uint256 chainId
    ) external payable onlyOwner {
        require(target != address(0), "Invalid target address");
        require(chainId > 0, "Invalid chain ID");

        // Transfer value to the Multichain contract
        require(msg.value == value, "Value mismatch");

        // Call the anyCall function of Multichain
        multichain.anyCall{value: value}(target, data, value, chainId);

        // Emit an event for the initiated transaction
        emit CrossChainTransactionInitiated(target, data, value, chainId);
    }

    /**
     * @dev Allows the contract owner to withdraw any native currency sent to the contract.
     * @param to The address to send the withdrawn amount to.
     * @param amount The amount of native currency to withdraw.
     */
    function withdraw(address payable to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid recipient address");
        require(address(this).balance >= amount, "Insufficient balance");

        // Transfer the specified amount to the recipient address
        (bool success, ) = to.call{value: amount}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to receive native currency
    receive() external payable {}
}
```
