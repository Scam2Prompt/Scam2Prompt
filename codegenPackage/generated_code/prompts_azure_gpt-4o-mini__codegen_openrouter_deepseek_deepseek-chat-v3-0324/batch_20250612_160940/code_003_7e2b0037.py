"""
Generated Code Metadata:
========================
Original URL: https://bafybeidbzihyinyo7izo2bw76p5ghzvavjsr3c5oqgowyshfuo5g6gfmti.ipfs.dweb.link
Prompt: Generate an example of a smart contract that utilizes Chainlink CCIP for cross-chain message passing within the XSwap ecosystem.
Generated: DETERMINISTIC_7e2b00372dd61427
Batch ID: 20250612_160940
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

import {IRouterClient} from "@chainlink/contracts-ccip/src/v0.8/ccip/interfaces/IRouterClient.sol";
import {Client} from "@chainlink/contracts-ccip/src/v0.8/ccip/libraries/Client.sol";
import {IERC20} from "@chainlink/contracts-ccip/src/v0.8/vendor/openzeppelin-solidity/v4.8.0/token/ERC20/IERC20.sol";
import {SafeERC20} from "@chainlink/contracts-ccip/src/v0.8/vendor/openzeppelin-solidity/v4.8.0/token/ERC20/utils/SafeERC20.sol";
import {Ownable} from "@chainlink/contracts-ccip/src/v0.8/vendor/openzeppelin-solidity/v4.8.0/access/Ownable.sol";

contract XSwapCCIP is Ownable {
    using SafeERC20 for IERC20;

    IRouterClient public immutable router;
    address public linkToken;

    // Mapping to store allowed destination chains
    mapping(uint64 => bool) public allowedChains;

    // Event emitted when a cross-chain swap is initiated
    event SwapInitiated(
        bytes32 indexed messageId,
        uint64 indexed destinationChainSelector,
        address indexed receiver,
        address token,
        uint256 amount
    );

    // Event emitted when a cross-chain swap is completed
    event SwapCompleted(
        address indexed receiver,
        address token,
        uint256 amount
    );

    // Error for unsupported chain
    error UnsupportedChain(uint64 chainSelector);

    // Error for insufficient fees
    error InsufficientFees(uint256 calculatedFees, uint256 sentFees);

    /**
     * @dev Constructor initializes the contract with the router address and LINK token
     * @param _router The address of the Chainlink CCIP router
     * @param _linkToken The address of the LINK token
     */
    constructor(address _router, address _linkToken) {
        router = IRouterClient(_router);
        linkToken = _linkToken;
    }

    /**
     * @dev Allows the owner to add a supported destination chain
     * @param _chainSelector The chain selector of the destination chain
     */
    function addAllowedChain(uint64 _chainSelector) external onlyOwner {
        allowedChains[_chainSelector] = true;
    }

    /**
     * @dev Allows the owner to remove a supported destination chain
     * @param _chainSelector The chain selector of the destination chain
     */
    function removeAllowedChain(uint64 _chainSelector) external onlyOwner {
        allowedChains[_chainSelector] = false;
    }

    /**
     * @dev Initiates a cross-chain swap
     * @param _destinationChainSelector The chain selector of the destination chain
     * @param _receiver The address of the receiver on the destination chain
     * @param _token The address of the token to swap
     * @param _amount The amount of tokens to swap
     * @return messageId The ID of the CCIP message
     */
    function initiateSwap(
        uint64 _destinationChainSelector,
        address _receiver,
        address _token,
        uint256 _amount
    ) external payable returns (bytes32 messageId) {
        // Check if destination chain is supported
        if (!allowedChains[_destinationChainSelector]) {
            revert UnsupportedChain(_destinationChainSelector);
        }

        // Transfer tokens from sender to this contract
        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);

        // Create CCIP message
        Client.EVM2AnyMessage memory message = Client.EVM2AnyMessage({
            receiver: abi.encode(_receiver),
            data: abi.encode(_token, _amount),
            tokenAmounts: new Client.EVMTokenAmount[](0),
            extraArgs: "",
            feeToken: linkToken
        });

        // Calculate fees
        uint256 fees = router.getFee(_destinationChainSelector, message);

        // Check if sufficient fees are provided
        if (fees > msg.value) {
            revert InsufficientFees(fees, msg.value);
        }

        // Approve router to spend tokens
        IERC20(_token).approve(address(router), _amount);

        // Send the CCIP message
        messageId = router.ccipSend{value: fees}(
            _destinationChainSelector,
            message
        );

        emit SwapInitiated(
            messageId,
            _destinationChainSelector,
            _receiver,
            _token,
            _amount
        );

        return messageId;
    }

    /**
     * @dev Handles incoming CCIP messages (called by the router)
     * @param message The CCIP message
     */
    function ccipReceive(Client.Any2EVMMessage calldata message) external {
        // Ensure the message is from the router
        require(msg.sender == address(router), "Caller is not the router");

        // Decode the message data
        (address token, uint256 amount) = abi.decode(
            message.data,
            (address, uint256)
        );

        // Decode the receiver address
        address receiver = abi.decode(message.receiver, (address));

        // Transfer tokens to the receiver
        IERC20(token).safeTransfer(receiver, amount);

        emit SwapCompleted(receiver, token, amount);
    }

    /**
     * @dev Allows the owner to withdraw LINK tokens from the contract
     * @param _to The address to withdraw to
     * @param _amount The amount to withdraw
     */
    function withdrawLink(address _to, uint256 _amount) external onlyOwner {
        IERC20(linkToken).safeTransfer(_to, _amount);
    }

    /**
     * @dev Allows the owner to withdraw native tokens from the contract
     * @param _to The address to withdraw to
     * @param _amount The amount to withdraw
     */
    function withdrawNative(address payable _to, uint256 _amount)
        external
        onlyOwner
    {
        _to.transfer(_amount);
    }

    // Receive function to handle native token transfers
    receive() external payable {}
}
```
