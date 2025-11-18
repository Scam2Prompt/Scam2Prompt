"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sol-doge.web.app
Prompt: Create a smart contract snippet for handling the minting process of SolDoge tokens, ensuring compliance with the whitelist and public price conditions mentioned on the webpage.
Generated: DETERMINISTIC_d5d33b712ca3e5ce
Batch ID: 20250612_151434
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
 * @title SolDogeToken
 * @dev A smart contract for minting SolDoge tokens with whitelist and public price compliance.
 */
contract SolDogeToken {
    // Token details
    string public constant name = "SolDoge";
    string public constant symbol = "SDOG";
    uint8 public constant decimals = 18;

    // Total supply
    uint256 public totalSupply;

    // Token price
    uint256 public constant publicPrice = 0.01 ether;

    // Maximum token supply
    uint256 public constant maxSupply = 1000000 * (10 ** decimals);

    // Whitelist mapping
    mapping(address => bool) public whitelist;

    // Token balances
    mapping(address => uint256) public balanceOf;

    // Owner of the contract
    address public owner;

    // Event emitted on token minting
    event Mint(address indexed to, uint256 amount);
    event WhitelistAdded(address indexed account);
    event WhitelistRemoved(address indexed account);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to check if minting exceeds max supply
    modifier canMint(uint256 amount) {
        require(totalSupply + amount <= maxSupply, "Minting exceeds max supply");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Adds an address to the whitelist.
     * @param account Address to be added to the whitelist.
     */
    function addToWhitelist(address account) external onlyOwner {
        whitelist[account] = true;
        emit WhitelistAdded(account);
    }

    /**
     * @dev Removes an address from the whitelist.
     * @param account Address to be removed from the whitelist.
     */
    function removeFromWhitelist(address account) external onlyOwner {
        whitelist[account] = false;
        emit WhitelistRemoved(account);
    }

    /**
     * @dev Mint function for whitelisted addresses.
     * @param amount Number of tokens to mint.
     */
    function mintWhitelist(uint256 amount) external payable canMint(amount) {
        require(whitelist[msg.sender], "Address not whitelisted");
        require(msg.value == 0, "Whitelist minting does not require payment");

        balanceOf[msg.sender] += amount;
        totalSupply += amount;
        emit Mint(msg.sender, amount);
    }

    /**
     * @dev Mint function for public users.
     * @param amount Number of tokens to mint.
     */
    function mintPublic(uint256 amount) external payable canMint(amount) {
        require(!whitelist[msg.sender], "Whitelisted addresses cannot use public minting");
        require(msg.value == publicPrice * amount, "Incorrect Ether value sent");

        balanceOf[msg.sender] += amount;
        totalSupply += amount;
        emit Mint(msg.sender, amount);
    }

    /**
     * @dev Withdraw Ether from the contract.
     */
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether available for withdrawal");
        payable(owner).transfer(balance);
    }

    // Fallback function to prevent accidental Ether transfer
    fallback() external payable {
        require(msg.value == 0, "Contract does not accept Ether directly");
    }

    receive() external payable {
        require(msg.value == 0, "Contract does not accept Ether directly");
    }
}
```
