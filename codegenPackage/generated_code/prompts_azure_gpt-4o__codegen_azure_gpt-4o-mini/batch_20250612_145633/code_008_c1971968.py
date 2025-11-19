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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Meme Coin Index Fund
interface IMemeCoinIndex {
    function getIndexValue() external view returns (uint256);
}

// MemeCoinIndexFund contract
contract MemeCoinIndexFund is Ownable {
    using SafeMath for uint256;

    // Struct to hold index information
    struct Index {
        string name;
        address indexContract;
        uint256 weight; // Weight of the index in the fund
    }

    // Array to hold indices
    Index[] public indices;

    // Total weight of all indices
    uint256 public totalWeight;

    // Event emitted when an index is added
    event IndexAdded(string name, address indexContract, uint256 weight);

    // Event emitted when an index is removed
    event IndexRemoved(string name);

    // Event emitted when the fund value is updated
    event FundValueUpdated(uint256 newValue);

    // Function to add a new index to the fund
    function addIndex(string memory _name, address _indexContract, uint256 _weight) external onlyOwner {
        require(_indexContract != address(0), "Invalid index contract address");
        require(_weight > 0, "Weight must be greater than zero");

        indices.push(Index({
            name: _name,
            indexContract: _indexContract,
            weight: _weight
        }));

        totalWeight = totalWeight.add(_weight);
        emit IndexAdded(_name, _indexContract, _weight);
    }

    // Function to remove an index from the fund
    function removeIndex(uint256 _index) external onlyOwner {
        require(_index < indices.length, "Index out of bounds");

        // Get the index to remove
        Index memory indexToRemove = indices[_index];

        // Shift indices to fill the gap
        for (uint256 i = _index; i < indices.length - 1; i++) {
            indices[i] = indices[i + 1];
        }
        indices.pop(); // Remove the last element

        totalWeight = totalWeight.sub(indexToRemove.weight);
        emit IndexRemoved(indexToRemove.name);
    }

    // Function to get the total value of the fund based on the indices
    function getFundValue() external view returns (uint256 totalValue) {
        totalValue = 0;

        for (uint256 i = 0; i < indices.length; i++) {
            uint256 indexValue = IMemeCoinIndex(indices[i].indexContract).getIndexValue();
            totalValue = totalValue.add(indexValue.mul(indices[i].weight).div(totalWeight));
        }

        emit FundValueUpdated(totalValue);
    }

    // Function to get the number of indices in the fund
    function getIndexCount() external view returns (uint256) {
        return indices.length;
    }

    // Function to get index details
    function getIndex(uint256 _index) external view returns (string memory name, address indexContract, uint256 weight) {
        require(_index < indices.length, "Index out of bounds");
        Index memory index = indices[_index];
        return (index.name, index.indexContract, index.weight);
    }
}
```
