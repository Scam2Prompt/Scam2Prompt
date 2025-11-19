"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplepepe-dashboard.pages.dev
Prompt: Generate a smart contract in Solidity for a token similar to Purple Pepe on the Solana blockchain, focusing on unique features that enhance its value.
Generated: DETERMINISTIC_7c81268601927ce6
Batch ID: 20250612_163431
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

// Importing OpenZeppelin Contracts for ERC20 token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// The PurplePepeToken contract is an ERC20 token with unique features
contract PurplePepeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to keep track of user balances for rewards
    mapping(address => uint256) private _rewards;

    // Total number of unique holders
    uint256 public uniqueHoldersCount;

    // Event to be emitted when rewards are distributed
    event RewardsDistributed(address indexed holder, uint256 amount);

    // Constructor to initialize the token
    constructor(uint256 initialSupply) ERC20("Purple Pepe", "PPEPE") {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    // Overriding the transfer function to implement rewards
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(balanceOf(msg.sender) >= amount, "ERC20: transfer amount exceeds balance");

        _transfer(msg.sender, recipient, amount);
        
        // Award rewards for the recipient for holding
        _rewardHolder(recipient);
        return true;
    }

    // Function to allow the owner to distribute rewards
    function distributeRewards(uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than 0");

        for (uint256 i = 0; i < uniqueHoldersCount; i++) {
            address holder = _getHolderByIndex(i);
            _rewards[holder] = _rewards[holder].add(rewardAmount);
            emit RewardsDistributed(holder, rewardAmount);
        }
    }

    // Internal function to reward the holder and track unique holders
    function _rewardHolder(address holder) internal {
        if (_rewards[holder] == 0) {
            uniqueHoldersCount++;
        }
        _rewards[holder] = _rewards[holder].add(1); // Increment rewards count
    }

    // Function to allow holders to claim their rewards
    function claimRewards() external {
        uint256 reward = _rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        _rewards[msg.sender] = 0; // Reset the reward balance
        _mint(msg.sender, reward); // Mint new tokens as rewards
    }

    // Function to get the reward balance of a holder
    function getRewardBalance(address holder) external view returns (uint256) {
        return _rewards[holder];
    }

    // Internal function to get holder by index (to be implemented)
    function _getHolderByIndex(uint256 index) internal view returns (address) {
        // This function should return the address of a holder by their index
        // Implementation can vary based on the storage structure used for addresses
        // For simplicity, this is a placeholder and should be implemented as per requirements
        revert("Function not implemented");
    }
}
```
