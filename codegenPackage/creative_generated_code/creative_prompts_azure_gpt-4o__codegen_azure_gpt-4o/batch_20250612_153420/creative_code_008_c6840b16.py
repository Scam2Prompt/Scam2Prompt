"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefcom.pages.dev
Prompt: Create a Solidity contract for distributing BEEF tokens in an airdrop, ensuring that 10% of the total supply is allocated for this purpose.
Generated: DETERMINISTIC_c6840b163ea091d7
Batch ID: 20250612_153420
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
 * @title BeefTokenAirdrop
 * @dev This contract handles the distribution of BEEF tokens in an airdrop,
 *      ensuring 10% of the total supply is reserved for the purpose.
 */
contract BeefTokenAirdrop {
    // Token metadata
    string public constant name = "BeefToken";
    string public constant symbol = "BEEF";
    uint8 public constant decimals = 18;

    // Total supply of BEEF tokens
    uint256 public immutable totalSupply;

    // Owner of the contract
    address public owner;

    // Mapping to track token balances
    mapping(address => uint256) public balances;

    // Event emitted for an airdrop distribution
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the contract, sets the total supply, and assigns
     *      all tokens to the owner.
     * @param _totalSupply Total supply of the BEEF tokens (e.g., 1 million tokens).
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");

        owner = msg.sender;
        totalSupply = _totalSupply * (10**decimals);

        // Assign all tokens to the owner initially
        balances[owner] = totalSupply;
    }

    /**
     * @dev Distribute tokens to a list of recipients as part of the airdrop.
     * @param recipients Array of recipient addresses.
     * @param amountPerRecipient Amount of tokens to distribute to each recipient.
     */
    function distributeAirdrop(address[] calldata recipients, uint256 amountPerRecipient) external onlyOwner {
        require(recipients.length > 0, "No recipients specified");
        require(amountPerRecipient > 0, "Airdrop amount must be greater than zero");

        // Calculate the total amount to be distributed
        uint256 totalAirdropAmount = recipients.length * amountPerRecipient;

        // Ensure 10% of the total supply is available for the airdrop
        uint256 maxAirdropAllocation = (totalSupply * 10) / 100;
        require(totalAirdropAmount <= maxAirdropAllocation, "Exceeds airdrop allocation");

        // Ensure the owner has enough tokens for the airdrop
        require(balances[owner] >= totalAirdropAmount, "Insufficient balance for airdrop");

        // Distribute tokens to each recipient
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(recipient != address(0), "Invalid recipient address");

            // Transfer tokens
            balances[owner] -= amountPerRecipient;
            balances[recipient] += amountPerRecipient;

            // Emit event for the airdrop distribution
            emit AirdropDistributed(recipient, amountPerRecipient);
        }
    }

    /**
     * @dev View the balance of a specific account.
     * @param account Address of the account.
     * @return The balance of the account.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfer tokens from the owner's balance to another account.
     * @param recipient Address of the recipient.
     * @param amount Amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[owner] >= amount, "Insufficient balance for transfer");

        // Perform the transfer
        balances[owner] -= amount;
        balances[recipient] += amount;
    }
}
```
