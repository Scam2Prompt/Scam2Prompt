"""
Generated Code Metadata:
========================
Original URL: https://optimisms.xyz
Prompt: Generate an example of how to implement instant domain transfer between wallets using 3DNS and Optimism.
Generated: DETERMINISTIC_4f8fd7ad98d7fffa
Batch ID: 20250622_205158
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title DomainTransfer
 * @dev Implements instant domain transfer between wallets using 3DNS and Optimism
 */
contract DomainTransfer is IERC721Receiver, Ownable {
    using Address for address;

    // 3DNS NFT contract address
    address public dnsNFTContract;

    // Mapping from token ID to owner address
    mapping(uint256 => address) private _tokenOwners;

    // Mapping owner address to token count
    mapping(address => uint256) private _balances;

    event DomainTransferred(
        address indexed from,
        address indexed to,
        uint256 indexed tokenId
    );

    /**
     * @dev Initializes the contract with the 3DNS NFT contract address
     * @param _dnsNFTContract Address of the 3DNS NFT contract
     */
    constructor(address _dnsNFTContract) {
        require(
            _dnsNFTContract != address(0),
            "DomainTransfer: invalid NFT contract address"
        );
        dnsNFTContract = _dnsNFTContract;
    }

    /**
     * @dev Transfers domain ownership instantly
     * @param to The address to transfer the domain to
     * @param tokenId The ID of the domain NFT to transfer
     */
    function transferDomain(address to, uint256 tokenId) external {
        require(to != address(0), "DomainTransfer: transfer to zero address");
        require(
            IERC721(dnsNFTContract).ownerOf(tokenId) == msg.sender,
            "DomainTransfer: sender is not owner"
        );

        // Transfer NFT through 3DNS contract
        IERC721(dnsNFTContract).safeTransferFrom(msg.sender, to, tokenId);

        // Update internal mappings
        _transfer(msg.sender, to, tokenId);

        emit DomainTransferred(msg.sender, to, tokenId);
    }

    /**
     * @dev Internal function to transfer ownership of a domain
     * @param from Current owner address
     * @param to New owner address
     * @param tokenId Domain NFT ID
     */
    function _transfer(
        address from,
        address to,
        uint256 tokenId
    ) internal {
        require(
            _tokenOwners[tokenId] == from,
            "DomainTransfer: transfer of token that is not own"
        );

        _balances[from] -= 1;
        _balances[to] += 1;
        _tokenOwners[tokenId] = to;

        emit DomainTransferred(from, to, tokenId);
    }

    /**
     * @dev Handles the receipt of an ERC721 token
     */
    function onERC721Received(
        address,
        address from,
        uint256 tokenId,
        bytes calldata
    ) external override returns (bytes4) {
        require(
            msg.sender == dnsNFTContract,
            "DomainTransfer: received NFT from unapproved contract"
        );

        // Update ownership mapping
        _tokenOwners[tokenId] = from;
        _balances[from] += 1;

        return this.onERC721Received.selector;
    }

    /**
     * @dev Returns the owner of a domain
     * @param tokenId Domain NFT ID
     * @return Owner address
     */
    function ownerOf(uint256 tokenId) public view returns (address) {
        address owner = _tokenOwners[tokenId];
        require(
            owner != address(0),
            "DomainTransfer: owner query for nonexistent token"
        );
        return owner;
    }

    /**
     * @dev Returns the balance of domains for an address
     * @param owner Address to query
     * @return Number of domains owned
     */
    function balanceOf(address owner) public view returns (uint256) {
        require(
            owner != address(0),
            "DomainTransfer: balance query for zero address"
        );
        return _balances[owner];
    }
}
```
