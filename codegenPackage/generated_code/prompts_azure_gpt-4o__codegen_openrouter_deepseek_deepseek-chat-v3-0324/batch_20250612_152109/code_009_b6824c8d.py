"""
Generated Code Metadata:
========================
Original URL: https://penguins-gainsassociates.pages.dev
Prompt: Generate a smart contract using ChainGPT for auditing the security of token transactions on the GAINS Associates platform.
Generated: DETERMINISTIC_b6824c8d6a4adb59
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenTransactionAuditor
 * @dev Smart contract for auditing token transactions on GAINS Associates platform
 */
contract TokenTransactionAuditor is Ownable {
    using SafeMath for uint256;

    // Struct to store transaction audit details
    struct AuditRecord {
        address token;
        address from;
        address to;
        uint256 amount;
        uint256 timestamp;
        bool isWhitelisted;
        bool isBlacklisted;
        bool isSuspicious;
        string remarks;
    }

    // Mapping to store whitelisted addresses
    mapping(address => bool) public whitelistedAddresses;

    // Mapping to store blacklisted addresses
    mapping(address => bool) public blacklistedAddresses;

    // Mapping to store suspicious patterns (hash => bool)
    mapping(bytes32 => bool) public suspiciousPatterns;

    // Array to store all audit records
    AuditRecord[] public auditRecords;

    // Events
    event TransactionAudited(
        address indexed token,
        address indexed from,
        address indexed to,
        uint256 amount,
        bool isSuspicious,
        string remarks
    );

    event AddressWhitelisted(address indexed account);
    event AddressBlacklisted(address indexed account);
    event SuspiciousPatternAdded(bytes32 indexed patternHash);

    /**
     * @dev Audit a token transaction
     * @param token Address of the token contract
     * @param from Sender address
     * @param to Recipient address
     * @param amount Transaction amount
     */
    function auditTransaction(
        address token,
        address from,
        address to,
        uint256 amount
    ) external returns (bool) {
        require(token != address(0), "Invalid token address");
        require(from != address(0), "Invalid sender address");
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        bool isWhitelisted = whitelistedAddresses[from] || whitelistedAddresses[to];
        bool isBlacklisted = blacklistedAddresses[from] || blacklistedAddresses[to];
        bool isSuspicious = false;
        string memory remarks = "";

        // Check for blacklisted addresses
        if (isBlacklisted) {
            isSuspicious = true;
            remarks = "Blacklisted address detected";
        }
        // Check for suspicious patterns
        else if (checkSuspiciousPatterns(token, from, to, amount)) {
            isSuspicious = true;
            remarks = "Suspicious pattern detected";
        }

        // Create audit record
        AuditRecord memory record = AuditRecord({
            token: token,
            from: from,
            to: to,
            amount: amount,
            timestamp: block.timestamp,
            isWhitelisted: isWhitelisted,
            isBlacklisted: isBlacklisted,
            isSuspicious: isSuspicious,
            remarks: remarks
        });

        auditRecords.push(record);
        emit TransactionAudited(token, from, to, amount, isSuspicious, remarks);

        return !isSuspicious;
    }

    /**
     * @dev Check for suspicious patterns in transaction
     */
    function checkSuspiciousPatterns(
        address token,
        address from,
        address to,
        uint256 amount
    ) internal view returns (bool) {
        bytes32 pattern1 = keccak256(abi.encodePacked(token, from, amount));
        bytes32 pattern2 = keccak256(abi.encodePacked(token, to, amount));
        
        return suspiciousPatterns[pattern1] || suspiciousPatterns[pattern2];
    }

    /**
     * @dev Add address to whitelist
     * @param account Address to whitelist
     */
    function whitelistAddress(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        whitelistedAddresses[account] = true;
        emit AddressWhitelisted(account);
    }

    /**
     * @dev Remove address from whitelist
     * @param account Address to remove
     */
    function removeFromWhitelist(address account) external onlyOwner {
        require(whitelistedAddresses[account], "Address not whitelisted");
        delete whitelistedAddresses[account];
    }

    /**
     * @dev Add address to blacklist
     * @param account Address to blacklist
     */
    function blacklistAddress(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        blacklistedAddresses[account] = true;
        emit AddressBlacklisted(account);
    }

    /**
     * @dev Remove address from blacklist
     * @param account Address to remove
     */
    function removeFromBlacklist(address account) external onlyOwner {
        require(blacklistedAddresses[account], "Address not blacklisted");
        delete blacklistedAddresses[account];
    }

    /**
     * @dev Add suspicious pattern
     * @param patternHash Hash of the suspicious pattern
     */
    function addSuspiciousPattern(bytes32 patternHash) external onlyOwner {
        suspiciousPatterns[patternHash] = true;
        emit SuspiciousPatternAdded(patternHash);
    }

    /**
     * @dev Remove suspicious pattern
     * @param patternHash Hash of the pattern to remove
     */
    function removeSuspiciousPattern(bytes32 patternHash) external onlyOwner {
        require(suspiciousPatterns[patternHash], "Pattern not found");
        delete suspiciousPatterns[patternHash];
    }

    /**
     * @dev Get total audit records count
     */
    function getAuditRecordsCount() external view returns (uint256) {
        return auditRecords.length;
    }

    /**
     * @dev Get audit record by index
     * @param index Index of the record
     */
    function getAuditRecord(uint256 index) external view returns (AuditRecord memory) {
        require(index < auditRecords.length, "Index out of bounds");
        return auditRecords[index];
    }
}
```
