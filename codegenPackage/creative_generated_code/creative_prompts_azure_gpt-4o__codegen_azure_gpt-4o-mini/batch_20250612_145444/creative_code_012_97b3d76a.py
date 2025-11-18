"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flockerz-claim.web.app
Prompt: Create a Solidity contract for a presale mechanism that rewards early adopters with staking bonuses and voting rights, as described in Flockerz.
Generated: DETERMINISTIC_97b3d76a4d6bed12
Batch ID: 20250612_145444
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Presale contract for early adopters with staking bonuses and voting rights
contract Presale is Ownable {
    // Struct to hold user information
    struct User {
        uint256 stakedAmount;
        uint256 bonusPoints;
        uint256 votes;
        bool isParticipating;
    }

    // Mapping of user addresses to their information
    mapping(address => User) public users;

    // The ERC20 token being sold in the presale
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public tokenPrice;
    uint256 public totalTokensSold;
    uint256 public totalTokensToSell;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Voted(address indexed voter, uint256 voteCount);

    // Constructor to initialize the contract
    constructor(
        address _token,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _tokenPrice,
        uint256 _totalTokensToSell
    ) {
        require(_token != address(0), "Invalid token address");
        require(_presaleStart < _presaleEnd, "Invalid presale duration");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_totalTokensToSell > 0, "Total tokens to sell must be greater than zero");

        token = IERC20(_token);
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        tokenPrice = _tokenPrice;
        totalTokensToSell = _totalTokensToSell;
    }

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale is not active");
        _;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 tokenAmount) external payable whenPresaleActive {
        require(tokenAmount > 0, "Amount must be greater than zero");
        require(totalTokensSold + tokenAmount <= totalTokensToSell, "Not enough tokens available");
        require(msg.value == tokenPrice * tokenAmount, "Incorrect Ether amount sent");

        // Update total tokens sold
        totalTokensSold += tokenAmount;

        // Update user data
        if (!users[msg.sender].isParticipating) {
            users[msg.sender].isParticipating = true;
        }
        users[msg.sender].stakedAmount += tokenAmount;
        users[msg.sender].bonusPoints += calculateBonus(tokenAmount);
        
        // Transfer tokens to the buyer
        require(token.transfer(msg.sender, tokenAmount), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to stake tokens for bonus points
    function stakeTokens(uint256 amount) external {
        require(users[msg.sender].isParticipating, "User not participating in presale");
        require(amount > 0, "Amount must be greater than zero");

        // Update user data
        users[msg.sender].stakedAmount += amount;
        users[msg.sender].bonusPoints += calculateBonus(amount);

        // Transfer tokens from user to contract for staking
        require(token.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens and receive bonus points
    function unstakeTokens(uint256 amount) external {
        require(users[msg.sender].stakedAmount >= amount, "Not enough staked tokens");

        // Update user data
        users[msg.sender].stakedAmount -= amount;

        // Transfer tokens back to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to calculate bonus points based on staked amount
    function calculateBonus(uint256 amount) internal pure returns (uint256) {
        // Example bonus calculation: 10% of staked amount
        return amount / 10;
    }

    // Function for users to vote based on their bonus points
    function vote(uint256 voteCount) external {
        require(users[msg.sender].isParticipating, "User not participating in presale");
        require(users[msg.sender].bonusPoints >= voteCount, "Not enough bonus points to vote");

        // Update user data
        users[msg.sender].bonusPoints -= voteCount;
        users[msg.sender].votes += voteCount;

        emit Voted(msg.sender, voteCount);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > presaleEnd, "Presale is still active");

        uint256 unsoldTokens = totalTokensToSell - totalTokensSold;
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        require(token.transfer(owner(), unsoldTokens), "Token transfer failed");
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
