"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Develop a simple smart contract using Solidity that utilizes Chainlink CCIP for secure cross-chain messages and token transfers, suitable for the XSwap protocol.
Generated: DETERMINISTIC_aa22c87600e7fec7
Batch ID: 20250622_205836
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

// Import Chainlink CCIP interfaces
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessageReceiver.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ICrossChainMessageSender.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/ITokenPool.sol";
import "@chainlink/contracts/src/v0.8/ccip/interfaces/IRouter.sol";

contract XSwapCrossChain {
    // Chainlink Router address (update with the correct address for your network)
    IRouter public immutable router;

    // Event emitted when a cross-chain message is sent
    event CrossChainMessageSent(
        uint64 indexed destinationChainId,
        address indexed receiver,
        bytes data
    );

    // Event emitted when a cross-chain token transfer is initiated
    event CrossChainTokenTransferInitiated(
        uint64 indexed destinationChainId,
        address indexed receiver,
        address token,
        uint256 amount
    );

    // Constructor to initialize the Chainlink Router
    constructor(address _router) {
        require(_router != address(0), "Router address cannot be zero");
        router = IRouter(_router);
    }

    /**
     * @notice Sends a cross-chain message to a receiver on another chain.
     * @param destinationChainId The ID of the destination chain.
     * @param receiver The address of the receiver on the destination chain.
     * @param data The message payload to send.
     */
    function sendCrossChainMessage(
        uint64 destinationChainId,
        address receiver,
        bytes memory data
    ) external payable {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(data.length > 0, "Message payload cannot be empty");

        // Send the cross-chain message using Chainlink CCIP
        router.ccipSend{value: msg.value}(
            destinationChainId,
            receiver,
            data
        );

        emit CrossChainMessageSent(destinationChainId, receiver, data);
    }

    /**
     * @notice Initiates a cross-chain token transfer.
     * @param destinationChainId The ID of the destination chain.
     * @param receiver The address of the receiver on the destination chain.
     * @param token The address of the token to transfer.
     * @param amount The amount of tokens to transfer.
     */
    function initiateCrossChainTokenTransfer(
        uint64 destinationChainId,
        address receiver,
        address token,
        uint256 amount
    ) external payable {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(token != address(0), "Token address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");

        // Approve the router to spend the tokens
        ITokenPool(token).approve(address(router), amount);

        // Initiate the cross-chain token transfer
        router.ccipSendToken{value: msg.value}(
            destinationChainId,
            receiver,
            token,
            amount
        );

        emit CrossChainTokenTransferInitiated(destinationChainId, receiver, token, amount);
    }

    /**
     * @notice Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @notice Withdraw Ether from the contract.
     * @param to The address to send the Ether to.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawEther(address payable to, uint256 amount) external {
        require(to != address(0), "Recipient address cannot be zero");
        require(amount <= address(this).balance, "Insufficient balance");

        to.transfer(amount);
    }
}
```
