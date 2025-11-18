"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bamboomeme.pages.dev
Prompt: Create a Solidity contract for a meme token that includes a community reward system, inspired by `$BAMBOO`'s claim reward feature.
Generated: DETERMINISTIC_2080fe14c5693ec8
Batch ID: 20250612_152240
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
 * @title MemeToken
 * @dev A token contract inspired by $BAMBOO, implementing a community reward feature.
 */
contract MemeToken {
    // ERC20 token parameters
    string public name = "MemeToken";
    string public symbol = "MEME";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Address balances
    mapping(address => uint256) private balances;

    // Allowances for ERC20 transfers
    mapping(address => mapping(address => uint256)) private allowances;

    // Rewards mapping for community members
    mapping(address => uint256) public rewards;

    // Owner of the contract
    address public owner;

    // Event declarations
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event RewardClaimed(address indexed claimant, uint256 amount);
    event RewardDistributed(address indexed member, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Modifier to validate address
    modifier validAddress(address _address) {
        require(_address != address(0), "Invalid address");
        _;
    }

    // Constructor to initialize the contract with a total supply
    constructor(uint256 _initialSupply) {
        owner = msg.sender;
        totalSupply = _initialSupply * (10 ** uint256(decimals));
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    // ERC20 balanceOf function
    function balanceOf(address _account) external view returns (uint256) {
        return balances[_account];
    }

    // ERC20 transfer function
    function transfer(address _to, uint256 _amount) external validAddress(_to) returns (bool) {
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        _transfer(msg.sender, _to, _amount);
        return true;
    }

    // ERC20 transferFrom function
    function transferFrom(
        address _from,
        address _to,
        uint256 _amount
    ) external validAddress(_to) returns (bool) {
        require(balances[_from] >= _amount, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _amount, "Transfer not allowed");
        allowances[_from][msg.sender] -= _amount;
        _transfer(_from, _to, _amount);
        return true;
    }

    // ERC20 approve function
    function approve(address _spender, uint256 _amount) external validAddress(_spender) returns (bool) {
        allowances[msg.sender][_spender] = _amount;
        emit Approval(msg.sender, _spender, _amount);
        return true;
    }

    // ERC20 allowance function
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    // Internal function to handle transfers
    function _transfer(
        address _from,
        address _to,
        uint256 _amount
    ) internal {
        balances[_from] -= _amount;
        balances[_to] += _amount;
        emit Transfer(_from, _to, _amount);
    }

    // Function to distribute rewards to community members
    function distributeRewards(address _member, uint256 _amount) external onlyOwner validAddress(_member) {
        require(balances[owner] >= _amount, "Insufficient token balance for rewards");
        rewards[_member] += _amount;
        emit RewardDistributed(_member, _amount);
    }

    // Function for members to claim their rewards
    function claimRewards() external {
        uint256 rewardAmount = rewards[msg.sender];
        require(rewardAmount > 0, "No rewards available to claim");
        require(balances[owner] >= rewardAmount, "Insufficient token balance for rewards");

        rewards[msg.sender] = 0; // Reset rewards to prevent re-claiming
        _transfer(owner, msg.sender, rewardAmount);

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to burn tokens
    function burn(uint256 _amount) external {
        require(balances[msg.sender] >= _amount, "Insufficient balance to burn");
        balances[msg.sender] -= _amount;
        totalSupply -= _amount;

        emit Transfer(msg.sender, address(0), _amount);
    }
}
```
