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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MemeFrenzyIndex
 * @author [Your Name]
 * @notice A dynamic index that adjusts its composition based on trending meme coins voted by $MEMEX token holders.
 */
contract MemeFrenzyIndex is Ownable {
    using SafeMath for uint256;

    // Mapping of meme coins to their respective weights in the index
    mapping(address => uint256) public memeCoinWeights;

    // Mapping of meme coins to their respective votes
    mapping(address => uint256) public memeCoinVotes;

    // Total weight of all meme coins in the index
    uint256 public totalWeight;

    // $MEMEX token contract
    IERC20 public memexToken;

    // Minimum and maximum weights for each meme coin
    uint256 public minWeight;
    uint256 public maxWeight;

    // Voting deadline for each meme coin
    mapping(address => uint256) public votingDeadlines;

    // Event emitted when a meme coin is added to the index
    event MemeCoinAdded(address indexed memeCoin, uint256 weight);

    // Event emitted when a meme coin is removed from the index
    event MemeCoinRemoved(address indexed memeCoin);

    // Event emitted when a meme coin's weight is updated
    event MemeCoinWeightUpdated(address indexed memeCoin, uint256 newWeight);

    // Event emitted when a vote is cast for a meme coin
    event VoteCast(address indexed voter, address indexed memeCoin, uint256 votes);

    /**
     * @param _memexToken $MEMEX token contract
     * @param _minWeight Minimum weight for each meme coin
     * @param _maxWeight Maximum weight for each meme coin
     */
    constructor(IERC20 _memexToken, uint256 _minWeight, uint256 _maxWeight) public {
        memexToken = _memexToken;
        minWeight = _minWeight;
        maxWeight = _maxWeight;
    }

    /**
     * @dev Adds a meme coin to the index
     * @param _memeCoin Meme coin contract
     * @param _initialWeight Initial weight of the meme coin
     */
    function addMemeCoin(address _memeCoin, uint256 _initialWeight) public onlyOwner {
        require(_initialWeight >= minWeight && _initialWeight <= maxWeight, "Invalid initial weight");
        memeCoinWeights[_memeCoin] = _initialWeight;
        totalWeight = totalWeight.add(_initialWeight);
        emit MemeCoinAdded(_memeCoin, _initialWeight);
    }

    /**
     * @dev Removes a meme coin from the index
     * @param _memeCoin Meme coin contract
     */
    function removeMemeCoin(address _memeCoin) public onlyOwner {
        require(memeCoinWeights[_memeCoin] > 0, "Meme coin not in index");
        uint256 weight = memeCoinWeights[_memeCoin];
        delete memeCoinWeights[_memeCoin];
        totalWeight = totalWeight.sub(weight);
        emit MemeCoinRemoved(_memeCoin);
    }

    /**
     * @dev Updates the weight of a meme coin in the index
     * @param _memeCoin Meme coin contract
     * @param _newWeight New weight of the meme coin
     */
    function updateMemeCoinWeight(address _memeCoin, uint256 _newWeight) public onlyOwner {
        require(_newWeight >= minWeight && _newWeight <= maxWeight, "Invalid new weight");
        require(memeCoinWeights[_memeCoin] > 0, "Meme coin not in index");
        uint256 oldWeight = memeCoinWeights[_memeCoin];
        memeCoinWeights[_memeCoin] = _newWeight;
        totalWeight = totalWeight.sub(oldWeight).add(_newWeight);
        emit MemeCoinWeightUpdated(_memeCoin, _newWeight);
    }

    /**
     * @dev Casts a vote for a meme coin
     * @param _memeCoin Meme coin contract
     * @param _votes Number of votes to cast
     */
    function castVote(address _memeCoin, uint256 _votes) public {
        require(memeCoinWeights[_memeCoin] > 0, "Meme coin not in index");
        require(memexToken.balanceOf(msg.sender) >= _votes, "Insufficient $MEMEX tokens");
        memeCoinVotes[_memeCoin] = memeCoinVotes[_memeCoin].add(_votes);
        memexToken.transferFrom(msg.sender, address(this), _votes);
        emit VoteCast(msg.sender, _memeCoin, _votes);
    }

    /**
     * @dev Updates the composition of the index based on trending meme coins
     */
    function updateIndexComposition() public {
        // Calculate total votes
        uint256 totalVotes = 0;
        for (address memeCoin in memeCoinWeights) {
            totalVotes = totalVotes.add(memeCoinVotes[memeCoin]);
        }

        // Update weights based on votes
        for (address memeCoin in memeCoinWeights) {
            uint256 weight = memeCoinVotes[memeCoin].mul(maxWeight).div(totalVotes);
            updateMemeCoinWeight(memeCoin, weight);
        }

        // Reset votes
        for (address memeCoin in memeCoinWeights) {
            memeCoinVotes[memeCoin] = 0;
        }
    }

    /**
     * @dev Gets the current composition of the index
     * @return Meme coin addresses and their respective weights
     */
    function getIndexComposition() public view returns (address[] memory, uint256[] memory) {
        address[] memory memeCoins = new address[](memeCoinWeights.length);
        uint256[] memory weights = new uint256[](memeCoinWeights.length);
        uint256 i = 0;
        for (address memeCoin in memeCoinWeights) {
            memeCoins[i] = memeCoin;
            weights[i] = memeCoinWeights[memeCoin];
            i++;
        }
        return (memeCoins, weights);
    }
}
```
