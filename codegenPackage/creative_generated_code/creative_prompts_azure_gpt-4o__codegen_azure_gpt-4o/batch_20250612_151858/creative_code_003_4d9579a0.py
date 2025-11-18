"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletpads.web.app
Prompt: Create a smart contract for launching IDO projects on WalletPads, ensuring compatibility with its decentralized protocol.
Generated: DETERMINISTIC_4d9579a0ec77d5cf
Batch ID: 20250612_151858
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
 * @title WalletPads IDO Launch Contract
 * @dev A decentralized smart contract for launching Initial DEX Offerings (IDOs) on WalletPads.
 *      This contract is designed to be compatible with WalletPads' decentralized protocol.
 */

contract WalletPadsIDO {
    // Struct to store details about each IDO project
    struct IDOProject {
        address creator;           // Address of the project creator
        string name;               // Name of the IDO project
        string symbol;             // Symbol of the token
        uint256 totalSupply;       // Total supply of tokens
        uint256 tokenPrice;        // Price per token in wei
        uint256 startTime;         // Start time of the IDO (in UNIX timestamp)
        uint256 endTime;           // End time of the IDO (in UNIX timestamp)
        uint256 tokensSold;        // Tokens sold during the IDO
        bool isActive;             // Status of the IDO (active/inactive)
    }

    // Mapping to store IDOs by their unique ID
    mapping(uint256 => IDOProject) public idoProjects;

    // Counter for assigning unique IDs to IDO projects
    uint256 public idoCount;

    // Events to notify actions within the contract
    event IDOCreated(uint256 indexed idoId, address indexed creator, string name, string symbol, uint256 totalSupply, uint256 tokenPrice, uint256 startTime, uint256 endTime);
    event TokenPurchased(uint256 indexed idoId, address indexed buyer, uint256 amount, uint256 totalCost);

    /**
     * @dev Modifier to ensure that the IDO exists and is active.
     * @param idoId The ID of the IDO.
     */
    modifier isIDOActive(uint256 idoId) {
        require(idoProjects[idoId].isActive, "IDO is not active");
        require(block.timestamp >= idoProjects[idoId].startTime, "IDO has not started");
        require(block.timestamp <= idoProjects[idoId].endTime, "IDO has ended");
        _;
    }

    /**
     * @dev Function to create a new IDO project.
     * @param name Name of the IDO project.
     * @param symbol Symbol of the token.
     * @param totalSupply Total supply of tokens.
     * @param tokenPrice Price per token in wei.
     * @param startTime Start time of the IDO (in UNIX timestamp).
     * @param endTime End time of the IDO (in UNIX timestamp).
     */
    function createIDO(
        string memory name,
        string memory symbol,
        uint256 totalSupply,
        uint256 tokenPrice,
        uint256 startTime,
        uint256 endTime
    ) external {
        require(bytes(name).length > 0, "Project name is required");
        require(bytes(symbol).length > 0, "Token symbol is required");
        require(totalSupply > 0, "Total supply must be greater than 0");
        require(tokenPrice > 0, "Token price must be greater than 0");
        require(startTime > block.timestamp, "Start time must be in the future");
        require(endTime > startTime, "End time must be after start time");

        // Increment IDO count and assign a new ID
        idoCount++;

        // Create the new IDO project
        idoProjects[idoCount] = IDOProject({
            creator: msg.sender,
            name: name,
            symbol: symbol,
            totalSupply: totalSupply,
            tokenPrice: tokenPrice,
            startTime: startTime,
            endTime: endTime,
            tokensSold: 0,
            isActive: true
        });

        // Emit IDO creation event
        emit IDOCreated(idoCount, msg.sender, name, symbol, totalSupply, tokenPrice, startTime, endTime);
    }

    /**
     * @dev Function to purchase tokens from an active IDO project.
     * @param idoId The ID of the IDO.
     * @param amount The number of tokens to purchase.
     */
    function purchaseTokens(uint256 idoId, uint256 amount) external payable isIDOActive(idoId) {
        IDOProject storage ido = idoProjects[idoId];

        uint256 totalCost = amount * ido.tokenPrice;

        // Validate purchase conditions
        require(amount > 0, "Amount must be greater than 0");
        require(msg.value == totalCost, "Incorrect Ether value sent");
        require(ido.tokensSold + amount <= ido.totalSupply, "Not enough tokens available");

        // Update the IDO project's state
        ido.tokensSold += amount;

        // Transfer funds to the project creator
        payable(ido.creator).transfer(totalCost);

        // Emit token purchase event
        emit TokenPurchased(idoId, msg.sender, amount, totalCost);
    }

    /**
     * @dev Function to deactivate an IDO.
     * @param idoId The ID of the IDO.
     */
    function deactivateIDO(uint256 idoId) external {
        IDOProject storage ido = idoProjects[idoId];
        require(msg.sender == ido.creator, "Only the creator can deactivate the IDO");
        require(ido.isActive, "IDO is already inactive");

        ido.isActive = false;
    }

    /**
     * @dev Fallback function to reject unintended transactions.
     */
    fallback() external payable {
        revert("Fallback function not supported");
    }

    /**
     * @dev Receive function to reject plain Ether transfers.
     */
    receive() external payable {
        revert("Receive function not supported");
    }
}
```
