"""
Generated Code Metadata:
========================
Original URL: https://node-sophon.com
Prompt: "Generate a simple smart contract using Solidity to interact with Sophon's blockchain, focusing on user-centric entertainment applications."
Generated: DETERMINISTIC_3e8b05dac9efd3a2
Batch ID: 20250622_210236
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
 * @title EntertainmentToken
 * @dev A simple ERC-20 token for user-centric entertainment applications on Sophon's blockchain
 */
contract EntertainmentToken {
    string public constant name = "EntertainmentToken";
    string public constant symbol = "ENT";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    
    address public owner;
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply * 10**uint256(decimals);
        balances[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @dev Transfer tokens to a specified address
     * @param to The address to transfer to
     * @param value The amount to be transferred
     */
    function transfer(address to, uint256 value) external returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(balances[msg.sender] >= value, "Insufficient balance");

        balances[msg.sender] -= value;
        balances[to] += value;
        emit Transfer(msg.sender, to, value);
        return true;
    }

    /**
     * @dev Approve the passed address to spend the specified amount of tokens on behalf of msg.sender
     * @param spender The address which will spend the funds
     * @param value The amount of tokens to be spent
     */
    function approve(address spender, uint256 value) external returns (bool) {
        allowances[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another
     * @param from The address which you want to send tokens from
     * @param to The address which you want to transfer to
     * @param value The amount of tokens to be transferred
     */
    function transferFrom(address from, address to, uint256 value) external returns (bool) {
        require(to != address(0), "Transfer to the zero address");
        require(balances[from] >= value, "Insufficient balance");
        require(allowances[from][msg.sender] >= value, "Allowance exceeded");

        balances[from] -= value;
        balances[to] += value;
        allowances[from][msg.sender] -= value;
        emit Transfer(from, to, value);
        return true;
    }

    /**
     * @dev Get the balance of the specified address
     * @param account The address to query the balance of
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Get the allowance of the specified spender
     * @param tokenOwner The address which owns the funds
     * @param spender The address which will spend the funds
     */
    function allowance(address tokenOwner, address spender) external view returns (uint256) {
        return allowances[tokenOwner][spender];
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param amount The amount of tokens to mint
     */
    function mint(uint256 amount) external onlyOwner {
        totalSupply += amount;
        balances[owner] += amount;
        emit Transfer(address(0), owner, amount);
    }

    /**
     * @dev Burn tokens (only owner)
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        require(balances[owner] >= amount, "Insufficient balance to burn");
        totalSupply -= amount;
        balances[owner] -= amount;
        emit Transfer(owner, address(0), amount);
    }

    /**
     * @dev Transfer ownership of the contract (only owner)
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}

/**
 * @title EntertainmentPlatform
 * @dev A simple entertainment platform contract for Sophon's blockchain
 */
contract EntertainmentPlatform {
    EntertainmentToken public token;
    uint256 public contentPrice = 100 * 10**18; // 100 ENT tokens
    address public platformOwner;

    struct Content {
        address creator;
        string title;
        string description;
        uint256 price;
        bool exists;
    }

    mapping(uint256 => Content) public contents;
    uint256 public contentCount;

    event ContentCreated(uint256 indexed contentId, address indexed creator, string title, string description, uint256 price);
    event ContentPurchased(uint256 indexed contentId, address indexed buyer, address indexed creator, uint256 price);

    modifier onlyOwner() {
        require(msg.sender == platformOwner, "Only owner can call this function");
        _;
    }

    constructor(address _tokenAddress) {
        platformOwner = msg.sender;
        token = EntertainmentToken(_tokenAddress);
    }

    /**
     * @dev Create new entertainment content
     * @param title The title of the content
     * @param description The description of the content
     * @param price The price in ENT tokens
     */
    function createContent(string memory title, string memory description, uint256 price) external {
        contentCount++;
        contents[contentCount] = Content({
            creator: msg.sender,
            title: title,
            description: description,
            price: price,
            exists: true
        });
        emit ContentCreated(contentCount, msg.sender, title, description, price);
    }

    /**
     * @dev Purchase entertainment content
     * @param contentId The ID of the content to purchase
     */
    function purchaseContent(uint256 contentId) external {
        Content storage content = contents[contentId];
        require(content.exists, "Content does not exist");
        require(token.transferFrom(msg.sender, content.creator, content.price), "Token transfer failed");

        emit ContentPurchased(contentId, msg.sender, content.creator, content.price);
    }

    /**
     * @dev Update content price (only owner)
     * @param newPrice The new price for content
     */
    function setContentPrice(uint256 newPrice) external onlyOwner {
        contentPrice = newPrice;
    }

    /**
     * @dev Transfer platform ownership (only owner)
     * @param newOwner The address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        platformOwner = newOwner;
    }
}
```
