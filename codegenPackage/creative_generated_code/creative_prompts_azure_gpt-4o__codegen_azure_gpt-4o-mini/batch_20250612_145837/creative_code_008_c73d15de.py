"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swiftmulauths.pages.dev
Prompt: Write code to implement a staking pool and presale functionality for cryptocurrency tokens, using the features described on the Swiftmulauths website.
Generated: DETERMINISTIC_c73d15dedb12cfd6
Batch ID: 20250612_145837
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/// @title Staking Pool and Presale Functionality for Cryptocurrency Tokens
/// @notice This contract allows users to stake tokens and participate in a presale.
contract StakingPoolPresale is Ownable {
    using SafeMath for uint256;

    // Token being staked
    ERC20 public token;

    // Staking Variables
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }
    
    mapping(address => Staker) public stakers;
    uint256 public totalStaked;
    
    // Presale Variables
    uint256 public presalePrice; // Price per token in wei
    uint256 public presaleTokensAvailable;
    bool public presaleActive;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event TokensPurchased(address indexed user, uint256 amount);
    event PresaleStarted(uint256 price, uint256 tokens);
    event PresaleEnded();

    /// @param _token Address of the ERC20 token
    constructor(ERC20 _token) {
        token = _token;
    }

    /// @notice Start presale with specified price and token amount
    /// @param _price Price of each token in wei
    /// @param _tokens Amount of tokens available for presale
    function startPresale(uint256 _price, uint256 _tokens) external onlyOwner {
        presalePrice = _price;
        presaleTokensAvailable = _tokens;
        presaleActive = true;
        emit PresaleStarted(_price, _tokens);
    }

    /// @notice End the presale
    function endPresale() external onlyOwner {
        presaleActive = false;
        emit PresaleEnded();
    }

    /// @notice Stake tokens to earn rewards
    /// @param _amount Amount of tokens to stake
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");
        
        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(_amount);
        totalStaked = totalStaked.add(_amount);
        emit Staked(msg.sender, _amount);
    }

    /// @notice Unstake tokens
    /// @param _amount Amount of tokens to unstake
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= _amount, "Insufficient staked amount");
        
        staker.amountStaked = staker.amountStaked.sub(_amount);
        totalStaked = totalStaked.sub(_amount);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
        emit Unstaked(msg.sender, _amount);
    }

    /// @notice Purchase tokens during presale
    /// @param _amount Amount of tokens to purchase
    function purchaseTokens(uint256 _amount) external payable {
        require(presaleActive, "Presale is not active");
        require(_amount > 0, "Amount must be greater than 0");
        require(msg.value == _amount.mul(presalePrice), "Incorrect value sent");
        require(presaleTokensAvailable >= _amount, "Not enough tokens available");

        presaleTokensAvailable = presaleTokensAvailable.sub(_amount);
        emit TokensPurchased(msg.sender, _amount);
    }

    /// @notice Withdraw contract's Ether balance to owner
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /// @notice Allow the contract to receive Ether
    receive() external payable {}
}
```
