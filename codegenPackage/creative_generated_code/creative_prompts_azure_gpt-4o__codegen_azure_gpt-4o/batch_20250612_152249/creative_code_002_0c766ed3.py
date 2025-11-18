"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Implement Chainlink's Cross-Chain Communication Protocol (CCIP) to transfer tokenized assets between two blockchains.
Generated: DETERMINISTIC_0c766ed3b64a86ce
Batch ID: 20250612_152249
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

// Import Chainlink's CCIP interface and libraries
import "@chainlink/contracts-ccip/interfaces/ICrossChainMessenger.sol";
import "@chainlink/contracts-ccip/interfaces/ICrossChainMessageReceiver.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract CrossChainTokenTransfer {
    // Address of the Chainlink Cross-Chain Messenger contract
    ICrossChainMessenger public immutable crossChainMessenger;
    
    // Token contract address (ERC20)
    IERC20 public token;

    // Event to emit transfer information
    event TokenTransferInitiated(
        address sender,
        uint256 amount,
        uint256 destinationChainId,
        address destinationAddress
    );

    event TokenReceived(
        address sender,
        uint256 amount,
        uint256 sourceChainId
    );

    // Constructor to set the Cross-Chain Messenger contract and token address
    constructor(address _crossChainMessenger, address _token) {
        require(_crossChainMessenger != address(0), "Invalid messenger address");
        require(_token != address(0), "Invalid token address");
        
        crossChainMessenger = ICrossChainMessenger(_crossChainMessenger);
        token = IERC20(_token);
    }

    /**
     * @notice Initiates a cross-chain token transfer
     * @param destinationChainId The ID of the destination chain
     * @param destinationAddress The recipient's address on the destination chain
     * @param amount The amount of tokens to transfer
     */
    function initiateTokenTransfer(
        uint256 destinationChainId,
        address destinationAddress,
        uint256 amount
    ) external {
        require(amount > 0, "Amount must be greater than 0");
        require(destinationAddress != address(0), "Invalid destination address");

        // Transfer tokens to this contract for custody
        require(
            token.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Encode the payload for cross-chain transfer
        bytes memory payload = abi.encode(amount);

        // Send a cross-chain message using the Cross-Chain Messenger
        crossChainMessenger.sendMessage(
            destinationChainId,
            destinationAddress,
            payload
        );

        emit TokenTransferInitiated(msg.sender, amount, destinationChainId, destinationAddress);
    }

    /**
     * @notice Handles incoming cross-chain messages
     * @dev Only callable by the Cross-Chain Messenger contract
     * @param sender The address that initiated the message
     * @param sourceChainId The ID of the source chain
     * @param payload The message payload
     */
    function receiveMessage(
        address sender,
        uint256 sourceChainId,
        bytes memory payload
    ) external {
        require(msg.sender == address(crossChainMessenger), "Unauthorized sender");

        // Decode the incoming payload
        uint256 amount = abi.decode(payload, (uint256));

        // Transfer tokens to the recipient (sender of the cross-chain message)
        require(
            token.transfer(sender, amount),
            "Token transfer failed"
        );

        emit TokenReceived(sender, amount, sourceChainId);
    }
}
```
