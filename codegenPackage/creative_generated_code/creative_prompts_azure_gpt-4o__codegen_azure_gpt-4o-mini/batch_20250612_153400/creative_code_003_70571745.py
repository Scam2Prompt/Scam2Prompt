"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Create a smart contract to issue Masa Soulbound Tokens (SBTs) for identity verification and rewards distribution.
Generated: DETERMINISTIC_70571745a3752727
Batch ID: 20250612_153400
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

// Import OpenZeppelin's ERC721 for token standards
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for Masa Soulbound Tokens (SBT)
contract MasaSoulboundToken is ERC721Enumerable, Ownable {
    // Mapping to track users' identity verification status
    mapping(address => bool) private _isVerified;
    
    // Event emitted when a token is issued
    event TokenIssued(address indexed to, uint256 tokenId);
    
    // Event emitted when a user is verified
    event UserVerified(address indexed user);

    // Counter for token IDs
    uint256 private _currentTokenId;

    // Constructor to initialize the token with a name and symbol
    constructor() ERC721("MasaSoulboundToken", "MSBT") {
        _currentTokenId = 0;
    }

    // Function to issue a Soulbound Token to a verified user
    function issueToken(address to) external onlyOwner {
        require(_isVerified[to], "User is not verified.");

        _currentTokenId++;
        _mint(to, _currentTokenId);
        
        emit TokenIssued(to, _currentTokenId);
    }

    // Function to verify a user's identity
    function verifyUser(address user) external onlyOwner {
        require(!_isVerified[user], "User is already verified.");

        _isVerified[user] = true;
        
        emit UserVerified(user);
    }

    // Function to check if a user is verified
    function isVerified(address user) external view returns (bool) {
        return _isVerified[user];
    }

    // Function to get the current token ID (useful for tracking)
    function currentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }

    // Override of the _beforeTokenTransfer method to prevent transfers
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        require(from == address(0), "Soulbound Tokens cannot be transferred.");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
