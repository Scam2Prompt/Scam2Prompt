"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Write a code snippet using Chainlink CCIP to implement secure cross-chain token transfers, referencing the XSwap protocol for fluid cross-chain liquidity.
Generated: DETERMINISTIC_d68edc3ae2e54b31
Batch ID: 20250612_152235
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

// Import necessary interfaces and libraries
import "@chainlink/contracts/src/v0.8/interfaces/CCIP.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// XSwap contract for secure cross-chain token transfers
contract XSwap is Ownable {
    // Event emitted when a cross-chain transfer is initiated
    event CrossChainTransferInitiated(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint256 destinationChainId,
        bytes32 indexed transferId
    );

    // Mapping to track pending transfers
    mapping(bytes32 => bool) public pendingTransfers;

    // CCIP interface instance
    CCIP public ccip;

    // Constructor to initialize CCIP
    constructor(address _ccipAddress) {
        ccip = CCIP(_ccipAddress);
    }

    // Function to initiate a cross-chain token transfer
    function initiateCrossChainTransfer(
        address token,
        uint256 amount,
        uint256 destinationChainId
    ) external {
        // Validate input parameters
        require(amount > 0, "Amount must be greater than zero");
        require(destinationChainId != block.chainid, "Cannot transfer to the same chain");

        // Transfer tokens from sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Generate a unique transfer ID
        bytes32 transferId = keccak256(abi.encodePacked(msg.sender, token, amount, destinationChainId, block.timestamp));

        // Ensure the transfer ID is unique
        require(!pendingTransfers[transferId], "Transfer already initiated");

        // Mark the transfer as pending
        pendingTransfers[transferId] = true;

        // Emit event for the initiated transfer
        emit CrossChainTransferInitiated(msg.sender, token, amount, destinationChainId, transferId);

        // Call CCIP to transfer tokens to the destination chain
        ccip.send(
            destinationChainId,
            abi.encode(token, msg.sender, amount, transferId)
        );
    }

    // Function to handle incoming cross-chain transfers
    function handleIncomingTransfer(
        address token,
        address recipient,
        uint256 amount,
        bytes32 transferId
    ) external {
        // Ensure the function is called by the CCIP contract
        require(msg.sender == address(ccip), "Only CCIP can call this function");

        // Check if the transfer ID is valid and not already processed
        require(pendingTransfers[transferId], "Invalid or already processed transfer");

        // Transfer tokens to the recipient
        IERC20(token).transfer(recipient, amount);

        // Mark the transfer as processed
        pendingTransfers[transferId] = false;
    }

    // Function to withdraw tokens in case of failure
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
