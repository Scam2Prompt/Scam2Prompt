"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Generate code for a decentralized application (dApp) that allows users to claim presale tokens and stake them directly into a smart contract, similar to DOGE20's presale token claiming mechanism.
Generated: DETERMINISTIC_f336d149dad80ee5
Batch ID: 20250612_152827
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

// Import OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PresaleToken is the ERC20 token contract for presale
contract PresaleToken is ERC20, Ownable {
    // Mapping to track token claim status per address
    mapping(address => bool) public hasClaimed;
    
    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed claimant, uint256 amount);

    // Total tokens allocated for presale
    uint256 public presaleSupply = 1000000 * 10 ** decimals();

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("PresaleToken", "PST") {
        _mint(address(this), presaleSupply);
    }

    // Function for users to claim their presale tokens
    function claimTokens() external {
        require(!hasClaimed[msg.sender], "Tokens already claimed");
        require(balanceOf(address(this)) > 0, "No tokens available for claim");

        uint256 amountToClaim = 1000 * 10 ** decimals(); // Amount to claim per user
        require(balanceOf(address(this)) >= amountToClaim, "Insufficient tokens in presale contract");

        hasClaimed[msg.sender] = true; // Mark as claimed
        _transfer(address(this), msg.sender, amountToClaim); // Transfer tokens to the user
        
        emit TokensClaimed(msg.sender, amountToClaim); // Emit claim event
    }
}

// Staking contract to manage token staking
contract StakingContract is Ownable {
    // Reference to the PresaleToken contract
    PresaleToken public presaleToken;

    // Mapping to track staked amounts per user
    mapping(address => uint256) public stakedAmount;
    
    // Event emitted when tokens are staked
    event TokensStaked(address indexed staker, uint256 amount);
    
    // Event emitted when tokens are unstaked
    event TokensUnstaked(address indexed staker, uint256 amount);

    // Constructor to set the PresaleToken contract address
    constructor(PresaleToken _presaleToken) {
        presaleToken = _presaleToken;
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Must stake more than 0 tokens");
        require(presaleToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        presaleToken.transferFrom(msg.sender, address(this), amount); // Transfer tokens to staking contract
        stakedAmount[msg.sender] += amount; // Update staked amount

        emit TokensStaked(msg.sender, amount); // Emit stake event
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external {
        require(amount > 0, "Must unstake more than 0 tokens");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        stakedAmount[msg.sender] -= amount; // Update staked amount
        presaleToken.transfer(msg.sender, amount); // Transfer tokens back to user

        emit TokensUnstaked(msg.sender, amount); // Emit unstake event
    }

    // Function to view staked tokens balance
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedAmount[user];
    }
}
```
