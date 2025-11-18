"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a Solidity implementation of an Omnichain Fungible Token (OFT) using LayerZero's `OFTCore` interface. Ensure the contract supports cross-chain token transfers without asset wrapping.
Generated: DETERMINISTIC_19817a65aa34052b
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

// Import the LayerZero OFTCore interface
import "@layerzerolabs/contracts/interfaces/OFTCore.sol";

// An implementation of an Omnichain Fungible Token (OFT) using LayerZero's OFTCore interface
contract MyOmnichainToken is OFTCore {
    // Mapping to track balances of each account
    mapping(address => uint256) private balances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Token name and symbol
    string public name;
    string public symbol;

    // Emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the token
    constructor(string memory _name, string memory _symbol, uint256 initialSupply) OFTCore() {
        name = _name;
        symbol = _symbol;
        _mint(msg.sender, initialSupply);
    }

    // Function to mint new tokens
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "Mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _totalSupply += amount;
        balances[account] += amount;

        emit Transfer(address(0), account, amount);
    }

    // Function to transfer tokens to another address
    function transfer(address to, uint256 amount) external returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // Function to get the balance of an account
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    // Function to get the total supply of the token
    function totalSupply() external view returns (uint256) {
        return _totalSupply;
    }

    // Function to support cross-chain token transfers
    function _crossChainTransfer(address to, uint256 amount) internal {
        require(balances[msg.sender] >= amount, "Insufficient balance for cross-chain transfer");
        balances[msg.sender] -= amount;

        // Logic to transfer tokens across chains using LayerZero
        // This is a placeholder for integration with LayerZero
        // require(LayerZero.send(to, amount), "Cross-chain transfer failed");

        emit Transfer(msg.sender, to, amount);
    }

    // Function to handle receiving tokens from other chains
    function _receiveTokens(address from, uint256 amount) internal {
        require(from != address(0), "Receive from the zero address");
        require(amount > 0, "Receive amount must be greater than zero");

        balances[from] += amount;
        _totalSupply += amount;

        emit Transfer(from, address(this), amount); // Emit an event for the receipt
    }

    // Additional functions can be implemented as needed, e.g., for approvals and allowances
}
```
