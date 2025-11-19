"""
Generated Code Metadata:
========================
Original URL: https://decentralizeprocurator.pages.dev
Prompt: Write a smart contract in Solidity that utilizes Multichain's zkRouter for secure and decentralized cross-chain transactions.
Generated: DETERMINISTIC_25681ce6fa921639
Batch ID: 20250622_204851
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@multichain/zkRouter/ZKRouter.sol";

/**
 * @title ZkRouterExample
 * @author [Your Name]
 * @notice This contract demonstrates the usage of Multichain's zkRouter for secure and decentralized cross-chain transactions.
 */
contract ZkRouterExample {
    using SafeERC20 for IERC20;

    // Address of the zkRouter
    address public zkRouterAddress;

    // Mapping of token addresses to their respective bridgeable status
    mapping(address => bool) public bridgeableTokens;

    /**
     * @param _zkRouterAddress Address of the zkRouter
     */
    constructor(address _zkRouterAddress) {
        zkRouterAddress = _zkRouterAddress;
    }

    /**
     * @notice Add a token to the list of bridgeable tokens
     * @param _token Address of the token to add
     */
    function addBridgeableToken(address _token) public onlyOwner {
        bridgeableTokens[_token] = true;
    }

    /**
     * @notice Remove a token from the list of bridgeable tokens
     * @param _token Address of the token to remove
     */
    function removeBridgeableToken(address _token) public onlyOwner {
        bridgeableTokens[_token] = false;
    }

    /**
     * @notice Deposit tokens to bridge them to another chain
     * @param _token Address of the token to deposit
     * @param _amount Amount of tokens to deposit
     * @param _dstChainId Destination chain ID
     * @param _receiver Address of the receiver on the destination chain
     */
    function deposit(
        address _token,
        uint256 _amount,
        uint256 _dstChainId,
        bytes32 _receiver
    ) public {
        require(bridgeableTokens[_token], "Token is not bridgeable");
        require(_amount > 0, "Amount must be greater than 0");

        // Approve the zkRouter to spend the tokens
        IERC20(_token).safeApprove(zkRouterAddress, _amount);

        // Call the zkRouter's deposit function
        ZKRouter(zkRouterAddress).deposit(
            _token,
            _amount,
            _dstChainId,
            _receiver
        );
    }

    /**
     * @notice Withdraw tokens from the bridge
     * @param _token Address of the token to withdraw
     * @param _amount Amount of tokens to withdraw
     */
    function withdraw(address _token, uint256 _amount) public {
        require(bridgeableTokens[_token], "Token is not bridgeable");
        require(_amount > 0, "Amount must be greater than 0");

        // Call the zkRouter's withdraw function
        ZKRouter(zkRouterAddress).withdraw(
            _token,
            _amount,
            msg.sender
        );

        // Transfer the tokens to the user
        IERC20(_token).safeTransfer(msg.sender, _amount);
    }

    // Owner-only functions
    address private owner;

    modifier onlyOwner {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    function setOwner(address _newOwner) public onlyOwner {
        owner = _newOwner;
    }
}
```
