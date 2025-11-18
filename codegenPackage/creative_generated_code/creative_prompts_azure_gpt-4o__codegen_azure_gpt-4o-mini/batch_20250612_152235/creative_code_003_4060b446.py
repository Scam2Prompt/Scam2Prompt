"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepe-claims.pages.dev
Prompt: Create an example of an ERC-20 token contract similar to $PEPE, including tokenomics features like airdrops.
Generated: DETERMINISTIC_4060b446cb172b02
Batch ID: 20250612_152235
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

// Importing the OpenZeppelin ERC20 Token Standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PepeToken is ERC20, Ownable {
    // Token details
    string private constant _name = "Pepe Token";
    string private constant _symbol = "PEPE";
    uint8 private constant _decimals = 18;
    
    // Airdrop configuration
    uint256 public airdropAmount;
    mapping(address => bool) public airdropClaimed;

    // Events
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to initialize the token supply and airdrop amount
    constructor(uint256 initialSupply, uint256 _airdropAmount) ERC20(_name, _symbol) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        require(_airdropAmount > 0, "Airdrop amount must be greater than zero");
        
        _mint(msg.sender, initialSupply * (10 ** uint256(_decimals))); // Mint initial supply to the deployer
        airdropAmount = _airdropAmount * (10 ** uint256(_decimals)); // Set airdrop amount
    }

    // Function to airdrop tokens to a list of addresses
    function airdropTokens(address[] calldata recipients) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            require(!airdropClaimed[recipients[i]], "Airdrop already claimed by this address");
            require(recipients[i] != address(0), "Invalid address");

            airdropClaimed[recipients[i]] = true; // Mark as claimed
            _transfer(owner(), recipients[i], airdropAmount); // Transfer airdrop amount
            emit Airdrop(recipients[i], airdropAmount);
        }
    }

    // Function to check if an address has claimed the airdrop
    function hasClaimedAirdrop(address account) external view returns (bool) {
        return airdropClaimed[account];
    }

    // Override the transfer function to include custom logic (if any)
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _transfer(msg.sender, recipient, amount);
        return true;
    }

    // Override the transferFrom function to include custom logic (if any)
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balanceOf(sender) >= amount, "Insufficient balance");
        
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);
        return true;
    }
}
```
