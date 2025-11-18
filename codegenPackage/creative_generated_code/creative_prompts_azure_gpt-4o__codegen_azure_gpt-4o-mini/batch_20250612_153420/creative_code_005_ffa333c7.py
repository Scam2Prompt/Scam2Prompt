"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Develop a script in Solidity for auditing the $SCOTTY smart contract, ensuring security against common vulnerabilities such as reentrancy and overflow issues.
Generated: DETERMINISTIC_ffa333c701e7ff7f
Batch ID: 20250612_153420
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

// Import OpenZeppelin's SafeMath for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// SCOTTY contract for token management
contract SCOTTY is ReentrancyGuard {
    using SafeMath for uint256; // Use SafeMath for safe math operations

    // Declare state variables
    string public name = "SCOTTYToken";
    string public symbol = "SCOTTY";
    uint8 public decimals = 18;
    uint256 private totalSupply_;
    
    // Mapping from addresses to balances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Events for Transfer and Approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to initialize total supply
    constructor(uint256 initialSupply) {
        totalSupply_ = initialSupply.mul(10 ** uint256(decimals));
        balances[msg.sender] = totalSupply_;
        emit Transfer(address(0), msg.sender, totalSupply_);
    }

    // Function to retrieve total supply
    function totalSupply() public view returns (uint256) {
        return totalSupply_;
    }

    // Function to retrieve balance of a specific address
    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    // Function to transfer tokens
    function transfer(address to, uint256 amount) public nonReentrant returns (bool) {
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[msg.sender] >= amount, "Insufficient balance");
        
        // Update balances
        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[to] = balances[to].add(amount);
        
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // Function to approve allowance for another address
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Cannot approve the zero address");
        
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // Function to transfer tokens on behalf of another address
    function transferFrom(address from, address to, uint256 amount) public nonReentrant returns (bool) {
        require(from != address(0), "Cannot transfer from the zero address");
        require(to != address(0), "Cannot transfer to the zero address");
        require(balances[from] >= amount, "Insufficient balance");
        require(allowances[from][msg.sender] >= amount, "Allowance exceeded");

        // Update balances and allowances
        balances[from] = balances[from].sub(amount);
        balances[to] = balances[to].add(amount);
        allowances[from][msg.sender] = allowances[from][msg.sender].sub(amount);
        
        emit Transfer(from, to, amount);
        return true;
    }

    // Function to check allowance
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }
}
```
