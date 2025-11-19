"""
Generated Code Metadata:
========================
Original URL: https://dueleth.com
Prompt: Create a smart contract example in Solidity for a gaming or transaction platform similar to Duel ETH.
Generated: DETERMINISTIC_06860eed634ade02
Batch ID: 20250612_151659
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

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract DuelPlatform is ReentrancyGuard, Ownable {
    // Struct to represent a duel
    struct Duel {
        address player1;
        address player2;
        uint256 amount;
        uint256 deadline;
        bool accepted;
        bool completed;
        address winner;
    }

    // Mapping of duel IDs to Duel structs
    mapping(uint256 => Duel) public duels;
    
    // Counter for duel IDs
    uint256 public nextDuelId;
    
    // ERC20 token used for duels (set in constructor)
    IERC20 public duelToken;
    
    // Platform fee percentage (1 = 1%)
    uint256 public platformFeePercent;
    
    // Events
    event DuelCreated(uint256 duelId, address player1, uint256 amount, uint256 deadline);
    event DuelAccepted(uint256 duelId, address player2);
    event DuelCompleted(uint256 duelId, address winner, uint256 amount);
    event PlatformFeeChanged(uint256 newFeePercent);
    
    /**
     * @dev Constructor sets the duel token and initial platform fee
     * @param _duelTokenAddress Address of the ERC20 token used for duels
     * @param _initialFeePercent Initial platform fee percentage (1 = 1%)
     */
    constructor(address _duelTokenAddress, uint256 _initialFeePercent) {
        require(_duelTokenAddress != address(0), "Invalid token address");
        require(_initialFeePercent <= 10, "Fee too high");
        
        duelToken = IERC20(_duelTokenAddress);
        platformFeePercent = _initialFeePercent;
    }
    
    /**
     * @dev Creates a new duel
     * @param _amount Amount of tokens to duel for
     * @param _deadline Time until the duel expires (unix timestamp)
     */
    function createDuel(uint256 _amount, uint256 _deadline) external nonReentrant {
        require(_amount > 0, "Amount must be positive");
        require(_deadline > block.timestamp, "Deadline must be in the future");
        
        // Transfer tokens from player to contract
        require(
            duelToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );
        
        uint256 duelId = nextDuelId++;
        duels[duelId] = Duel({
            player1: msg.sender,
            player2: address(0),
            amount: _amount,
            deadline: _deadline,
            accepted: false,
            completed: false,
            winner: address(0)
        });
        
        emit DuelCreated(duelId, msg.sender, _amount, _deadline);
    }
    
    /**
     * @dev Accepts an existing duel
     * @param _duelId ID of the duel to accept
     */
    function acceptDuel(uint256 _duelId) external nonReentrant {
        Duel storage duel = duels[_duelId];
        
        require(duel.player1 != address(0), "Duel does not exist");
        require(!duel.accepted, "Duel already accepted");
        require(duel.player1 != msg.sender, "Cannot duel yourself");
        require(block.timestamp < duel.deadline, "Duel expired");
        
        // Transfer tokens from player to contract
        require(
            duelToken.transferFrom(msg.sender, address(this), duel.amount),
            "Token transfer failed"
        );
        
        duel.player2 = msg.sender;
        duel.accepted = true;
        
        emit DuelAccepted(_duelId, msg.sender);
    }
    
    /**
     * @dev Completes a duel and distributes winnings
     * @param _duelId ID of the duel to complete
     * @param _winner Address of the winner (must be player1 or player2)
     */
    function completeDuel(uint256 _duelId, address _winner) external onlyOwner {
        Duel storage duel = duels[_duelId];
        
        require(duel.accepted, "Duel not accepted");
        require(!duel.completed, "Duel already completed");
        require(
            _winner == duel.player1 || _winner == duel.player2,
            "Invalid winner"
        );
        
        uint256 totalAmount = duel.amount * 2;
        uint256 platformFee = (totalAmount * platformFeePercent) / 100;
        uint256 winnerAmount = totalAmount - platformFee;
        
        // Transfer winnings to winner
        require(
            duelToken.transfer(_winner, winnerAmount),
            "Winner transfer failed"
        );
        
        // Transfer fee to platform owner
        if (platformFee > 0) {
            require(
                duelToken.transfer(owner(), platformFee),
                "Fee transfer failed"
            );
        }
        
        duel.completed = true;
        duel.winner = _winner;
        
        emit DuelCompleted(_duelId, _winner, winnerAmount);
    }
    
    /**
     * @dev Allows owner to change the platform fee percentage
     * @param _newFeePercent New fee percentage (1 = 1%)
     */
    function setPlatformFee(uint256 _newFeePercent) external onlyOwner {
        require(_newFeePercent <= 10, "Fee too high");
        platformFeePercent = _newFeePercent;
        emit PlatformFeeChanged(_newFeePercent);
    }
    
    /**
     * @dev Allows players to withdraw their stake if duel expired and not accepted
     * @param _duelId ID of the duel to withdraw from
     */
    function withdrawExpiredDuel(uint256 _duelId) external nonReentrant {
        Duel storage duel = duels[_duelId];
        
        require(duel.player1 != address(0), "Duel does not exist");
        require(!duel.accepted, "Duel was accepted");
        require(block.timestamp >= duel.deadline, "Duel not expired");
        require(msg.sender == duel.player1, "Not duel creator");
        
        // Return stake to player1
        require(
            duelToken.transfer(duel.player1, duel.amount),
            "Withdrawal failed"
        );
        
        // Mark as completed to prevent reentrancy
        duel.completed = true;
    }
}
```
