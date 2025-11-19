"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a code snippet that demonstrates how to implement the _debitSender function in an OFT contract using LayerZero.
Generated: DETERMINISTIC_e8542032e931436f
Batch ID: 20250612_164304
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

import { IERC20 } from "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import { SafeERC20 } from "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import { Ownable } from "@openzeppelin/contracts/access/Ownable.sol";
import { OFT } from "@layerzerolabs/lz-token-contracts/contracts/token/oft/OFT.sol";
import { ILayerZeroEndpoint } from "@layerzerolabs/lz-token-contracts/contracts/interfaces/ILayerZeroEndpoint.sol";

contract MyOFT is OFT {
    using SafeERC20 for IERC20;

    // Mapping of senders to their respective configurations
    mapping(address => mapping(uint16 => uint256)) public _debitSenders;

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 _initialSupply,
        address _lzEndpoint
    ) OFT(name_, symbol_, _lzEndpoint) {
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Debits the sender's balance for a specific chain ID.
     * @param _sender The address of the sender.
     * @param _chainId The chain ID to debit for.
     * @param _amount The amount to debit.
     */
    function _debitSender(
        address _sender,
        uint16 _chainId,
        uint256 _amount
    ) internal virtual override {
        // Ensure the sender has sufficient balance
        require(balanceOf(_sender) >= _amount, "Insufficient balance");

        // Update the sender's debit configuration
        _debitSenders[_sender][_chainId] += _amount;

        // Burn the tokens from the sender's balance
        _burn(_sender, _amount);
    }

    /**
     * @dev Credits the sender's balance for a specific chain ID.
     * @param _sender The address of the sender.
     * @param _chainId The chain ID to credit for.
     * @param _amount The amount to credit.
     */
    function _creditSender(
        address _sender,
        uint16 _chainId,
        uint256 _amount
    ) internal virtual override {
        // Update the sender's debit configuration
        _debitSenders[_sender][_chainId] -= _amount;

        // Mint the tokens to the sender's balance
        _mint(_sender, _amount);
    }

    // Additional functions for testing and demonstration purposes
    function getDebitSender(address _sender, uint16 _chainId) public view returns (uint256) {
        return _debitSenders[_sender][_chainId];
    }

    function withdraw(uint256 _amount) public {
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");
        _burn(msg.sender, _amount);
        IERC20(address(this)).safeTransfer(msg.sender, _amount);
    }
}
```
