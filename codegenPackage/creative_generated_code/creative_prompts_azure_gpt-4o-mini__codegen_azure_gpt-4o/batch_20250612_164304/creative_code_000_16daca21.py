"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumbull.pages.dev
Prompt: Generate a simple smart contract for a meme coin similar to $EBULL that emphasizes community engagement and charity donations.
Generated: DETERMINISTIC_16daca21f465f954
Batch ID: 20250612_164304
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
 * @title MemeCoin
 * @dev A simple ERC20 token for community engagement and charity donations.
 */
contract MemeCoin {
    // Token metadata
    string public name = "MemeCoin";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to track balances
    mapping(address => uint256) private balances;

    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Charity wallet address
    address public charityAddress;

    // Fee settings (e.g., percentage for charity)
    uint256 public charityFeePercent = 2; // 2% of every transfer goes to charity

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event CharityAddressUpdated(address indexed previousAddress, address indexed newAddress);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to limit access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor. Sets the total supply, owner, and initial charity address.
     * @param _initialSupply The initial supply of tokens.
     * @param _charityAddress The initial charity wallet address.
     */
    constructor(uint256 _initialSupply, address _charityAddress) {
        require(_charityAddress != address(0), "Invalid charity address");
        owner = msg.sender;
        charityAddress = _charityAddress;
        totalSupply = _initialSupply * (10**decimals);
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address.
     * @param account The address to query the balance for.
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens to a specified address, applying the charity fee.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Allows a spender to spend tokens on behalf of the owner.
     * @param spender The address authorized to spend.
     * @param amount The amount authorized to spend.
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens on behalf of an owner, applying the charity fee.
     * @param from The address from which tokens will be transferred.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     */
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(allowances[from][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[from][msg.sender] -= amount;
        _transfer(from, to, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of a spender for a given owner.
     * @param owner The address of the owner.
     * @param spender The address authorized to spend.
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to transfer tokens, applying the charity fee.
     * @param from The sender address.
     * @param to The recipient address.
     * @param amount The amount to transfer.
     */
    function _transfer(address from, address to, uint256 amount) internal {
        require(to != address(0), "Transfer to the zero address");
        require(balances[from] >= amount, "Transfer amount exceeds balance");

        uint256 charityFee = (amount * charityFeePercent) / 100;
        uint256 transferAmount = amount - charityFee;

        balances[from] -= amount;
        balances[charityAddress] += charityFee;
        balances[to] += transferAmount;

        emit Transfer(from, charityAddress, charityFee);
        emit Transfer(from, to, transferAmount);
    }

    /**
     * @dev Updates the charity wallet address.
     * @param newCharityAddress The new charity wallet address.
     */
    function updateCharityAddress(address newCharityAddress) public onlyOwner {
        require(newCharityAddress != address(0), "Invalid charity address");
        emit CharityAddressUpdated(charityAddress, newCharityAddress);
        charityAddress = newCharityAddress;
    }

    /**
     * @dev Transfers ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Invalid owner address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }
}
```
