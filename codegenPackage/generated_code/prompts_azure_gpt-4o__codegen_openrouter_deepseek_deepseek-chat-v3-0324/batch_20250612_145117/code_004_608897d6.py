"""
Generated Code Metadata:
========================
Original URL: https://ragnarokdao.finance
Prompt: Create a smart contract that manages access control for a DeFi platform, ensuring users meet specific requirements before interacting with the app.
Generated: DETERMINISTIC_608897d6dcfd74ad
Batch ID: 20250612_145117
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

import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeFiAccessControl
 * @dev Smart contract for managing access control in a DeFi platform
 */
contract DeFiAccessControl is AccessControl, Pausable {
    using SafeMath for uint256;

    bytes32 public constant KYC_VERIFIED_ROLE = keccak256("KYC_VERIFIED_ROLE");
    bytes32 public constant MIN_BALANCE_ROLE = keccak256("MIN_BALANCE_ROLE");
    bytes32 public constant WHITELISTED_ROLE = keccak256("WHITELISTED_ROLE");

    uint256 public minTokenBalance;
    address public tokenAddress;

    event RequirementsUpdated(uint256 newMinBalance, address newTokenAddress);
    event UserVerified(address indexed user, string requirement);

    /**
     * @dev Constructor sets up roles and initial requirements
     * @param _admin The address of the admin
     * @param _minTokenBalance Minimum token balance required
     * @param _tokenAddress Address of the token contract
     */
    constructor(
        address _admin,
        uint256 _minTokenBalance,
        address _tokenAddress
    ) {
        require(_admin != address(0), "Invalid admin address");
        require(_tokenAddress != address(0), "Invalid token address");

        _setupRole(DEFAULT_ADMIN_ROLE, _admin);
        minTokenBalance = _minTokenBalance;
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Updates the minimum requirements for access
     * @param _newMinBalance New minimum token balance
     * @param _newTokenAddress New token address
     */
    function updateRequirements(
        uint256 _newMinBalance,
        address _newTokenAddress
    ) external onlyRole(DEFAULT_ADMIN_ROLE) {
        require(_newTokenAddress != address(0), "Invalid token address");
        minTokenBalance = _newMinBalance;
        tokenAddress = _newTokenAddress;
        emit RequirementsUpdated(_newMinBalance, _newTokenAddress);
    }

    /**
     * @dev Verifies KYC for a user
     * @param user Address to verify
     */
    function verifyKYC(address user) external onlyRole(DEFAULT_ADMIN_ROLE) {
        grantRole(KYC_VERIFIED_ROLE, user);
        emit UserVerified(user, "KYC");
    }

    /**
     * @dev Whitelists a user
     * @param user Address to whitelist
     */
    function whitelistUser(address user) external onlyRole(DEFAULT_ADMIN_ROLE) {
        grantRole(WHITELISTED_ROLE, user);
        emit UserVerified(user, "Whitelist");
    }

    /**
     * @dev Checks if a user meets all requirements
     * @param user Address to check
     * @return bool True if user meets all requirements
     */
    function checkAccess(address user) external view returns (bool) {
        return
            hasRole(KYC_VERIFIED_ROLE, user) &&
            hasRole(WHITELISTED_ROLE, user) &&
            hasRole(MIN_BALANCE_ROLE, user);
    }

    /**
     * @dev Pauses the contract
     */
    function pause() external onlyRole(DEFAULT_ADMIN_ROLE) {
        _pause();
    }

    /**
     * @dev Unpauses the contract
     */
    function unpause() external onlyRole(DEFAULT_ADMIN_ROLE) {
        _unpause();
    }

    /**
     * @dev Updates token balance status for a user
     * @param user Address to update
     * @param balance Current token balance
     */
    function updateTokenBalance(
        address user,
        uint256 balance
    ) external whenNotPaused {
        require(
            msg.sender == tokenAddress,
            "Only token contract can update balance"
        );

        if (balance >= minTokenBalance) {
            grantRole(MIN_BALANCE_ROLE, user);
        } else {
            revokeRole(MIN_BALANCE_ROLE, user);
        }
    }
}
```
