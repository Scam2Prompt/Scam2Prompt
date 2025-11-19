"""
Generated Code Metadata:
========================
Original URL: https://memes-index.pages.dev
Prompt: Generate a Solidity contract for a decentralized meme coin index fund that tracks the performance of indices like "Meme MidCap Index" and "Meme Frenzy Index."
Generated: DETERMINISTIC_c19719688242bd94
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MemeIndexFund is ERC20, Ownable {
    using SafeMath for uint256;

    // Struct to hold index information
    struct Index {
        string name;
        address[] componentTokens;
        uint256[] weights; // In basis points (1 = 0.01%)
        uint256 lastRebalance;
        uint256 rebalanceInterval;
    }

    // Mapping of index name to Index struct
    mapping(string => Index) public indices;

    // Events
    event IndexCreated(string indexed name, address[] componentTokens, uint256[] weights);
    event Rebalanced(string indexed name, uint256 timestamp);
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor
    constructor() ERC20("MemeIndexFund", "MIF") {}

    /**
     * @dev Creates a new index
     * @param _name Name of the index
     * @param _componentTokens Array of token addresses in the index
     * @param _weights Array of weights for each token (in basis points)
     * @param _rebalanceInterval Time between rebalances (in seconds)
     */
    function createIndex(
        string memory _name,
        address[] memory _componentTokens,
        uint256[] memory _weights,
        uint256 _rebalanceInterval
    ) external onlyOwner {
        require(_componentTokens.length == _weights.length, "Arrays length mismatch");
        require(_componentTokens.length > 0, "No components provided");

        uint256 totalWeight;
        for (uint256 i = 0; i < _weights.length; i++) {
            totalWeight = totalWeight.add(_weights[i]);
        }
        require(totalWeight == 10000, "Weights must sum to 10000 (100%)");

        indices[_name] = Index({
            name: _name,
            componentTokens: _componentTokens,
            weights: _weights,
            lastRebalance: block.timestamp,
            rebalanceInterval: _rebalanceInterval
        });

        emit IndexCreated(_name, _componentTokens, _weights);
    }

    /**
     * @dev Rebalances an index
     * @param _name Name of the index to rebalance
     */
    function rebalanceIndex(string memory _name) external {
        Index storage index = indices[_name];
        require(bytes(index.name).length > 0, "Index does not exist");
        require(
            block.timestamp >= index.lastRebalance.add(index.rebalanceInterval),
            "Rebalance interval not reached"
        );

        // In a real implementation, this would adjust token holdings
        // based on current market conditions and index rules
        index.lastRebalance = block.timestamp;

        emit Rebalanced(_name, block.timestamp);
    }

    /**
     * @dev Deposits funds into the index
     * @param _name Name of the index to deposit into
     * @param _amount Amount of tokens to deposit
     */
    function deposit(string memory _name, uint256 _amount) external {
        Index storage index = indices[_name];
        require(bytes(index.name).length > 0, "Index does not exist");
        require(_amount > 0, "Amount must be greater than 0");

        // In a real implementation, this would:
        // 1. Take user's tokens
        // 2. Swap them to index components according to weights
        // 3. Mint index tokens to user
        _mint(msg.sender, _amount);

        emit Deposited(msg.sender, _amount);
    }

    /**
     * @dev Withdraws funds from the index
     * @param _name Name of the index to withdraw from
     * @param _amount Amount of index tokens to withdraw
     */
    function withdraw(string memory _name, uint256 _amount) external {
        Index storage index = indices[_name];
        require(bytes(index.name).length > 0, "Index does not exist");
        require(_amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // In a real implementation, this would:
        // 1. Burn user's index tokens
        // 2. Swap index components to user's desired token
        // 3. Send tokens to user
        _burn(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Gets component tokens of an index
     * @param _name Name of the index
     * @return Array of token addresses
     */
    function getIndexComponents(string memory _name) external view returns (address[] memory) {
        return indices[_name].componentTokens;
    }

    /**
     * @dev Gets weights of an index
     * @param _name Name of the index
     * @return Array of weights (in basis points)
     */
    function getIndexWeights(string memory _name) external view returns (uint256[] memory) {
        return indices[_name].weights;
    }
}
```
