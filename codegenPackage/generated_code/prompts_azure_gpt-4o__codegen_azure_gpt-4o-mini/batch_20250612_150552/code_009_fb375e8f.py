"""
Generated Code Metadata:
========================
Original URL: https://dogeverse-22u.pages.dev
Prompt: Generate a Solidity smart contract for handling the tokenomics of $DOGEVERSE, including minting, staking, and allocation percentages for liquidity, marketing, and ecosystem funds.
Generated: DETERMINISTIC_fb375e8fe83543aa
Batch ID: 20250612_150552
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Contract for the $DOGEVERSE token
contract DogeverseToken is ERC20, Ownable, ReentrancyGuard {
    // Allocation percentages
    uint256 public liquidityAllocation = 20; // 20% for liquidity
    uint256 public marketingAllocation = 10; // 10% for marketing
    uint256 public ecosystemAllocation = 10; // 10% for ecosystem
    uint256 public totalSupplyAllocation = 100; // Total allocation percentage

    // Mapping for staking balances
    mapping(address => uint256) private _stakingBalances;
    mapping(address => uint256) private _stakingTimestamps;

    // Events
    event Minted(address indexed to, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("Dogeverse", "$DOGEVERSE") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint 1,000,000 tokens
    }

    // Function to mint new tokens
    function mint(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        _mint(to, amount);
        emit Minted(to, amount);
    }

    // Function to stake tokens
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Transfer tokens to the contract for staking
        _transfer(msg.sender, address(this), amount);
        _stakingBalances[msg.sender] += amount;
        _stakingTimestamps[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(_stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staking balance and transfer tokens back to the user
        _stakingBalances[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the staking balance of a user
    function stakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    // Function to get the total allocation percentages
    function getAllocationPercentages() external view returns (uint256, uint256, uint256) {
        return (liquidityAllocation, marketingAllocation, ecosystemAllocation);
    }

    // Function to withdraw tokens from the contract (for owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Cannot withdraw from the zero address");
        require(amount > 0, "Amount must be greater than zero");

        ERC20 token = ERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        token.transfer(msg.sender, amount);
    }
}
```
