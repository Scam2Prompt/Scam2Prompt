"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-io.web.app
Prompt: Write a smart contract example using the Data Ownership Protocol (DOP) to selectively disclose ERC20 token holdings while maintaining privacy for other assets.
Generated: DETERMINISTIC_4c2e3163ef95d776
Batch ID: 20250612_150917
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

// Importing the necessary interfaces for ERC20 and DOP
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract allows users to register their ERC20 token holdings
// and selectively disclose their holdings while keeping other assets private.
contract DataOwnershipProtocol is Ownable {
    
    // Struct to hold user's token data
    struct TokenData {
        address tokenAddress; // The address of the ERC20 token
        uint256 balance;      // The balance of the token for the user
    }

    // Mapping from user address to their token data
    mapping(address => TokenData[]) private userTokens;

    // Event to log when a user adds a new token
    event TokenAdded(address indexed user, address indexed tokenAddress, uint256 balance);

    // Event to log when a user updates the balance of an existing token
    event TokenUpdated(address indexed user, address indexed tokenAddress, uint256 newBalance);

    // Function to register a new token holding
    function registerToken(address _tokenAddress) external {
        require(_tokenAddress != address(0), "Invalid token address");

        IERC20 token = IERC20(_tokenAddress);
        uint256 balance = token.balanceOf(msg.sender);

        require(balance > 0, "No tokens to register");

        // Add the token data to the user's list
        userTokens[msg.sender].push(TokenData({
            tokenAddress: _tokenAddress,
            balance: balance
        }));

        emit TokenAdded(msg.sender, _tokenAddress, balance);
    }

    // Function to update the balance of an existing token
    function updateTokenBalance(address _tokenAddress) external {
        require(_tokenAddress != address(0), "Invalid token address");

        IERC20 token = IERC20(_tokenAddress);
        uint256 newBalance = token.balanceOf(msg.sender);

        // Search for the token in the user's holdings
        for (uint256 i = 0; i < userTokens[msg.sender].length; i++) {
            if (userTokens[msg.sender][i].tokenAddress == _tokenAddress) {
                userTokens[msg.sender][i].balance = newBalance;
                emit TokenUpdated(msg.sender, _tokenAddress, newBalance);
                return;
            }
        }
        
        revert("Token not found in user's holdings");
    }

    // Function to get the holdings of a user, only accessible by the owner (for privacy)
    function getUserTokens(address _user) external view onlyOwner returns (TokenData[] memory) {
        return userTokens[_user];
    }
}
```
