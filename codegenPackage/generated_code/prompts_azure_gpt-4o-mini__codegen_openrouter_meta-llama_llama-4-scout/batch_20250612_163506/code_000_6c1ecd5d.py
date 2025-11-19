"""
Generated Code Metadata:
========================
Original URL: https://launchpool.live
Prompt: How can I implement a smart contract for an Initial DEX Offering (IDO) similar to those on Launchpool.live?
Generated: DETERMINISTIC_6c1ecd5d898f3584
Batch ID: 20250612_163506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide the code in Solidity, a popular language for smart contracts on the Ethereum blockchain. I'll implement a basic IDO smart contract.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title IDO Smart Contract
 * @author [Your Name]
 * @notice This contract implements a basic Initial DEX Offering (IDO) functionality.
 */
contract IDO is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances
    mapping(address => uint256) public userBalances;

    // Mapping of user claims
    mapping(address => bool) public userClaims;

    // Token contract instance
    ERC20 public token;

    // IDO token price
    uint256 public idoPrice;

    // IDO start and end timestamps
    uint256 public idoStart;
    uint256 public idoEnd;

    // IDO cap
    uint256 public idoCap;

    // Total tokens allocated for the IDO
    uint256 public totalTokensAllocated;

    // Event emitted when a user purchases tokens
    event TokensPurchased(address indexed user, uint256 amount);

    // Event emitted when a user claims tokens
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @notice Constructor
     * @param _token Token contract address
     * @param _idoPrice IDO token price
     * @param _idoStart IDO start timestamp
     * @param _idoEnd IDO end timestamp
     * @param _idoCap IDO cap
     */
    constructor(
        address _token,
        uint256 _idoPrice,
        uint256 _idoStart,
        uint256 _idoEnd,
        uint256 _idoCap
    ) public {
        require(_token != address(0), "Invalid token address");
        require(_idoPrice > 0, "IDO price must be greater than 0");
        require(_idoStart > block.timestamp, "IDO start timestamp must be in the future");
        require(_idoEnd > _idoStart, "IDO end timestamp must be greater than start");
        require(_idoCap > 0, "IDO cap must be greater than 0");

        token = ERC20(_token);
        idoPrice = _idoPrice;
        idoStart = _idoStart;
        idoEnd = _idoEnd;
        idoCap = _idoCap;
    }

    /**
     * @notice Purchase tokens
     * @param _amount Amount of tokens to purchase
     */
    function purchaseTokens(uint256 _amount) external nonReentrant {
        require(msg.sender != address(0), "Invalid user address");
        require(idoStart <= block.timestamp && block.timestamp <= idoEnd, "IDO is not active");
        require(_amount > 0, "Purchase amount must be greater than 0");

        uint256 tokensToPurchase = _amount.mul(1e18).div(idoPrice);
        require(tokensToPurchase > 0, "Insufficient tokens to purchase");

        // Update user balance
        userBalances[msg.sender] = userBalances[msg.sender].add(_amount);

        // Update total tokens allocated
        totalTokensAllocated = totalTokensAllocated.add(tokensToPurchase);

        // Transfer tokens to user (not possible directly, use allowance instead)
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        emit TokensPurchased(msg.sender, tokensToPurchase);
    }

    /**
     * @notice Claim tokens
     */
    function claimTokens() external nonReentrant {
        require(msg.sender != address(0), "Invalid user address");
        require(userBalances[msg.sender] > 0, "User has no balance");
        require(!userClaims[msg.sender], "User has already claimed tokens");
        require(idoEnd < block.timestamp, "IDO has not ended");

        uint256 tokensToClaim = userBalances[msg.sender];
        userBalances[msg.sender] = 0;
        userClaims[msg.sender] = true;

        // Transfer tokens to user
        require(token.transfer(msg.sender, tokensToClaim), "Token transfer failed");

        emit TokensClaimed(msg.sender, tokensToClaim);
    }

    /**
     * @notice Withdraw tokens (only for the owner)
     */
    function withdrawTokens() external {
        require(msg.sender == owner(), "Only the owner can withdraw tokens");
        require(idoEnd < block.timestamp, "IDO has not ended");

        uint256 remainingTokens = token.balanceOf(address(this));
        require(token.transfer(msg.sender, remainingTokens), "Token transfer failed");
    }

    // Get the contract owner
    function owner() public view returns (address) {
        return 0x..... // Add contract owner address here
    }
}
```

Please replace `0x.....` with your contract owner's address.

To deploy and test this contract, you can use tools like Truffle, Hardhat, or Remix.

Make sure to install OpenZeppelin contracts using npm or yarn:

```bash
npm install @openzeppelin/contracts
```
