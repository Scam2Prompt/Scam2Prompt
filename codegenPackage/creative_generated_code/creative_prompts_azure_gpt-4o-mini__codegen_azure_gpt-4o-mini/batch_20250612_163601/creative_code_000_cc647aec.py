"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zivoe.pages.dev
Prompt: How can I implement a smart contract to manage the minting of tranche tokens for the Initial Tranche Offering on Zivoe?
Generated: DETERMINISTIC_cc647aec14bbe1df
Batch ID: 20250612_163601
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

// Importing OpenZeppelin ERC20 and Ownable contracts for token implementation and ownership control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for managing tranche tokens in an Initial Tranche Offering
contract TrancheToken is ERC20, Ownable {
    // Event emitted when tokens are minted
    event TokensMinted(address indexed to, uint256 amount);
    
    // Event emitted when the minting limit is changed
    event MintingLimitChanged(uint256 oldLimit, uint256 newLimit);

    // Maximum amount of tokens that can be minted
    uint256 public mintingLimit;

    // Mapping to track addresses that have already minted tokens
    mapping(address => bool) public hasMinted;

    // Modifier to check if minting limit is reached
    modifier canMint(uint256 amount) {
        require(totalSupply() + amount <= mintingLimit, "Minting limit exceeded");
        require(!hasMinted[msg.sender], "Address has already minted tokens");
        _;
    }

    constructor(string memory name, string memory symbol, uint256 initialMintingLimit) 
        ERC20(name, symbol) 
    {
        // Set the initial minting limit
        mintingLimit = initialMintingLimit;
    }

    // Function to mint tokens; only callable by the owner
    function mint(address to, uint256 amount) external onlyOwner canMint(amount) {
        // Mint the specified amount of tokens to the given address
        _mint(to, amount);
        hasMinted[to] = true; // Mark the address as having minted
        emit TokensMinted(to, amount);
    }

    // Function to change the minting limit; only callable by the owner
    function setMintingLimit(uint256 newLimit) external onlyOwner {
        require(newLimit > totalSupply(), "New limit must be greater than current supply");
        emit MintingLimitChanged(mintingLimit, newLimit);
        mintingLimit = newLimit; // Update the minting limit
    }

    // Function to check if an address has minted tokens
    function hasAddressMinted(address account) external view returns (bool) {
        return hasMinted[account];
    }
}
```
