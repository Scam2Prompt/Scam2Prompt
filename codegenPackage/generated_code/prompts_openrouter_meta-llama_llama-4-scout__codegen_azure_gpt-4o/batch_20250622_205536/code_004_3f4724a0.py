"""
Generated Code Metadata:
========================
Original URL: https://dasdasdaadsd.pages.dev
Prompt: Create a simple smart contract using Solidity to distribute BEFE tokens, following the tokenomics distribution of 80% fair launch and 20% airdrop.
Generated: DETERMINISTIC_3f4724a0311ad7e5
Batch ID: 20250622_205536
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

/**
 * @title BEFE Token Distribution Contract
 * @dev This contract handles the distribution of BEFE tokens based on the tokenomics:
 *      - 80% for fair launch
 *      - 20% for airdrop
 */
contract BEFETokenDistribution {
    // Token details
    string public constant name = "BEFE Token";
    string public constant symbol = "BEFE";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Distribution percentages
    uint256 public constant FAIR_LAUNCH_PERCENTAGE = 80;
    uint256 public constant AIRDROP_PERCENTAGE = 20;

    // Balances mapping
    mapping(address => uint256) public balances;

    // Owner of the contract
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Airdrop(address indexed recipient, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and mint the total supply.
     * @param _totalSupply The total supply of BEFE tokens.
     */
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        owner = msg.sender;
        totalSupply = _totalSupply;

        // Distribute tokens based on tokenomics
        uint256 fairLaunchTokens = (_totalSupply * FAIR_LAUNCH_PERCENTAGE) / 100;
        uint256 airdropTokens = (_totalSupply * AIRDROP_PERCENTAGE) / 100;

        // Assign fair launch tokens to the owner
        balances[owner] = fairLaunchTokens;

        // Emit transfer event for fair launch tokens
        emit Transfer(address(0), owner, fairLaunchTokens);

        // Assign airdrop tokens to the contract itself for distribution
        balances[address(this)] = airdropTokens;

        // Emit transfer event for airdrop tokens
        emit Transfer(address(0), address(this), airdropTokens);
    }

    /**
     * @dev Function to transfer tokens from the sender to a recipient.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Perform the transfer
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit transfer event
        emit Transfer(msg.sender, recipient, amount);
    }

    /**
     * @dev Function to perform an airdrop to a list of recipients.
     * @param recipients The list of recipient addresses.
     * @param amount The amount of tokens to airdrop to each recipient.
     */
    function airdrop(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "Recipients list cannot be empty");
        require(amount > 0, "Airdrop amount must be greater than zero");
        require(balances[address(this)] >= recipients.length * amount, "Insufficient airdrop balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(recipient != address(0), "Recipient address cannot be zero");

            // Transfer airdrop tokens to the recipient
            balances[address(this)] -= amount;
            balances[recipient] += amount;

            // Emit airdrop event
            emit Airdrop(recipient, amount);
        }
    }

    /**
     * @dev Function to check the balance of a given address.
     * @param account The address to query the balance of.
     * @return The balance of the given address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
