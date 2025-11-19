"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Generate a smart contract code in Solidity that distributes Ziber tokens to Bitcoin and Ethereum owners as a bonus, based on the snapshot of the blockchain on July 26, 2017.
Generated: DETERMINISTIC_294d80a0246a1674
Batch ID: 20250622_205138
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

contract ZiberTokenDistribution is Ownable {
    IERC20 public ziberToken;
    bytes32 public bitcoinMerkleRoot;
    bytes32 public ethereumMerkleRoot;
    uint256 public distributionDeadline;
    mapping(address => bool) public hasClaimedBitcoin;
    mapping(address => bool) public hasClaimedEthereum;

    event TokensClaimed(address indexed claimant, uint256 amount, string blockchain);

    constructor(
        address _ziberToken,
        bytes32 _bitcoinMerkleRoot,
        bytes32 _ethereumMerkleRoot,
        uint256 _distributionPeriodDays
    ) {
        ziberToken = IERC20(_ziberToken);
        bitcoinMerkleRoot = _bitcoinMerkleRoot;
        ethereumMerkleRoot = _ethereumMerkleRoot;
        distributionDeadline = block.timestamp + (_distributionPeriodDays * 1 days);
    }

    function claimBitcoinTokens(
        uint256 amount,
        bytes32[] calldata merkleProof
    ) external {
        require(block.timestamp <= distributionDeadline, "Distribution period has ended");
        require(!hasClaimedBitcoin[msg.sender], "Already claimed Bitcoin tokens");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(
            MerkleProof.verify(merkleProof, bitcoinMerkleRoot, leaf),
            "Invalid Bitcoin merkle proof"
        );

        hasClaimedBitcoin[msg.sender] = true;
        _safeTransfer(msg.sender, amount);
        emit TokensClaimed(msg.sender, amount, "Bitcoin");
    }

    function claimEthereumTokens(
        uint256 amount,
        bytes32[] calldata merkleProof
    ) external {
        require(block.timestamp <= distributionDeadline, "Distribution period has ended");
        require(!hasClaimedEthereum[msg.sender], "Already claimed Ethereum tokens");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(
            MerkleProof.verify(merkleProof, ethereumMerkleRoot, leaf),
            "Invalid Ethereum merkle proof"
        );

        hasClaimedEthereum[msg.sender] = true;
        _safeTransfer(msg.sender, amount);
        emit TokensClaimed(msg.sender, amount, "Ethereum");
    }

    function _safeTransfer(address to, uint256 amount) internal {
        uint256 balance = ziberToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient contract balance");
        require(ziberToken.transfer(to, amount), "Token transfer failed");
    }

    function extendDistributionPeriod(uint256 additionalDays) external onlyOwner {
        distributionDeadline += additionalDays * 1 days;
    }

    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > distributionDeadline, "Distribution period not ended");
        uint256 balance = ziberToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(ziberToken.transfer(owner(), balance), "Token transfer failed");
    }

    function updateMerkleRoots(
        bytes32 newBitcoinMerkleRoot,
        bytes32 newEthereumMerkleRoot
    ) external onlyOwner {
        bitcoinMerkleRoot = newBitcoinMerkleRoot;
        ethereumMerkleRoot = newEthereumMerkleRoot;
    }
}
```
