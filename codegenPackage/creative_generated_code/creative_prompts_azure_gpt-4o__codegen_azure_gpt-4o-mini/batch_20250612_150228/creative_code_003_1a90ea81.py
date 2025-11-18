"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: Write a smart contract in Solidity for a utility token that supports gameplay rewards and integrates with the Pixels platform's Chapter Two release.
Generated: DETERMINISTIC_1a90ea8166379456
Batch ID: 20250612_150228
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

// Import the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// UtilityToken is an ERC20 token used for gameplay rewards on the Pixels platform.
contract UtilityToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Mapping to track user rewards
    mapping(address => uint256) private _rewards;

    // Constructor to initialize the utility token with a name and symbol
    constructor() ERC20("UtilityToken", "UTK") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rewards to a user
    // Only callable by the contract owner
    function distributeRewards(address user, uint256 amount) external onlyOwner {
        require(user != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        // Update the rewards mapping
        _rewards[user] = _rewards[user].add(amount);

        // Emit event for rewards distribution
        emit RewardsDistributed(user, amount);
    }

    // Function to claim rewards by a user
    function claimRewards() external {
        uint256 amount = _rewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards after claiming
        _rewards[msg.sender] = 0;

        // Transfer the rewards to the user
        _mint(msg.sender, amount);
    }

    // Function to view user's rewards
    function viewRewards(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to burn tokens (for tokenomics adjustments)
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    // Function to withdraw ether from the contract (if needed for operational costs)
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Fallback function to receive ether
    receive() external payable {}
}
```
