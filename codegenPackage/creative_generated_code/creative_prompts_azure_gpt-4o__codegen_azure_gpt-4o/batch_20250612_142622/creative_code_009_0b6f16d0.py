"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.fuckopensea.art
Prompt: Develop a smart contract feature that prevents the use of OpenSea for trading NFTs, while allowing other marketplaces like Blur or Looks Rare, as discussed on the "Fuck OpenSea" website.
Generated: DETERMINISTIC_0b6f16d0e14691e3
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title AntiOpenSeaNFT
 * @dev Smart contract for minting NFTs with a restriction on trading via OpenSea marketplace.
 */
contract AntiOpenSeaNFT {
    // Token properties
    string public name = "AntiOpenSeaNFT";
    string public symbol = "AOSNFT";
    uint256 public totalSupply;

    // Owner of the contract
    address public owner;

    // Mapping for NFT ownership
    mapping(uint256 => address) private _owners;

    // Mapping for approved marketplaces
    mapping(address => bool) public approvedMarketplaces;

    // Event declarations
    event Mint(address indexed to, uint256 indexed tokenId);
    event MarketplaceApprovalUpdated(address indexed marketplace, bool approved);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor setting the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Mint a new NFT.
     * @param to Address of the token recipient.
     * @param tokenId Unique ID of the token.
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(_owners[tokenId] == address(0), "Token already minted");

        _owners[tokenId] = to;
        totalSupply++;
        emit Mint(to, tokenId);
    }

    /**
     * @dev Update marketplace approval status.
     * @param marketplace Address of the marketplace.
     * @param approved Boolean status of approval (true or false).
     */
    function updateMarketplaceApproval(address marketplace, bool approved) external onlyOwner {
        require(marketplace != address(0), "Invalid marketplace address");
        approvedMarketplaces[marketplace] = approved;
        emit MarketplaceApprovalUpdated(marketplace, approved);
    }

    /**
     * @dev Restrict trading on OpenSea.
     * @param operator Address attempting to transfer the NFT.
     * @return bool indicating approval status.
     */
    function isApprovedOperator(address operator) public view returns (bool) {
        return approvedMarketplaces[operator];
    }

    /**
     * @dev Transfer function adhering to marketplace restrictions.
     * @param from Address of the current token owner.
     * @param to Address of the token recipient.
     * @param tokenId ID of the token to transfer.
     */
    function transferFrom(address from, address to, uint256 tokenId) external {
        require(from != address(0) && to != address(0), "Invalid address");
        require(_owners[tokenId] == from, "Caller is not the token owner");
        require(isApprovedOperator(msg.sender), "Marketplace not approved");

        _owners[tokenId] = to;
    }

    /**
     * @dev Retrieve the owner of an NFT.
     * @param tokenId ID of the token.
     * @return Address of the token owner.
     */
    function ownerOf(uint256 tokenId) external view returns (address) {
        return _owners[tokenId];
    }
}
```
