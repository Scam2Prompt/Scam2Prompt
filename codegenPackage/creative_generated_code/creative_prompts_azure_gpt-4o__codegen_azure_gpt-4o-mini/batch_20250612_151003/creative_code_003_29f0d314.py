"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d-510.pages.dev
Prompt: Create a smart contract in Solidity for a utility token like Lingo, ensuring it includes functionality for interacting with a Community DAO to select RWA investments.
Generated: DETERMINISTIC_29f0d314d29e4daa
Batch ID: 20250612_151003
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

// Importing OpenZeppelin Contracts for ERC20 and Ownable functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Utility token contract that extends ERC20 and Ownable
contract LingoToken is ERC20, Ownable {
    // Community DAO address to interact with
    address public communityDAO;

    // Event emitted when the community DAO is set
    event CommunityDAOSet(address indexed newDAO);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Lingo Token", "LINGO") {
        // Mint initial supply to the deployer
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to set the Community DAO address
    function setCommunityDAO(address _communityDAO) external onlyOwner {
        require(_communityDAO != address(0), "Invalid address");
        communityDAO = _communityDAO;
        emit CommunityDAOSet(_communityDAO);
    }

    // Function to approve DAO for spending tokens
    function approveDAO(uint256 amount) external onlyOwner {
        require(communityDAO != address(0), "Community DAO not set");
        _approve(msg.sender, communityDAO, amount);
    }

    // Function to transfer tokens from the contract to a specified address
    function transferFromDAO(address recipient, uint256 amount) external {
        require(msg.sender == communityDAO, "Only DAO can transfer");
        _transfer(address(this), recipient, amount);
    }

    // Function to withdraw any mistakenly sent ERC20 tokens to this contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
