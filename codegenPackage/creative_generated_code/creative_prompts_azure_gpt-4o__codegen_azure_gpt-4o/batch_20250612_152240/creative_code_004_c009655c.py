"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layerzero-networks.pages.dev
Prompt: Create a Solidity contract using LayerZero's `OFTCore` to implement cross-chain token transfers. Include methods for debiting and crediting tokens across blockchain networks.
Generated: DETERMINISTIC_c009655c0d61ec1e
Batch ID: 20250612_152240
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

// Import LayerZero's OFTCore contract
import "./OFTCore.sol"; // Ensure the correct import path for OFTCore

/**
 * @title CrossChainToken
 * @dev Implements cross-chain token transfers using LayerZero's OFTCore.
 */
contract CrossChainToken is OFTCore {
    // Token name and symbol
    string public name = "CrossChainToken";
    string public symbol = "CCT";

    // Token decimal places
    uint8 public decimals = 18;

    // Event emitted when tokens are debited cross-chain
    event TokenDebited(address indexed sender, uint256 amount, uint16 dstChainId);

    // Event emitted when tokens are credited cross-chain
    event TokenCredited(address indexed recipient, uint256 amount, uint16 srcChainId);

    /**
     * @dev Constructor initializes the OFTCore base contract with the LayerZero endpoint.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint.
     */
    constructor(address _layerZeroEndpoint) OFTCore(_layerZeroEndpoint) {}

    /**
     * @dev Debit tokens for a cross-chain transfer.
     * @param _dstChainId The destination chain ID.
     * @param _recipient Recipient address on the destination chain.
     * @param _amount Amount of tokens to transfer.
     * @param _adapterParams Adapter parameters for LayerZero (e.g., gas settings).
     */
    function debitTokens(
        uint16 _dstChainId,
        bytes calldata _recipient,
        uint256 _amount,
        bytes calldata _adapterParams
    ) external payable {
        // Validate input
        require(_amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Burn tokens from sender's balance
        _burn(msg.sender, _amount);

        // Call LayerZero's send function to transfer tokens cross-chain
        _send(
            msg.sender,
            _dstChainId,
            _recipient,
            _amount,
            _adapterParams
        );

        emit TokenDebited(msg.sender, _amount, _dstChainId);
    }

    /**
     * @dev Credit tokens received on the current chain.
     * @param _srcChainId The source chain ID.
     * @param _recipient Recipient address on this chain.
     * @param _amount Amount of tokens credited.
     */
    function creditTokens(
        uint16 _srcChainId,
        address _recipient,
        uint256 _amount
    ) external {
        // Validate input
        require(_amount > 0, "Amount must be greater than zero");

        // Mint tokens to the recipient's balance
        _mint(_recipient, _amount);

        emit TokenCredited(_recipient, _amount, _srcChainId);
    }

    /**
     * @dev Override _creditTo function from OFTCore to handle incoming cross-chain transfers.
     * @param _recipient Recipient address on this chain.
     * @param _amount Amount of tokens credited.
     */
    function _creditTo(address _recipient, uint256 _amount) internal override {
        // Mint tokens to the recipient
        _mint(_recipient, _amount);
    }

    /**
     * @dev Internal function to mint tokens.
     * @param account Address to mint tokens to.
     * @param amount Amount of tokens to mint.
     */
    function _mint(address account, uint256 amount) internal {
        // Add implementation for minting tokens (not shown in OFTCore)
        // Typically involves increasing the balance and total supply.
    }

    /**
     * @dev Internal function to burn tokens.
     * @param account Address to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal {
        // Add implementation for burning tokens (not shown in OFTCore)
        // Typically involves decreasing the balance and total supply.
    }
}
```

Note: Ensure LayerZero's `OFTCore` is properly imported and available in the project. The `_mint` and `_burn` functions should also be implemented based on your token's requirements.
