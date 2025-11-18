"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Write a smart contract in Solidity for an ERC20 token named `$MBAG` with 18 decimals, incorporating features like staking, referral incentives, and token burning as described in MoonBag's tokenomics.
Generated: DETERMINISTIC_655ca992a5a9c7fe
Batch ID: 20250612_145625
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

// Import the OpenZeppelin ERC20 contract and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the ERC20 token contract
contract MoonBagToken is ERC20, Ownable {
    // Mapping to track staked balances
    mapping(address => uint256) private _stakedBalances;
    // Mapping to track referral addresses
    mapping(address => address) public referrals;
    // Mapping to track token burners
    mapping(address => bool) public burners;

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event ReferrerAssigned(address indexed user, address indexed referrer);
    event TokensBurned(address indexed burner, uint256 amount);

    // Constructor to initialize token details
    constructor() ERC20("MoonBag", "$MBAG") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Initial supply
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _stakedBalances[msg.sender] += amount;
        _transfer(msg.sender, address(this), amount); // Transfer tokens to contract

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(_stakedBalances[msg.sender] >= amount, "Insufficient staked balance");
        
        _stakedBalances[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount); // Transfer tokens back to user

        emit Unstaked(msg.sender, amount);
    }

    // Function to assign a referrer
    function assignReferrer(address referrer) external {
        require(referrals[msg.sender] == address(0), "Referrer already assigned");
        require(referrer != msg.sender, "Cannot refer yourself");
        
        referrals[msg.sender] = referrer;

        emit ReferrerAssigned(msg.sender, referrer);
    }

    // Function to burn tokens
    function burn(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _burn(msg.sender, amount); // Burn the tokens

        emit TokensBurned(msg.sender, amount);
    }

    // Function to get staked balance of an account
    function stakedBalance(address account) external view returns (uint256) {
        return _stakedBalances[account];
    }
    
    // Owner can withdraw tokens accidentally sent to the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient contract balance");

        _transfer(address(this), msg.sender, amount);
    }
}
```
