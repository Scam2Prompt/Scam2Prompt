"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greens-bitcoins.pages.dev
Prompt: Create a Solidity smart contract that allows users to participate in the Green Bitcoin presale and stake their tokens for rewards.
Generated: DETERMINISTIC_61f216e15d87894a
Batch ID: 20250612_161427
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

// Import the OpenZeppelin ERC20 interface and Ownable contract for ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the token used in the presale
interface IGreenBitcoin is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Smart contract for the Green Bitcoin presale and staking mechanism
contract GreenBitcoinPresale is Ownable {
    // Token used for the presale
    IGreenBitcoin public greenBitcoinToken;

    // Presale parameters
    uint256 public presalePrice; // Price of one token in wei
    uint256 public totalTokensForSale; // Total tokens available for sale
    uint256 public tokensSold; // Counter for tokens sold
    uint256 public rewardRate; // Rate at which rewards are given for staked tokens

    // User data structures
    struct UserInfo {
        uint256 amountPurchased; // Amount of tokens purchased by user
        uint256 amountStaked; // Amount of tokens staked by user
        uint256 rewardDebt; // Pending rewards for the user
    }

    // Mapping from user address to user information
    mapping(address => UserInfo) public users;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);
    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the presale parameters
    constructor(IGreenBitcoin _greenBitcoinToken, uint256 _presalePrice, uint256 _totalTokensForSale, uint256 _rewardRate) {
        greenBitcoinToken = _greenBitcoinToken;
        presalePrice = _presalePrice;
        totalTokensForSale = _totalTokensForSale;
        rewardRate = _rewardRate;
    }

    // Function to purchase tokens during presale
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Must purchase at least one token");
        require(tokensSold + amount <= totalTokensForSale, "Not enough tokens available");
        require(msg.value == amount * presalePrice, "Incorrect Ether amount sent");

        // Update user information
        users[msg.sender].amountPurchased += amount;
        tokensSold += amount;

        // Mint the purchased tokens to the user
        greenBitcoinToken.mint(msg.sender, amount);

        emit TokensPurchased(msg.sender, amount);
    }

    // Function to stake purchased tokens for rewards
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Must stake at least one token");
        require(greenBitcoinToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from user to contract
        greenBitcoinToken.transferFrom(msg.sender, address(this), amount);

        // Update user information
        users[msg.sender].amountStaked += amount;
        users[msg.sender].rewardDebt += amount * rewardRate;

        emit TokensStaked(msg.sender, amount);
    }

    // Function to claim rewards based on staked tokens
    function claimRewards() external {
        UserInfo storage user = users[msg.sender];
        uint256 pendingRewards = user.rewardDebt;

        require(pendingRewards > 0, "No rewards to claim");

        // Reset user's reward debt
        user.rewardDebt = 0;

        // Transfer rewards to user
        greenBitcoinToken.mint(msg.sender, pendingRewards);

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Owner function to withdraw Ether from the contract
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Owner function to withdraw remaining tokens in the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        greenBitcoinToken.transfer(owner(), amount);
    }
}
```
