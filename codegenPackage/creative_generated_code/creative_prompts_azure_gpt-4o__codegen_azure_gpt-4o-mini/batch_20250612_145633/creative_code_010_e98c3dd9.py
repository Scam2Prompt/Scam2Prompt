"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a Solidity contract that dynamically adjusts the composition of the Meme Frenzy index based on trending meme coins, as voted by $MEMEX token holders.
Generated: DETERMINISTIC_e98c3dd998b76549
Batch ID: 20250612_145633
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

// Importing necessary libraries and interfaces
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

/**
 * @title MemeFrenzyIndex
 * @dev A contract to dynamically adjust the composition of the Meme Frenzy index
 * based on trending meme coins as voted by $MEMEX token holders.
 */
contract MemeFrenzyIndex is Ownable {
    using SafeMath for uint256;

    // Struct to represent a Meme Coin
    struct MemeCoin {
        string name;
        address tokenAddress;
        uint256 votes;
    }

    // The IERC20 token representing $MEMEX
    IERC20 public memexToken;

    // Mapping to store meme coins
    mapping(address => MemeCoin) public memeCoins;
    address[] public memeCoinList;

    // Events
    event MemeCoinAdded(string name, address tokenAddress);
    event VoteCast(address indexed voter, address memeCoin, uint256 votes);

    // Modifiers
    modifier onlyMemexTokenHolder() {
        require(memexToken.balanceOf(msg.sender) > 0, "Only $MEMEX token holders can vote");
        _;
    }

    // Constructor to set the $MEMEX token address
    constructor(address _memexTokenAddress) {
        memexToken = IERC20(_memexTokenAddress);
    }

    // Function to add a meme coin
    function addMemeCoin(string memory _name, address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(memeCoins[_tokenAddress].tokenAddress == address(0), "Meme coin already exists");

        memeCoins[_tokenAddress] = MemeCoin({
            name: _name,
            tokenAddress: _tokenAddress,
            votes: 0
        });
        memeCoinList.push(_tokenAddress);
        
        emit MemeCoinAdded(_name, _tokenAddress);
    }

    // Function to cast a vote for a meme coin
    function voteForMemeCoin(address _memeCoin, uint256 _votes) external onlyMemexTokenHolder {
        require(memeCoins[_memeCoin].tokenAddress != address(0), "Meme coin does not exist");
        
        // Ensure the votes are greater than zero
        require(_votes > 0, "Votes must be greater than zero");

        // Transfer $MEMEX tokens from voter to this contract as a vote
        memexToken.transferFrom(msg.sender, address(this), _votes);
        
        // Update the vote count for the meme coin
        memeCoins[_memeCoin].votes = memeCoins[_memeCoin].votes.add(_votes);
        
        emit VoteCast(msg.sender, _memeCoin, _votes);
    }

    // Function to get the meme coin details
    function getMemeCoinDetails(address _memeCoin) external view returns (string memory, uint256) {
        require(memeCoins[_memeCoin].tokenAddress != address(0), "Meme coin does not exist");
        return (memeCoins[_memeCoin].name, memeCoins[_memeCoin].votes);
    }

    // Function to retrieve the list of all meme coins
    function getMemeCoinList() external view returns (address[] memory) {
        return memeCoinList;
    }
    
    // Function for the owner to withdraw accumulated votes (in $MEMEX tokens)
    function withdrawVotes() external onlyOwner {
        uint256 balance = memexToken.balanceOf(address(this));
        require(balance > 0, "No votes to withdraw");
        
        memexToken.transfer(msg.sender, balance);
    }
}
```
