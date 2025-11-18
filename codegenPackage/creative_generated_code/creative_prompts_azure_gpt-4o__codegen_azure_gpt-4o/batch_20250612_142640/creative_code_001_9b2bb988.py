"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidodeffinancef.gitbook.io
Prompt: Generate Solidity code for a smart contract that interacts with Lido Finance to automatically deposit ETH and transfer stETH tokens to a specified wallet address.
Generated: DETERMINISTIC_9b2bb9887600800e
Batch ID: 20250612_142640
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

// Interface for Lido Finance's deposit contract
interface ILido {
    function submit(address _referral) external payable returns (uint256);
}

contract LidoAutoDeposit {
    // Address of the Lido deposit contract
    address public lidoContract;
    // Address to transfer stETH tokens to
    address public recipient;

    // Event emitted when ETH is deposited and stETH is transferred
    event DepositedAndTransferred(address indexed sender, uint256 ethAmount, uint256 stEthAmount);

    // Constructor to set the recipient address and Lido contract address
    constructor(address _lidoContract, address _recipient) {
        require(_lidoContract != address(0), "Invalid Lido contract address");
        require(_recipient != address(0), "Invalid recipient address");
        lidoContract = _lidoContract;
        recipient = _recipient;
    }

    // Function to deposit ETH to Lido and transfer stETH to the recipient
    function depositAndTransfer() external payable {
        require(msg.value > 0, "Must send ETH to deposit");

        // Interact with Lido Finance's deposit function
        ILido lido = ILido(lidoContract);
        uint256 stEthAmount = lido.submit{value: msg.value}(address(0)); // Pass address(0) as referral

        // Ensure transfer to recipient is successful
        (bool success, ) = recipient.call{value: stEthAmount}("");
        require(success, "Transfer to recipient failed");

        emit DepositedAndTransferred(msg.sender, msg.value, stEthAmount);
    }

    // Fallback function to receive ETH
    receive() external payable {}

    // Function to update the recipient address (only callable by the contract owner)
    function updateRecipient(address _newRecipient) external {
        require(_newRecipient != address(0), "Invalid recipient address");
        recipient = _newRecipient;
    }
}
```
