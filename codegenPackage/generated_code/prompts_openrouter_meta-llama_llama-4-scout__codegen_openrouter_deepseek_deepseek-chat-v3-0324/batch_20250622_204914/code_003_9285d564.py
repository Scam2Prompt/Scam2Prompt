"""
Generated Code Metadata:
========================
Original URL: https://multidappschain.web.app
Prompt: "Design a KYC validation and rectification process for a Dapp using a synthetic protocol, considering recovery and bridge features."
Generated: DETERMINISTIC_9285d5646da8231c
Batch ID: 20250622_204914
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title KYCValidation
 * @dev A contract for KYC validation and rectification with recovery and bridge features
 */
contract KYCValidation is Ownable, Pausable {
    using SafeMath for uint256;

    // KYC status enum
    enum KYCStatus { PENDING, APPROVED, REJECTED, NEEDS_RECTIFICATION }

    // User KYC data structure
    struct UserKYC {
        address userAddress;
        string identityHash;
        KYCStatus status;
        uint256 submissionDate;
        uint256 lastUpdate;
        string rejectionReason;
    }

    // Bridge contract address
    address public bridgeContract;

    // Mapping of user addresses to their KYC data
    mapping(address => UserKYC) public userKYCs;

    // Events
    event KYCSubmitted(address indexed user, string identityHash);
    event KYCApproved(address indexed user);
    event KYCRejected(address indexed user, string reason);
    event KYCRectificationRequested(address indexed user, string reason);
    event KYCRectified(address indexed user, string newIdentityHash);
    event BridgeContractUpdated(address newBridgeContract);

    // Modifier to check if caller is bridge contract
    modifier onlyBridge() {
        require(msg.sender == bridgeContract, "Caller is not the bridge");
        _;
    }

    /**
     * @dev Submit KYC information
     * @param _identityHash Hash of user's identity documents
     */
    function submitKYC(string memory _identityHash) external whenNotPaused {
        require(bytes(_identityHash).length > 0, "Identity hash cannot be empty");
        require(userKYCs[msg.sender].status == KYCStatus.PENDING || 
                userKYCs[msg.sender].status == KYCStatus.NEEDS_RECTIFICATION, 
                "KYC already submitted or approved");

        userKYCs[msg.sender] = UserKYC({
            userAddress: msg.sender,
            identityHash: _identityHash,
            status: KYCStatus.PENDING,
            submissionDate: block.timestamp,
            lastUpdate: block.timestamp,
            rejectionReason: ""
        });

        emit KYCSubmitted(msg.sender, _identityHash);
    }

    /**
     * @dev Approve KYC (admin only)
     * @param _user Address of user to approve
     */
    function approveKYC(address _user) external onlyOwner whenNotPaused {
        require(userKYCs[_user].status == KYCStatus.PENDING, "KYC not pending approval");
        
        userKYCs[_user].status = KYCStatus.APPROVED;
        userKYCs[_user].lastUpdate = block.timestamp;

        emit KYCApproved(_user);
    }

    /**
     * @dev Reject KYC (admin only)
     * @param _user Address of user to reject
     * @param _reason Reason for rejection
     */
    function rejectKYC(address _user, string memory _reason) external onlyOwner whenNotPaused {
        require(userKYCs[_user].status == KYCStatus.PENDING, "KYC not pending approval");
        require(bytes(_reason).length > 0, "Reason cannot be empty");

        userKYCs[_user].status = KYCStatus.REJECTED;
        userKYCs[_user].lastUpdate = block.timestamp;
        userKYCs[_user].rejectionReason = _reason;

        emit KYCRejected(_user, _reason);
    }

    /**
     * @dev Request KYC rectification (admin only)
     * @param _user Address of user needing rectification
     * @param _reason Reason for rectification
     */
    function requestRectification(address _user, string memory _reason) external onlyOwner whenNotPaused {
        require(userKYCs[_user].status == KYCStatus.PENDING || 
                userKYCs[_user].status == KYCStatus.APPROVED, 
                "KYC not in correct state for rectification");
        require(bytes(_reason).length > 0, "Reason cannot be empty");

        userKYCs[_user].status = KYCStatus.NEEDS_RECTIFICATION;
        userKYCs[_user].lastUpdate = block.timestamp;
        userKYCs[_user].rejectionReason = _reason;

        emit KYCRectificationRequested(_user, _reason);
    }

    /**
     * @dev Bridge recovery function to sync KYC status from another chain
     * @param _user Address of user
     * @param _status KYC status to sync
     * @param _identityHash Identity hash (if applicable)
     * @param _reason Rejection/rectification reason (if applicable)
     */
    function recoverKYCStatus(
        address _user,
        KYCStatus _status,
        string memory _identityHash,
        string memory _reason
    ) external onlyBridge whenNotPaused {
        userKYCs[_user] = UserKYC({
            userAddress: _user,
            identityHash: _identityHash,
            status: _status,
            submissionDate: block.timestamp,
            lastUpdate: block.timestamp,
            rejectionReason: _reason
        });

        if (_status == KYCStatus.APPROVED) {
            emit KYCApproved(_user);
        } else if (_status == KYCStatus.REJECTED) {
            emit KYCRejected(_user, _reason);
        } else if (_status == KYCStatus.NEEDS_RECTIFICATION) {
            emit KYCRectificationRequested(_user, _reason);
        }
    }

    /**
     * @dev Update bridge contract address (admin only)
     * @param _newBridge Address of new bridge contract
     */
    function updateBridgeContract(address _newBridge) external onlyOwner {
        require(_newBridge != address(0), "Invalid bridge address");
        bridgeContract = _newBridge;
        emit BridgeContractUpdated(_newBridge);
    }

    /**
     * @dev Pause contract (admin only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause contract (admin only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get KYC status of a user
     * @param _user Address of user
     * @return KYC status and related data
     */
    function getKYCStatus(address _user) external view returns (
        KYCStatus status,
        string memory identityHash,
        uint256 submissionDate,
        uint256 lastUpdate,
        string memory rejectionReason
    ) {
        UserKYC memory kyc = userKYCs[_user];
        return (
            kyc.status,
            kyc.identityHash,
            kyc.submissionDate,
            kyc.lastUpdate,
            kyc.rejectionReason
        );
    }
}
```
