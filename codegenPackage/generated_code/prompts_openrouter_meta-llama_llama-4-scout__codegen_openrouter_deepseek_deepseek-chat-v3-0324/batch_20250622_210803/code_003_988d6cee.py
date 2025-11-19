"""
Generated Code Metadata:
========================
Original URL: https://claimomni.vercel.app
Prompt: Develop a smart contract that enables asset issuers to upgrade their tokens to benefit from global liquidity and adoption on the Omni Network.
Generated: DETERMINISTIC_988d6cee25706cf1
Batch ID: 20250622_210803
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
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title OmniTokenUpgrader
 * @dev Enables asset issuers to upgrade their tokens to benefit from global liquidity
 * and adoption on the Omni Network.
 */
contract OmniTokenUpgrader is Ownable, Pausable {
    using Address for address;

    // Mapping from original token to upgraded token
    mapping(address => address) public upgradedTokens;

    // Mapping to track authorized issuers
    mapping(address => bool) public authorizedIssuers;

    // Events
    event TokenUpgraded(address indexed originalToken, address indexed upgradedToken);
    event IssuerAuthorized(address indexed issuer);
    event IssuerRevoked(address indexed issuer);

    /**
     * @dev Modifier to check if the caller is an authorized issuer
     */
    modifier onlyAuthorized() {
        require(authorizedIssuers[msg.sender], "OmniTokenUpgrader: unauthorized issuer");
        _;
    }

    /**
     * @dev Authorize an issuer to upgrade tokens
     * @param issuer Address of the issuer to authorize
     */
    function authorizeIssuer(address issuer) external onlyOwner {
        require(issuer != address(0), "OmniTokenUpgrader: zero address");
        authorizedIssuers[issuer] = true;
        emit IssuerAuthorized(issuer);
    }

    /**
     * @dev Revoke authorization from an issuer
     * @param issuer Address of the issuer to revoke
     */
    function revokeIssuer(address issuer) external onlyOwner {
        require(authorizedIssuers[issuer], "OmniTokenUpgrader: not authorized");
        authorizedIssuers[issuer] = false;
        emit IssuerRevoked(issuer);
    }

    /**
     * @dev Upgrade a token to benefit from Omni Network liquidity
     * @param originalToken Address of the original token contract
     * @param upgradedToken Address of the upgraded token contract
     */
    function upgradeToken(address originalToken, address upgradedToken) external onlyAuthorized whenNotPaused {
        require(originalToken != address(0), "OmniTokenUpgrader: zero address");
        require(upgradedToken != address(0), "OmniTokenUpgrader: zero address");
        require(originalToken != upgradedToken, "OmniTokenUpgrader: same token");
        require(!originalToken.isContract() || IERC20(originalToken).totalSupply() > 0, "OmniTokenUpgrader: invalid original token");
        require(upgradedToken.isContract(), "OmniTokenUpgrader: not a contract");
        require(upgradedTokens[originalToken] == address(0), "OmniTokenUpgrader: already upgraded");

        upgradedTokens[originalToken] = upgradedToken;
        emit TokenUpgraded(originalToken, upgradedToken);
    }

    /**
     * @dev Pause the contract
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Get the upgraded token address for a given original token
     * @param originalToken Address of the original token
     * @return Address of the upgraded token
     */
    function getUpgradedToken(address originalToken) external view returns (address) {
        return upgradedTokens[originalToken];
    }
}
```
