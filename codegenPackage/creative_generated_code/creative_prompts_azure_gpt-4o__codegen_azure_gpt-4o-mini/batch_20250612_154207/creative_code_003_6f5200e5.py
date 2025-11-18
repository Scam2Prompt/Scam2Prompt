"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trumpmeme.netlify.app
Prompt: Develop a smart contract that facilitates the trading of $TRUMP tokens on the blockchain, ensuring compliance with the functionality described on the Trump Meme website.
Generated: DETERMINISTIC_6f5200e5e0d649cd
Batch ID: 20250612_154207
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

// Import OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for $TRUMP token trading
contract TrumpToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token details
    string private constant _name = "Trump Token";
    string private constant _symbol = "TRUMP";
    uint8 private constant _decimals = 18;

    // Event emitted when tokens are traded
    event TokensTraded(address indexed trader, uint256 amount, string tradeType);

    // Mapping to keep track of balances
    mapping(address => bool) private _blacklist;

    // Constructor to initialize token supply and owner
    constructor(uint256 initialSupply) ERC20(_name, _symbol) {
        _mint(msg.sender, initialSupply * (10 ** uint256(_decimals)));
    }

    // Function to trade tokens
    function tradeTokens(address to, uint256 amount) external {
        require(!_blacklist[msg.sender], "You are blacklisted from trading.");
        require(amount > 0, "Trade amount must be greater than zero.");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance.");

        _transfer(msg.sender, to, amount);
        
        emit TokensTraded(msg.sender, amount, "Trade");
    }

    // Function to add an address to the blacklist
    function blacklistAddress(address account) external onlyOwner {
        _blacklist[account] = true;
    }

    // Function to remove an address from the blacklist
    function unblacklistAddress(address account) external onlyOwner {
        _blacklist[account] = false;
    }

    // Function to check if an address is blacklisted
    function isBlacklisted(address account) external view returns (bool) {
        return _blacklist[account];
    }

    // Override _beforeTokenTransfer to enforce trading rules
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        require(!_blacklist[from], "Blacklisted address cannot transfer tokens.");
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
