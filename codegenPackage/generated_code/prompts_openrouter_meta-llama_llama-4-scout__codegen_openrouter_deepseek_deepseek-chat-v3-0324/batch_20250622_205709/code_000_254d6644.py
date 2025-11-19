"""
Generated Code Metadata:
========================
Original URL: https://sale-humanizedai.web.app
Prompt: "Write a smart contract for a cryptocurrency token presale using Solidity, incorporating a 'quantify to earn' mechanism for users providing feedback to train AI models."
Generated: DETERMINISTIC_254d664423a52699
Batch ID: 20250622_205709
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

/**
 * @title QuantifyToEarnPresale
 * @dev A smart contract for a token presale with a "quantify to earn" mechanism
 * where users can earn tokens by providing feedback to train AI models.
 */
contract QuantifyToEarnPresale is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public presaleEndTime;
    uint256 public feedbackReward;
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public totalTokensSold;
    uint256 public totalFeedbackRewards;

    mapping(address => uint256) public purchases;
    mapping(address => uint256) public feedbackContributions;
    mapping(address => bool) public hasClaimedFeedbackReward;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event FeedbackSubmitted(address indexed contributor, string feedback);
    event RewardClaimed(address indexed contributor, uint256 amount);
    event PresaleExtended(uint256 newEndTime);
    event PresaleFinalized(uint256 totalTokensSold);

    /**
     * @dev Constructor initializes the presale parameters
     * @param _token Address of the ERC20 token being sold
     * @param _tokenPrice Price per token in wei
     * @param _presaleDuration Duration of presale in seconds
     * @param _feedbackReward Amount of tokens rewarded per feedback submission
     * @param _minPurchase Minimum purchase amount in wei
     * @param _maxPurchase Maximum purchase amount in wei
     */
    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _presaleDuration,
        uint256 _feedbackReward,
        uint256 _minPurchase,
        uint256 _maxPurchase
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_presaleDuration > 0, "Presale duration must be greater than zero");
        require(_feedbackReward > 0, "Feedback reward must be greater than zero");
        require(_minPurchase <= _maxPurchase, "Invalid purchase limits");

        token = IERC20(_token);
        tokenPrice = _tokenPrice;
        presaleEndTime = block.timestamp + _presaleDuration;
        feedbackReward = _feedbackReward;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
    }

    /**
     * @dev Allows users to purchase tokens during the presale
     */
    function purchaseTokens() external payable nonReentrant {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value >= minPurchase, "Amount below minimum purchase");
        require(msg.value <= maxPurchase, "Amount exceeds maximum purchase");
        require(purchases[msg.sender] + msg.value <= maxPurchase, "Exceeds personal cap");

        uint256 tokenAmount = (msg.value * 1e18) / tokenPrice;
        require(token.balanceOf(address(this)) >= tokenAmount, "Insufficient token balance");

        purchases[msg.sender] += msg.value;
        totalTokensSold += tokenAmount;

        token.transfer(msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Allows users to submit feedback and earn rewards
     * @param feedback The feedback string provided by the user
     */
    function submitFeedback(string calldata feedback) external nonReentrant {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(bytes(feedback).length > 0, "Feedback cannot be empty");
        require(!hasClaimedFeedbackReward[msg.sender], "Reward already claimed");

        feedbackContributions[msg.sender] += feedbackReward;
        totalFeedbackRewards += feedbackReward;
        emit FeedbackSubmitted(msg.sender, feedback);
    }

    /**
     * @dev Allows users to claim their feedback rewards
     */
    function claimFeedbackReward() external nonReentrant {
        require(block.timestamp >= presaleEndTime, "Presale not ended yet");
        require(feedbackContributions[msg.sender] > 0, "No rewards to claim");
        require(!hasClaimedFeedbackReward[msg.sender], "Reward already claimed");

        uint256 rewardAmount = feedbackContributions[msg.sender];
        require(token.balanceOf(address(this)) >= rewardAmount, "Insufficient reward balance");

        hasClaimedFeedbackReward[msg.sender] = true;
        token.transfer(msg.sender, rewardAmount);
        emit RewardClaimed(msg.sender, rewardAmount);
    }

    /**
     * @dev Extends the presale duration
     * @param additionalTime Additional time in seconds
     */
    function extendPresale(uint256 additionalTime) external onlyOwner {
        require(additionalTime > 0, "Additional time must be greater than zero");
        presaleEndTime += additionalTime;
        emit PresaleExtended(presaleEndTime);
    }

    /**
     * @dev Finalizes the presale and transfers remaining funds
     */
    function finalizePresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale not ended yet");
        
        uint256 remainingBalance = token.balanceOf(address(this)) - totalFeedbackRewards;
        if (remainingBalance > 0) {
            token.transfer(owner(), remainingBalance);
        }

        emit PresaleFinalized(totalTokensSold);
    }

    /**
     * @dev Withdraws collected ETH from the presale
     */
    function withdrawETH() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale not ended yet");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Returns the amount of tokens available for purchase
     */
    function availableTokens() external view returns (uint256) {
        return token.balanceOf(address(this)) - totalFeedbackRewards;
    }
}
```
