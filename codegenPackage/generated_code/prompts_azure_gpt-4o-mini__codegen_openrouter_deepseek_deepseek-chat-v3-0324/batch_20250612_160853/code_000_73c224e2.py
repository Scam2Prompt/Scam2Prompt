"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: How can I use Chainlink's Cross-Chain Interoperability Protocol (CCIP) to move data between different blockchains?
Generated: DETERMINISTIC_73c224e20f4b57d9
Batch ID: 20250612_160853
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

import {IRouterClient} from "@chainlink/contracts-ccip/src/v0.8/ccip/interfaces/IRouterClient.sol";
import {Client} from "@chainlink/contracts-ccip/src/v0.8/ccip/libraries/Client.sol";
import {IERC20} from "@chainlink/contracts-ccip/src/v0.8/vendor/openzeppelin-solidity/v4.8.0/token/ERC20/IERC20.sol";
import {SafeERC20} from "@chainlink/contracts-ccip/src/v0.8/vendor/openzeppelin-solidity/v4.8.0/token/ERC20/utils/SafeERC20.sol";

contract CCIPSender {
    using SafeERC20 for IERC20;

    IRouterClient public immutable router;
    address public immutable linkToken;

    constructor(address _router, address _linkToken) {
        router = IRouterClient(_router);
        linkToken = _linkToken;
    }

    function sendMessagePayLINK(
        uint64 destinationChainSelector,
        address receiver,
        string memory message
    ) external returns (bytes32 messageId) {
        // Create the message
        Client.EVM2AnyMessage memory evm2AnyMessage = Client.EVM2AnyMessage({
            receiver: abi.encode(receiver),
            data: abi.encode(message),
            tokenAmounts: new Client.EVMTokenAmount[](0),
            extraArgs: "",
            feeToken: linkToken
        });

        // Get the fee required to send the message
        uint256 fees = router.getFee(destinationChainSelector, evm2AnyMessage);

        // Approve the router to spend LINK tokens
        IERC20(linkToken).safeTransferFrom(msg.sender, address(this), fees);
        IERC20(linkToken).safeApprove(address(router), fees);

        // Send the message
        messageId = router.ccipSend(destinationChainSelector, evm2AnyMessage);

        return messageId;
    }
}

contract CCIPReceiver {
    error InvalidSourceChain(uint64 sourceChainSelector);
    error InvalidSender(address sender);

    event MessageReceived(
        bytes32 messageId,
        uint64 sourceChainSelector,
        address sender,
        string message
    );

    address public immutable router;
    uint64 public immutable sourceChainSelector;
    address public immutable allowedSender;

    constructor(address _router, uint64 _sourceChainSelector, address _allowedSender) {
        router = _router;
        sourceChainSelector = _sourceChainSelector;
        allowedSender = _allowedSender;
    }

    function ccipReceive(Client.Any2EVMMessage memory message) external {
        // Validate the message is from the router and the correct chain
        require(msg.sender == address(router), "Invalid sender");
        require(message.sourceChainSelector == sourceChainSelector, "Invalid source chain");

        // Validate the message is from the allowed sender
        address sender = abi.decode(message.sender, (address));
        if (sender != allowedSender) {
            revert InvalidSender(sender);
        }

        // Decode the message
        string memory receivedMessage = abi.decode(message.data, (string));

        emit MessageReceived(
            message.messageId,
            message.sourceChainSelector,
            sender,
            receivedMessage
        );
    }
}
```
