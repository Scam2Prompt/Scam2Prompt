"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wolfyyy.pages.dev
Prompt: Create a smart contract in Solidity that incorporates the governance token WOOL, allowing users to breed Wolves and Sheep while managing land resources as described in Wolf Game.
Generated: DETERMINISTIC_9b754c3308174a7c
Batch ID: 20250612_151310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/// @title Wolf Game Contract
/// @notice This contract implements a governance token (WOOL) and allows users to breed Wolves and Sheep.
/// @dev All interactions are managed on-chain with proper access control and validation.

contract WolfGame {
    // Governance token (WOOL)
    string public constant tokenName = "WOOL";
    string public constant tokenSymbol = "WOOL";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Owner of the contract
    address public owner;

    // Land resources
    uint256 public maxLandResources;
    uint256 public availableLandResources;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Breeding(address indexed breeder, string animalType, uint256 resourceCost);

    // Constructor
    constructor(uint256 _initialSupply, uint256 _maxLandResources) {
        owner = msg.sender; // Set the deployer as the owner
        totalSupply = _initialSupply * 10**decimals; // Set initial supply of WOOL
        balances[owner] = totalSupply; // Assign all tokens to the owner
        maxLandResources = _maxLandResources;
        availableLandResources = _maxLandResources;
    }

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // ERC20 Functions

    /// @notice Transfers WOOL tokens to another address
    /// @param _to Recipient address
    /// @param _value Amount of tokens to transfer
    function transfer(address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balances[msg.sender] >= _value, "Insufficient balance");
        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    /// @notice Gets the WOOL token balance of an address
    /// @param _owner Address to query
    /// @return Token balance of the given address
    function balanceOf(address _owner) external view returns (uint256) {
        return balances[_owner];
    }

    /// @notice Approves another address to spend tokens on behalf of the caller
    /// @param _spender Address allowed to spend the caller's tokens
    /// @param _value Amount of tokens the spender is allowed to spend
    function approve(address _spender, uint256 _value) external returns (bool) {
        allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
        return true;
    }

    /// @notice Gets the remaining amount of tokens a spender is allowed to spend on behalf of an owner
    /// @param _owner Token owner address
    /// @param _spender Address allowed to spend the owner's tokens
    /// @return Remaining allowance
    function allowance(address _owner, address _spender) external view returns (uint256) {
        return allowances[_owner][_spender];
    }

    /// @notice Transfers WOOL tokens from one address to another using an allowance
    /// @param _from Address to transfer tokens from
    /// @param _to Address to transfer tokens to
    /// @param _value Amount of tokens to transfer
    function transferFrom(address _from, address _to, uint256 _value) external returns (bool) {
        require(_to != address(0), "Cannot transfer to zero address");
        require(balances[_from] >= _value, "Insufficient balance");
        require(allowances[_from][msg.sender] >= _value, "Allowance exceeded");
        balances[_from] -= _value;
        balances[_to] += _value;
        allowances[_from][msg.sender] -= _value;
        emit Transfer(_from, _to, _value);
        return true;
    }

    // Wolf Game Specific Functions

    /// @notice Breeds a new animal (Wolf or Sheep) and decreases land resources
    /// @param animalType The type of animal to breed ("Wolf" or "Sheep")
    /// @param resourceCost The amount of resources required to breed the animal
    function breedAnimal(string memory animalType, uint256 resourceCost) external returns (bool) {
        require(resourceCost > 0, "Resource cost must be greater than 0");
        require(availableLandResources >= resourceCost, "Not enough land resources available");
        require(
            keccak256(abi.encodePacked(animalType)) == keccak256("Wolf") || 
            keccak256(abi.encodePacked(animalType)) == keccak256("Sheep"),
            "Invalid animal type"
        );

        availableLandResources -= resourceCost;
        emit Breeding(msg.sender, animalType, resourceCost);
        return true;
    }

    /// @notice Adds more land resources (only callable by the owner)
    /// @param amount The amount of resources to add
    function addLandResources(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(availableLandResources + amount <= maxLandResources, "Exceeds max land resources");
        availableLandResources += amount;
    }

    /// @notice Adjusts the maximum land resources (only callable by the owner)
    /// @param newMax The new maximum land resources
    function adjustMaxLandResources(uint256 newMax) external onlyOwner {
        require(newMax > 0, "Max land resources must be greater than 0");
        require(newMax >= availableLandResources, "New max cannot be less than available resources");
        maxLandResources = newMax;
    }
}
```
