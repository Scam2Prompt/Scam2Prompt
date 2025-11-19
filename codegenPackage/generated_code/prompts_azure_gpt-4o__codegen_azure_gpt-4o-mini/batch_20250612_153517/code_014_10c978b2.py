"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Create a Solidity contract for multi-chain compatibility of $HEHE tokens, ensuring seamless transactions across Ethereum and Binance Smart Chain.
Generated: DETERMINISTIC_10c978b2929ffa0e
Batch ID: 20250612_153517
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MultiChainToken is an ERC20 token that supports multi-chain compatibility
contract MultiChainToken is ERC20, Ownable {
    // Mapping to track the balances of users on different chains
    mapping(address => mapping(uint256 => uint256)) private _balances;

    // Event emitted when tokens are transferred across chains
    event CrossChainTransfer(address indexed from, address indexed to, uint256 amount, uint256 targetChainId);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("HEHE Token", "HEHE") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to transfer tokens to another address on the same chain
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        // Ensure the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        // Call the parent transfer function
        super.transfer(recipient, amount);
        return true;
    }

    // Function to handle cross-chain transfers
    function transferToChain(address recipient, uint256 amount, uint256 targetChainId) external returns (bool) {
        // Ensure the sender has enough balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        // Burn the tokens on the current chain
        _burn(msg.sender, amount);
        // Emit an event for the cross-chain transfer
        emit CrossChainTransfer(msg.sender, recipient, amount, targetChainId);
        return true;
    }

    // Function to mint new tokens (only owner can mint)
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }

    // Function to burn tokens (only owner can burn)
    function burn(uint256 amount) external onlyOwner {
        _burn(msg.sender, amount);
    }

    // Function to check the balance of a user on a specific chain
    function balanceOnChain(address account, uint256 chainId) external view returns (uint256) {
        return _balances[account][chainId];
    }

    // Function to update the balance of a user on a specific chain (for cross-chain operations)
    function updateBalanceOnChain(address account, uint256 chainId, uint256 amount) external onlyOwner {
        _balances[account][chainId] = amount;
    }
}
```
