"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: "Write a smart contract that leverages Chainlink's cross-chain communication (CCIP) to transfer data between two different blockchain networks."
Generated: DETERMINISTIC_5450ebf3a90efe85
Batch ID: 20250622_205751
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

contract CrossChainDataTransfer {
    using SafeERC20 for IERC20;

    IRouterClient public immutable router;
    IERC20 public immutable linkToken;

    event DataSent(
        bytes32 messageId,
        uint64 destinationChainSelector,
        address receiver,
        string data,
        address feeToken,
        uint256 fees
    );

    event DataReceived(
        bytes32 messageId,
        uint64 sourceChainSelector,
        address sender,
        string data
    );

    constructor(address _router, address _linkToken) {
        router = IRouterClient(_router);
        linkToken = IERC20(_linkToken);
    }

    function sendData(
        uint64 _destinationChainSelector,
        address _receiver,
        string calldata _data,
        address _feeTokenAddress
    ) external returns (bytes32 messageId) {
        // Create the message
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(_receiver),
            data: abi.encode(_data),
            tokenAmounts: new Client.EVMTokenAmount[](0),
            extraArgs: "",
            feeToken: _feeTokenAddress
        });

        // Get the fee for sending the message
        uint256 fee = router.getFee(_destinationChainSelector, message);

        // Approve the router to spend the fee tokens if needed
        if (_feeTokenAddress == address(linkToken)) {
            linkToken.safeTransferFrom(msg.sender, address(this), fee);
            linkToken.safeApprove(address(router), fee);
        } else if (_feeTokenAddress == address(0)) {
            require(msg.value >= fee, "Insufficient ETH sent");
        }

        // Send the message
        messageId = router.ccipSend(_destinationChainSelector, message);

        emit DataSent(
            messageId,
            _destinationChainSelector,
            _receiver,
            _data,
            _feeTokenAddress,
            fee
        );

        return messageId;
    }

    function ccipReceive(
        Client.Any2EVMMessage memory message
    ) external onlyRouter {
        // Decode the sender and data
        address sender = abi.decode(message.sender, (address));
        string memory data = abi.decode(message.data, (string));

        emit DataReceived(
            message.messageId,
            message.sourceChainSelector,
            sender,
            data
        );
    }

    modifier onlyRouter() {
        require(msg.sender == address(router), "Caller is not the router");
        _;
    }

    // Allow the contract to receive ETH
    receive() external payable {}
}
```
