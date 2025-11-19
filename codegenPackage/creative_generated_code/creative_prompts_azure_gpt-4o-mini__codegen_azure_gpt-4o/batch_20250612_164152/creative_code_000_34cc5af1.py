"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tesneiro-5281.vercel.app
Prompt: Generate a smart contract for a token airdrop similar to Neiro's 10,000,000 token giveaway for 100 participants on Ethereum.
Generated: DETERMINISTIC_34cc5af17f1c306e
Batch ID: 20250612_164152
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
 * @title TokenAirdrop
 * @dev A smart contract for distributing tokens to predefined recipients
 */
contract TokenAirdrop {
    IERC20 public token; // The ERC20 token to be distributed
    address public owner; // The address of the contract owner

    uint256 public totalTokensToDistribute = 10_000_000 * (10 ** 18); // Total tokens to distribute
    uint256 public numberOfRecipients = 100; // Total number of participants

    mapping(address => bool) public recipients; // Tracks recipients who have claimed their tokens
    uint256 public tokensPerRecipient; // Tokens allocated per participant

    event TokensClaimed(address indexed recipient, uint256 amount);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _token Address of the ERC20 token contract.
     */
    constructor(address _token) {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
        owner = msg.sender;
        tokensPerRecipient = totalTokensToDistribute / numberOfRecipients;
    }

    /**
     * @dev Function to add recipients eligible for the airdrop.
     * @param _recipients List of recipient addresses.
     */
    function addRecipients(address[] memory _recipients) external onlyOwner {
        require(_recipients.length <= numberOfRecipients, "Too many recipients");
        
        for (uint256 i = 0; i < _recipients.length; i++) {
            require(_recipients[i] != address(0), "Recipient address cannot be zero");
            recipients[_recipients[i]] = true;
        }
    }

    /**
     * @dev Function for recipients to claim their tokens.
     */
    function claimTokens() external {
        require(recipients[msg.sender], "You are not eligible for the airdrop");
        require(token.balanceOf(address(this)) >= tokensPerRecipient, "Insufficient contract balance");
        require(!recipients[msg.sender], "Tokens already claimed");

        recipients[msg.sender] = false; // Mark recipient as having claimed tokens
        require(
            token.transfer(msg.sender, tokensPerRecipient),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, tokensPerRecipient);
    }

    /**
     * @dev Allows the owner to withdraw remaining tokens in the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No tokens to withdraw");

        require(
            token.transfer(owner, remainingTokens),
            "Token transfer failed"
        );
    }
}

/**
 * @dev Interface for ERC20 token.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
