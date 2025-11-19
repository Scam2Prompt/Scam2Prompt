"""
Generated Code Metadata:
========================
Original URL: https://layerswap.fi
Prompt: Develop a smart contract that interacts with LayerSwap for efficient cross-chain asset transfers.
Generated: DETERMINISTIC_a1dc3f9c42ed6c44
Batch ID: 20250612_153809
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

// Interface for LayerSwap
interface ILayerSwap {
    function swap(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        uint256 deadline
    ) external returns (bool);
}

// Smart contract for cross-chain asset transfers using LayerSwap
contract CrossChainAssetTransfer is Ownable {
    ILayerSwap public layerSwap; // Instance of LayerSwap interface

    // Event emitted when a swap is initiated
    event SwapInitiated(
        address indexed fromToken,
        address indexed toToken,
        uint256 amount,
        address indexed recipient,
        uint256 deadline
    );

    // Constructor to set the LayerSwap contract address
    constructor(address _layerSwapAddress) {
        require(_layerSwapAddress != address(0), "Invalid LayerSwap address");
        layerSwap = ILayerSwap(_layerSwapAddress);
    }

    // Function to initiate a cross-chain asset transfer
    function initiateSwap(
        address fromToken,
        address toToken,
        uint256 amount,
        address recipient,
        uint256 deadline
    ) external {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Invalid recipient address");
        require(deadline > block.timestamp, "Deadline must be in the future");

        // Transfer tokens from the sender to this contract
        IERC20(fromToken).transferFrom(msg.sender, address(this), amount);

        // Approve LayerSwap to spend the tokens
        IERC20(fromToken).approve(address(layerSwap), amount);

        // Call the LayerSwap swap function
        bool success = layerSwap.swap(fromToken, toToken, amount, recipient, deadline);
        require(success, "LayerSwap swap failed");

        // Emit an event for the swap
        emit SwapInitiated(fromToken, toToken, amount, recipient, deadline);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }

    // Function to update the LayerSwap contract address (only owner)
    function updateLayerSwapAddress(address newLayerSwapAddress) external onlyOwner {
        require(newLayerSwapAddress != address(0), "Invalid LayerSwap address");
        layerSwap = ILayerSwap(newLayerSwapAddress);
    }
}
```
