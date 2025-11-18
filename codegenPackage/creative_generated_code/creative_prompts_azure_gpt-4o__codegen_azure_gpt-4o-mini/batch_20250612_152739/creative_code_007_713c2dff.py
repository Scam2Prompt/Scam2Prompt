"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoindapp.pages.dev
Prompt: Write Solidity code for a Proof-of-Stake (POS) token that incorporates eco-friendly features similar to Green Bitcoin’s energy-efficient blockchain model.
Generated: DETERMINISTIC_713c2dff02905a15
Batch ID: 20250612_152739
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
 * @title EcoFriendlyPOS
 * @dev A basic Proof-of-Stake token contract that incorporates eco-friendly features.
 */
contract EcoFriendlyPOS {
    // State variables
    string public name; // Name of the token
    string public symbol; // Symbol of the token
    uint8 public decimals; // Decimal places for the token
    uint256 public totalSupply; // Total supply of the token

    // Mapping from address to balance
    mapping(address => uint256) private balances;
    // Mapping from address to staking balance
    mapping(address => uint256) private stakingBalances;
    // Mapping to keep track of stakers
    mapping(address => bool) private stakers;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Staked(address indexed staker, uint256 value);
    event Unstaked(address indexed staker, uint256 value);
    
    // Constructor to set initial values
    constructor(string memory _name, string memory _symbol, uint8 _decimals, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply * 10 ** uint256(decimals);
        balances[msg.sender] = totalSupply; // Assign total supply to the contract deployer
    }

    /**
     * @dev Function to transfer tokens between accounts
     * @param _to The address of the recipient
     * @param _value The amount of tokens to transfer
     */
    function transfer(address _to, uint256 _value) public returns (bool) {
        require(_to != address(0), "Invalid recipient address");
        require(balances[msg.sender] >= _value, "Insufficient balance");

        balances[msg.sender] -= _value;
        balances[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /**
     * @dev Function to stake tokens
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(balances[msg.sender] >= _amount, "Insufficient balance to stake");
        require(_amount > 0, "Amount must be greater than zero");
        
        balances[msg.sender] -= _amount;
        stakingBalances[msg.sender] += _amount;
        stakers[msg.sender] = true;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Function to unstake tokens
     * @param _amount The amount of tokens to unstake
     */
    function unstake(uint256 _amount) public {
        require(stakingBalances[msg.sender] >= _amount, "Insufficient staked balance");
        require(_amount > 0, "Amount must be greater than zero");
        
        stakingBalances[msg.sender] -= _amount;
        balances[msg.sender] += _amount;

        // Check if the staker's staking balance is now zero and remove from stakers mapping
        if (stakingBalances[msg.sender] == 0) {
            stakers[msg.sender] = false;
        }

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Function to get the balance of tokens for a specific address
     * @param _owner The address to query the balance of
     * @return The balance of the requested address
     */
    function balanceOf(address _owner) public view returns (uint256) {
        return balances[_owner];
    }

    /**
     * @dev Function to get the staking balance of a specific address
     * @param _staker The address to query the staking balance of
     * @return The staking balance of the requested address
     */
    function stakingBalanceOf(address _staker) public view returns (uint256) {
        return stakingBalances[_staker];
    }

    /**
     * @dev Function to check if an address is a staker
     * @param _staker The address to check
     * @return True if the address is a staker, false otherwise
     */
    function isStaker(address _staker) public view returns (bool) {
        return stakers[_staker];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}
```
