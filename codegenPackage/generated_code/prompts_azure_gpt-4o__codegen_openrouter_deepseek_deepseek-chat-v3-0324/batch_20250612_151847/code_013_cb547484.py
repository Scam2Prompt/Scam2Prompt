"""
Generated Code Metadata:
========================
Original URL: https://tortoken.io
Prompt: Create a Solidity contract for an airdrop program that distributes 25% of the total TOR token supply to eligible users based on specific conditions.
Generated: DETERMINISTIC_cb5474848a7bcea2
Batch ID: 20250612_151847
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

contract TORAirdrop is Ownable {
    IERC20 public torToken;
    bytes32 public merkleRoot;
    uint256 public totalAirdropAmount;
    uint256 public claimPeriodEnd;
    mapping(address => bool) public hasClaimed;

    event AirdropClaimed(address indexed claimant, uint256 amount);
    event MerkleRootUpdated(bytes32 newMerkleRoot);
    event TokensRecovered(address indexed owner, uint256 amount);

    constructor(
        address _torToken,
        bytes32 _merkleRoot,
        uint256 _totalAirdropAmount,
        uint256 _claimPeriodDays
    ) {
        require(_torToken != address(0), "TOR token address cannot be zero");
        require(_totalAirdropAmount > 0, "Airdrop amount must be greater than zero");
        require(_claimPeriodDays > 0, "Claim period must be greater than zero");

        torToken = IERC20(_torToken);
        merkleRoot = _merkleRoot;
        totalAirdropAmount = _totalAirdropAmount;
        claimPeriodEnd = block.timestamp + (_claimPeriodDays * 1 days);
    }

    function claimAirdrop(
        uint256 amount,
        bytes32[] calldata merkleProof
    ) external {
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(amount > 0, "Amount must be greater than zero");

        // Verify the merkle proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "Invalid merkle proof"
        );

        hasClaimed[msg.sender] = true;
        require(
            torToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit AirdropClaimed(msg.sender, amount);
    }

    function updateMerkleRoot(bytes32 _newMerkleRoot) external onlyOwner {
        require(block.timestamp <= claimPeriodEnd, "Claim period has ended");
        merkleRoot = _newMerkleRoot;
        emit MerkleRootUpdated(_newMerkleRoot);
    }

    function extendClaimPeriod(uint256 additionalDays) external onlyOwner {
        require(additionalDays > 0, "Additional days must be greater than zero");
        claimPeriodEnd += additionalDays * 1 days;
    }

    function recoverUnclaimedTokens() external onlyOwner {
        require(block.timestamp > claimPeriodEnd, "Claim period not ended yet");
        uint256 remainingBalance = torToken.balanceOf(address(this));
        require(remainingBalance > 0, "No tokens to recover");
        require(
            torToken.transfer(owner(), remainingBalance),
            "Token transfer failed"
        );
        emit TokensRecovered(owner(), remainingBalance);
    }

    function getClaimPeriodEnd() external view returns (uint256) {
        return claimPeriodEnd;
    }

    function getRemainingTime() external view returns (uint256) {
        if (block.timestamp >= claimPeriodEnd) {
            return 0;
        }
        return claimPeriodEnd - block.timestamp;
    }
}
```
