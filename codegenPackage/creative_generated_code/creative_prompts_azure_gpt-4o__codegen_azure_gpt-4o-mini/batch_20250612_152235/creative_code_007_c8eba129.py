"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plnksale.vercel.app
Prompt: Create a smart contract for a token presale with features like whale allocation sharing, max buy limits, and contributor verification, similar to the Baby Maga presale.
Generated: DETERMINISTIC_c8eba12952b86685
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // Token to be sold
    IERC20 public token;

    // Presale parameters
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public maxBuyLimit;
    uint256 public whaleAllocationLimit;

    // Mapping to track contributions and whitelist status
    mapping(address => uint256) public contributions;
    mapping(address => bool) public isWhitelisted;

    // Events for logging
    event TokensPurchased(address indexed buyer, uint256 amount);
    event WhitelistUpdated(address indexed account, bool isWhitelisted);

    // Modifier to check if presale is active
    modifier isPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _token,
        uint256 _startTime,
        uint256 _endTime,
        uint256 _maxBuyLimit,
        uint256 _whaleAllocationLimit
    ) {
        require(_token != address(0), "Invalid token address");
        require(_startTime < _endTime, "Invalid presale time");
        
        token = IERC20(_token);
        presaleStartTime = _startTime;
        presaleEndTime = _endTime;
        maxBuyLimit = _maxBuyLimit;
        whaleAllocationLimit = _whaleAllocationLimit;
    }

    // Function to buy tokens during the presale
    function buyTokens(uint256 _amount) external payable isPresaleActive {
        require(_amount > 0, "Amount must be greater than zero");
        require(msg.value == _amount, "Ether sent does not match amount requested");
        
        uint256 totalContribution = contributions[msg.sender].add(_amount);
        
        if (totalContribution > whaleAllocationLimit) {
            require(totalContribution <= whaleAllocationLimit, "Exceeds whale allocation limit");
        } else {
            require(totalContribution <= maxBuyLimit, "Exceeds max buy limit");
        }

        // Update contribution
        contributions[msg.sender] = totalContribution;

        // Emit event for logging
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to update whitelist status
    function updateWhitelist(address _account, bool _status) external onlyOwner {
        isWhitelisted[_account] = _status;
        emit WhitelistUpdated(_account, _status);
    }

    // Function to withdraw funds (only owner)
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens (only owner)
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 tokenBalance = token.balanceOf(address(this));
        require(tokenBalance > 0, "No tokens to withdraw");
        token.transfer(owner(), tokenBalance);
    }

    // Function to check if the buyer is whitelisted
    function checkWhitelist(address _account) external view returns (bool) {
        return isWhitelisted[_account];
    }

    // Fallback function to accept Ether
    receive() external payable {}
}
```
