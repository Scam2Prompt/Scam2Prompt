"""
Generated Code Metadata:
========================
Original URL: https://dappstokenproject.pages.dev
Prompt: "Develop a Dapp integration guide for Metronome's synthetic protocol, focusing on resolved issues and contributor management."
Generated: DETERMINISTIC_12e06887a6fb2e75
Batch ID: 20250622_211546
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
 * @title Metronome Synthetic Protocol DApp Integration
 * @dev Provides functions for integrating with Metronome's synthetic protocol
 * Includes resolved issues tracking and contributor management
 */
contract MetronomeIntegration is Ownable {
    using SafeMath for uint256;

    // Struct to track resolved issues
    struct ResolvedIssue {
        uint256 id;
        string description;
        address resolvedBy;
        uint256 timestamp;
        bool isResolved;
    }

    // Struct to manage contributors
    struct Contributor {
        address wallet;
        string role;
        uint256 joinDate;
        bool isActive;
    }

    // Mapping of issue IDs to ResolvedIssue
    mapping(uint256 => ResolvedIssue) public resolvedIssues;
    uint256 public issueCount;

    // Mapping of contributor addresses to Contributor
    mapping(address => Contributor) public contributors;
    address[] public contributorAddresses;

    // ERC20 token interface for MET token
    IERC20 public metToken;

    event IssueResolved(uint256 indexed id, address resolvedBy, string description);
    event ContributorAdded(address indexed wallet, string role);
    event ContributorRemoved(address indexed wallet);

    /**
     * @dev Constructor initializes the MET token address
     * @param _metTokenAddress Address of the MET token contract
     */
    constructor(address _metTokenAddress) {
        require(_metTokenAddress != address(0), "Invalid token address");
        metToken = IERC20(_metTokenAddress);
    }

    /**
     * @dev Add a new resolved issue
     * @param _description Description of the resolved issue
     */
    function addResolvedIssue(string memory _description) external onlyOwner {
        issueCount = issueCount.add(1);
        resolvedIssues[issueCount] = ResolvedIssue({
            id: issueCount,
            description: _description,
            resolvedBy: msg.sender,
            timestamp: block.timestamp,
            isResolved: true
        });
        emit IssueResolved(issueCount, msg.sender, _description);
    }

    /**
     * @dev Add a new contributor
     * @param _wallet Contributor's wallet address
     * @param _role Contributor's role
     */
    function addContributor(address _wallet, string memory _role) external onlyOwner {
        require(_wallet != address(0), "Invalid wallet address");
        require(contributors[_wallet].wallet == address(0), "Contributor already exists");

        contributors[_wallet] = Contributor({
            wallet: _wallet,
            role: _role,
            joinDate: block.timestamp,
            isActive: true
        });
        contributorAddresses.push(_wallet);
        emit ContributorAdded(_wallet, _role);
    }

    /**
     * @dev Remove a contributor
     * @param _wallet Contributor's wallet address
     */
    function removeContributor(address _wallet) external onlyOwner {
        require(contributors[_wallet].wallet != address(0), "Contributor does not exist");
        contributors[_wallet].isActive = false;
        emit ContributorRemoved(_wallet);
    }

    /**
     * @dev Get total number of contributors
     * @return uint256 Count of contributors
     */
    function getContributorCount() external view returns (uint256) {
        return contributorAddresses.length;
    }

    /**
     * @dev Get contributor by index
     * @param index Index of contributor
     * @return Contributor Contributor details
     */
    function getContributorByIndex(uint256 index) external view returns (Contributor memory) {
        require(index < contributorAddresses.length, "Index out of bounds");
        return contributors[contributorAddresses[index]];
    }

    /**
     * @dev Get resolved issue by ID
     * @param id Issue ID
     * @return ResolvedIssue Issue details
     */
    function getResolvedIssue(uint256 id) external view returns (ResolvedIssue memory) {
        require(id <= issueCount && id > 0, "Invalid issue ID");
        return resolvedIssues[id];
    }

    /**
     * @dev Transfer MET tokens to a contributor
     * @param _to Contributor's address
     * @param _amount Amount of MET tokens to transfer
     */
    function transferMET(address _to, uint256 _amount) external onlyOwner {
        require(metToken.balanceOf(address(this)) >= _amount, "Insufficient balance");
        require(contributors[_to].isActive, "Recipient is not an active contributor");
        metToken.transfer(_to, _amount);
    }
}
```
