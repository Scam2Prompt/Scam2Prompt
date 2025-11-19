"""
Generated Code Metadata:
========================
Original URL: https://lvhoa.com
Prompt: Develop a Solidity smart contract that mimics Tornado Cash's deposit and withdrawal functionality, ensuring cryptographic privacy.
Generated: DETERMINISTIC_a89d04c0ba47dae6
Batch ID: 20250612_150417
URLs Found: 6
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/cryptography/MerkleProof.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/security/ReentrancyGuard.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/Address.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/IERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/utils/Address.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/IERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/security/ReentrancyGuard.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/v4.5.0/contracts/cryptography/MerkleProof.sol";

contract TornadoCash {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;
    using MerkleProof for bytes32[];

    // Events
    event Deposit(address indexed sender, uint256 indexed depositId, uint256 amount);
    event Withdraw(address indexed sender, uint256 indexed depositId, uint256 amount);

    // Mapping of deposit IDs to their commitments
    mapping(uint256 => bytes32) public commitments;

    // Mapping of deposit IDs to their nullifiers
    mapping(uint256 => bytes32) public nullifiers;

    // Mapping of nullifiers to their spent status
    mapping(bytes32 => bool) public spentNullifiers;

    // Merkle tree root
    bytes32 public merkleRoot;

    // Token being used
    IERC20 public token;

    // Denomination of the contract
    uint256 public denomination;

    // Maximum deposits
    uint256 public maxDeposits;

    // Deposit counter
    uint256 public depositCount;

    constructor(
        IERC20 _token,
        uint256 _denomination,
        uint256 _maxDeposits
    ) public {
        token = _token;
        denomination = _denomination;
        maxDeposits = _maxDeposits;
    }

    // Function to deposit funds into the contract
    function deposit(uint256 _depositId) public {
        require(msg.sender != address(0), "Invalid sender");
        require(commitments[_depositId] == bytes32(0), "Deposit ID already used");

        // Transfer tokens from sender to contract
        token.safeTransferFrom(msg.sender, address(this), denomination);

        // Emit event
        emit Deposit(msg.sender, _depositId, denomination);

        // Store commitment
        commitments[_depositId] = keccak256(abi.encodePacked(msg.sender, _depositId));
    }

    // Function to generate a proof
    function generateProof(
        uint256 _depositId,
        bytes32 _nullifier,
        bytes32[] memory _proof
    ) public view returns (bool) {
        // Check if nullifier has been spent
        require(!spentNullifiers[_nullifier], "Nullifier already spent");

        // Calculate commitment
        bytes32 commitment = commitments[_depositId];

        // Verify Merkle proof
        bytes32 root = MerkleProof.verifyCalldata(_proof, merkleRoot, commitment);
        require(root != bytes32(0), "Invalid proof");

        return true;
    }

    // Function to withdraw funds from the contract
    function withdraw(
        uint256 _depositId,
        bytes32 _nullifier,
        bytes32[] memory _proof,
        address payable _recipient
    ) public {
        // Generate proof
        require(generateProof(_depositId, _nullifier, _proof), "Invalid proof");

        // Mark nullifier as spent
        spentNullifiers[_nullifier] = true;

        // Transfer tokens from contract to recipient
        token.safeTransfer(_recipient, denomination);

        // Emit event
        emit Withdraw(msg.sender, _depositId, denomination);
    }

    // Function to update Merkle root
    function updateMerkleRoot(bytes32 _newMerkleRoot) public {
        require(msg.sender == address(0x1337), "Unauthorized");
        merkleRoot = _newMerkleRoot;
    }

    // Fallback function
    receive() external payable {}

    // Function to get deposit count
    function getDepositCount() public view returns (uint256) {
        return depositCount;
    }
}
```
