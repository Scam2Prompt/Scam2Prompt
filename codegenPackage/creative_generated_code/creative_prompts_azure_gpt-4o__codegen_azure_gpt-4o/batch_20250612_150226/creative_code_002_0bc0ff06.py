"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Provide a code example for burning tokens in a LayerZero-based OFT contract using the `_debitSender` and `_debitThis` methods.
Generated: DETERMINISTIC_0bc0ff06fab6ffb5
Batch ID: 20250612_150226
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

import "@layerzerolabs/oft/OFT.sol";

/// @title LayerZero-based OFT Token Contract with Burn Functionality
/// @dev An example implementation of burning tokens using `_debitSender` and `_debitThis` methods.
contract MyOFT is OFT {
    /// @notice Constructor for the OFT contract.
    /// @param _name Token name.
    /// @param _symbol Token symbol.
    /// @param _lzEndpoint LayerZero endpoint address.
    constructor(
        string memory _name,
        string memory _symbol,
        address _lzEndpoint
    ) OFT(_name, _symbol, _lzEndpoint) {}

    /// @notice Burns tokens from the sender's address in the current chain.
    /// @dev Uses `_debitSender` to handle cross-chain state consistency.
    /// @param _amount The amount of tokens to burn.
    function burnTokens(uint256 _amount) external {
        // Ensure the sender has sufficient balance
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Debit tokens from the sender
        _debitSender(msg.sender, _amount);

        // Perform the actual burn operation
        _burn(address(this), _amount);

        // Emit an event for transparency and tracking
        emit TokensBurned(msg.sender, _amount);
    }

    /// @notice Burns tokens from the contract address in the current chain.
    /// @dev Uses `_debitThis` to handle cross-chain state consistency.
    /// @param _amount The amount of tokens to burn.
    function burnContractTokens(uint256 _amount) external {
        // Ensure the contract itself has sufficient balance
        require(balanceOf(address(this)) >= _amount, "Insufficient contract balance");

        // Debit tokens from the contract
        _debitThis(_amount);

        // Perform the actual burn operation
        _burn(address(this), _amount);

        // Emit an event for transparency and tracking
        emit ContractTokensBurned(_amount);
    }

    /// @notice Event emitted when tokens are burned by the sender.
    /// @param sender The address of the sender who burned the tokens.
    /// @param amount The amount of tokens burned.
    event TokensBurned(address indexed sender, uint256 amount);

    /// @notice Event emitted when tokens are burned from the contract address.
    /// @param amount The amount of tokens burned.
    event ContractTokensBurned(uint256 amount);
}
```

This code defines a LayerZero-compatible OFT contract with functionality to burn tokens using the `_debitSender` and `_debitThis` methods. It implements basic error handling and follows best practices for Solidity development.
