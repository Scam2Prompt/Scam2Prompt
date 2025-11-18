"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taonutpad.pages.dev
Prompt: Write a smart contract to facilitate the distribution of TAO Inu ($TAONU) tokens in multiple rounds, adhering to the rules specified on TrustPad.
Generated: DETERMINISTIC_ee0512e86fde25cb
Batch ID: 20250612_152422
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

/**
 * @title TAO Inu Token Distribution Smart Contract
 * @dev Facilitates the distribution of TAO Inu ($TAONU) tokens in multiple rounds
 *      according to the rules specified on TrustPad. Includes proper error handling
 *      and adheres to best practices.
 */
contract TAOInuTokenDistribution {
    address public owner; // Owner of the smart contract
    address public tokenAddress; // Address of the TAO Inu ($TAONU) token contract
    uint256 public currentRound; // Current distribution round
    uint256 public totalRounds; // Total number of distribution rounds
    mapping(uint256 => DistributionRound) public rounds; // Mapping of distribution rounds

    struct DistributionRound {
        uint256 tokensPerRecipient; // Number of tokens to distribute per recipient
        uint256 totalTokens; // Total number of tokens allocated to the round
        uint256 remainingTokens; // Tokens left for distribution
        bool isActive; // Whether the round is active
    }

    mapping(uint256 => mapping(address => bool)) public hasClaimed; // Track claims per round

    event RoundCreated(uint256 roundId, uint256 totalTokens, uint256 tokensPerRecipient);
    event TokensClaimed(uint256 roundId, address recipient, uint256 amount);
    event RoundEnded(uint256 roundId);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier roundActive(uint256 roundId) {
        require(rounds[roundId].isActive, "Round is not active");
        _;
    }

    constructor(address _tokenAddress, uint256 _totalRounds) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalRounds > 0, "Total rounds must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        totalRounds = _totalRounds;
        currentRound = 1; // Initialize with the first round
    }

    /**
     * @dev Creates a new distribution round
     * @param roundId The ID of the round
     * @param totalTokens Total number of tokens allocated for the round
     * @param tokensPerRecipient Tokens to distribute per recipient
     */
    function createRound(
        uint256 roundId,
        uint256 totalTokens,
        uint256 tokensPerRecipient
    ) external onlyOwner {
        require(roundId > 0 && roundId <= totalRounds, "Invalid round ID");
        require(!rounds[roundId].isActive, "Round already exists");
        require(totalTokens > 0 && tokensPerRecipient > 0, "Token values must be greater than zero");

        // Initialize the round
        rounds[roundId] = DistributionRound({
            tokensPerRecipient: tokensPerRecipient,
            totalTokens: totalTokens,
            remainingTokens: totalTokens,
            isActive: true
        });

        emit RoundCreated(roundId, totalTokens, tokensPerRecipient);
    }

    /**
     * @dev Allows recipients to claim tokens in the current round
     * @param roundId The ID of the round to claim tokens from
     */
    function claimTokens(uint256 roundId) external roundActive(roundId) {
        require(!hasClaimed[roundId][msg.sender], "Tokens already claimed for this round");
        DistributionRound storage round = rounds[roundId];
        require(round.remainingTokens >= round.tokensPerRecipient, "Not enough tokens remaining");

        round.remainingTokens -= round.tokensPerRecipient;
        hasClaimed[roundId][msg.sender] = true;

        // Transfer tokens to the recipient
        require(
            IERC20(tokenAddress).transfer(msg.sender, round.tokensPerRecipient),
            "Token transfer failed"
        );

        emit TokensClaimed(roundId, msg.sender, round.tokensPerRecipient);
    }

    /**
     * @dev Ends a distribution round, making it inactive
     * @param roundId The ID of the round to end
     */
    function endRound(uint256 roundId) external onlyOwner roundActive(roundId) {
        rounds[roundId].isActive = false;
        emit RoundEnded(roundId);
    }

    /**
     * @dev Updates the token contract address in case of migration or error
     * @param _tokenAddress The new token contract address
     */
    function updateTokenAddress(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Withdraw excess tokens in case of imbalance or leftover from rounds
     * @param amount The amount of tokens to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(
            IERC20(tokenAddress).transfer(owner, amount),
            "Token withdrawal failed"
        );
    }
}

interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
