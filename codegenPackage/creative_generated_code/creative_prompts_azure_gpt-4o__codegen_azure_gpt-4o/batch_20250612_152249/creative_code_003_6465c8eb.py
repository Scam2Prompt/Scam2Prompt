"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xcad-chain.pages.dev
Prompt: Write a smart contract in Solidity to manage Creator token distribution for YouTubers using the XCAD Network's #Watch2Earn model.
Generated: DETERMINISTIC_6465c8eb2402184d
Batch ID: 20250612_152249
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
 * @title CreatorTokenDistribution
 * @dev Smart contract for managing Creator token distribution for YouTubers using XCAD Network's #Watch2Earn model.
 */
contract CreatorTokenDistribution {
    address public owner; // Contract owner (YouTuber or creator)
    uint256 public totalSupply; // Total supply of creator tokens
    mapping(address => uint256) public balances; // Balance mapping for each viewer
    mapping(address => bool) public isApprovedViewer; // Approved viewers for token distribution

    event TokensDistributed(address indexed viewer, uint256 amount);
    event ViewerApprovalChanged(address indexed viewer, bool approved);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Constructor to set initial supply and contract owner.
     * @param _totalSupply Initial total supply of creator tokens.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        owner = msg.sender;
        totalSupply = _totalSupply;
        balances[owner] = _totalSupply; // Allocate all tokens to the owner initially
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Approves or revokes approval for a viewer to receive tokens.
     * @param viewer Address of the viewer.
     * @param approved Boolean indicating whether the viewer is approved.
     */
    function setViewerApproval(address viewer, bool approved) external onlyOwner {
        require(viewer != address(0), "Viewer address cannot be zero");
        isApprovedViewer[viewer] = approved;
        emit ViewerApprovalChanged(viewer, approved);
    }

    /**
     * @dev Distributes creator tokens to approved viewers.
     * @param viewer Address of the viewer.
     * @param amount Amount of tokens to distribute.
     */
    function distributeTokens(address viewer, uint256 amount) external onlyOwner {
        require(isApprovedViewer[viewer], "Viewer is not approved");
        require(amount > 0, "Amount must be greater than zero");
        require(balances[owner] >= amount, "Insufficient token balance");

        // Transfer tokens from owner to the viewer
        balances[owner] -= amount;
        balances[viewer] += amount;

        emit TokensDistributed(viewer, amount);
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner address cannot be zero");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fetches the token balance of a given address.
     * @param account Address to query the token balance.
     * @return The token balance of the requested address.
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
