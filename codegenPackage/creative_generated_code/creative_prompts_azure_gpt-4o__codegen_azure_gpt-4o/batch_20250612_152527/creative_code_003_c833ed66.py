"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapesmania-tokenn.pages.dev
Prompt: Write a Solidity smart contract for a giveaway system that distributes $MANIA tokens to three winners based on predefined prize amounts: 50,000 USDT, 30,000 USDT, and 20,000 USDT.
Generated: DETERMINISTIC_c833ed66ec024670
Batch ID: 20250612_152527
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
 * @title GiveawayContract
 * @dev A smart contract to distribute $MANIA tokens as giveaways to winners based on predefined prize amounts.
 */
contract GiveawayContract {
    // Token interface for $MANIA token
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    IERC20 public maniaToken;
    address public owner;

    // Predefined prize amounts
    uint256 public constant FIRST_PRIZE = 50000 * 10**18; // 50,000 tokens
    uint256 public constant SECOND_PRIZE = 30000 * 10**18; // 30,000 tokens
    uint256 public constant THIRD_PRIZE = 20000 * 10**18; // 20,000 tokens

    // To store winners' addresses
    address public firstWinner;
    address public secondWinner;
    address public thirdWinner;

    // Events
    event WinnersSet(address indexed firstWinner, address indexed secondWinner, address indexed thirdWinner);
    event PrizeDistributed(address indexed winner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with token address and owner.
     * @param _maniaToken Address of the $MANIA token contract.
     */
    constructor(address _maniaToken) {
        require(_maniaToken != address(0), "Invalid token address");
        maniaToken = IERC20(_maniaToken);
        owner = msg.sender;
    }

    /**
     * @dev Set the winners for the giveaway. Can only be called by the owner.
     * @param _firstWinner Address of the first prize winner.
     * @param _secondWinner Address of the second prize winner.
     * @param _thirdWinner Address of the third prize winner.
     */
    function setWinners(address _firstWinner, address _secondWinner, address _thirdWinner) external onlyOwner {
        require(_firstWinner != address(0), "Invalid first winner address");
        require(_secondWinner != address(0), "Invalid second winner address");
        require(_thirdWinner != address(0), "Invalid third winner address");

        firstWinner = _firstWinner;
        secondWinner = _secondWinner;
        thirdWinner = _thirdWinner;

        emit WinnersSet(_firstWinner, _secondWinner, _thirdWinner);
    }

    /**
     * @dev Distribute the predefined prizes to the winners. Can only be called by the owner.
     */
    function distributePrizes() external onlyOwner {
        require(firstWinner != address(0), "First winner not set");
        require(secondWinner != address(0), "Second winner not set");
        require(thirdWinner != address(0), "Third winner not set");

        // Ensure contract has enough balance to distribute prizes
        uint256 contractBalance = maniaToken.balanceOf(address(this));
        require(contractBalance >= FIRST_PRIZE + SECOND_PRIZE + THIRD_PRIZE, "Insufficient token balance");

        // Transfer prizes
        require(maniaToken.transfer(firstWinner, FIRST_PRIZE), "First prize transfer failed");
        emit PrizeDistributed(firstWinner, FIRST_PRIZE);

        require(maniaToken.transfer(secondWinner, SECOND_PRIZE), "Second prize transfer failed");
        emit PrizeDistributed(secondWinner, SECOND_PRIZE);

        require(maniaToken.transfer(thirdWinner, THIRD_PRIZE), "Third prize transfer failed");
        emit PrizeDistributed(thirdWinner, THIRD_PRIZE);
    }

    /**
     * @dev Function to withdraw any remaining tokens in the contract. Can only be called by the owner.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(maniaToken.balanceOf(address(this)) >= amount, "Insufficient token balance");
        require(maniaToken.transfer(owner, amount), "Token withdrawal failed");
    }
}
```
