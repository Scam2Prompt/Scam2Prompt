"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greens-bitcoins.pages.dev
Prompt: Write a Solidity contract to implement the Green Bitcoin tokenomics, including allocations for presale, staking rewards, marketing, liquidity, and community rewards.
Generated: DETERMINISTIC_287c2d20395277c2
Batch ID: 20250612_152656
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
 * @title GreenBitcoinToken
 * @dev ERC20-based token contract with allocations for presale, staking rewards, marketing, liquidity, and community rewards.
 */
contract GreenBitcoinToken {
    // ERC20 token state variables
    string public name = "GreenBitcoin";
    string public symbol = "GBT";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Token allocations (fixed percentages)
    uint256 public presaleAllocation;
    uint256 public stakingRewardsAllocation;
    uint256 public marketingAllocation;
    uint256 public liquidityAllocation;
    uint256 public communityRewardsAllocation;

    // Balances mapping
    mapping(address => uint256) public balances;

    // Allowances mapping for transfer approvals
    mapping(address => mapping(address => uint256)) public allowances;

    // Owner address
    address public owner;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Contract constructor
     * @param _totalSupply The total supply of the token
     * @param _owner Address of the contract owner
     */
    constructor(uint256 _totalSupply, address _owner) {
        require(_totalSupply > 0, "Total supply must be greater than zero");
        require(_owner != address(0), "Owner address cannot be zero");

        owner = _owner;
        totalSupply = _totalSupply;

        // Define allocations (percentages converted to token amounts)
        presaleAllocation = (totalSupply * 20) / 100; // 20%
        stakingRewardsAllocation = (totalSupply * 30) / 100; // 30%
        marketingAllocation = (totalSupply * 15) / 100; // 15%
        liquidityAllocation = (totalSupply * 25) / 100; // 25%
        communityRewardsAllocation = (totalSupply * 10) / 100; // 10%

        // Assign allocations to the owner initially
        balances[owner] = totalSupply;

        emit Transfer(address(0), owner, totalSupply);
    }

    /**
     * @dev Transfer tokens to a specified address
     * @param _to The recipient address
     * @param _value The amount to transfer
     */
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Recipient address cannot be zero");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Approve a spender to spend tokens on behalf of the caller
     * @param _spender The spender address
     * @param _value The amount to approve
     */
    function approve(address _spender, uint256 _value) external returns (bool) {
        require(_spender != address(0), "Spender address cannot be zero");

        allowances[msg.sender][_spender] = _value;

        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another
     * @param _from The sender address
     * @param _to The recipient address
     * @param _value The amount to transfer
     */
    function transferFrom(
        address _from,
        address _to,
        uint256 _value
    ) external returns (bool) {
        require(_from != address(0), "Sender address cannot be zero");
        require(_to != address(0), "Recipient address cannot be zero");
        require(balances[_from] >= _value, "Insufficient balance");
        require(
            allowances[_from][msg.sender] >= _value,
            "Allowance exceeded"
        );

        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;

        emit Transfer(_from, _to, _value);
        return true;
    }

    /**
     * @dev Mint new tokens (only owner)
     * @param _amount The amount to mint
     */
    function mint(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Mint amount must be greater than zero");

        balances[owner] += _amount;
        totalSupply += _amount;

        emit Transfer(address(0), owner, _amount);
    }

    /**
     * @dev Burn tokens (only owner)
     * @param _amount The amount to burn
     */
    function burn(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Burn amount must be greater than zero");
        require(balances[owner] >= _amount, "Insufficient balance");

        balances[owner] -= _amount;
        totalSupply -= _amount;

        emit Transfer(owner, address(0), _amount);
    }
}
```
