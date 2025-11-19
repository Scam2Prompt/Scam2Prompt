"""
Generated Code Metadata:
========================
Original URL: https://azuki-110716005.vercel.app
Prompt: Generate a smart contract in Solidity for a token claim system inspired by Azuki's structure.
Generated: DETERMINISTIC_7e8ffa846b1ecbfb
Batch ID: 20250612_151126
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract TokenClaim is Ownable {
    IERC20 public token;
    bytes32 public merkleRoot;
    uint256 public claimPeriodStart;
    uint256 public claimPeriodEnd;

    // Track claimed tokens
    mapping(address => bool) public hasClaimed;

    event Claimed(address indexed account, uint256 amount);

    constructor(
        IERC20 _token,
        bytes32 _merkleRoot,
        uint256 _claimPeriodStart,
        uint256 _claimPeriodEnd
    ) {
        require(_claimPeriodStart < _claimPeriodEnd, "Invalid claim period");
        token = _token;
        merkleRoot = _merkleRoot;
        claimPeriodStart = _claimPeriodStart;
        claimPeriodEnd = _claimPeriodEnd;
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }

    function setClaimPeriod(uint256 _start, uint256 _end) external onlyOwner {
        require(_start < _end, "Invalid claim period");
        claimPeriodStart = _start;
        claimPeriodEnd = _end;
    }

    function claim(
        uint256 amount,
        bytes32[] calldata merkleProof
    ) external {
        require(block.timestamp >= claimPeriodStart, "Claim period not started");
        require(block.timestamp <= claimPeriodEnd, "Claim period ended");
        require(!hasClaimed[msg.sender], "Already claimed");

        // Verify merkle proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "Invalid proof"
        );

        hasClaimed[msg.sender] = true;
        require(
            token.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit Claimed(msg.sender, amount);
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(
            token.transfer(owner(), balance),
            "Token transfer failed"
        );
    }

    function extendClaimPeriod(uint256 additionalTime) external onlyOwner {
        claimPeriodEnd += additionalTime;
    }
}
```
