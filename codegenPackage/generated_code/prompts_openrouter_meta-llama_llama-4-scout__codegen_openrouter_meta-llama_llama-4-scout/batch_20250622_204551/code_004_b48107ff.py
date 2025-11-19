"""
Generated Code Metadata:
========================
Original URL: https://ytyyyy.pages.dev
Prompt: Design a smart contract for a decentralized protocol like Allo, allowing users to convert earned points to tokens.
Generated: DETERMINISTIC_b48107ffe71abb79
Batch ID: 20250622_204551
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AlloPointsToTokenConverter
 * @author [Your Name]
 * @notice This contract allows users to convert earned points to tokens in a decentralized protocol.
 */
contract AlloPointsToTokenConverter is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user points balance
    mapping(address => uint256) public userPointsBalance;

    // Mapping of user token balance
    mapping(address => uint256) public userTokenBalance;

    // Token contract instance
    IERC20 public token;

    // Points per token conversion rate
    uint256 public pointsPerToken;

    // Event emitted when user converts points to tokens
    event PointsConvertedToTokens(address indexed user, uint256 points, uint256 tokens);

    // Event emitted when points are added to a user's balance
    event PointsAdded(address indexed user, uint256 points);

    // Event emitted when tokens are transferred to a user's balance
    event TokensTransferred(address indexed user, uint256 tokens);

    /**
     * @notice Constructor for the AlloPointsToTokenConverter contract
     * @param _token Address of the token contract
     * @param _pointsPerToken Conversion rate of points to tokens
     */
    constructor(address _token, uint256 _pointsPerToken) {
        require(_token != address(0), "Token address cannot be zero");
        require(_pointsPerToken > 0, "Points per token conversion rate must be greater than zero");

        token = IERC20(_token);
        pointsPerToken = _pointsPerToken;
    }

    /**
     * @notice Adds points to a user's balance
     * @param _user Address of the user
     * @param _points Amount of points to add
     */
    function addPoints(address _user, uint256 _points) external {
        require(_user != address(0), "User address cannot be zero");
        require(_points > 0, "Points to add must be greater than zero");

        userPointsBalance[_user] = userPointsBalance[_user].add(_points);
        emit PointsAdded(_user, _points);
    }

    /**
     * @notice Converts user points to tokens
     * @param _user Address of the user
     * @param _points Amount of points to convert
     */
    function convertPointsToTokens(address _user, uint256 _points) external nonReentrant {
        require(_user != address(0), "User address cannot be zero");
        require(_points > 0, "Points to convert must be greater than zero");
        require(userPointsBalance[_user] >= _points, "User does not have enough points");

        uint256 tokens = _points.div(pointsPerToken);
        userPointsBalance[_user] = userPointsBalance[_user].sub(_points);
        userTokenBalance[_user] = userTokenBalance[_user].add(tokens);

        // Transfer tokens to user
        require(token.transfer(_user, tokens), "Token transfer failed");

        emit PointsConvertedToTokens(_user, _points, tokens);
        emit TokensTransferred(_user, tokens);
    }

    /**
     * @notice Gets user points balance
     * @param _user Address of the user
     * @return User points balance
     */
    function getUserPointsBalance(address _user) external view returns (uint256) {
        return userPointsBalance[_user];
    }

    /**
     * @notice Gets user token balance
     * @param _user Address of the user
     * @return User token balance
     */
    function getUserTokenBalance(address _user) external view returns (uint256) {
        return userTokenBalance[_user];
    }
}
```
