"""
Generated Code Metadata:
========================
Original URL: https://cctpbridge.vercel.app
Prompt: Generate a smart contract code for a CCTP-powered cross-chain bridge.
Generated: DETERMINISTIC_51865dd3bb3aa4db
Batch ID: 20250622_210802
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

// Interface for the CCTP (Cross-Chain Transfer Protocol)
interface ICCTP {
    function transfer(address token, uint256 amount, address recipient, uint256 destinationChainId) external;
}

// Smart contract for a CCTP-powered cross-chain bridge
contract CrossChainBridge is Ownable {
    using Address for address;

    // Event emitted when a transfer is initiated
    event TransferInitiated(address indexed token, uint256 amount, address indexed recipient, uint256 destinationChainId);

    // CCTP contract address
    ICCTP public cctp;

    // Constructor to set the CCTP contract address
    constructor(address _cctpAddress) {
        require(_cctpAddress.isContract(), "Invalid CCTP contract address");
        cctp = ICCTP(_cctpAddress);
    }

    // Function to initiate a cross-chain transfer
    function initiateTransfer(address token, uint256 amount, address recipient, uint256 destinationChainId) external {
        require(token.isContract(), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        require(destinationChainId != 0, "Invalid destination chain ID");

        // Transfer the token from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the CCTP contract to spend the tokens
        IERC20(token).approve(address(cctp), amount);

        // Call the CCTP transfer function
        cctp.transfer(token, amount, recipient, destinationChainId);

        // Emit the transfer event
        emit TransferInitiated(token, amount, recipient, destinationChainId);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token.isContract(), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the tokens to the owner
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the CCTP contract address (only owner)
    function updateCCTPAddress(address newCctpAddress) external onlyOwner {
        require(newCctpAddress.isContract(), "Invalid CCTP contract address");
        cctp = ICCTP(newCctpAddress);
    }
}
```
