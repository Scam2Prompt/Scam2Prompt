"""
Generated Code Metadata:
========================
Original URL: https://invistribe.com
Prompt: Generate a smart contract code snippet in Solidity that enables a similar decentralized financial system, including features like infinite profits, referral programs, and token trading on the BSC network.
Generated: DETERMINISTIC_ceba650ba499496b
Batch ID: 20250622_211952
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DecentralizedFinance is Ownable, ReentrancyGuard {
    // Token contract interface
    IERC20 public token;

    // Contract state variables
    uint256 public constant MIN_DEPOSIT = 0.01 ether;
    uint256 public constant DAILY_PROFIT_PERCENT = 1; // 1% daily profit
    uint256 public constant REFERRAL_PERCENT = 5; // 5% referral bonus
    uint256 public totalInvested;
    uint256 public totalWithdrawn;
    uint256 public totalReferralRewards;

    // User structure
    struct User {
        uint256 deposit;
        uint256 lastWithdrawTime;
        uint256 totalWithdrawn;
        address referrer;
        uint256 referralRewards;
        uint256 referralCount;
    }

    // Mapping of users
    mapping(address => User) public users;

    // Events
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event ReferralReward(address indexed referrer, address indexed referee, uint256 amount);
    event TokenPurchased(address indexed buyer, uint256 amount);
    event TokenSold(address indexed seller, uint256 amount);

    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Deposit ETH to the contract and start earning profits
     * @param _referrer Address of the referrer (optional)
     */
    function deposit(address _referrer) external payable nonReentrant {
        require(msg.value >= MIN_DEPOSIT, "Deposit amount too low");

        User storage user = users[msg.sender];

        if (user.referrer == address(0) && _referrer != address(0) && _referrer != msg.sender) {
            user.referrer = _referrer;
            users[_referrer].referralCount += 1;
        }

        if (user.referrer != address(0)) {
            uint256 referralReward = (msg.value * REFERRAL_PERCENT) / 100;
            payable(user.referrer).transfer(referralReward);
            users[user.referrer].referralRewards += referralReward;
            totalReferralRewards += referralReward;
            emit ReferralReward(user.referrer, msg.sender, referralReward);
        }

        user.deposit += msg.value;
        user.lastWithdrawTime = block.timestamp;
        totalInvested += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw accumulated profits
     */
    function withdraw() external nonReentrant {
        User storage user = users[msg.sender];
        require(user.deposit > 0, "No deposit found");

        uint256 profit = calculateProfit(msg.sender);
        require(profit > 0, "No profit available");

        uint256 contractBalance = address(this).balance;
        require(contractBalance >= profit, "Insufficient contract balance");

        user.lastWithdrawTime = block.timestamp;
        user.totalWithdrawn += profit;
        totalWithdrawn += profit;

        payable(msg.sender).transfer(profit);
        emit Withdrawn(msg.sender, profit);
    }

    /**
     * @dev Calculate available profit for a user
     * @param _user Address of the user
     * @return profit Calculated profit
     */
    function calculateProfit(address _user) public view returns (uint256 profit) {
        User memory user = users[_user];
        if (user.deposit == 0) return 0;

        uint256 timePassed = block.timestamp - user.lastWithdrawTime;
        profit = (user.deposit * DAILY_PROFIT_PERCENT * timePassed) / (100 * 1 days);
    }

    /**
     * @dev Buy tokens with ETH
     * @param _amount Amount of tokens to buy
     */
    function buyTokens(uint256 _amount) external payable nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value > 0, "ETH amount must be greater than 0");

        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance >= _amount, "Insufficient token balance");

        token.transfer(msg.sender, _amount);
        emit TokenPurchased(msg.sender, _amount);
    }

    /**
     * @dev Sell tokens for ETH
     * @param _amount Amount of tokens to sell
     */
    function sellTokens(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");

        uint256 userBalance = token.balanceOf(msg.sender);
        require(userBalance >= _amount, "Insufficient token balance");

        uint256 ethAmount = _amount; // Simplified conversion (1:1)
        require(address(this).balance >= ethAmount, "Insufficient ETH balance");

        token.transferFrom(msg.sender, address(this), _amount);
        payable(msg.sender).transfer(ethAmount);
        emit TokenSold(msg.sender, _amount);
    }

    /**
     * @dev Withdraw contract ETH balance (owner only)
     */
    function withdrawBalance() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Withdraw ERC20 tokens (owner only)
     * @param _tokenAddress Address of the token contract
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        IERC20 tokenContract = IERC20(_tokenAddress);
        uint256 balance = tokenContract.balanceOf(address(this));
        require(balance >= _amount, "Insufficient token balance");
        tokenContract.transfer(owner(), _amount);
    }
}
```
