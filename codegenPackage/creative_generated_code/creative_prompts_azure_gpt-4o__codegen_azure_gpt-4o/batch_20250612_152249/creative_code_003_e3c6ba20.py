"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btconbase-en.pages.dev
Prompt: Write a smart contract on the Base chain to facilitate community-driven token distribution for Bitcoin on Base, adhering to the CC0 license principles.
Generated: DETERMINISTIC_e3c6ba20639b0bf3
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.0;

/**
 * @title CommunityDrivenTokenDistribution
 * @dev Smart contract to facilitate community-driven token distribution for Bitcoin on Base chain.
 */
contract CommunityDrivenTokenDistribution {
    // Token distribution details
    struct Distribution {
        address recipient;
        uint256 amount;
        bool distributed;
    }

    // Owner of the contract
    address public owner;

    // List of distributions
    Distribution[] public distributions;

    // Event emitted when distribution is created
    event DistributionCreated(address indexed recipient, uint256 amount);

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor sets the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a distribution.
     * @param _recipient Address of the recipient.
     * @param _amount Amount of tokens to distribute (in smallest unit).
     */
    function createDistribution(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than 0");

        // Add distribution to the list
        distributions.push(Distribution({
            recipient: _recipient,
            amount: _amount,
            distributed: false
        }));

        emit DistributionCreated(_recipient, _amount);
    }

    /**
     * @dev Function to distribute tokens for a specific distribution ID.
     * @param _distributionId ID of the distribution to execute.
     */
    function distributeTokens(uint256 _distributionId) external {
        require(_distributionId < distributions.length, "Invalid distribution ID");
        Distribution storage dist = distributions[_distributionId];
        require(!dist.distributed, "Tokens have already been distributed");
        require(dist.amount > 0, "Invalid distribution amount");

        // Distribute tokens
        dist.distributed = true;

        // Transfer tokens to recipient
        (bool success, ) = dist.recipient.call{value: dist.amount}("");
        require(success, "Token transfer failed");

        emit TokensDistributed(dist.recipient, dist.amount);
    }

    /**
     * @dev Function to get the total number of distributions created.
     * @return count Total number of distributions.
     */
    function getDistributionCount() external view returns (uint256 count) {
        return distributions.length;
    }

    /**
     * @dev Function to retrieve details of a specific distribution.
     * @param _distributionId ID of the distribution to retrieve.
     * @return recipient Address of the recipient.
     * @return amount Amount of tokens to distribute.
     * @return distributed True if tokens have been distributed, false otherwise.
     */
    function getDistributionDetails(uint256 _distributionId) external view returns (
        address recipient,
        uint256 amount,
        bool distributed
    ) {
        require(_distributionId < distributions.length, "Invalid distribution ID");
        Distribution memory dist = distributions[_distributionId];
        return (dist.recipient, dist.amount, dist.distributed);
    }

    /**
     * @dev Function to receive Ether for distribution.
     * Contract must hold sufficient balance for token distribution.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw Ether from the contract (onlyOwner).
     * @param _amount Amount to withdraw.
     */
    function withdraw(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        (bool success, ) = owner.call{value: _amount}("");
        require(success, "Withdraw failed");
    }
}
```
