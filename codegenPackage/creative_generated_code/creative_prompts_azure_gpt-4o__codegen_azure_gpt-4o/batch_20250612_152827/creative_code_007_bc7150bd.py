"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Suggest a method to audit a smart contract for a token presale to ensure compliance with the 5,000 ETH cap and the total supply limit of 100,000,000 KSI.
Generated: DETERMINISTIC_bc7150bda140c4ba
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenPresaleAudit
 * @dev Audits a token presale smart contract for compliance with ETH cap and token supply limit.
 */
contract TokenPresaleAudit {
    // Constants
    uint256 public constant MAX_ETH_CAP = 5000 ether; // Maximum ETH cap for the presale
    uint256 public constant MAX_TOKEN_SUPPLY = 100_000_000 * (10 ** 18); // Maximum token supply (in wei)

    // State variables
    uint256 public totalEthContributed; // Tracks total ETH contributed during the presale
    uint256 public totalTokensIssued;  // Tracks total tokens issued during the presale
    address public owner;              // Owner of the smart contract

    // Events
    event ContributionReceived(address indexed contributor, uint256 ethAmount, uint256 tokenAmount);
    event AuditFailed(string reason);
    event AuditPassed();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to simulate a contribution to the presale.
     * @param contributor The address of the contributor.
     * @param ethAmount The amount of ETH contributed.
     * @param tokenAmount The amount of tokens issued for the contribution.
     */
    function simulateContribution(address contributor, uint256 ethAmount, uint256 tokenAmount) external onlyOwner {
        require(contributor != address(0), "Contributor address cannot be zero");
        require(ethAmount > 0, "ETH amount must be greater than zero");
        require(tokenAmount > 0, "Token amount must be greater than zero");

        // Update tracking variables
        totalEthContributed += ethAmount;
        totalTokensIssued += tokenAmount;

        // Emit contribution event
        emit ContributionReceived(contributor, ethAmount, tokenAmount);

        // Check compliance after the contribution
        _audit();
    }

    /**
     * @dev Audits the contract to ensure compliance with ETH cap and token supply limits.
     */
    function audit() external onlyOwner {
        _audit();
    }

    /**
     * @dev Internal function to perform the audit.
     */
    function _audit() internal {
        if (totalEthContributed > MAX_ETH_CAP) {
            emit AuditFailed("ETH cap exceeded");
        } else if (totalTokensIssued > MAX_TOKEN_SUPPLY) {
            emit AuditFailed("Token supply cap exceeded");
        } else {
            emit AuditPassed();
        }
    }
}
```
