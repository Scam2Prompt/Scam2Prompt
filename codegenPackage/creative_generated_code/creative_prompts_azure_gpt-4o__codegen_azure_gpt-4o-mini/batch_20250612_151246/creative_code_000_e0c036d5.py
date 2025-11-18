"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockbanki.pages.dev
Prompt: Write a smart contract in Solidity for staking $PEPU tokens on the Pepe Unchained Layer 2 blockchain, ensuring compatibility with Ethereum bridging.
Generated: DETERMINISTIC_e0c036d57e4416b9
Batch ID: 20250612_151246
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

// Importing OpenZeppelin's Ownable and SafeERC20 for security and ownership management
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

// Interface for the ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract PepuStaking is Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public pepuToken; // Reference to the $PEPU token contract
    uint256 public totalStaked; // Total amount of tokens staked
    mapping(address => uint256) public stakedAmounts; // Amount staked by each user
    mapping(address => uint256) public lastStakedTimestamp; // Last timestamp a user staked

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the $PEPU token address
    constructor(address _pepuToken) {
        require(_pepuToken != address(0), "Invalid token address");
        pepuToken = IERC20(_pepuToken);
    }

    // Modifier to ensure staked amounts are greater than zero
    modifier hasStaked() {
        require(stakedAmounts[msg.sender] > 0, "No tokens staked");
        _;
    }

    // Function to stake $PEPU tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the tokens from the user to the contract
        pepuToken.safeTransferFrom(msg.sender, address(this), amount);
        
        // Update the user's staked amount and total staked amount
        stakedAmounts[msg.sender] += amount;
        totalStaked += amount;
        lastStakedTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $PEPU tokens
    function unstake(uint256 amount) external hasStaked {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Update the user's staked amount and total staked amount
        stakedAmounts[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer the tokens back to the user
        pepuToken.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to check the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakedAmounts[user];
    }

    // Function to withdraw accidentally sent tokens to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(pepuToken), "Cannot withdraw staked tokens");
        IERC20(tokenAddress).safeTransfer(msg.sender, amount);
    }
}
```
