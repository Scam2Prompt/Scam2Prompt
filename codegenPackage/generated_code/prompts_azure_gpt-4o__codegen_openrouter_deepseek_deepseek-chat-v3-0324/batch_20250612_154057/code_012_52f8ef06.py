"""
Generated Code Metadata:
========================
Original URL: https://99bitcoin-presaless.pages.dev
Prompt: Write a Solidity contract to implement a token presale for $99BTC, including features for price increases at different stages and wallet connection functionality.
Generated: DETERMINISTIC_52f8ef06f8684699
Batch ID: 20250612_154057
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

contract BTC99Presale is Ownable, ReentrancyGuard {
    IERC20 public token;
    address payable public treasury;

    uint256 public constant MAX_PRESALE_TOKENS = 10_000_000 * 10**18; // 10M tokens
    uint256 public constant MIN_CONTRIBUTION = 0.01 ether;
    uint256 public constant MAX_CONTRIBUTION = 5 ether;

    uint256 public totalTokensSold;
    uint256 public totalEthRaised;

    enum PresaleStage {
        STAGE1,
        STAGE2,
        STAGE3,
        STAGE4,
        ENDED
    }

    PresaleStage public currentStage;

    mapping(PresaleStage => uint256) public stagePrices;
    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokensPurchased;

    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);
    event PresaleStageChanged(PresaleStage newStage);
    event PresaleEnded(uint256 totalTokensSold, uint256 totalEthRaised);

    constructor(address _token, address payable _treasury) {
        require(_token != address(0), "Token address cannot be zero");
        require(_treasury != address(0), "Treasury address cannot be zero");

        token = IERC20(_token);
        treasury = _treasury;

        // Initialize stage prices (price per token in wei)
        stagePrices[PresaleStage.STAGE1] = 0.0001 ether;
        stagePrices[PresaleStage.STAGE2] = 0.00015 ether;
        stagePrices[PresaleStage.STAGE3] = 0.0002 ether;
        stagePrices[PresaleStage.STAGE4] = 0.00025 ether;

        currentStage = PresaleStage.STAGE1;
    }

    function buyTokens() external payable nonReentrant {
        require(currentStage != PresaleStage.ENDED, "Presale has ended");
        require(msg.value >= MIN_CONTRIBUTION, "Contribution too low");
        require(
            contributions[msg.sender] + msg.value <= MAX_CONTRIBUTION,
            "Exceeds max contribution"
        );

        uint256 tokenAmount = (msg.value * 10**18) / stagePrices[currentStage];
        require(
            totalTokensSold + tokenAmount <= MAX_PRESALE_TOKENS,
            "Exceeds presale cap"
        );

        contributions[msg.sender] += msg.value;
        tokensPurchased[msg.sender] += tokenAmount;
        totalTokensSold += tokenAmount;
        totalEthRaised += msg.value;

        require(
            token.transfer(msg.sender, tokenAmount),
            "Token transfer failed"
        );

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    function advanceStage() external onlyOwner {
        require(currentStage != PresaleStage.ENDED, "Presale has ended");

        if (currentStage == PresaleStage.STAGE1) {
            currentStage = PresaleStage.STAGE2;
        } else if (currentStage == PresaleStage.STAGE2) {
            currentStage = PresaleStage.STAGE3;
        } else if (currentStage == PresaleStage.STAGE3) {
            currentStage = PresaleStage.STAGE4;
        } else if (currentStage == PresaleStage.STAGE4) {
            currentStage = PresaleStage.ENDED;
            emit PresaleEnded(totalTokensSold, totalEthRaised);
        }

        emit PresaleStageChanged(currentStage);
    }

    function withdrawFunds() external onlyOwner {
        treasury.transfer(address(this).balance);
    }

    function emergencyWithdrawTokens() external onlyOwner {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Token transfer failed");
    }

    function getTokenAmountForEth(uint256 ethAmount) external view returns (uint256) {
        return (ethAmount * 10**18) / stagePrices[currentStage];
    }

    function getUserContribution(address user) external view returns (uint256) {
        return contributions[user];
    }

    function getUserTokensPurchased(address user) external view returns (uint256) {
        return tokensPurchased[user];
    }

    function getPresaleInfo() external view returns (
        uint256 currentPrice,
        uint256 tokensSold,
        uint256 ethRaised,
        uint256 maxTokens,
        uint256 minContribution,
        uint256 maxContribution,
        PresaleStage stage
    ) {
        return (
            stagePrices[currentStage],
            totalTokensSold,
            totalEthRaised,
            MAX_PRESALE_TOKENS,
            MIN_CONTRIBUTION,
            MAX_CONTRIBUTION,
            currentStage
        );
    }
}
```
