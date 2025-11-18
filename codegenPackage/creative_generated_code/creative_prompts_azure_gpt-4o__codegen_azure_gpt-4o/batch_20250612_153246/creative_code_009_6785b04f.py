"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mollars-in.web.app
Prompt: Create a step-by-step guide for deploying a decentralized token like MOLLARS on the Ethereum blockchain, including presale setup and wallet integration.
Generated: DETERMINISTIC_6785b04f5b130ddd
Batch ID: 20250612_153246
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
 * @title MOLLARS Token Contract
 * @dev ERC20 compliant token for MOLLARS with presale functionality
 */
contract MOLLARS {
    // Token details
    string public constant name = "MOLLARS";
    string public constant symbol = "MOL";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    // Balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the token contract
    address public owner;

    // Presale-related variables
    uint256 public tokenPriceInWei; // Price per token during presale
    uint256 public presaleEndTime;
    bool public presaleActive;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event TokensPurchased(address indexed buyer, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier presaleActiveCheck() {
        require(presaleActive && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    /**
     * @dev Constructor to set the initial supply and owner
     * @param initialSupply The initial supply of tokens (in smallest unit)
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        totalSupply = initialSupply;
        balances[owner] = initialSupply;
        emit Transfer(address(0), owner, initialSupply);
    }

    /**
     * @dev Transfer tokens to a specific address
     * @param to The recipient address
     * @param amount The amount to transfer
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;
        balances[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approve an address to spend tokens on behalf of the owner
     * @param spender The address allowed to spend
     * @param amount The amount to approve
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another (via allowance)
     * @param from The sender address
     * @param to The recipient address
     * @param amount The amount to transfer
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Cannot transfer to zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        balances[from] -= amount;
        balances[to] += amount;
        allowances[from][msg.sender] -= amount;
        emit Transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Check the balance of a specific address
     * @param account The address to query
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Check the allowance of a spender for a specific owner
     * @param ownerAddr The address of the owner
     * @param spender The address of the spender
     */
    function allowance(address ownerAddr, address spender) public view returns (uint256) {
        return allowances[ownerAddr][spender];
    }

    /**
     * @dev Start the presale with a specific token price and duration
     * @param priceInWei The price per token (in Wei)
     * @param durationInSeconds The duration of the presale
     */
    function startPresale(uint256 priceInWei, uint256 durationInSeconds) external onlyOwner {
        require(!presaleActive, "Presale is already active");
        presaleActive = true;
        tokenPriceInWei = priceInWei;
        presaleEndTime = block.timestamp + durationInSeconds;
    }

    /**
     * @dev End the presale
     */
    function endPresale() external onlyOwner {
        presaleActive = false;
    }

    /**
     * @dev Buy tokens during the presale
     */
    function buyTokens() external payable presaleActiveCheck {
        require(msg.value > 0, "Ether value must be greater than zero");

        uint256 tokensToBuy = msg.value / tokenPriceInWei;
        require(balances[owner] >= tokensToBuy, "Insufficient tokens for presale");

        balances[owner] -= tokensToBuy;
        balances[msg.sender] += tokensToBuy;
        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    /**
     * @dev Withdraw Ether collected during the presale
     */
    function withdrawEther() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```
