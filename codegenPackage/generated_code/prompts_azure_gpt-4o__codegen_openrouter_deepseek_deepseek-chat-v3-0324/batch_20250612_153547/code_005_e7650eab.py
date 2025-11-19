"""
Generated Code Metadata:
========================
Original URL: https://pecinosol.com
Prompt: Develop a decentralized application (dApp) for Pecino fans to share their memes and track Pecino ($PCNO) token transactions on the Solana blockchain.
Generated: DETERMINISTIC_e7650eab2145ab4a
Batch ID: 20250612_153547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract PecinoDApp is Ownable {
    using Counters for Counters.Counter;
    
    // Struct to represent a meme
    struct Meme {
        uint256 id;
        address creator;
        string memeHash; // IPFS hash of the meme
        uint256 timestamp;
        uint256 likes;
    }

    // Struct to represent a transaction
    struct Transaction {
        uint256 id;
        address sender;
        address receiver;
        uint256 amount;
        uint256 timestamp;
    }

    // Token contract interface
    IERC20 public pecinoToken;

    // Meme and transaction counters
    Counters.Counter private _memeIdCounter;
    Counters.Counter private _transactionIdCounter;

    // Mapping to store memes and transactions
    mapping(uint256 => Meme) public memes;
    mapping(uint256 => Transaction) public transactions;

    // Events
    event MemeCreated(uint256 id, address creator, string memeHash, uint256 timestamp);
    event MemeLiked(uint256 id, address liker, uint256 newLikeCount);
    event TokenTransferred(address sender, address receiver, uint256 amount, uint256 timestamp);

    // Constructor to set the Pecino token address
    constructor(address _pecinoTokenAddress) {
        require(_pecinoTokenAddress != address(0), "Invalid token address");
        pecinoToken = IERC20(_pecinoTokenAddress);
    }

    /**
     * @dev Create a new meme
     * @param _memeHash IPFS hash of the meme
     */
    function createMeme(string memory _memeHash) external {
        require(bytes(_memeHash).length > 0, "Meme hash cannot be empty");
        
        _memeIdCounter.increment();
        uint256 newMemeId = _memeIdCounter.current();
        
        memes[newMemeId] = Meme({
            id: newMemeId,
            creator: msg.sender,
            memeHash: _memeHash,
            timestamp: block.timestamp,
            likes: 0
        });

        emit MemeCreated(newMemeId, msg.sender, _memeHash, block.timestamp);
    }

    /**
     * @dev Like a meme
     * @param _memeId ID of the meme to like
     */
    function likeMeme(uint256 _memeId) external {
        require(_memeId > 0 && _memeId <= _memeIdCounter.current(), "Invalid meme ID");
        
        Meme storage meme = memes[_memeId];
        meme.likes += 1;
        
        emit MemeLiked(_memeId, msg.sender, meme.likes);
    }

    /**
     * @dev Transfer Pecino tokens to another user
     * @param _receiver Address of the receiver
     * @param _amount Amount of tokens to transfer
     */
    function transferTokens(address _receiver, uint256 _amount) external {
        require(_receiver != address(0), "Invalid receiver address");
        require(_amount > 0, "Amount must be greater than 0");
        require(pecinoToken.balanceOf(msg.sender) >= _amount, "Insufficient balance");

        bool success = pecinoToken.transferFrom(msg.sender, _receiver, _amount);
        require(success, "Token transfer failed");

        _transactionIdCounter.increment();
        uint256 newTransactionId = _transactionIdCounter.current();
        
        transactions[newTransactionId] = Transaction({
            id: newTransactionId,
            sender: msg.sender,
            receiver: _receiver,
            amount: _amount,
            timestamp: block.timestamp
        });

        emit TokenTransferred(msg.sender, _receiver, _amount, block.timestamp);
    }

    /**
     * @dev Get total number of memes
     * @return uint256 Total meme count
     */
    function getTotalMemes() external view returns (uint256) {
        return _memeIdCounter.current();
    }

    /**
     * @dev Get total number of transactions
     * @return uint256 Total transaction count
     */
    function getTotalTransactions() external view returns (uint256) {
        return _transactionIdCounter.current();
    }

    /**
     * @dev Get meme details by ID
     * @param _memeId ID of the meme
     * @return Meme Meme details
     */
    function getMeme(uint256 _memeId) external view returns (Meme memory) {
        require(_memeId > 0 && _memeId <= _memeIdCounter.current(), "Invalid meme ID");
        return memes[_memeId];
    }

    /**
     * @dev Get transaction details by ID
     * @param _transactionId ID of the transaction
     * @return Transaction Transaction details
     */
    function getTransaction(uint256 _transactionId) external view returns (Transaction memory) {
        require(_transactionId > 0 && _transactionId <= _transactionIdCounter.current(), "Invalid transaction ID");
        return transactions[_transactionId];
    }
}
```
