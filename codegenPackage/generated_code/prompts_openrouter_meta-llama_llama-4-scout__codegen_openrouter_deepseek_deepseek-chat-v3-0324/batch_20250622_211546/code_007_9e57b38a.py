"""
Generated Code Metadata:
========================
Original URL: https://dappchainserver.pages.dev
Prompt: Design a smart contract for a multi-chain airdrop platform like TrustPad, focusing on security and scalability.
Generated: DETERMINISTIC_9e57b38ab82a00b9
Batch ID: 20250622_211546
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

/**
 * @title MultiChainAirdrop
 * @dev A secure and scalable multi-chain airdrop platform contract
 */
contract MultiChainAirdrop is Ownable, ReentrancyGuard {
    struct Airdrop {
        address tokenAddress;
        bytes32 merkleRoot;
        uint256 totalAmount;
        uint256 claimedAmount;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    mapping(uint256 => Airdrop) public airdrops;
    mapping(uint256 => mapping(address => bool)) public hasClaimed;
    uint256 public airdropCount;

    event AirdropCreated(
        uint256 indexed airdropId,
        address indexed tokenAddress,
        bytes32 merkleRoot,
        uint256 totalAmount,
        uint256 startTime,
        uint256 endTime
    );
    event TokensClaimed(
        uint256 indexed airdropId,
        address indexed recipient,
        uint256 amount
    );
    event AirdropCancelled(uint256 indexed airdropId);
    event TokensWithdrawn(address indexed token, uint256 amount);

    /**
     * @dev Create a new airdrop
     * @param tokenAddress Address of the token to be airdropped
     * @param merkleRoot Merkle root of the airdrop distribution
     * @param totalAmount Total amount of tokens to be distributed
     * @param startTime When the airdrop becomes claimable
     * @param endTime When the airdrop stops being claimable
     */
    function createAirdrop(
        address tokenAddress,
        bytes32 merkleRoot,
        uint256 totalAmount,
        uint256 startTime,
        uint256 endTime
    ) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(endTime > startTime, "Invalid time range");
        require(totalAmount > 0, "Amount must be positive");

        uint256 airdropId = airdropCount++;
        airdrops[airdropId] = Airdrop({
            tokenAddress: tokenAddress,
            merkleRoot: merkleRoot,
            totalAmount: totalAmount,
            claimedAmount: 0,
            startTime: startTime,
            endTime: endTime,
            isActive: true
        });

        IERC20 token = IERC20(tokenAddress);
        require(
            token.transferFrom(msg.sender, address(this), totalAmount),
            "Token transfer failed"
        );

        emit AirdropCreated(
            airdropId,
            tokenAddress,
            merkleRoot,
            totalAmount,
            startTime,
            endTime
        );
    }

    /**
     * @dev Claim tokens from an airdrop
     * @param airdropId ID of the airdrop to claim from
     * @param amount Amount of tokens to claim
     * @param merkleProof Merkle proof for the claim
     */
    function claimTokens(
        uint256 airdropId,
        uint256 amount,
        bytes32[] calldata merkleProof
    ) external nonReentrant {
        Airdrop storage airdrop = airdrops[airdropId];
        require(airdrop.isActive, "Airdrop not active");
        require(block.timestamp >= airdrop.startTime, "Airdrop not started");
        require(block.timestamp <= airdrop.endTime, "Airdrop ended");
        require(!hasClaimed[airdropId][msg.sender], "Already claimed");
        require(amount > 0, "Amount must be positive");

        bytes32 leaf = keccak256(abi.encodePacked(msg.sender, amount));
        require(
            MerkleProof.verify(merkleProof, airdrop.merkleRoot, leaf),
            "Invalid proof"
        );

        hasClaimed[airdropId][msg.sender] = true;
        airdrop.claimedAmount += amount;

        IERC20 token = IERC20(airdrop.tokenAddress);
        require(
            token.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensClaimed(airdropId, msg.sender, amount);
    }

    /**
     * @dev Cancel an airdrop and return remaining tokens to owner
     * @param airdropId ID of the airdrop to cancel
     */
    function cancelAirdrop(uint256 airdropId) external onlyOwner {
        Airdrop storage airdrop = airdrops[airdropId];
        require(airdrop.isActive, "Airdrop not active");

        airdrop.isActive = false;
        uint256 remainingAmount = airdrop.totalAmount - airdrop.claimedAmount;

        if (remainingAmount > 0) {
            IERC20 token = IERC20(airdrop.tokenAddress);
            require(
                token.transfer(owner(), remainingAmount),
                "Token transfer failed"
            );
        }

        emit AirdropCancelled(airdropId);
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to the contract
     * @param tokenAddress Address of the token to withdraw
     */
    function withdrawTokens(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        
        IERC20 token = IERC20(tokenAddress);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");

        require(
            token.transfer(owner(), balance),
            "Token transfer failed"
        );

        emit TokensWithdrawn(tokenAddress, balance);
    }

    /**
     * @dev Check if a user has claimed from a specific airdrop
     * @param airdropId ID of the airdrop
     * @param user Address of the user
     * @return bool Whether the user has claimed
     */
    function hasUserClaimed(uint256 airdropId, address user) external view returns (bool) {
        return hasClaimed[airdropId][user];
    }
}
```
