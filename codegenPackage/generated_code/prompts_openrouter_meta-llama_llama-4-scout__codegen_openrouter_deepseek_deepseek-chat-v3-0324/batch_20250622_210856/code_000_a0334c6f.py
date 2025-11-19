"""
Generated Code Metadata:
========================
Original URL: https://airdrop1.org
Prompt: What are the smart contract code implementations for distributing cryptocurrency airdrops, as discussed on airdrop1.org?
Generated: DETERMINISTIC_a0334c6f1b78c420
Batch ID: 20250622_210856
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract AirdropDistributor is Ownable {
    IERC20 public token;
    bytes32 public merkleRoot;
    uint256 public airdropAmount;
    mapping(address => bool) public hasClaimed;

    event AirdropClaimed(address indexed claimant, uint256 amount);
    event MerkleRootUpdated(bytes32 newMerkleRoot);
    event AirdropAmountUpdated(uint256 newAmount);

    constructor(
        IERC20 _token,
        bytes32 _merkleRoot,
        uint256 _airdropAmount
    ) {
        token = _token;
        merkleRoot = _merkleRoot;
        airdropAmount = _airdropAmount;
    }

    function updateMerkleRoot(bytes32 _newMerkleRoot) external onlyOwner {
        merkleRoot = _newMerkleRoot;
        emit MerkleRootUpdated(_newMerkleRoot);
    }

    function updateAirdropAmount(uint256 _newAmount) external onlyOwner {
        airdropAmount = _newAmount;
        emit AirdropAmountUpdated(_newAmount);
    }

    function claimAirdrop(bytes32[] calldata merkleProof) external {
        require(!hasClaimed[msg.sender], "Airdrop already claimed");
        
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "Invalid Merkle proof"
        );

        hasClaimed[msg.sender] = true;
        require(
            token.transfer(msg.sender, airdropAmount),
            "Token transfer failed"
        );

        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(
            token.transfer(owner(), balance),
            "Token transfer failed"
        );
    }
}
```
