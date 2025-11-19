"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Recommend a suitable programming language and libraries for building applications on the Botanix EVM that can seamlessly port from existing EVM environments.
Generated: DETERMINISTIC_580121746aebec3a
Batch ID: 20250622_205751
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

// Import OpenZeppelin contracts for ERC20, ERC721, and other standard implementations
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BotanixEVMCompatibleContract
 * @dev A sample contract demonstrating compatibility with Botanix EVM
 * using Solidity and OpenZeppelin libraries for seamless porting from existing EVM environments
 */
contract BotanixEVMCompatibleContract is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1000000 * 10**18;
    
    constructor() ERC20("BotanixToken", "BTX") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    /**
     * @dev Mint additional tokens (owner only)
     * @param to The address to mint to
     * @param amount The amount to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }

    /**
     * @dev Transfer tokens with additional checks
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     */
    function safeTransfer(address recipient, uint256 amount) public nonReentrant {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        _transfer(msg.sender, recipient, amount);
    }
}

/**
 * @title BotanixNFT
 * @dev An ERC721 NFT contract demonstrating NFT compatibility
 */
contract BotanixNFT is ERC721, Ownable {
    using SafeMath for uint256;

    uint256 public nextTokenId;
    string public baseURI;

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT
     * @param to The address to mint to
     */
    function mint(address to) public onlyOwner {
        _safeMint(to, nextTokenId);
        nextTokenId = nextTokenId.add(1);
    }

    /**
     * @dev Set the base URI for token metadata
     * @param newBaseURI The new base URI
     */
    function setBaseURI(string memory newBaseURI) public onlyOwner {
        baseURI = newBaseURI;
    }

    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
}
```
