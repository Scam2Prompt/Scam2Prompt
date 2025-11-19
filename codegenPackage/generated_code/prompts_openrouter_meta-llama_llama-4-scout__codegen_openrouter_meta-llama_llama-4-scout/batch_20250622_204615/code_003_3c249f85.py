"""
Generated Code Metadata:
========================
Original URL: https://layear3.com
Prompt: "Design a basic smart contract for managing airdrop distributions on a blockchain platform like Ethereum, inspired by the Fuse Airdrop campaign."
Generated: DETERMINISTIC_3c249f85ae8b9d22
Batch ID: 20250622_204615
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title AirdropContract
 * @author [Your Name]
 * @notice A basic smart contract for managing airdrop distributions on Ethereum.
 */
contract AirdropContract is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of addresses to their airdrop claim status
    mapping(address => bool) public claimed;

    // Mapping of addresses to their airdrop amounts
    mapping(address => uint256) public airdropAmounts;

    // ERC20 token to be airdropped
    IERC20 public token;

    // Total airdrop amount
    uint256 public totalAirdropAmount;

    // Airdrop start timestamp
    uint256 public startTimestamp;

    // Airdrop end timestamp
    uint256 public endTimestamp;

    /**
     * @notice Constructor for AirdropContract
     * @param _tokenAddress Address of the ERC20 token to be airdropped
     * @param _totalAirdropAmount Total amount of tokens to be airdropped
     * @param _startTimestamp Timestamp when airdrop starts
     * @param _endTimestamp Timestamp when airdrop ends
     */
    constructor(
        address _tokenAddress,
        uint256 _totalAirdropAmount,
        uint256 _startTimestamp,
        uint256 _endTimestamp
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_totalAirdropAmount > 0, "Total airdrop amount must be greater than 0");
        require(_startTimestamp < _endTimestamp, "Invalid timestamp range");

        token = IERC20(_tokenAddress);
        totalAirdropAmount = _totalAirdropAmount;
        startTimestamp = _startTimestamp;
        endTimestamp = _endTimestamp;
    }

    /**
     * @notice Claim airdrop tokens
     */
    function claim() public {
        require(block.timestamp >= startTimestamp && block.timestamp <= endTimestamp, "Airdrop not active");
        require(!claimed[msg.sender], "Already claimed");

        uint256 amount = airdropAmounts[msg.sender];
        require(amount > 0, "No airdrop amount allocated");

        claimed[msg.sender] = true;

        token.safeTransfer(msg.sender, amount);
    }

    /**
     * @notice Set airdrop amount for an address
     * @param _address Address to set airdrop amount for
     * @param _amount Airdrop amount for the address
     */
    function setAirdropAmount(address _address, uint256 _amount) public onlyOwner {
        require(_address != address(0), "Invalid address");
        require(_amount > 0, "Airdrop amount must be greater than 0");
        require(airdropAmounts[_address] == 0, "Airdrop amount already set");

        airdropAmounts[_address] = _amount;
        totalAirdropAmount = totalAirdropAmount.add(_amount);
    }

    /**
     * @notice Withdraw remaining tokens
     */
    function withdraw() public onlyOwner {
        uint256 remainingAmount = token.balanceOf(address(this)).sub(totalAirdropAmount);
        token.safeTransfer(msg.sender, remainingAmount);
    }

    /**
     * @notice Check if airdrop can be claimed
     * @param _address Address to check
     * @return bool Whether airdrop can be claimed
     */
    function canClaim(address _address) public view returns (bool) {
        return
            block.timestamp >= startTimestamp &&
            block.timestamp <= endTimestamp &&
            !claimed[_address] &&
            airdropAmounts[_address] > 0;
    }
}
```
