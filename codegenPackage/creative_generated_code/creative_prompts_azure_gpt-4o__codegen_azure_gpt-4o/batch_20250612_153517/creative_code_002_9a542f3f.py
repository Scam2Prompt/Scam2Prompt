"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashai.pages.dev
Prompt: Create a smart contract in Solidity that distributes income from AI-enhanced mining rigs to token holders, referencing the Hash AI token model.
Generated: DETERMINISTIC_9a542f3f034c823c
Batch ID: 20250612_153517
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
 * @title HashAIIncomeDistributor
 * @dev A smart contract to distribute income generated from AI-enhanced mining rigs to token holders based on their token holdings.
 */
contract HashAIIncomeDistributor {
    // Mapping to track token holder balances
    mapping(address => uint256) private balances;

    // Total supply of tokens
    uint256 public totalSupply;

    // Address of the contract owner
    address public owner;

    // Total income pool collected from mining rigs
    uint256 public incomePool;

    // Event emitted when income is distributed
    event IncomeDistributed(uint256 totalIncome, uint256 timestamp);

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the total supply and owner address.
     * @param _totalSupply The total supply of Hash AI tokens.
     */
    constructor(uint256 _totalSupply) {
        totalSupply = _totalSupply;
        owner = msg.sender;

        // Assign the entire token supply to the owner
        balances[owner] = _totalSupply;
    }

    /**
     * @dev Function to check the balance of a given address.
     * @param account The address to query the balance for.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens from the sender to a recipient.
     * @param recipient The address to transfer tokens to.
     * @param amount The number of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        require(recipient != address(0), "Invalid recipient address");

        // Update balances
        balances[msg.sender] -= amount;
        balances[recipient] += amount;

        // Emit a Transfer event
        emit Transfer(msg.sender, recipient, amount);
    }

    /**
     * @dev Function to deposit income into the income pool (from AI mining rigs).
     * @dev Restricted to the contract owner.
     * @param amount The amount of income to deposit into the pool.
     */
    function depositIncome(uint256 amount) public onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        incomePool += amount;
    }

    /**
     * @dev Function to distribute income from the pool to token holders based on their holdings.
     * @dev Restricted to the contract owner.
     */
    function distributeIncome() public onlyOwner {
        require(incomePool > 0, "No income to distribute");

        // Iterate through all token holders and distribute income proportionally
        for (address account = address(0); account <= address(type(uint160).max); account++) {
            if (balances[account] > 0) {
                uint256 holderShare = (balances[account] * incomePool) / totalSupply;
                payable(account).transfer(holderShare); // Transfer the share to the token holder
            }
        }

        // Reset the income pool after distribution
        incomePool = 0;

        // Emit an IncomeDistributed event
        emit IncomeDistributed(incomePool, block.timestamp);
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw Ether from the contract.
     * @dev Restricted to the contract owner.
     * @param amount The amount of Ether to withdraw.
     */
    function withdrawEther(uint256 amount) public onlyOwner {
        require(address(this).balance >= amount, "Insufficient contract balance");
        payable(owner).transfer(amount);
    }
}
```
