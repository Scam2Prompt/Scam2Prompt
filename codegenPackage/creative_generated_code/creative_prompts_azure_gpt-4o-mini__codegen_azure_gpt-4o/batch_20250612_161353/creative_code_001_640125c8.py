"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: Write a code snippet that demonstrates how to selectively disclose token holdings using the DOP framework on Ethereum.
Generated: DETERMINISTIC_640125c8e3893e80
Batch ID: 20250612_161353
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
 * @title Selective Token Disclosure using Decentralized Oracle Protocol (DOP)
 * @notice This contract allows users to selectively disclose token holdings via a decentralized oracle
 */
contract SelectiveDisclosure {
    // Event emitted when token holdings are disclosed
    event TokenHoldingsDisclosed(address indexed user, uint256 tokenBalance, address oracle);

    // Mapping to store a user's approved disclosure permissions
    mapping(address => bool) public approvedOracles;

    /**
     * @notice Approve or revoke an oracle for disclosures
     * @param oracle Address of the oracle
     * @param approved Boolean indicating approval status
     */
    function setOracleApproval(address oracle, bool approved) external {
        require(oracle != address(0), "Invalid oracle address");
        approvedOracles[oracle] = approved;
    }

    /**
     * @notice Disclose token holdings to an approved oracle
     * @param oracle Address of the oracle requesting disclosures
     * @param tokenAddress Address of the token contract
     */
    function discloseHoldings(address oracle, address tokenAddress) external {
        require(approvedOracles[oracle], "Oracle not approved");
        require(tokenAddress != address(0), "Invalid token address");

        // Get the token balance of the sender
        uint256 balance = IERC20(tokenAddress).balanceOf(msg.sender);

        // Emit an event for disclosure (can be picked up by the oracle off-chain)
        emit TokenHoldingsDisclosed(msg.sender, balance, oracle);
    }
}

/**
 * @dev Interface for ERC20 token contracts
 */
interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
