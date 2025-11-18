"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that integrates with the Pudgy Penguins ecosystem to distribute exclusive rewards to registered users.
Generated: DETERMINISTIC_7ddf5ef38fed412a
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

// Import interfaces for ERC20 and ERC721 to interact with the Pudgy Penguins token and NFT
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PudgyPenguinsRewards is Ownable {
    // Address of the Pudgy Penguins NFT contract
    IERC721 public pudgyPenguinsNFT;

    // Address of the reward token (ERC20)
    IERC20 public rewardToken;

    // Mapping to keep track of registered users
    mapping(address => bool) public registeredUsers;

    // Event emitted when a user is registered
    event UserRegistered(address indexed user);
    
    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Modifier to check if the user is registered
    modifier onlyRegistered() {
        require(registeredUsers[msg.sender], "User not registered");
        _;
    }

    constructor(address _pudgyPenguinsNFT, address _rewardToken) {
        require(_pudgyPenguinsNFT != address(0), "Invalid NFT address");
        require(_rewardToken != address(0), "Invalid token address");
        
        pudgyPenguinsNFT = IERC721(_pudgyPenguinsNFT);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to register a user who owns a Pudgy Penguin
    function registerUser() external {
        require(pudgyPenguinsNFT.balanceOf(msg.sender) > 0, "Must own a Pudgy Penguin");
        registeredUsers[msg.sender] = true;
        emit UserRegistered(msg.sender);
    }

    // Function to distribute rewards to registered users
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        
        // Loop through registered users and distribute rewards
        for (uint256 i = 0; i < registeredUsersCount(); i++) {
            address user = getRegisteredUser(i);
            require(rewardToken.balanceOf(address(this)) >= amount, "Insufficient rewards available");
            rewardToken.transfer(user, amount);
            emit RewardsDistributed(user, amount);
        }
    }

    // Function to get the count of registered users
    function registeredUsersCount() public view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < 2**256 - 1; i++) {
            if (registeredUsers[address(i)]) {
                count++;
            }
        }
        return count;
    }

    // Function to get registered user address by index
    function getRegisteredUser(uint256 index) public view returns (address) {
        require(index < registeredUsersCount(), "Index out of bounds");
        for (uint256 i = 0; i < 2**256 - 1; i++) {
            if (registeredUsers[address(i)]) {
                if (index == 0) {
                    return address(i);
                }
                index--;
            }
        }
        revert("User not found");
    }

    // Function to withdraw remaining tokens in the contract to the owner
    function withdrawTokens() external onlyOwner {
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        rewardToken.transfer(msg.sender, balance);
    }
}
```
