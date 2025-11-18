"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-mocafoundation.pages.dev
Prompt: Create a smart contract in Solidity for distributing $MOCA tokens based on eligibility criteria described by the Moca Foundation.
Generated: DETERMINISTIC_4896d97cf15c7187
Batch ID: 20250612_150927
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
 * @title MOCA Token Distribution Smart Contract
 * @dev This contract handles the distribution of $MOCA tokens based on eligibility criteria.
 */
contract MocaTokenDistribution {
    // Address of the MOCA ERC20 token contract
    address public mocaTokenAddress;

    // Owner of the contract (typically the Moca Foundation)
    address public owner;

    // Mapping to track eligibility and allocation
    mapping(address => uint256) public allocations;

    // Event emitted when tokens are distributed
    event TokensDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor - sets the initial values
    constructor(address _mocaTokenAddress) {
        require(_mocaTokenAddress != address(0), "Invalid token address");
        mocaTokenAddress = _mocaTokenAddress;
        owner = msg.sender; // Set the deployer as the contract owner
    }

    /**
     * @dev Updates the eligibility and allocation for a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of $MOCA tokens allocated to the recipient.
     */
    function updateAllocation(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Allocation must be greater than zero");
        allocations[recipient] = amount;
    }

    /**
     * @dev Distributes $MOCA tokens to eligible recipients.
     * Recipients must have a non-zero allocation.
     */
    function distributeTokens() external {
        uint256 allocation = allocations[msg.sender];
        require(allocation > 0, "No allocation available");

        allocations[msg.sender] = 0; // Reset the allocation to prevent re-entry attacks

        bool success = IERC20(mocaTokenAddress).transfer(msg.sender, allocation);
        require(success, "Token transfer failed");

        emit TokensDistributed(msg.sender, allocation);
    }

    /**
     * @dev Allows the owner to withdraw any tokens mistakenly sent to this contract.
     * @param tokenAddress The address of the token to withdraw.
     * @param recipient The address to send the withdrawn tokens to.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, address recipient, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        bool success = IERC20(tokenAddress).transfer(recipient, amount);
        require(success, "Token transfer failed");
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}

// Interface for standard ERC20 token functions
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
