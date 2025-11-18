"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Generate a Solidity contract that includes a whitelist mechanism for early supporters of an NFT project, similar to the Prime Ape Planet whitelist.
Generated: DETERMINISTIC_27a66fdf9a99734f
Batch ID: 20250612_151659
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

// Importing the ERC721 standard interface
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the NFT with a whitelist mechanism
contract WhitelistNFT is ERC721Enumerable, Ownable {
    // Mapping to store whitelisted addresses
    mapping(address => bool) private _whitelist;

    // Counter for the token IDs
    uint256 private _currentTokenId;

    // Event to emit when an address is added to the whitelist
    event Whitelisted(address indexed account);
    // Event to emit when an address is removed from the whitelist
    event Unwhitelisted(address indexed account);

    // Constructor to initialize the NFT with a name and symbol
    constructor() ERC721("WhitelistNFT", "WLNFT") {}

    // Modifier to check if an address is whitelisted
    modifier onlyWhitelisted() {
        require(_whitelist[msg.sender], "Not whitelisted");
        _;
    }

    // Function to add an address to the whitelist
    function addToWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        require(!_whitelist[account], "Already whitelisted");

        _whitelist[account] = true;
        emit Whitelisted(account);
    }

    // Function to remove an address from the whitelist
    function removeFromWhitelist(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        require(_whitelist[account], "Not whitelisted");

        delete _whitelist[account];
        emit Unwhitelisted(account);
    }

    // Function to check if an address is whitelisted
    function isWhitelisted(address account) external view returns (bool) {
        return _whitelist[account];
    }

    // Function to mint a new NFT, only callable by whitelisted addresses
    function mint() external onlyWhitelisted {
        _currentTokenId++;
        _safeMint(msg.sender, _currentTokenId);
    }
}
```
