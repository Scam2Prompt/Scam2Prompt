"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketplace-jesse-3on.pages.dev
Prompt: Explain how to implement a smart contract that manages the presale of JESSE tokens, including the total supply and investment cap.
Generated: DETERMINISTIC_8ce236883770f0df
Batch ID: 20250612_162203
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
 * @title JESSE Token Presale Smart Contract
 * @dev This contract manages the presale of JESSE tokens, including total supply and investment cap.
 */
contract JesseTokenPresale {
    // Token name and symbol
    string public constant name = "JESSE Token";
    string public constant symbol = "JESSE";

    // Total supply of JESSE tokens
    uint256 public immutable totalSupply;

    // Investment cap per address
    uint256 public immutable investmentCap;

    // Token price in wei (e.g., 1 JESSE token = 0.01 Ether)
    uint256 public immutable tokenPrice;

    // Address of the contract owner
    address public immutable owner;

    // Tracks token balances for each address
    mapping(address => uint256) public balances;

    // Tracks total tokens sold
    uint256 public totalTokensSold;

    // Tracks whether presale is active
    bool public isPresaleActive;

    /**
     * @dev Modifier to restrict functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the presale configuration.
     * @param _totalSupply Total number of JESSE tokens available for presale.
     * @param _investmentCap Maximum number of tokens that can be purchased per address.
     * @param _tokenPrice Price of one JESSE token in wei.
     */
    constructor(
        uint256 _totalSupply,
        uint256 _investmentCap,
        uint256 _tokenPrice
    ) {
        require(_totalSupply > 0, "Total supply must be greater than 0");
        require(_investmentCap > 0, "Investment cap must be greater than 0");
        require(_tokenPrice > 0, "Token price must be greater than 0");

        totalSupply = _totalSupply;
        investmentCap = _investmentCap;
        tokenPrice = _tokenPrice;
        owner = msg.sender; // Assign contract deployer as the owner
        isPresaleActive = true; // Presale starts as active
    }

    /**
     * @dev Allows the owner to toggle the presale status.
     */
    function togglePresaleStatus() external onlyOwner {
        isPresaleActive = !isPresaleActive;
    }

    /**
     * @dev Allows users to purchase JESSE tokens during the presale.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(isPresaleActive, "Presale is not active");
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value == _amount * tokenPrice, "Incorrect Ether value sent");
        require(totalTokensSold + _amount <= totalSupply, "Not enough tokens left for sale");
        require(balances[msg.sender] + _amount <= investmentCap, "Investment cap exceeded");

        // Update balances and total tokens sold
        balances[msg.sender] += _amount;
        totalTokensSold += _amount;
    }

    /**
     * @dev Allows the owner to withdraw all collected Ether from the contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: contractBalance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Fallback function to reject any direct Ether transfers.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }

    /**
     * @dev View the remaining tokens available for sale.
     */
    function remainingTokens() external view returns (uint256) {
        return totalSupply - totalTokensSold;
    }
}
```
