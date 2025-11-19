"""
Generated Code Metadata:
========================
Original URL: https://projectdeksa.pages.dev
Prompt: Develop a smart contract in Solidity for the $MASA token, incorporating features that reflect its utility in the virtual economy of the DEKSA project.
Generated: DETERMINISTIC_758ac069e5cf4f1b
Batch ID: 20250612_163848
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

// Importing OpenZeppelin's ERC20 implementation for standard token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// The MASA token contract
contract MASAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track balances of users for staking
    mapping(address => uint256) private _stakingBalances;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Masa Token", "$MASA") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens from the user to the contract
        _transfer(msg.sender, address(this), amount);
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update the staking balance
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].sub(amount);
        
        // Transfer tokens back to the user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check the staking balance of a user
    function stakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    // Function to allow the owner to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _mint(to, amount);
    }

    // Function to allow the owner to burn tokens
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        _burn(msg.sender, amount);
    }
}
```
