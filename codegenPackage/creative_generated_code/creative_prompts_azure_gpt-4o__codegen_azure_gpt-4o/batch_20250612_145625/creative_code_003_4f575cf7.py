"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoiindogsclub.pages.dev
Prompt: Create a smart contract on ERC20 for facilitating token purchases during the Bitcoin Dogs presale, ensuring compatibility with the BRC20 wallet claiming process.
Generated: DETERMINISTIC_4f575cf72be1d9b4
Batch ID: 20250612_145625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the ERC20 smart contract code for facilitating token purchases during the Bitcoin Dogs presale, ensuring compatibility with the BRC20 wallet claiming process. The code is written in Solidity, following best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title BitcoinDogsPresale
 * @dev An ERC20 token for the Bitcoin Dogs presale with functionality 
 *      for token purchases and compatibility for BRC20 wallet claiming process.
 */
contract BitcoinDogsPresale {
    // ERC20 standard variables
    string public name = "Bitcoin Dogs Token";
    string public symbol = "BDT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Presale-specific variables
    uint256 public tokenPrice = 0.001 ether; // Price per token in wei
    address public owner;
    bool public presaleActive = true;

    // Mapping to store balances
    mapping(address => uint256) public balanceOf;

    // Events for logging
    event Transfer(address indexed from, address indexed to, uint256 value);
    event TokensPurchased(address indexed purchaser, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event PresaleEnded();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleIsActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Constructor to initialize owner and token supply
    constructor(uint256 _totalSupply) {
        owner = msg.sender;
        totalSupply = _totalSupply * 10**decimals;
        balanceOf[address(this)] = totalSupply; // Assign total supply to contract
        emit Transfer(address(0), address(this), totalSupply);
    }

    /**
     * @dev Public function to purchase tokens during the presale.
     *      Ensures that the presale is active and sufficient tokens are available.
     */
    function purchaseTokens() public payable presaleIsActive {
        require(msg.value > 0, "Ether sent must be greater than zero");
        
        uint256 tokensToBuy = (msg.value * 10**decimals) / tokenPrice;
        require(balanceOf[address(this)] >= tokensToBuy, "Not enough tokens available for sale");

        balanceOf[address(this)] -= tokensToBuy;
        balanceOf[msg.sender] += tokensToBuy;

        emit Transfer(address(this), msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Function to allow BRC20-compatible wallet users to claim their tokens.
     *      This can be further customized with wallet verification if required.
     * @param claimer Address of the claimer
     * @param amount Amount of tokens to claim
     */
    function claimTokens(address claimer, uint256 amount) public onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf[address(this)] >= amount, "Not enough tokens available for claim");

        balanceOf[address(this)] -= amount;
        balanceOf[claimer] += amount;

        emit Transfer(address(this), claimer, amount);
        emit TokensClaimed(claimer, amount);
    }

    /**
     * @dev Function to end the presale. Only callable by the owner.
     *      This will deactivate the ability to purchase tokens.
     */
    function endPresale() public onlyOwner {
        presaleActive = false;
        emit PresaleEnded();
    }

    /**
     * @dev Owner can withdraw the collected Ether after presale ends.
     */
    function withdrawFunds() public onlyOwner {
        require(!presaleActive, "Cannot withdraw funds while presale is active");
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Fallback function: Ether transfers not allowed");
    }

    /**
     * @dev Receive function for handling Ether sent to the contract.
     */
    receive() external payable {
        purchaseTokens();
    }
}
```

> Ensure that the code is deployed and tested properly in a development environment like Remix or Hardhat before using it in production.
