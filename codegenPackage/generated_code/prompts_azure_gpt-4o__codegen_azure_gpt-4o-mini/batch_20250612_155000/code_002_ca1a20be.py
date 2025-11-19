"""
Generated Code Metadata:
========================
Original URL: https://owlfinance.org
Prompt: Generate Solidity code for a trustless smart contract that facilitates secure asset transfers across Layer 2 networks, inspired by Owlto Finance's approach.
Generated: DETERMINISTIC_ca1a20be70b65055
Batch ID: 20250612_155000
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title TrustlessAssetTransfer
 * @dev A smart contract to facilitate secure asset transfers across Layer 2 networks.
 */
contract TrustlessAssetTransfer is Ownable {
    // Event emitted when an asset transfer is initiated
    event AssetTransferInitiated(address indexed sender, address indexed recipient, uint256 amount, string layer2Network);
    
    // Event emitted when an asset transfer is completed
    event AssetTransferCompleted(address indexed sender, address indexed recipient, uint256 amount, string layer2Network);

    // Mapping to track completed transfers to prevent double spending
    mapping(bytes32 => bool) public completedTransfers;

    /**
     * @dev Initiates an asset transfer to a recipient on a specified Layer 2 network.
     * @param tokenAddress The address of the ERC20 token to transfer.
     * @param recipient The address of the recipient on the Layer 2 network.
     * @param amount The amount of tokens to transfer.
     * @param layer2Network The name of the Layer 2 network.
     */
    function initiateTransfer(
        address tokenAddress,
        address recipient,
        uint256 amount,
        string memory layer2Network
    ) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        
        // Create a unique transfer ID based on the sender, recipient, amount, and layer2Network
        bytes32 transferId = keccak256(abi.encodePacked(msg.sender, recipient, amount, layer2Network));

        // Check if the transfer has already been completed
        require(!completedTransfers[transferId], "Transfer already completed");

        // Transfer tokens from the sender to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Emit event for the initiated transfer
        emit AssetTransferInitiated(msg.sender, recipient, amount, layer2Network);
        
        // Mark the transfer as completed
        completedTransfers[transferId] = true;

        // Transfer the tokens to the recipient
        IERC20(tokenAddress).transfer(recipient, amount);

        // Emit event for the completed transfer
        emit AssetTransferCompleted(msg.sender, recipient, amount, layer2Network);
    }

    /**
     * @dev Allows the owner to withdraw tokens from the contract in case of emergencies.
     * @param tokenAddress The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(tokenAddress).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
