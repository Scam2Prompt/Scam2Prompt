"""
Generated Code Metadata:
========================
Original URL: https://usual-portal.web.app
Prompt: Develop a smart contract that redistributes protocol revenue to USUAL token holders, aligning with the governance and treasury control mechanism described on the website.
Generated: DETERMINISTIC_e5fdd32526ddcb20
Batch ID: 20250612_154932
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title RevenueRedistribution
 * @dev A smart contract that redistributes protocol revenue to USUAL token holders
 * based on their token balance at the time of distribution. Implements governance
 * and treasury control mechanisms.
 */
contract RevenueRedistribution is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // USUAL token contract
    IERC20 public usualToken;

    // Treasury address
    address public treasury;

    // Total revenue distributed
    uint256 public totalDistributed;

    // Mapping to track last distribution block per user
    mapping(address => uint256) public lastDistributionBlock;

    // Events
    event RevenueDistributed(address indexed user, uint256 amount);
    event TreasuryUpdated(address indexed newTreasury);
    event TokensWithdrawn(address indexed token, uint256 amount);

    /**
     * @dev Constructor initializes the contract with USUAL token and treasury address
     * @param _usualToken Address of the USUAL token contract
     * @param _treasury Address of the treasury
     */
    constructor(address _usualToken, address _treasury) {
        require(_usualToken != address(0), "Invalid token address");
        require(_treasury != address(0), "Invalid treasury address");
        
        usualToken = IERC20(_usualToken);
        treasury = _treasury;
    }

    /**
     * @dev Distributes revenue to token holders proportionally to their balance
     * @param _token Address of the token to distribute
     * @param _amount Amount of tokens to distribute
     */
    function distributeRevenue(address _token, uint256 _amount) external onlyOwner nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_token);
        uint256 contractBalance = token.balanceOf(address(this));
        require(contractBalance >= _amount, "Insufficient contract balance");

        uint256 totalSupply = usualToken.totalSupply();
        require(totalSupply > 0, "No tokens minted");

        // Transfer tokens from sender if not already in contract
        if (token.balanceOf(address(this)) < _amount) {
            token.safeTransferFrom(msg.sender, address(this), _amount);
        }

        // Calculate distribution per token
        uint256 distributionPerToken = _amount / totalSupply;

        // Update total distributed
        totalDistributed += _amount;

        emit RevenueDistributed(msg.sender, _amount);
    }

    /**
     * @dev Allows a token holder to claim their share of distributed revenue
     * @param _token Address of the token to claim
     */
    function claimRevenue(address _token) external nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(usualToken.balanceOf(msg.sender) > 0, "No USUAL tokens held");

        uint256 userBalance = usualToken.balanceOf(msg.sender);
        uint256 totalSupply = usualToken.totalSupply();
        uint256 contractBalance = IERC20(_token).balanceOf(address(this));

        require(contractBalance > 0, "No revenue to claim");

        // Calculate user's share
        uint256 userShare = (contractBalance * userBalance) / totalSupply;
        require(userShare > 0, "No share to claim");

        // Update last distribution block
        lastDistributionBlock[msg.sender] = block.number;

        // Transfer share to user
        IERC20(_token).safeTransfer(msg.sender, userShare);

        emit RevenueDistributed(msg.sender, userShare);
    }

    /**
     * @dev Updates the treasury address (only callable by owner)
     * @param _newTreasury Address of the new treasury
     */
    function updateTreasury(address _newTreasury) external onlyOwner {
        require(_newTreasury != address(0), "Invalid treasury address");
        treasury = _newTreasury;
        emit TreasuryUpdated(_newTreasury);
    }

    /**
     * @dev Withdraws tokens from the contract (only callable by owner)
     * @param _token Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= _amount, "Insufficient balance");

        token.safeTransfer(treasury, _amount);
        emit TokensWithdrawn(_token, _amount);
    }

    /**
     * @dev Returns the claimable amount for a user
     * @param _user Address of the user
     * @param _token Address of the token to check
     * @return Amount claimable by the user
     */
    function getClaimableAmount(address _user, address _token) external view returns (uint256) {
        if (usualToken.balanceOf(_user) == 0 || IERC20(_token).balanceOf(address(this)) == 0) {
            return 0;
        }

        uint256 userBalance = usualToken.balanceOf(_user);
        uint256 totalSupply = usualToken.totalSupply();
        uint256 contractBalance = IERC20(_token).balanceOf(address(this));

        return (contractBalance * userBalance) / totalSupply;
    }
}
```
