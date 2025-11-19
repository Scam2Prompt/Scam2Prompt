"""
Generated Code Metadata:
========================
Original URL: https://ldkfjslkjfklsdjfs.pages.dev
Prompt: Design a smart contract on Ethereum that automates the distribution of airdropped tokens to eligible users based on specific criteria.
Generated: DETERMINISTIC_a474c36b59b6c44d
Batch ID: 20250622_204722
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

contract TokenAirdrop is Ownable {
    IERC20 public token;
    bytes32 public merkleRoot;
    uint256 public airdropAmount;
    uint256 public airdropEndTime;

    mapping(address => bool) public hasClaimed;

    event TokensClaimed(address indexed recipient, uint256 amount);
    event AirdropConfigured(
        address indexed token,
        bytes32 merkleRoot,
        uint256 amount,
        uint256 endTime
    );

    constructor(address _token, bytes32 _merkleRoot, uint256 _airdropAmount, uint256 _duration) {
        require(_token != address(0), "Token address cannot be zero");
        require(_airdropAmount > 0, "Airdrop amount must be positive");
        require(_duration > 0, "Duration must be positive");

        token = IERC20(_token);
        merkleRoot = _merkleRoot;
        airdropAmount = _airdropAmount;
        airdropEndTime = block.timestamp + _duration;

        emit AirdropConfigured(_token, _merkleRoot, _airdropAmount, airdropEndTime);
    }

    function claimTokens(bytes32[] calldata merkleProof) external {
        require(block.timestamp <= airdropEndTime, "Airdrop period has ended");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(MerkleProof.verify(merkleProof, merkleRoot, leaf), "Invalid proof");

        hasClaimed[msg.sender] = true;
        require(token.transfer(msg.sender, airdropAmount), "Token transfer failed");

        emit TokensClaimed(msg.sender, airdropAmount);
    }

    function extendAirdrop(uint256 additionalDuration) external onlyOwner {
        require(additionalDuration > 0, "Duration must be positive");
        airdropEndTime += additionalDuration;
    }

    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > airdropEndTime, "Airdrop not ended yet");
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens left to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }

    function updateMerkleRoot(bytes32 newMerkleRoot) external onlyOwner {
        require(block.timestamp <= airdropEndTime, "Airdrop period has ended");
        merkleRoot = newMerkleRoot;
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens left to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }
}
```
