"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Write a smart contract in Solidity to handle the fair-launch mechanism for coins, ensuring no presale or team allocation, as outlined on the Fun Virtuals Agent platform.
Generated: DETERMINISTIC_12e958f3b65ae31e
Batch ID: 20250612_154016
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

/// @title FairLaunch Contract
/// @notice This contract implements a fair launch mechanism for a cryptocurrency token.
///         No presale or team allocation is allowed. Tokens are distributed evenly to
///         all participants during the launch period.
contract FairLaunch {
    // State variables
    string public constant name = "FairLaunch Token";
    string public constant symbol = "FLT";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;
    uint256 public launchEndTime;
    uint256 public tokensPerEther;
    
    mapping(address => uint256) public balances;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensWithdrawn(address indexed user, uint256 amount);

    /// @notice Constructor to initialize the contract parameters.
    /// @param _launchDuration Duration of the launch in seconds.
    /// @param _tokensPerEther Number of tokens distributed per Ether sent.
    constructor(uint256 _launchDuration, uint256 _tokensPerEther) {
        require(_launchDuration > 0, "Launch duration must be greater than 0");
        require(_tokensPerEther > 0, "Tokens per Ether must be greater than 0");

        launchEndTime = block.timestamp + _launchDuration;
        tokensPerEther = _tokensPerEther;
    }

    /// @notice Fallback function to accept Ether and distribute tokens.
    receive() external payable {
        buyTokens();
    }

    /// @notice Function to buy tokens with Ether.
    /// @dev This function allows users to buy tokens during the launch period.
    function buyTokens() public payable {
        require(block.timestamp < launchEndTime, "Launch period has ended");
        require(msg.value > 0, "Must send Ether to purchase tokens");

        uint256 tokensToMint = msg.value * tokensPerEther;
        totalSupply += tokensToMint;
        balances[msg.sender] += tokensToMint;

        emit TokensPurchased(msg.sender, tokensToMint);
    }

    /// @notice Function to withdraw tokens after the launch ends.
    /// @dev Allows users to withdraw their allocated tokens after the launch.
    function withdrawTokens() public {
        require(block.timestamp >= launchEndTime, "Launch period not ended");
        require(balances[msg.sender] > 0, "No tokens to withdraw");

        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0; // Set balance to 0 before the transfer to prevent re-entrancy
        payable(msg.sender).transfer(amount); // Transfer Ether equivalent to the user's tokens

        emit TokensWithdrawn(msg.sender, amount);
    }

    /// @notice Function to check the contract's balance.
    /// @return The current balance of the contract in Wei.
    function contractBalance() public view returns (uint256) {
        return address(this).balance;
    }

    /// @notice Function to get the balance of a specific user.
    /// @param user The address of the user whose balance is to be checked.
    /// @return The token balance of the specified user.
    function balanceOf(address user) public view returns (uint256) {
        return balances[user];
    }
}
```
