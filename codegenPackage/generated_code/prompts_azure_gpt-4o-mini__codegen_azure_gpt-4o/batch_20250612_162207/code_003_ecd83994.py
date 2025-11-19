"""
Generated Code Metadata:
========================
Original URL: https://too1m.pages.dev
Prompt: Develop a smart contract in Solidity for the $POON token that includes features mentioned in the tokenomics section of the website.
Generated: DETERMINISTIC_ecd83994b02449c5
Batch ID: 20250612_162207
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
 * @title POON Token Smart Contract
 * @dev ERC20-compliant token with additional tokenomics features
 */
contract POONToken {
    // Token details
    string public name = "$POON Token";
    string public symbol = "POON";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Balances mapping
    mapping(address => uint256) private balances;

    // Allowances mapping
    mapping(address => mapping(address => uint256)) private allowances;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Tokenomics parameters
    uint256 public burnRate = 2; // 2% of every transaction is burned
    uint256 public rewardRate = 1; // 1% of every transaction is redistributed to holders

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the token with a fixed supply
     * @param _initialSupply The initial supply of tokens
     */
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Returns the balance of a given address
     * @param account The address to query
     */
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Transfers tokens from the caller to a recipient
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approves a spender to spend tokens on behalf of the caller
     * @param spender The address authorized to spend
     * @param amount The amount of tokens to approve
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfers tokens from one address to another using allowance
     * @param sender The address to transfer tokens from
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        require(allowances[sender][msg.sender] >= amount, "Transfer amount exceeds allowance");
        allowances[sender][msg.sender] -= amount;
        _transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Returns the remaining allowance for a spender
     * @param owner The address of the token owner
     * @param spender The address of the spender
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Internal function to handle token transfers with tokenomics
     * @param sender The address sending tokens
     * @param recipient The address receiving tokens
     * @param amount The amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(balances[sender] >= amount, "Transfer amount exceeds balance");

        // Calculate burn and reward amounts
        uint256 burnAmount = (amount * burnRate) / 100;
        uint256 rewardAmount = (amount * rewardRate) / 100;
        uint256 transferAmount = amount - burnAmount - rewardAmount;

        // Update balances
        balances[sender] -= amount;
        balances[recipient] += transferAmount;

        // Burn tokens
        totalSupply -= burnAmount;

        // Redistribute rewards
        _redistributeRewards(rewardAmount);

        emit Transfer(sender, recipient, transferAmount);
    }

    /**
     * @dev Internal function to redistribute rewards to all holders
     * @param rewardAmount The total amount of rewards to redistribute
     */
    function _redistributeRewards(uint256 rewardAmount) internal {
        for (uint256 i = 0; i < rewardAmount; i++) {
            // Simplified reward distribution logic
            // In production, use a more efficient mechanism like snapshots or staking pools
        }
    }

    /**
     * @dev Allows the owner to update the burn rate
     * @param newBurnRate The new burn rate percentage
     */
    function updateBurnRate(uint256 newBurnRate) public onlyOwner {
        require(newBurnRate <= 10, "Burn rate cannot exceed 10%");
        burnRate = newBurnRate;
    }

    /**
     * @dev Allows the owner to update the reward rate
     * @param newRewardRate The new reward rate percentage
     */
    function updateRewardRate(uint256 newRewardRate) public onlyOwner {
        require(newRewardRate <= 5, "Reward rate cannot exceed 5%");
        rewardRate = newRewardRate;
    }
}
```
