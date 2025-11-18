"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poodlana-token.pages.dev
Prompt: Provide a Solidity smart contract snippet for a memecoin presale similar to Poodlana, ensuring token distribution is 100% unlocked from day one with no lock-ups or vesting periods.
Generated: DETERMINISTIC_7dcc74e34dcaf77f
Batch ID: 20250612_151343
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
 * @title MemecoinPresale
 * @notice A smart contract for managing a memecoin presale with 100% unlocked token distribution.
 */
contract MemecoinPresale {
    // Token-related variables
    string public constant name = "Memecoin";
    string public constant symbol = "MEME";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Mapping for tracking balances
    mapping(address => uint256) public balanceOf;

    // Presale-related variables
    uint256 public constant presaleRate = 1000; // Number of MEME tokens per 1 ETH
    address public owner;

    // Event declarations
    event TokensPurchased(address indexed buyer, uint256 ethSpent, uint256 tokensReceived);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Constructor for initializing the contract
    constructor(uint256 _totalSupply) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        owner = msg.sender; // Set the deployer as the contract owner
        totalSupply = _totalSupply;
        balanceOf[address(this)] = totalSupply; // Allocate entire supply to the contract
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Allows users to purchase MEME tokens during the presale.
     */
    function buyTokens() external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        uint256 tokensToPurchase = msg.value * presaleRate;
        require(balanceOf[address(this)] >= tokensToPurchase, "Not enough tokens available for sale");

        // Transfer tokens to the buyer
        balanceOf[address(this)] -= tokensToPurchase;
        balanceOf[msg.sender] += tokensToPurchase;

        emit TokensPurchased(msg.sender, msg.value, tokensToPurchase);
    }

    /**
     * @notice Allows the owner to withdraw collected ETH from the presale contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No ETH available for withdrawal");

        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "ETH withdrawal failed");
    }

    /**
     * @notice Allows the owner to transfer ownership of the contract.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @notice Fallback function to handle direct ETH transfers to the contract.
     */
    receive() external payable {
        buyTokens(); // Automatically buy tokens when ETH is sent directly to the contract
    }
}
```
