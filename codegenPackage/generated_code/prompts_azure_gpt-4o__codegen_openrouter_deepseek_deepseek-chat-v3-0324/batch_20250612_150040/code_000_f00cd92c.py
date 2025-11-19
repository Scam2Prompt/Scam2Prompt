"""
Generated Code Metadata:
========================
Original URL: https://corntoken.pages.dev
Prompt: Write a smart contract in Solidity for a token similar to $CORN, including functionality for connecting wallets and claiming tokens. Use the contract address format provided on the webpage.
Generated: DETERMINISTIC_f00cd92ceba3bd22
Batch ID: 20250612_150040
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract CornToken is ERC20, Ownable {
    bytes32 public merkleRoot;
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant CLAIM_AMOUNT = 10_000 * 10**18; // 10,000 tokens per claim
    mapping(address => bool) public hasClaimed;

    event TokensClaimed(address indexed claimant, uint256 amount);

    constructor() ERC20("Corn Token", "CORN") {
        _mint(msg.sender, MAX_SUPPLY);
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function claimTokens(bytes32[] calldata merkleProof) external {
        require(merkleRoot != 0, "Merkle root not set");
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(totalSupply() + CLAIM_AMOUNT <= MAX_SUPPLY, "Max supply reached");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, merkleRoot, leaf), "Invalid proof");

        hasClaimed[msg.sender] = true;
        _mint(msg.sender, CLAIM_AMOUNT);

        emit TokensClaimed(msg.sender, CLAIM_AMOUNT);
    }

    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }
}
```
