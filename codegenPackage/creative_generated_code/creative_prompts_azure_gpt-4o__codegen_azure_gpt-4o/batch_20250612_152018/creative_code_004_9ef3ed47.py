"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://asx-capital.pages.dev
Prompt: Write a Solidity function that calculates and distributes yield from DeFi investments to $ASX token holders, ensuring safety mechanisms for risk mitigation as outlined on the ASX Capital site.
Generated: DETERMINISTIC_9ef3ed47bf190f71
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title YieldDistributor
 * @dev Contract to calculate and distribute yield from DeFi investments to $ASX token holders.
 */
contract YieldDistributor {
    // Mapping to track $ASX token holder balances
    mapping(address => uint256) public asxTokenBalances;

    // Mapping to track accumulated yield for each address
    mapping(address => uint256) public yieldBalances;

    // Total supply of $ASX tokens
    uint256 public totalASXSupply;

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized.");
        _;
    }

    // Event to log yield distribution
    event YieldDistributed(address indexed holder, uint256 yieldAmount);

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to update a token holder's balance.
     * @param holder Address of the token holder.
     * @param balance New balance for the token holder.
     */
    function updateTokenBalance(address holder, uint256 balance) external onlyOwner {
        totalASXSupply -= asxTokenBalances[holder];
        asxTokenBalances[holder] = balance;
        totalASXSupply += balance;
    }

    /**
     * @dev Function to calculate and distribute yield.
     * @param totalYield Total yield generated from DeFi investments.
     */
    function distributeYield(uint256 totalYield) external onlyOwner {
        require(totalYield > 0, "Yield must be greater than zero.");
        require(totalASXSupply > 0, "No $ASX token holders exist.");

        for (address holder : getTokenHolders()) {
            uint256 holderBalance = asxTokenBalances[holder];
            uint256 yieldShare = (totalYield * holderBalance) / totalASXSupply;
            yieldBalances[holder] += yieldShare;
            emit YieldDistributed(holder, yieldShare);
        }
    }

    /**
     * @dev Function to allow token holders to withdraw their accumulated yield.
     */
    function withdrawYield() external {
        uint256 yieldAmount = yieldBalances[msg.sender];
        require(yieldAmount > 0, "No yield to withdraw.");

        yieldBalances[msg.sender] = 0;
        (bool success, ) = msg.sender.call{value: yieldAmount}("");
        require(success, "Yield transfer failed.");
    }

    /**
     * @dev Helper function to fetch all token holders. 
     * NOTE: This is a placeholder, as dynamic arrays of holders are not feasible in Solidity without external solutions.
     * Production contracts should implement this differently, e.g., using off-chain indexing or event-driven tracking.
     */
    function getTokenHolders() private view returns (address[] memory) {
        // Placeholder - Replace with actual logic to fetch token holders
        address[] memory holders = new address[](0);
        return holders;
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
