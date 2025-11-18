"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-lnds-64z.pages.dev
Prompt: Write a smart contract function that verifies ETH deposits and distributes Leonidas tokens to the depositor's wallet address, following the presale cap of 1000 ETH.
Generated: DETERMINISTIC_2029c337137d2896
Batch ID: 20250612_153224
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
 * @title LeonidasTokenPresale
 * @dev This contract handles ETH deposits and distributes Leonidas tokens during presale.
 */
contract LeonidasTokenPresale {
    // Leonidas token contract interface
    IERC20 public immutable leonidasToken;

    // Presale cap in ETH
    uint256 public constant PRESALE_CAP = 1000 ether;

    // Tokens per ETH (example rate: 1000 tokens per 1 ETH)
    uint256 public constant TOKENS_PER_ETH = 1000;

    // Total ETH deposited
    uint256 public totalDepositedETH;

    // Owner of the contract
    address public owner;

    // Events
    event DepositReceived(address indexed depositor, uint256 ethAmount, uint256 tokenAmount);
    event TokensWithdrawn(address indexed user, uint256 tokenAmount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the token contract and sets the owner.
     * @param _leonidasToken Address of the Leonidas token contract.
     */
    constructor(address _leonidasToken) {
        require(_leonidasToken != address(0), "Token address cannot be zero");
        leonidasToken = IERC20(_leonidasToken);
        owner = msg.sender;
    }

    /**
     * @dev Receive function to accept ETH deposits and distribute Leonidas tokens.
     * Ensures the presale cap is not exceeded.
     */
    receive() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        require(totalDepositedETH + msg.value <= PRESALE_CAP, "Presale cap exceeded");

        // Calculate token amount to distribute
        uint256 tokenAmount = msg.value * TOKENS_PER_ETH;

        // Ensure contract has enough Leonidas tokens
        require(leonidasToken.balanceOf(address(this)) >= tokenAmount, "Insufficient tokens in contract");

        // Update total ETH deposited
        totalDepositedETH += msg.value;

        // Transfer tokens to depositor
        leonidasToken.transfer(msg.sender, tokenAmount);

        emit DepositReceived(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Allows the owner to withdraw remaining Leonidas tokens after the presale ends.
     * @param _to Address to receive the remaining tokens.
     */
    function withdrawRemainingTokens(address _to) external onlyOwner {
        require(_to != address(0), "Recipient address cannot be zero");

        uint256 remainingTokens = leonidasToken.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens left to withdraw");

        leonidasToken.transfer(_to, remainingTokens);

        emit TokensWithdrawn(_to, remainingTokens);
    }
}

/**
 * @dev Minimal ERC20 interface for interacting with Leonidas token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
