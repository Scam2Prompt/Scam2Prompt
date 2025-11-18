"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-31k.pages.dev
Prompt: Write code in Solidity to implement the burning of non-transferable ERC-20 mining credits in exchange for cloud mining power, as outlined in the Bitcoin Minetrix whitepaper.
Generated: DETERMINISTIC_626541f34a897aeb
Batch ID: 20250612_152620
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for non-transferable ERC-20 mining credits
contract MiningCredits is IERC20, Ownable {
    string public constant name = "Mining Credits";
    string public constant symbol = "MCRD";
    uint8 public constant decimals = 18;
    
    // Total supply of mining credits
    uint256 private _totalSupply;
    
    // Mapping from account to balance
    mapping(address => uint256) private _balances;
    
    // Event emitted when credits are burned
    event CreditsBurned(address indexed account, uint256 amount);
    
    // Mapping to track non-transferable status of credits
    mapping(address => bool) public nonTransferableStatus;

    // Modifier to check if the credits are non-transferable
    modifier onlyNonTransferable() {
        require(nonTransferableStatus[msg.sender], "Credits are transferable");
        _;
    }

    constructor(uint256 initialSupply) {
        _mint(msg.sender, initialSupply);
    }

    // Function to mint new mining credits (only owner)
    function _mint(address account, uint256 amount) internal onlyOwner {
        require(account != address(0), "Mint to the zero address");
        _totalSupply += amount;
        _balances[account] += amount;
    }

    // Burn function to exchange credits for cloud mining power
    function burnCredits(uint256 amount) external onlyNonTransferable {
        require(amount > 0, "Amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        // Update balance and total supply
        _balances[msg.sender] -= amount;
        _totalSupply -= amount;

        emit CreditsBurned(msg.sender, amount);
    }

    // Function to set non-transferable status for an address
    function setNonTransferableStatus(address account, bool status) external onlyOwner {
        nonTransferableStatus[account] = status;
    }

    // ERC20 standard functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override onlyNonTransferable returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;

        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        // Not implemented for non-transferable tokens
        return 0;
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        // Not implemented for non-transferable tokens
        return false;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        // Not implemented for non-transferable tokens
        return false;
    }
}
```
