"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aethirclaim-ifbf5prj-iamsorryman.4everland.app
Prompt: Generate a smart contract in Solidity for a presale token with a total supply of 100,000,000 tokens and a presale cap of 1000 ETH.
Generated: DETERMINISTIC_e8850ba803cd1c3d
Batch ID: 20250612_145436
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
 * @title PresaleToken
 * @dev A smart contract for a token presale with a total supply and ETH cap.
 */
contract PresaleToken {
    // Token details
    string public constant name = "PresaleToken";
    string public constant symbol = "PST";
    uint8 public constant decimals = 18;
    uint256 public constant totalSupply = 100_000_000 * (10 ** uint256(decimals)); // Total supply: 100,000,000 tokens

    // Presale parameters
    uint256 public constant presaleCap = 1000 ether; // Maximum ETH that can be collected
    uint256 public totalRaised; // Total ETH raised in the presale
    address public owner; // Contract owner address
    bool public presaleOpen; // Status of the presale

    // Balances mapping
    mapping(address => uint256) public balanceOf;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event PresaleOpened();
    event PresaleClosed();

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier whenPresaleOpen() {
        require(presaleOpen, "Presale is not open");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Set the deployer as the owner
        balanceOf[address(this)] = totalSupply; // Assign all tokens to the contract initially
    }

    /**
     * @dev Allows the owner to transfer contract ownership.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Opens the presale for participation.
     * Only the owner can call this function.
     */
    function openPresale() external onlyOwner {
        require(!presaleOpen, "Presale is already open");
        presaleOpen = true;
        emit PresaleOpened();
    }

    /**
     * @dev Closes the presale.
     * Only the owner can call this function.
     */
    function closePresale() external onlyOwner {
        require(presaleOpen, "Presale is already closed");
        presaleOpen = false;
        emit PresaleClosed();
    }

    /**
     * @dev Fallback function to handle ETH sent to the contract.
     * Buys tokens during the presale.
     */
    receive() external payable whenPresaleOpen {
        buyTokens();
    }

    /**
     * @dev Allows users to buy tokens during the presale.
     * The number of tokens is calculated based on the ETH sent.
     */
    function buyTokens() public payable whenPresaleOpen {
        require(msg.value > 0, "Must send ETH to purchase tokens");
        require(totalRaised + msg.value <= presaleCap, "Exceeds presale cap");

        // Token price: 1 ETH = 1000 tokens
        uint256 tokensToBuy = msg.value * 1000;

        // Ensure the contract has enough tokens to sell
        require(balanceOf[address(this)] >= tokensToBuy, "Not enough tokens available");

        // Update balances and total raised
        balanceOf[address(this)] -= tokensToBuy;
        balanceOf[msg.sender] += tokensToBuy;
        totalRaised += msg.value;

        emit TokensPurchased(msg.sender, tokensToBuy, msg.value);
    }

    /**
     * @dev Allows the owner to withdraw the ETH raised in the presale.
     * Only callable after the presale has ended.
     */
    function withdrawFunds() external onlyOwner {
        require(!presaleOpen, "Presale must be closed to withdraw funds");
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Allows the owner to withdraw unsold tokens after the presale is closed.
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleOpen, "Presale must be closed to withdraw tokens");
        uint256 unsoldTokens = balanceOf[address(this)];
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        balanceOf[address(this)] -= unsoldTokens;
        balanceOf[owner] += unsoldTokens;
    }
}
```
