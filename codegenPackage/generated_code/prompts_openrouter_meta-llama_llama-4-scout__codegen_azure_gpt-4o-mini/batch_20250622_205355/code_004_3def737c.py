"""
Generated Code Metadata:
========================
Original URL: https://arbidoge.pages.dev
Prompt: Design a simple buy, sell, and transfer contract for a meme token with no taxes, inspired by Arbidoge's contract structure.
Generated: DETERMINISTIC_3def737c1bf8df91
Batch ID: 20250622_205355
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

// MemeToken contract inherits from ERC20 and Ownable
contract MemeToken is ERC20, Ownable {
    // Mapping to keep track of balances for each address
    mapping(address => bool) private _isExcludedFromFees;

    // Events for buy, sell, and transfer actions
    event Buy(address indexed buyer, uint256 amount);
    event Sell(address indexed seller, uint256 amount);
    event Transfer(address indexed from, address indexed to, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("MemeToken", "MEME") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals());
        // Exclude the deployer from fees
        _isExcludedFromFees[msg.sender] = true;
    }

    // Function to buy tokens
    function buy(uint256 amount) external payable {
        require(msg.value > 0, "Must send ETH to buy tokens");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens to the buyer
        _transfer(owner(), msg.sender, amount);
        emit Buy(msg.sender, amount);
    }

    // Function to sell tokens
    function sell(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the seller to the contract
        _transfer(msg.sender, owner(), amount);
        // Transfer ETH to the seller
        payable(msg.sender).transfer(amount); // Assuming 1 token = 1 ETH for simplicity
        emit Sell(msg.sender, amount);
    }

    // Override the transfer function to include event emission
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        emit Transfer(_msgSender(), recipient, amount);
        return true;
    }

    // Override the transferFrom function to include event emission
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // Function to exclude an address from fees
    function excludeFromFees(address account) external onlyOwner {
        _isExcludedFromFees[account] = true;
    }

    // Function to include an address back to fees
    function includeInFees(address account) external onlyOwner {
        _isExcludedFromFees[account] = false;
    }

    // Function to check if an address is excluded from fees
    function isExcludedFromFees(address account) external view returns (bool) {
        return _isExcludedFromFees[account];
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
