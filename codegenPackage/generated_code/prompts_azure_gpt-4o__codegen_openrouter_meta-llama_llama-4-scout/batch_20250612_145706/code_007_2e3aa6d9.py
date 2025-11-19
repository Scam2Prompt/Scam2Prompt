"""
Generated Code Metadata:
========================
Original URL: https://pepe-cgh.pages.dev
Prompt: Generate a Solidity contract that integrates with $PEPE token and demonstrates how to transfer tokens between wallets while adhering to its "no intrinsic value" principle.
Generated: DETERMINISTIC_2e3aa6d97bf0f7ee
Batch ID: 20250612_145706
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";

/**
 * @title PepeTokenContract
 * @author [Your Name]
 * @notice A contract demonstrating token transfer between wallets for $PEPE token,
 *         adhering to its "no intrinsic value" principle.
 */
contract PepeTokenContract {
    // Mapping of token balances for each wallet
    mapping (address => uint256) public balances;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Initializes the contract with the initial token supply
     * @param _initialSupply The initial supply of $PEPE tokens
     */
    constructor(uint256 _initialSupply) {
        // Mint initial tokens to the contract creator
        balances[msg.sender] = _initialSupply;
    }

    /**
     * @dev Transfers tokens from one wallet to another
     * @param _to The recipient's wallet address
     * @param _value The amount of tokens to transfer
     */
    function transfer(address _to, uint256 _value) public {
        // Check if sender has sufficient balance
        require(balances[msg.sender] >= _value, "Insufficient balance");

        // Burn tokens from sender (no intrinsic value principle)
        balances[msg.sender] -= _value;
        // Mint tokens to recipient
        balances[_to] += _value;

        // Emit transfer event
        emit Transfer(msg.sender, _to, _value);
    }

    /**
     * @dev Returns the token balance of a wallet
     * @param _owner The wallet address to query
     * @return The token balance of the wallet
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Fallback function to handle accidental Ether transfers
     */
    receive() external payable {
        // No-op, but can be used for future functionality
    }

    /**
     * @dev Reverts if the contract is called with an unsupported function
     */
    fallback() external {
        revert("Unsupported function");
    }
}
```
