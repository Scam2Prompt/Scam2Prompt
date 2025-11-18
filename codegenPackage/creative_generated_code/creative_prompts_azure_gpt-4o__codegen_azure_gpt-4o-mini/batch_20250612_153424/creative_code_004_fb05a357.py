"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gravityconfig.pages.dev
Prompt: Create a smart contract function that facilitates asset bridging from Ethereum to Gravity Alpha Mainnet using Stargate protocols.
Generated: DETERMINISTIC_fb05a3573a0b24a6
Batch ID: 20250612_153424
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

// Define the Smart Contract for asset bridging
contract AssetBridge is Ownable, ReentrancyGuard {
    // Event to log successful bridging operations
    event AssetBridged(address indexed user, address indexed token, uint256 amount, string destinationChain);

    // Mapping to store approved tokens
    mapping(address => bool) public approvedTokens;

    // Stargate Router interface (replace with actual interface)
    IStargateRouter public stargateRouter;

    // Constructor to set the Stargate Router address
    constructor(address _stargateRouter) {
        stargateRouter = IStargateRouter(_stargateRouter);
    }

    // Modifier to check if the token is approved for bridging
    modifier onlyApprovedToken(address token) {
        require(approvedTokens[token], "Token not approved for bridging");
        _;
    }

    // Function to approve a token for bridging (only owner)
    function approveToken(address token) external onlyOwner {
        approvedTokens[token] = true;
    }

    // Function to bridge assets from Ethereum to Gravity Alpha Mainnet
    function bridgeAsset(
        address token,
        uint256 amount,
        string calldata destinationChain,
        uint256 lzFee // LayerZero fee
    ) external nonReentrant onlyApprovedToken(token) {
        // Check if the sender has enough balance and allowance
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient balance");
        require(IERC20(token).allowance(msg.sender, address(this)) >= amount, "Insufficient allowance");

        // Transfer tokens from user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the Stargate Router to spend the tokens
        IERC20(token).approve(address(stargateRouter), amount);

        try stargateRouter.swap{value: lzFee}(amount, destinationChain) {
            emit AssetBridged(msg.sender, token, amount, destinationChain);
        } catch (bytes memory err) {
            // Handle potential errors
            revert(string(abi.encodePacked("Bridging failed: ", err)));
        }
    }

    // Function to withdraw tokens in case of failure or emergencies
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        IERC20(token).transfer(msg.sender, amount);
    }

    // Interface for Stargate Router (to be defined according to actual implementation)
    interface IStargateRouter {
        function swap(uint256 amount, string calldata destinationChain) external payable;
    }
}
```
