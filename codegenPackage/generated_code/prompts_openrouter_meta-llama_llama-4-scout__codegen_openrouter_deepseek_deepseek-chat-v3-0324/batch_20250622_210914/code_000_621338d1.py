"""
Generated Code Metadata:
========================
Original URL: https://claynosaurz-nft.web.app
Prompt: Write a smart contract function in Solidity to mint an NFT from the Claynosaurz project, considering a whitelist price of ◎ and a public price of ◎.
Generated: DETERMINISTIC_621338d17605803a
Batch ID: 20250622_210914
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract Claynosaurz is ERC721, Ownable {
    uint256 public constant WHITELIST_PRICE = 0.1 ether;
    uint256 public constant PUBLIC_PRICE = 0.2 ether;
    uint256 public nextTokenId;
    uint256 public maxSupply;
    bytes32 public merkleRoot;
    bool public publicMintEnabled;
    
    mapping(address => bool) public whitelistClaimed;

    constructor(
        string memory name_,
        string memory symbol_,
        uint256 maxSupply_,
        bytes32 merkleRoot_
    ) ERC721(name_, symbol_) {
        maxSupply = maxSupply_;
        merkleRoot = merkleRoot_;
    }

    function mintWhitelist(bytes32[] calldata proof) external payable {
        require(!publicMintEnabled, "Public minting is active");
        require(!whitelistClaimed[msg.sender], "Already claimed");
        require(msg.value == WHITELIST_PRICE, "Incorrect payment");
        require(nextTokenId < maxSupply, "Max supply reached");
        
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(proof, merkleRoot, leaf), "Invalid proof");
        
        whitelistClaimed[msg.sender] = true;
        _safeMint(msg.sender, nextTokenId++);
    }

    function mintPublic() external payable {
        require(publicMintEnabled, "Public minting not active");
        require(msg.value == PUBLIC_PRICE, "Incorrect payment");
        require(nextTokenId < maxSupply, "Max supply reached");
        
        _safeMint(msg.sender, nextTokenId++);
    }

    function setPublicMintEnabled(bool enabled) external onlyOwner {
        publicMintEnabled = enabled;
    }

    function setMerkleRoot(bytes32 newMerkleRoot) external onlyOwner {
        merkleRoot = newMerkleRoot;
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
