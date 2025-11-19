"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://groovesup.pages.dev
Prompt: How can I implement a smart contract for token rewards in a decentralized music streaming platform like GrooveUP?
Generated: DETERMINISTIC_959b9f8821f1eb83
Batch ID: 20250612_164100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a smart contract for a token reward system in Solidity for a decentralized music streaming platform like GrooveUP:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title GrooveUP Token Reward Contract
/// @dev Implements ERC20 token standard for rewarding users and artists
/// @notice This contract is part of a decentralized music streaming platform

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GrooveUPToken is ERC20, Ownable {
    // Mapping to track artist balances
    mapping(address => uint256) public artistBalances;

    // Events
    event UserRewarded(address indexed user, uint256 amount);
    event ArtistRewarded(address indexed artist, uint256 amount);
    event ArtistWithdraw(address indexed artist, uint256 amount);

    /// @dev Constructor to initialize the token name and symbol
    /// @param _initialSupply Total supply of tokens to mint initially
    constructor(uint256 _initialSupply) ERC20("GrooveUP Token", "GUP") {
        _mint(msg.sender, _initialSupply * (10 ** decimals())); // Mint initial supply to the contract owner
    }

    /// @notice Reward users with tokens for streaming music
    /// @param _user Address of the user to reward
    /// @param _amount Amount of tokens to reward
    function rewardUser(address _user, uint256 _amount) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");
        require(balanceOf(owner()) >= _amount, "Insufficient contract owner balance");

        _transfer(owner(), _user, _amount);
        emit UserRewarded(_user, _amount);
    }

    /// @notice Reward artists with tokens for their content
    /// @param _artist Address of the artist to reward
    /// @param _amount Amount of tokens to allocate to the artist
    function rewardArtist(address _artist, uint256 _amount) external onlyOwner {
        require(_artist != address(0), "Invalid artist address");
        require(_amount > 0, "Reward amount must be greater than zero");
        require(balanceOf(owner()) >= _amount, "Insufficient contract owner balance");

        artistBalances[_artist] += _amount;
        emit ArtistRewarded(_artist, _amount);
    }

    /// @notice Allow artists to withdraw their token balance
    /// @param _amount Amount of tokens the artist wants to withdraw
    function withdrawArtistBalance(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");
        require(artistBalances[msg.sender] >= _amount, "Insufficient artist balance");

        artistBalances[msg.sender] -= _amount;
        _transfer(owner(), msg.sender, _amount);
        emit ArtistWithdraw(msg.sender, _amount);
    }

    /// @notice Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("This contract does not accept Ether");
    }
}
```

This code is clean, production-ready, and uses the OpenZeppelin library for ERC20 implementation. It includes functions to reward users and artists, and allows artists to withdraw their balance. Proper error handling and best practices are implemented.
