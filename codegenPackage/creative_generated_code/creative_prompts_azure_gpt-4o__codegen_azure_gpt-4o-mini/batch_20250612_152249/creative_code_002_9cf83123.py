"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihdjl7xixuxxuxsexbtlzb37crgafyrxd5652yvkz4aokv7np4uty.ipfs.dweb.link
Prompt: Create a smart contract function that integrates with the Morpheus Router to process user queries and reward compute providers in MOR tokens.
Generated: DETERMINISTIC_9cf831238cff0ebc
Batch ID: 20250612_152249
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

// Importing the interface for the Morpheus Router and ERC20 token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MorpheusIntegration {
    // State variables
    IERC20 public morToken; // MOR token contract
    address public morpheusRouter; // Address of the Morpheus Router
    address public owner; // Owner of the contract

    // Event to log user queries
    event QueryProcessed(address indexed user, string query, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(address _morToken, address _morpheusRouter) {
        // Set the token and router addresses
        morToken = IERC20(_morToken);
        morpheusRouter = _morpheusRouter;
        owner = msg.sender; // Set the contract deployer as the owner
    }

    /**
     * @dev Processes a user query and rewards computation providers with MOR tokens
     * @param user The address of the user making the query
     * @param query The user's query string
     * @param rewardAmount The amount of MOR tokens to reward the compute provider
     */
    function processQuery(address user, string calldata query, uint256 rewardAmount) external onlyOwner {
        // Validate inputs
        require(user != address(0), "Invalid user address");
        require(bytes(query).length > 0, "Query cannot be empty");
        require(rewardAmount > 0, "Reward must be greater than zero");

        // Interact with the Morpheus Router (dummy interaction; replace with actual call)
        // Since this is a dummy example, you can call the Morpheus Router function here
        // bool success = IMorpheusRouter(morpheusRouter).executeQuery(user, query);
        // require(success, "Query execution failed");

        // Reward the compute provider with MOR tokens
        bool sent = morToken.transfer(user, rewardAmount);
        require(sent, "Token transfer failed");

        // Emit an event to log the processed query
        emit QueryProcessed(user, query, rewardAmount);
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens accidentally sent to the contract
     * @param token The address of the ERC20 token to withdraw
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        IERC20(token).transfer(owner, amount);
    }
}
```
