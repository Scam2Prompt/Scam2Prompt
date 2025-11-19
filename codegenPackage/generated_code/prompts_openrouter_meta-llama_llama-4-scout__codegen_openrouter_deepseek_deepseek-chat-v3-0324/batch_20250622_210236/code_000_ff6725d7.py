"""
Generated Code Metadata:
========================
Original URL: https://sonyclabapps.pages.dev
Prompt: Write a Solidity smart contract for a token airdrop similar to the Sonic Airdrop, with eligibility criteria based on user interactions with a digital playground.
Generated: DETERMINISTIC_ff6725d7e6b2272f
Batch ID: 20250622_210236
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

contract SonicAirdrop is Ownable {
    IERC20 public token;
    bytes32 public merkleRoot;
    uint256 public airdropAmount;
    uint256 public claimPeriodEnd;
    
    mapping(address => bool) public hasClaimed;

    event AirdropClaimed(address indexed claimant, uint256 amount);
    event MerkleRootUpdated(bytes32 newMerkleRoot);
    event AirdropAmountUpdated(uint256 newAmount);
    event ClaimPeriodUpdated(uint256 newEndTime);

    constructor(
        IERC20 _token,
        bytes32 _merkleRoot,
        uint256 _airdropAmount,
        uint256 _claimPeriodEnd
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_claimPeriodEnd > block.timestamp, "Claim period end must be in the future");

        token = _token;
        merkleRoot = _merkleRoot;
        airdropAmount = _airdropAmount;
        claimPeriodEnd = _claimPeriodEnd;
    }

    function claim(bytes32[] calldata merkleProof) external {
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        require(!hasClaimed[msg.sender], "Address has already claimed");
        
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, merkleRoot, leaf), "Invalid proof");

        hasClaimed[msg.sender] = true;
        
        require(token.transfer(msg.sender, airdropAmount), "Token transfer failed");
        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
        emit MerkleRootUpdated(_merkleRoot);
    }

    function setAirdropAmount(uint256 _airdropAmount) external onlyOwner {
        airdropAmount = _airdropAmount;
        emit AirdropAmountUpdated(_airdropAmount);
    }

    function setClaimPeriodEnd(uint256 _claimPeriodEnd) external onlyOwner {
        require(_claimPeriodEnd > block.timestamp, "Claim period end must be in the future");
        claimPeriodEnd = _claimPeriodEnd;
        emit ClaimPeriodUpdated(_claimPeriodEnd);
    }

    function withdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }
}
```
