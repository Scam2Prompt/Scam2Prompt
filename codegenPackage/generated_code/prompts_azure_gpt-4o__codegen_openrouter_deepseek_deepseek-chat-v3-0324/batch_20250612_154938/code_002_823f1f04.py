"""
Generated Code Metadata:
========================
Original URL: https://gorodshansona.ru
Prompt: Provide an example of a smart contract that integrates Immutable X's zero-knowledge proof technology for scaling NFT transactions, referencing the details from gorodshansona.ru.
Generated: DETERMINISTIC_823f1f04304b359b
Batch ID: 20250612_154938
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

import "@imtbl/imx-contracts/contracts/IMintable.sol";
import "@imtbl/imx-contracts/contracts/utils/Minting.sol";

/**
 * @title IMXNFTContract
 * @dev NFT contract integrated with Immutable X for zk-rollup scaling
 * @notice This contract implements IMintable interface for Immutable X integration
 * Reference: gorodshansona.ru
 */
contract IMXNFTContract is IMintable {
    // Contract owner
    address public owner;

    // Token details
    string public name;
    string public symbol;
    uint256 public tokenCounter;

    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;

    // Mapping from owner address to token count
    mapping(address => uint256) private _balances;

    // Event emitted when a token is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    // Modifier to restrict function access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor function
     * @param _name Name of the NFT collection
     * @param _symbol Symbol of the NFT collection
     */
    constructor(string memory _name, string memory _symbol) {
        owner = msg.sender;
        name = _name;
        symbol = _symbol;
        tokenCounter = 0;
    }

    /**
     * @dev Mints a new NFT (only callable by owner)
     * @param to Address to mint the NFT to
     * @param quantity Number of NFTs to mint
     */
    function mint(address to, uint256 quantity) external onlyOwner {
        for (uint256 i = 0; i < quantity; i++) {
            tokenCounter++;
            _mint(to, tokenCounter);
        }
    }

    /**
     * @dev Implementation of IMintable interface for Immutable X
     * @param to Address to mint the NFT to
     * @param quantity Number of NFTs to mint
     * @param mintingBlob Blob containing minting data (encoded according to IMX standards)
     */
    function mintFor(
        address to,
        uint256 quantity,
        bytes calldata mintingBlob
    ) external override {
        // Only Immutable X can call this function
        require(msg.sender == 0x5FDCCA53617f4d2b9134B29090C87D01058e27e9, "Function can only be called by Immutable X");

        // Decode the minting blob
        (uint256[] memory tokenIds, ) = Minting.decode(mintingBlob);

        require(tokenIds.length == quantity, "Invalid token IDs length");

        for (uint256 i = 0; i < quantity; i++) {
            _mint(to, tokenIds[i]);
        }
    }

    /**
     * @dev Internal mint function
     * @param to Address to mint the NFT to
     * @param tokenId ID of the token to mint
     */
    function _mint(address to, uint256 tokenId) internal {
        require(to != address(0), "Mint to the zero address");
        require(_owners[tokenId] == address(0), "Token already minted");

        _balances[to] += 1;
        _owners[tokenId] = to;

        emit Minted(to, tokenId);
    }

    /**
     * @dev Returns the owner of a token
     * @param tokenId ID of the token
     * @return Address of the token owner
     */
    function ownerOf(uint256 tokenId) public view returns (address) {
        address owner_ = _owners[tokenId];
        require(owner_ != address(0), "Owner query for nonexistent token");
        return owner_;
    }

    /**
     * @dev Returns the balance of an address
     * @param _owner Address to query
     * @return Number of tokens owned by the address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        require(_owner != address(0), "Balance query for the zero address");
        return _balances[_owner];
    }

    /**
     * @dev Transfers ownership of the contract to a new address
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        owner = newOwner;
    }
}
```
