"""
Generated Code Metadata:
========================
Original URL: https://go-beam.pages.dev
Prompt: Generate a smart contract code snippet for a simple Web3 game that uses BEAM token for in-game purchases and USDC for cross-border transactions.
Generated: DETERMINISTIC_829d033c3e359b23
Batch ID: 20250622_211131
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

contract Web3Game is Ownable, ReentrancyGuard {
    // Token contracts
    IERC20 public beamToken;
    IERC20 public usdcToken;

    // Game state variables
    mapping(address => uint256) public playerScores;
    mapping(address => uint256) public beamBalances;
    mapping(address => uint256) public usdcBalances;

    // Events
    event BeamDeposited(address indexed player, uint256 amount);
    event USDCTransferred(address indexed sender, address indexed receiver, uint256 amount);
    event ItemPurchased(address indexed player, uint256 itemId, uint256 price);
    event ScoreUpdated(address indexed player, uint256 newScore);

    /**
     * @dev Constructor initializes the token contracts
     * @param _beamTokenAddress Address of the BEAM token contract
     * @param _usdcTokenAddress Address of the USDC token contract
     */
    constructor(address _beamTokenAddress, address _usdcTokenAddress) {
        require(_beamTokenAddress != address(0), "BEAM token address cannot be zero");
        require(_usdcTokenAddress != address(0), "USDC token address cannot be zero");
        
        beamToken = IERC20(_beamTokenAddress);
        usdcToken = IERC20(_usdcTokenAddress);
    }

    /**
     * @dev Deposit BEAM tokens to player's in-game balance
     * @param amount Amount of BEAM tokens to deposit
     */
    function depositBeam(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        bool success = beamToken.transferFrom(msg.sender, address(this), amount);
        require(success, "BEAM transfer failed");
        
        beamBalances[msg.sender] += amount;
        emit BeamDeposited(msg.sender, amount);
    }

    /**
     * @dev Transfer USDC between players (cross-border transactions)
     * @param receiver Address of the receiver
     * @param amount Amount of USDC to transfer
     */
    function transferUSDC(address receiver, uint256 amount) external nonReentrant {
        require(receiver != address(0), "Receiver address cannot be zero");
        require(amount > 0, "Amount must be greater than zero");
        require(usdcBalances[msg.sender] >= amount, "Insufficient USDC balance");

        usdcBalances[msg.sender] -= amount;
        usdcBalances[receiver] += amount;
        
        emit USDCTransferred(msg.sender, receiver, amount);
    }

    /**
     * @dev Purchase in-game item using BEAM tokens
     * @param itemId ID of the item to purchase
     * @param price Price of the item in BEAM tokens
     */
    function purchaseItem(uint256 itemId, uint256 price) external nonReentrant {
        require(price > 0, "Price must be greater than zero");
        require(beamBalances[msg.sender] >= price, "Insufficient BEAM balance");

        beamBalances[msg.sender] -= price;
        // In a real implementation, you would handle the item distribution here
        
        emit ItemPurchased(msg.sender, itemId, price);
    }

    /**
     * @dev Update player score
     * @param newScore New score to set for the player
     */
    function updateScore(uint256 newScore) external {
        require(newScore > playerScores[msg.sender], "New score must be higher than current score");
        
        playerScores[msg.sender] = newScore;
        emit ScoreUpdated(msg.sender, newScore);
    }

    /**
     * @dev Withdraw BEAM tokens from contract (owner only)
     * @param amount Amount of BEAM tokens to withdraw
     */
    function withdrawBeam(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(beamToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        bool success = beamToken.transfer(owner(), amount);
        require(success, "BEAM withdrawal failed");
    }

    /**
     * @dev Withdraw USDC from contract (owner only)
     * @param amount Amount of USDC to withdraw
     */
    function withdrawUSDC(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        bool success = usdcToken.transfer(owner(), amount);
        require(success, "USDC withdrawal failed");
    }
}
```
