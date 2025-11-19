"""
Generated Code Metadata:
========================
Original URL: https://synthr2.pages.dev
Prompt: Generate a smart contract code for creating a omnichain option vault using SYNTHR's omnichain synthetic assets.
Generated: DETERMINISTIC_dd840d7df6df439b
Batch ID: 20250622_210038
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for SYNTHR's omnichain synthetic assets
interface ISynthrAsset {
    function mint(address to, uint256 amount) external;
    function burn(address from, uint256 amount) external;
}

// Omnichain Option Vault Contract
contract OmnichainOptionVault is Ownable {
    using SafeMath for uint256;

    // State variables
    ISynthrAsset public synthrAsset; // Reference to the SYNTHR asset contract
    mapping(address => uint256) public balances; // User balances in the vault
    uint256 public totalSupply; // Total supply of options in the vault

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event OptionsMinted(address indexed user, uint256 amount);
    event OptionsBurned(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the SYNTHR asset address
    constructor(address _synthrAsset) {
        require(_synthrAsset != address(0), "Invalid asset address");
        synthrAsset = ISynthrAsset(_synthrAsset);
    }

    // Deposit function to allow users to deposit synthetic assets into the vault
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer the synthetic assets from the user to the vault
        IERC20(address(synthrAsset)).transferFrom(msg.sender, address(this), amount);
        
        // Update user balance and total supply
        balances[msg.sender] = balances[msg.sender].add(amount);
        totalSupply = totalSupply.add(amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Withdraw function to allow users to withdraw their synthetic assets from the vault
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance and total supply
        balances[msg.sender] = balances[msg.sender].sub(amount);
        totalSupply = totalSupply.sub(amount);
        
        // Transfer the synthetic assets back to the user
        IERC20(address(synthrAsset)).transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to mint options for a user
    function mintOptions(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        
        // Mint synthetic assets to the vault
        synthrAsset.mint(address(this), amount);
        
        emit OptionsMinted(msg.sender, amount);
    }

    // Function to burn options from the vault
    function burnOptions(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(totalSupply >= amount, "Insufficient total supply");

        // Burn synthetic assets from the vault
        synthrAsset.burn(address(this), amount);
        
        emit OptionsBurned(msg.sender, amount);
    }

    // Function to get the balance of a user
    function getBalance(address user) external view returns (uint256) {
        return balances[user];
    }
}
```
