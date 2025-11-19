"""
Generated Code Metadata:
========================
Original URL: https://flarenetwork-xrpconnect.com
Prompt: Design a smart contract on the Flare Network using Solidity to distribute airdrops to eligible users based on their XRP holdings.
Generated: DETERMINISTIC_2b73571e77c2aa4f
Batch ID: 20250622_211952
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title XRPHoldersAirdrop
 * @dev A smart contract to distribute airdrops to eligible users based on their XRP holdings.
 * The contract allows the owner to set eligibility criteria, add eligible addresses with their XRP balances,
 * and distribute tokens to eligible users proportionally to their XRP holdings.
 */
contract XRPHoldersAirdrop is Ownable {
    using SafeMath for uint256;

    // The token to be distributed in the airdrop
    IERC20 public airdropToken;

    // Total XRP holdings of all eligible users
    uint256 public totalXRPHoldings;

    // Minimum XRP holdings required to be eligible for the airdrop
    uint256 public minXRPHoldings;

    // Mapping to store XRP holdings of eligible addresses
    mapping(address => uint256) public xrpBalances;

    // Mapping to track whether an address has claimed their airdrop
    mapping(address => bool) public hasClaimed;

    // Events
    event AirdropTokenSet(address indexed token);
    event MinXRPHoldingsSet(uint256 minHoldings);
    event EligibleAddressAdded(address indexed user, uint256 xrpBalance);
    event AirdropClaimed(address indexed user, uint256 amount);
    event TokensWithdrawn(address indexed owner, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the airdrop token.
     * @param _airdropToken Address of the token to be distributed in the airdrop.
     */
    constructor(address _airdropToken) {
        require(_airdropToken != address(0), "Invalid token address");
        airdropToken = IERC20(_airdropToken);
        emit AirdropTokenSet(_airdropToken);
    }

    /**
     * @dev Set the minimum XRP holdings required to be eligible for the airdrop.
     * @param _minXRPHoldings Minimum XRP holdings required.
     */
    function setMinXRPHoldings(uint256 _minXRPHoldings) external onlyOwner {
        minXRPHoldings = _minXRPHoldings;
        emit MinXRPHoldingsSet(_minXRPHoldings);
    }

    /**
     * @dev Add an eligible address with its XRP holdings.
     * @param _user Address of the eligible user.
     * @param _xrpBalance XRP holdings of the user.
     */
    function addEligibleAddress(address _user, uint256 _xrpBalance) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(_xrpBalance >= minXRPHoldings, "Insufficient XRP holdings");
        require(xrpBalances[_user] == 0, "User already added");

        xrpBalances[_user] = _xrpBalance;
        totalXRPHoldings = totalXRPHoldings.add(_xrpBalance);
        emit EligibleAddressAdded(_user, _xrpBalance);
    }

    /**
     * @dev Batch add eligible addresses with their XRP holdings.
     * @param _users Array of eligible user addresses.
     * @param _xrpBalances Array of XRP holdings corresponding to each user.
     */
    function batchAddEligibleAddresses(
        address[] calldata _users,
        uint256[] calldata _xrpBalances
    ) external onlyOwner {
        require(_users.length == _xrpBalances.length, "Arrays length mismatch");

        for (uint256 i = 0; i < _users.length; i++) {
            require(_users[i] != address(0), "Invalid user address");
            require(_xrpBalances[i] >= minXRPHoldings, "Insufficient XRP holdings");
            require(xrpBalances[_users[i]] == 0, "User already added");

            xrpBalances[_users[i]] = _xrpBalances[i];
            totalXRPHoldings = totalXRPHoldings.add(_xrpBalances[i]);
            emit EligibleAddressAdded(_users[i], _xrpBalances[i]);
        }
    }

    /**
     * @dev Claim the airdrop tokens proportional to the user's XRP holdings.
     */
    function claimAirdrop() external {
        require(xrpBalances[msg.sender] > 0, "Not eligible for airdrop");
        require(!hasClaimed[msg.sender], "Already claimed");

        uint256 userXRPBalance = xrpBalances[msg.sender];
        uint256 airdropAmount = calculateAirdropAmount(userXRPBalance);

        require(
            airdropToken.balanceOf(address(this)) >= airdropAmount,
            "Insufficient airdrop tokens"
        );

        hasClaimed[msg.sender] = true;
        airdropToken.transfer(msg.sender, airdropAmount);
        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Calculate the airdrop amount based on the user's XRP holdings.
     * @param _userXRPBalance XRP holdings of the user.
     * @return Amount of airdrop tokens to be distributed.
     */
    function calculateAirdropAmount(uint256 _userXRPBalance) public view returns (uint256) {
        uint256 totalAirdropTokens = airdropToken.balanceOf(address(this));
        return _userXRPBalance.mul(totalAirdropTokens).div(totalXRPHoldings);
    }

    /**
     * @dev Withdraw remaining airdrop tokens after distribution is complete.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            airdropToken.balanceOf(address(this)) >= _amount,
            "Insufficient balance"
        );
        airdropToken.transfer(owner(), _amount);
        emit TokensWithdrawn(owner(), _amount);
    }
}
```
