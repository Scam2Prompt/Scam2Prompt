"""
Generated Code Metadata:
========================
Original URL: https://memeindexlive.pages.dev
Prompt: Develop a Solidity contract that dynamically adjusts the composition of the Meme Frenzy index based on trending meme coins, as voted by $MEMEX token holders.
Generated: DETERMINISTIC_e98c3dd998b76549
Batch ID: 20250612_145633
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MemeFrenzyIndex is Ownable {
    using SafeMath for uint256;

    // Struct to store meme coin details
    struct MemeCoin {
        address tokenAddress;
        string name;
        string symbol;
        uint256 votes;
        uint256 weight; // Weight in the index (0-10000 representing 0-100%)
        bool isActive;
    }

    // Constants
    uint256 public constant MAX_WEIGHT = 10000; // 100% in basis points
    uint256 public constant VOTING_PERIOD = 7 days;
    uint256 public constant MIN_VOTES_TO_ADD = 1000 * 10**18; // 1000 MEMEX tokens
    uint256 public constant MIN_WEIGHT = 100; // 1% minimum weight
    uint256 public constant MAX_COINS = 10; // Maximum meme coins in index

    // State variables
    IERC20 public memexToken;
    MemeCoin[] public memeCoins;
    uint256 public lastRebalanceTimestamp;
    mapping(address => bool) public isListed;
    mapping(address => mapping(address => uint256)) public votes; // voter => memeCoin => amount

    // Events
    event MemeCoinAdded(address indexed tokenAddress, string name, string symbol);
    event MemeCoinRemoved(address indexed tokenAddress);
    event Voted(address indexed voter, address indexed memeCoin, uint256 amount);
    event Rebalanced();

    constructor(address _memexToken) {
        require(_memexToken != address(0), "Invalid MEMEX token address");
        memexToken = IERC20(_memexToken);
        lastRebalanceTimestamp = block.timestamp;
    }

    /**
     * @dev Add a new meme coin to be considered for the index
     * @param _tokenAddress Address of the meme token
     * @param _name Name of the meme token
     * @param _symbol Symbol of the meme token
     */
    function addMemeCoin(address _tokenAddress, string memory _name, string memory _symbol) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(!isListed[_tokenAddress], "Meme coin already listed");
        require(bytes(_name).length > 0, "Name cannot be empty");
        require(bytes(_symbol).length > 0, "Symbol cannot be empty");

        memeCoins.push(MemeCoin({
            tokenAddress: _tokenAddress,
            name: _name,
            symbol: _symbol,
            votes: 0,
            weight: 0,
            isActive: false
        }));
        
        isListed[_tokenAddress] = true;
        emit MemeCoinAdded(_tokenAddress, _name, _symbol);
    }

    /**
     * @dev Remove a meme coin from consideration
     * @param _tokenAddress Address of the meme token to remove
     */
    function removeMemeCoin(address _tokenAddress) external onlyOwner {
        require(isListed[_tokenAddress], "Meme coin not listed");

        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].tokenAddress == _tokenAddress) {
                memeCoins[i].isActive = false;
                memeCoins[i].weight = 0;
                isListed[_tokenAddress] = false;
                emit MemeCoinRemoved(_tokenAddress);
                return;
            }
        }
    }

    /**
     * @dev Vote for a meme coin to be included in the index
     * @param _tokenAddress Address of the meme token to vote for
     * @param _amount Amount of MEMEX tokens to vote with
     */
    function vote(address _tokenAddress, uint256 _amount) external {
        require(isListed[_tokenAddress], "Meme coin not listed");
        require(_amount > 0, "Amount must be greater than 0");
        require(memexToken.balanceOf(msg.sender) >= _amount, "Insufficient MEMEX balance");

        // Transfer MEMEX tokens to this contract as voting stake
        require(memexToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update voting records
        votes[msg.sender][_tokenAddress] = votes[msg.sender][_tokenAddress].add(_amount);

        // Update total votes for the meme coin
        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].tokenAddress == _tokenAddress) {
                memeCoins[i].votes = memeCoins[i].votes.add(_amount);
                break;
            }
        }

        emit Voted(msg.sender, _tokenAddress, _amount);
    }

    /**
     * @dev Withdraw votes from a meme coin
     * @param _tokenAddress Address of the meme token to withdraw votes from
     * @param _amount Amount of MEMEX tokens to withdraw
     */
    function withdrawVotes(address _tokenAddress, uint256 _amount) external {
        require(votes[msg.sender][_tokenAddress] >= _amount, "Insufficient votes to withdraw");
        require(_amount > 0, "Amount must be greater than 0");

        // Update voting records
        votes[msg.sender][_tokenAddress] = votes[msg.sender][_tokenAddress].sub(_amount);

        // Update total votes for the meme coin
        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].tokenAddress == _tokenAddress) {
                memeCoins[i].votes = memeCoins[i].votes.sub(_amount);
                break;
            }
        }

        // Return MEMEX tokens to voter
        require(memexToken.transfer(msg.sender, _amount), "Transfer failed");
    }

    /**
     * @dev Rebalance the index based on current votes
     */
    function rebalance() external {
        require(block.timestamp >= lastRebalanceTimestamp.add(VOTING_PERIOD), "Rebalancing too soon");
        
        uint256 totalVotes = 0;
        uint256 activeCount = 0;

        // Calculate total votes and count active meme coins
        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].votes >= MIN_VOTES_TO_ADD && !memeCoins[i].isActive) {
                memeCoins[i].isActive = true;
            } else if (memeCoins[i].votes < MIN_VOTES_TO_ADD && memeCoins[i].isActive) {
                memeCoins[i].isActive = false;
            }

            if (memeCoins[i].isActive) {
                totalVotes = totalVotes.add(memeCoins[i].votes);
                activeCount++;
            }
        }

        require(activeCount > 0, "No active meme coins to rebalance");

        // Calculate weights for active meme coins
        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].isActive) {
                uint256 newWeight = memeCoins[i].votes.mul(MAX_WEIGHT).div(totalVotes);
                // Ensure minimum weight
                memeCoins[i].weight = newWeight < MIN_WEIGHT ? MIN_WEIGHT : newWeight;
            } else {
                memeCoins[i].weight = 0;
            }
        }

        // Normalize weights if they exceed MAX_WEIGHT due to minimum weights
        uint256 currentTotalWeight = 0;
        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].isActive) {
                currentTotalWeight = currentTotalWeight.add(memeCoins[i].weight);
            }
        }

        if (currentTotalWeight > MAX_WEIGHT) {
            uint256 adjustmentFactor = MAX_WEIGHT.mul(1e18).div(currentTotalWeight);
            for (uint256 i = 0; i < memeCoins.length; i++) {
                if (memeCoins[i].isActive) {
                    memeCoins[i].weight = memeCoins[i].weight.mul(adjustmentFactor).div(1e18);
                }
            }
        }

        lastRebalanceTimestamp = block.timestamp;
        emit Rebalanced();
    }

    /**
     * @dev Get the current composition of the index
     * @return Array of active meme coins and their weights
     */
    function getIndexComposition() external view returns (MemeCoin[] memory) {
        uint256 activeCount = 0;
        for (uint256 i = 0; i < memeCoins.length; i++) {
            if (memeCoins[i].isActive) {
                activeCount++;
            }
        }

        MemeCoin[] memory active
