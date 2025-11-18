"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://berrycoinerc.vip
Prompt: Generate Solidity code for a new smart contract that integrates with the $BERRY token and adds a feature for tracking community contributions.
Generated: DETERMINISTIC_b6a2fd2f0011fe37
Batch ID: 20250612_153925
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
 * @title CommunityContributionTracker
 * @dev Smart contract for integrating with the $BERRY token and tracking community contributions.
 */
contract CommunityContributionTracker {
    // Address of the $BERRY token contract
    address public berryTokenAddress;

    // Struct to represent a community contribution
    struct Contribution {
        address contributor;
        uint256 amount;
        string description;
        uint256 timestamp;
    }

    // Array to store all contributions
    Contribution[] public contributions;

    // Mapping to track total contributions for each address
    mapping(address => uint256) public totalContributions;

    // Event emitted when a new contribution is added
    event ContributionAdded(
        address indexed contributor,
        uint256 amount,
        string description,
        uint256 timestamp
    );

    /**
     * @dev Constructor to initialize the contract with the $BERRY token address.
     * @param _berryTokenAddress Address of the $BERRY token contract.
     */
    constructor(address _berryTokenAddress) {
        require(_berryTokenAddress != address(0), "Invalid token address");
        berryTokenAddress = _berryTokenAddress;
    }

    /**
     * @dev Function to add a community contribution.
     * @param amount Amount of $BERRY tokens contributed.
     * @param description Description of the contribution.
     */
    function addContribution(uint256 amount, string memory description) external {
        require(amount > 0, "Contribution amount must be greater than zero");
        require(bytes(description).length > 0, "Description cannot be empty");

        // Interact with the $BERRY token contract to transfer tokens
        IERC20 berryToken = IERC20(berryTokenAddress);
        require(
            berryToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Record the contribution
        contributions.push(Contribution({
            contributor: msg.sender,
            amount: amount,
            description: description,
            timestamp: block.timestamp
        }));

        // Update total contributions for the contributor
        totalContributions[msg.sender] += amount;

        // Emit the ContributionAdded event
        emit ContributionAdded(msg.sender, amount, description, block.timestamp);
    }

    /**
     * @dev Function to get the total number of contributions.
     * @return Total number of contributions recorded in the contract.
     */
    function getTotalContributions() external view returns (uint256) {
        return contributions.length;
    }

    /**
     * @dev Function to retrieve details of a specific contribution by index.
     * @param index Index of the contribution in the array.
     * @return Details of the contribution.
     */
    function getContribution(uint256 index)
        external
        view
        returns (
            address contributor,
            uint256 amount,
            string memory description,
            uint256 timestamp
        )
    {
        require(index < contributions.length, "Invalid index");
        Contribution memory contribution = contributions[index];
        return (
            contribution.contributor,
            contribution.amount,
            contribution.description,
            contribution.timestamp
        );
    }
}

/**
 * @dev Interface for interacting with ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
