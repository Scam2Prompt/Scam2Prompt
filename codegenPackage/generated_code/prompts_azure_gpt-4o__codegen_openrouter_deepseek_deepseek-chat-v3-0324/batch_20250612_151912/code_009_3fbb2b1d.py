"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: Write a Solidity smart contract for distributing eosGAS tokens during an airdrop program, ensuring compliance with KYC requirements as mentioned on the website.
Generated: DETERMINISTIC_3fbb2b1d34e97129
Batch ID: 20250612_151912
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/cryptography/MerkleProof.sol";

contract EosGASAirdrop is Ownable, Pausable {
    IERC20 public eosGAS;
    bytes32 public merkleRoot;
    uint256 public airdropAmount;
    uint256 public airdropEndTime;

    // Track claimed addresses
    mapping(address => bool) public hasClaimed;

    // Events
    event TokensClaimed(address indexed recipient, uint256 amount);
    event AirdropExtended(uint256 newEndTime);
    event MerkleRootUpdated(bytes32 newMerkleRoot);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _eosGAS Address of the eosGAS token contract
     * @param _merkleRoot Root of the Merkle tree containing eligible addresses
     * @param _airdropAmount Amount of tokens to distribute per claim
     * @param _airdropDuration Duration of the airdrop in seconds
     */
    constructor(
        address _eosGAS,
        bytes32 _merkleRoot,
        uint256 _airdropAmount,
        uint256 _airdropDuration
    ) {
        require(_eosGAS != address(0), "Invalid token address");
        require(_airdropAmount > 0, "Airdrop amount must be positive");
        require(_airdropDuration > 0, "Airdrop duration must be positive");

        eosGAS = IERC20(_eosGAS);
        merkleRoot = _merkleRoot;
        airdropAmount = _airdropAmount;
        airdropEndTime = block.timestamp + _airdropDuration;
    }

    /**
     * @dev Claim tokens during airdrop
     * @param merkleProof Proof that the sender is eligible for the airdrop
     */
    function claimTokens(bytes32[] calldata merkleProof) external whenNotPaused {
        require(block.timestamp <= airdropEndTime, "Airdrop has ended");
        require(!hasClaimed[msg.sender], "Tokens already claimed");

        // Verify the merkle proof
        bytes32 leaf = keccak256(abi.encodePacked(msg.sender));
        require(
            MerkleProof.verify(merkleProof, merkleRoot, leaf),
            "Invalid proof"
        );

        hasClaimed[msg.sender] = true;
        require(
            eosGAS.transfer(msg.sender, airdropAmount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Extend the airdrop duration
     * @param additionalTime Additional time in seconds
     */
    function extendAirdrop(uint256 additionalTime) external onlyOwner {
        require(additionalTime > 0, "Additional time must be positive");
        airdropEndTime += additionalTime;
        emit AirdropExtended(airdropEndTime);
    }

    /**
     * @dev Update the Merkle root
     * @param newMerkleRoot New Merkle root
     */
    function updateMerkleRoot(bytes32 newMerkleRoot) external onlyOwner {
        merkleRoot = newMerkleRoot;
        emit MerkleRootUpdated(newMerkleRoot);
    }

    /**
     * @dev Withdraw remaining tokens after airdrop ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp > airdropEndTime, "Airdrop not ended yet");
        uint256 balance = eosGAS.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(eosGAS.transfer(owner(), balance), "Token transfer failed");
        emit TokensWithdrawn(owner(), balance);
    }

    /**
     * @dev Pause the airdrop in case of emergency
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the airdrop
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Check if an address has claimed tokens
     * @param account Address to check
     * @return bool Whether the address has claimed
     */
    function hasAddressClaimed(address account) external view returns (bool) {
        return hasClaimed[account];
    }

    /**
     * @dev Check if airdrop is active
     * @return bool Whether the airdrop is active
     */
    function isAirdropActive() external view returns (bool) {
        return block.timestamp <= airdropEndTime && !paused();
    }
}
```
