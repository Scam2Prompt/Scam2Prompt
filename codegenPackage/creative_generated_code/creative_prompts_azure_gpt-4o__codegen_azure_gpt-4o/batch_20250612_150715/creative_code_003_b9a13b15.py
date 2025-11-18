"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Write code to mint a soulbound Moxie Pass required for participating in Farcaster auctions. Ensure the minting process adheres to the protocol's requirements.
Generated: DETERMINISTIC_b9a13b15513635ca
Batch ID: 20250612_150715
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

/**
 * @title MoxiePass
 * @dev A Soulbound Token (SBT) implementation for minting Moxie Passes
 *      required for participating in Farcaster auctions.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MoxiePass is ERC721Enumerable, Ownable {
    // Soulbound mapping to prevent token transfers
    mapping(uint256 => bool) private _soulboundTokens;

    // Event emitted when a Moxie Pass is minted
    event MoxiePassMinted(address indexed owner, uint256 indexed tokenId);

    // Constructor to initialize the contract
    constructor() ERC721("MoxiePass", "MXP") {}

    /**
     * @dev Mint a new soulbound Moxie Pass.
     * @param recipient The address receiving the Moxie Pass.
     */
    function mintMoxiePass(address recipient) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");
        
        // Generate a new tokenId
        uint256 tokenId = totalSupply() + 1;

        // Mint the token and make it soulbound
        _mint(recipient, tokenId);
        _soulboundTokens[tokenId] = true;

        emit MoxiePassMinted(recipient, tokenId);
    }

    /**
     * @dev Override transfer functions to enforce soulbound behavior.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(from == address(0) || to == address(0), "Moxie Pass is soulbound and cannot be transferred");
        super._beforeTokenTransfer(from, to, tokenId);
    }

    /**
     * @dev Prevent approvals to ensure soulbound behavior.
     */
    function approve(address, uint256) public override {
        revert("Approval is disabled for soulbound tokens");
    }

    function setApprovalForAll(address, bool) public override {
        revert("Approval for all is disabled for soulbound tokens");
    }

    /**
     * @dev Check if a token is soulbound.
     * @param tokenId The token ID to check.
     */
    function isSoulbound(uint256 tokenId) public view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _soulboundTokens[tokenId];
    }
}
```
