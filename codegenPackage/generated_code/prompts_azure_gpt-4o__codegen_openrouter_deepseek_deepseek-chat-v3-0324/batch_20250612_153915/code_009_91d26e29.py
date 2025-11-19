"""
Generated Code Metadata:
========================
Original URL: https://ton-station-2.gitbook.io
Prompt: Provide examples of integrating $SOON token utility into a Web3 game store, inspired by TON Station's collaboration with Web3 gaming studios.
Generated: DETERMINISTIC_91d26e29266a8f56
Batch ID: 20250612_153915
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

/**
 * @title Web3GameStore
 * @dev A contract for a Web3 game store that integrates $SOON token utility
 */
contract Web3GameStore is Ownable, ReentrancyGuard {
    IERC20 public soonToken;
    
    struct Game {
        uint256 id;
        string name;
        uint256 price;
        uint256 soonDiscount; // Discount percentage when paying with SOON tokens
        bool isActive;
    }
    
    mapping(uint256 => Game) public games;
    mapping(address => mapping(uint256 => bool)) public purchasedGames;
    uint256 public gameCount;
    
    event GameAdded(uint256 indexed gameId, string name, uint256 price, uint256 soonDiscount);
    event GamePurchased(address indexed buyer, uint256 indexed gameId, bool usedSoonToken, uint256 amountPaid);
    event Withdrawn(address indexed owner, uint256 amount);
    
    /**
     * @dev Constructor initializes the contract with the $SOON token address
     * @param _soonTokenAddress Address of the $SOON token contract
     */
    constructor(address _soonTokenAddress) {
        require(_soonTokenAddress != address(0), "Invalid token address");
        soonToken = IERC20(_soonTokenAddress);
    }
    
    /**
     * @dev Add a new game to the store
     * @param _name Name of the game
     * @param _price Price in native currency
     * @param _soonDiscount Discount percentage when paying with SOON tokens
     */
    function addGame(string memory _name, uint256 _price, uint256 _soonDiscount) external onlyOwner {
        require(_price > 0, "Price must be greater than 0");
        require(_soonDiscount <= 100, "Discount cannot exceed 100%");
        
        gameCount++;
        games[gameCount] = Game({
            id: gameCount,
            name: _name,
            price: _price,
            soonDiscount: _soonDiscount,
            isActive: true
        });
        
        emit GameAdded(gameCount, _name, _price, _soonDiscount);
    }
    
    /**
     * @dev Toggle game active status
     * @param _gameId ID of the game to toggle
     */
    function toggleGameActive(uint256 _gameId) external onlyOwner {
        require(_gameId > 0 && _gameId <= gameCount, "Invalid game ID");
        games[_gameId].isActive = !games[_gameId].isActive;
    }
    
    /**
     * @dev Purchase a game using native currency
     * @param _gameId ID of the game to purchase
     */
    function purchaseWithNative(uint256 _gameId) external payable nonReentrant {
        require(_gameId > 0 && _gameId <= gameCount, "Invalid game ID");
        Game storage game = games[_gameId];
        require(game.isActive, "Game is not available");
        require(!purchasedGames[msg.sender][_gameId], "Game already purchased");
        require(msg.value >= game.price, "Insufficient payment");
        
        purchasedGames[msg.sender][_gameId] = true;
        emit GamePurchased(msg.sender, _gameId, false, game.price);
    }
    
    /**
     * @dev Purchase a game using $SOON tokens
     * @param _gameId ID of the game to purchase
     */
    function purchaseWithSoon(uint256 _gameId) external nonReentrant {
        require(_gameId > 0 && _gameId <= gameCount, "Invalid game ID");
        Game storage game = games[_gameId];
        require(game.isActive, "Game is not available");
        require(!purchasedGames[msg.sender][_gameId], "Game already purchased");
        
        uint256 discountedPrice = game.price * (100 - game.soonDiscount) / 100;
        uint256 balance = soonToken.balanceOf(msg.sender);
        require(balance >= discountedPrice, "Insufficient SOON token balance");
        
        bool success = soonToken.transferFrom(msg.sender, address(this), discountedPrice);
        require(success, "Token transfer failed");
        
        purchasedGames[msg.sender][_gameId] = true;
        emit GamePurchased(msg.sender, _gameId, true, discountedPrice);
    }
    
    /**
     * @dev Withdraw native currency from contract
     */
    function withdrawNative() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
        
        emit Withdrawn(owner(), balance);
    }
    
    /**
     * @dev Withdraw $SOON tokens from contract
     */
    function withdrawSoon() external onlyOwner {
        uint256 balance = soonToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        
        bool success = soonToken.transfer(owner(), balance);
        require(success, "Token transfer failed");
        
        emit Withdrawn(owner(), balance);
    }
}
```

```javascript
// Frontend integration example using ethers.js
import { ethers } from 'ethers';
import Web3GameStoreABI from './Web3GameStoreABI.json';

const gameStoreAddress = "0x..."; // Contract address
const soonTokenAddress = "0x..."; // SOON token address

// Initialize provider and signer
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();

// Initialize contracts
const gameStoreContract = new ethers.Contract(
  gameStoreAddress,
  Web3GameStoreABI,
  signer
);

const soonTokenContract = new ethers.Contract(
  soonTokenAddress,
  ['function approve(address spender, uint256 amount) external returns (bool)'],
  signer
);

// Example function to purchase game with native currency
async function purchaseWithNative(gameId, price) {
  try {
    const tx = await gameStoreContract.purchaseWithNative(gameId, {
      value: ethers.utils.parseEther(price.toString())
    });
    await tx.wait();
    console.log('Purchase successful!');
  } catch (error) {
    console.error('Purchase failed:', error);
  }
}

// Example function to purchase game with SOON tokens
async function purchaseWithSoon(gameId, price, discount) {
  try {
    // Calculate discounted price
    const discountedPrice = price * (100 - discount) / 100;
    const priceInWei = ethers.utils.parseEther(discountedPrice.toString());
    
    // Approve token transfer
    const approveTx = await soonTokenContract.approve(
      gameStoreAddress,
      priceInWei
    );
    await approveTx.wait();
    
    // Purchase game
    const purchaseTx = await gameStoreContract.purchaseWithSoon(gameId);
    await purchaseTx.wait();
    console.log('Purchase with SOON successful!');
  } catch (error) {
    console.error('Purchase with SOON failed:', error);
  }
}

// Example function to fetch games
async function fetchGames() {
  try {
    const gameCount = await gameStoreContract.gameCount();
    const games = [];
    
    for (let i = 1; i <= gameCount; i++) {
      const game = await gameStoreContract.games(i);
      games.push({
        id: game.id.toString(),
        name: game.name,
        price: ethers.utils.formatEther(game.price),
        soonDiscount: game.soonDiscount.toString(),
        isActive: game.isActive
      });
    }
    
    return games;
  } catch (error) {
    console.error('Error fetching games:', error);
    return [];
  }
}
```
