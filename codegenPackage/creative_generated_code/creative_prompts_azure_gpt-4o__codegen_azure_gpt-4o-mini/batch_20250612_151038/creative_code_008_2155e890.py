"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pacmoon-8ko.pages.dev
Prompt: Create a smart contract for managing airdrop events in a cryptocurrency ecosystem, referencing the "Pacmoon" airdrop functionality.
Generated: DETERMINISTIC_2155e890aba4dfe1
Batch ID: 20250612_151038
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for security and standard functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AirdropManager
 * @dev Smart contract for managing airdrop events in a cryptocurrency ecosystem
 */
contract AirdropManager is Ownable {
    // Token that will be used for airdrops
    IERC20 public token;

    // Structure to define the details of an airdrop event
    struct Airdrop {
        uint256 amountPerRecipient;  // Amount of tokens each recipient will receive
        address[] recipients;         // List of recipients for the airdrop
        bool executed;               // Status of the airdrop execution
    }

    // Mapping to store airdrop events by ID
    mapping(uint256 => Airdrop) public airdrops;
    uint256 public airdropCount; // Counter for airdrop events

    // Event emitted when an airdrop is created
    event AirdropCreated(uint256 indexed airdropId, uint256 amountPerRecipient, address[] recipients);

    // Event emitted when an airdrop is executed
    event AirdropExecuted(uint256 indexed airdropId);

    /**
     * @dev Constructor to initialize the contract with the token to be used for airdrops
     * @param _token Address of the ERC20 token to be used for the airdrop
     */
    constructor(IERC20 _token) {
        require(address(_token) != address(0), "Token address cannot be zero");
        token = _token;
    }

    /**
     * @dev Create a new airdrop event
     * @param amountPerRecipient Amount of tokens each recipient will receive
     * @param recipients Array of recipient addresses
     * Emits an {AirdropCreated} event.
     */
    function createAirdrop(uint256 amountPerRecipient, address[] calldata recipients) external onlyOwner {
        require(amountPerRecipient > 0, "Amount per recipient must be greater than zero");
        require(recipients.length > 0, "At least one recipient is required");

        airdropCount++;
        airdrops[airdropCount] = Airdrop({
            amountPerRecipient: amountPerRecipient,
            recipients: recipients,
            executed: false
        });

        emit AirdropCreated(airdropCount, amountPerRecipient, recipients);
    }

    /**
     * @dev Execute a previously created airdrop event
     * @param airdropId ID of the airdrop to execute
     */
    function executeAirdrop(uint256 airdropId) external onlyOwner {
        Airdrop storage airdrop = airdrops[airdropId];

        require(!airdrop.executed, "Airdrop has already been executed");
        require(airdrop.recipients.length > 0, "No recipients for this airdrop");

        uint256 totalAmount = airdrop.amountPerRecipient * airdrop.recipients.length;

        // Ensure the contract has enough tokens to execute the airdrop
        require(token.balanceOf(address(this)) >= totalAmount, "Insufficient balance for airdrop");

        // Distribute tokens to each recipient
        for (uint256 i = 0; i < airdrop.recipients.length; i++) {
            address recipient = airdrop.recipients[i];
            require(recipient != address(0), "Invalid recipient address");
            
            // Transfer tokens to recipient
            token.transfer(recipient, airdrop.amountPerRecipient);
        }

        airdrop.executed = true; // Mark the airdrop as executed

        emit AirdropExecuted(airdropId);
    }

    /**
     * @dev Allow the contract to receive ERC20 tokens for airdrops
     * @param amount Amount of tokens to withdraw
     * @param to Address to send the tokens to
     */
    function withdrawTokens(uint256 amount, address to) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the specified address
        token.transfer(to, amount);
    }
}
```
