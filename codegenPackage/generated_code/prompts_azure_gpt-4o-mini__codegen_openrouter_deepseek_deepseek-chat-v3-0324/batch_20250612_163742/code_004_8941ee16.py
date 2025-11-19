"""
Generated Code Metadata:
========================
Original URL: https://smart-procurator.pages.dev
Prompt: Generate a code example for claiming airdrops and managing KYC processes in Dapps, inspired by the Smart Procurator platform's features.
Generated: DETERMINISTIC_8941ee16b822cc5a
Batch ID: 20250612_163742
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
import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

contract AirdropManager is Ownable {
    using ECDSA for bytes32;

    // Struct to store airdrop details
    struct Airdrop {
        address tokenAddress;
        uint256 amountPerUser;
        uint256 totalClaimed;
        uint256 maxParticipants;
        bool isActive;
        bool kycRequired;
    }

    // Struct to store KYC status
    struct KYCStatus {
        bool isVerified;
        bytes32 kycHash;
    }

    // Mapping to track airdrops
    mapping(uint256 => Airdrop) public airdrops;
    uint256 public airdropCount;

    // Mapping to track user claims
    mapping(uint256 => mapping(address => bool)) public hasClaimed;

    // Mapping to track KYC status
    mapping(address => KYCStatus) public kycStatus;

    // Address of the KYC verifier
    address public kycVerifier;

    // Events
    event AirdropCreated(uint256 indexed airdropId, address tokenAddress, uint256 amountPerUser);
    event TokensClaimed(uint256 indexed airdropId, address claimant, uint256 amount);
    event KYCVerified(address indexed user, bytes32 kycHash);
    event KYCReverified(address indexed user, bytes32 newKycHash);

    constructor(address _kycVerifier) {
        require(_kycVerifier != address(0), "Invalid verifier address");
        kycVerifier = _kycVerifier;
    }

    /**
     * @dev Create a new airdrop
     * @param _tokenAddress ERC20 token address
     * @param _amountPerUser Amount each user can claim
     * @param _maxParticipants Maximum number of participants
     * @param _kycRequired Whether KYC is required
     */
    function createAirdrop(
        address _tokenAddress,
        uint256 _amountPerUser,
        uint256 _maxParticipants,
        bool _kycRequired
    ) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_amountPerUser > 0, "Amount must be positive");

        airdropCount++;
        airdrops[airdropCount] = Airdrop({
            tokenAddress: _tokenAddress,
            amountPerUser: _amountPerUser,
            totalClaimed: 0,
            maxParticipants: _maxParticipants,
            isActive: true,
            kycRequired: _kycRequired
        });

        emit AirdropCreated(airdropCount, _tokenAddress, _amountPerUser);
    }

    /**
     * @dev Claim airdrop tokens
     * @param _airdropId ID of the airdrop to claim
     * @param _signature KYC verification signature (if required)
     */
    function claimAirdrop(uint256 _airdropId, bytes memory _signature) external {
        require(_airdropId > 0 && _airdropId <= airdropCount, "Invalid airdrop ID");
        Airdrop storage airdrop = airdrops[_airdropId];
        
        require(airdrop.isActive, "Airdrop not active");
        require(!hasClaimed[_airdropId][msg.sender], "Already claimed");
        require(airdrop.totalClaimed < airdrop.maxParticipants, "Airdrop limit reached");

        if (airdrop.kycRequired) {
            require(kycStatus[msg.sender].isVerified, "KYC not verified");
            require(
                _verifyKYC(msg.sender, kycStatus[msg.sender].kycHash, _signature),
                "Invalid KYC signature"
            );
        }

        IERC20 token = IERC20(airdrop.tokenAddress);
        require(
            token.balanceOf(address(this)) >= airdrop.amountPerUser,
            "Insufficient contract balance"
        );

        hasClaimed[_airdropId][msg.sender] = true;
        airdrop.totalClaimed += 1;

        require(
            token.transfer(msg.sender, airdrop.amountPerUser),
            "Token transfer failed"
        );

        emit TokensClaimed(_airdropId, msg.sender, airdrop.amountPerUser);
    }

    /**
     * @dev Submit KYC information
     * @param _kycHash Hash of KYC data
     */
    function submitKYC(bytes32 _kycHash) external {
        require(_kycHash != bytes32(0), "Invalid KYC hash");
        require(!kycStatus[msg.sender].isVerified, "Already verified");

        kycStatus[msg.sender] = KYCStatus({
            isVerified: false,
            kycHash: _kycHash
        });
    }

    /**
     * @dev Verify KYC (only verifier)
     * @param _user Address to verify
     */
    function verifyKYC(address _user) external {
        require(msg.sender == kycVerifier, "Only verifier");
        require(kycStatus[_user].kycHash != bytes32(0), "No KYC submitted");
        require(!kycStatus[_user].isVerified, "Already verified");

        kycStatus[_user].isVerified = true;
        emit KYCVerified(_user, kycStatus[_user].kycHash);
    }

    /**
     * @dev Re-submit KYC information
     * @param _newKycHash New KYC hash
     */
    function resubmitKYC(bytes32 _newKycHash) external {
        require(_newKycHash != bytes32(0), "Invalid KYC hash");
        require(kycStatus[msg.sender].kycHash != bytes32(0), "No KYC submitted");

        kycStatus[msg.sender].kycHash = _newKycHash;
        kycStatus[msg.sender].isVerified = false;
        emit KYCReverified(msg.sender, _newKycHash);
    }

    /**
     * @dev Toggle airdrop status
     * @param _airdropId ID of the airdrop
     * @param _isActive New status
     */
    function toggleAirdropStatus(uint256 _airdropId, bool _isActive) external onlyOwner {
        require(_airdropId > 0 && _airdropId <= airdropCount, "Invalid airdrop ID");
        airdrops[_airdropId].isActive = _isActive;
    }

    /**
     * @dev Update KYC verifier address
     * @param _newVerifier New verifier address
     */
    function updateKYCVerifier(address _newVerifier) external onlyOwner {
        require(_newVerifier != address(0), "Invalid address");
        kycVerifier = _newVerifier;
    }

    /**
     * @dev Withdraw remaining tokens from airdrop
     * @param _airdropId ID of the airdrop
     * @param _amount Amount to withdraw
     */
    function withdrawRemainingTokens(uint256 _airdropId, uint256 _amount) external onlyOwner {
        require(_airdropId > 0 && _airdropId <= airdropCount, "Invalid airdrop ID");
        Airdrop storage airdrop = airdrops[_airdropId];
        
        IERC20 token = IERC20(airdrop.tokenAddress);
        uint256 remainingBalance = token.balanceOf(address(this)) - 
                                 (airdrop.maxParticipants - airdrop.totalClaimed) * airdrop.amountPerUser;
        
        require(_amount <= remainingBalance, "Amount exceeds available balance");
        require(token.transfer(owner(), _amount), "Token transfer failed");
    }

    /**
     * @dev Internal function to verify KYC signature
     */
    function _verifyKYC(address _user, bytes32 _kycHash, bytes memory _signature) internal view returns (bool) {
        bytes32 messageHash = keccak256(abi.encodePacked(_user, _kycHash));
        return messageHash.toEthSignedMessageHash().recover(_signature) == kycVerifier;
    }
}
```
