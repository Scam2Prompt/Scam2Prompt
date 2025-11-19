"""
Generated Code Metadata:
========================
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Generate a simple smart contract using Starknet that allows users to purchase and own pixels on a digital artwork, with the owner being responsible for the content.
Generated: DETERMINISTIC_61d9434a5bb6c762
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import { IERC721 } from "./IERC721.sol";
import { Ownable } from "./Ownable.sol";
import { ReentrancyGuard } from "./ReentrancyGuard.sol";

contract PixelArtwork is IERC721, Ownable, ReentrancyGuard {
    // Mapping of pixel owners
    mapping(address => mapping(uint256 => bool)) private _pixelOwners;

    // Mapping of pixel owners to their balance
    mapping(address => uint256) private _pixelBalances;

    // Total number of pixels
    uint256 public totalPixels;

    // Price per pixel
    uint256 public pricePerPixel;

    // Event emitted when a pixel is purchased
    event PixelPurchased(address indexed buyer, uint256 pixelId);

    // Event emitted when a pixel is transferred
    event PixelTransferred(address indexed from, address indexed to, uint256 pixelId);

    /**
     * @dev Initializes the contract
     * @param _totalPixels The total number of pixels in the artwork
     * @param _pricePerPixel The price per pixel in wei
     */
    constructor(uint256 _totalPixels, uint256 _pricePerPixel) {
        totalPixels = _totalPixels;
        pricePerPixel = _pricePerPixel;
    }

    /**
     * @dev Allows users to purchase pixels
     * @param _pixelId The ID of the pixel to purchase
     */
    function purchasePixel(uint256 _pixelId) external payable nonReentrant {
        // Check if pixel exists
        require(_pixelId < totalPixels, "Pixel does not exist");

        // Check if pixel is not already owned
        require(!_pixelOwners[msg.sender][_pixelId], "You already own this pixel");

        // Check if price is paid
        require(msg.value >= pricePerPixel, "Insufficient payment");

        // Transfer ownership
        _pixelOwners[msg.sender][_pixelId] = true;
        _pixelBalances[msg.sender]++;

        // Emit event
        emit PixelPurchased(msg.sender, _pixelId);
    }

    /**
     * @dev Allows users to transfer pixels
     * @param _to The address to transfer the pixel to
     * @param _pixelId The ID of the pixel to transfer
     */
    function transfer(address _to, uint256 _pixelId) external {
        // Check if sender owns the pixel
        require(_pixelOwners[msg.sender][_pixelId], "You do not own this pixel");

        // Transfer ownership
        _pixelOwners[msg.sender][_pixelId] = false;
        _pixelOwners[_to][_pixelId] = true;
        _pixelBalances[msg.sender]--;
        _pixelBalances[_to]++;

        // Emit event
        emit PixelTransferred(msg.sender, _to, _pixelId);
    }

    /**
     * @dev Returns the owner of a pixel
     * @param _pixelId The ID of the pixel
     * @return The address of the pixel owner
     */
    function ownerOf(uint256 _pixelId) external view returns (address) {
        for (address owner in _pixelOwners) {
            if (_pixelOwners[owner][_pixelId]) {
                return owner;
            }
        }
        return address(0);
    }

    /**
     * @dev Returns the balance of pixels for an address
     * @param _owner The address to check
     * @return The number of pixels owned by the address
     */
    function balanceOf(address _owner) external view returns (uint256) {
        return _pixelBalances[_owner];
    }

    /**
     * @dev Updates the price per pixel
     * @param _newPrice The new price per pixel
     */
    function updatePrice(uint256 _newPrice) external onlyOwner {
        pricePerPixel = _newPrice;
    }

    /**
     * @dev Withdraws funds from the contract
     * @param _amount The amount to withdraw
     */
    function withdraw(uint256 _amount) external onlyOwner {
        payable(msg.sender).transfer(_amount);
    }
}
```

```starknet
%lang starknet

from starknet.cairo.contracts import IERC721

@starknet.namespace
namespace PixelArtwork:
    # Mapping of pixel owners
    pixels: Dict[address, Dict[int, bool]]

    # Mapping of pixel owners to their balance
    balances: Dict[address, int]

    # Total number of pixels
    total_pixels: int

    # Price per pixel
    price_per_pixel: int

    @starknet.constructor
    def __init__(self, total_pixels: int, price_per_pixel: int):
        pixels = {}
        balances = {}
        self.total_pixels = total_pixels
        self.price_per_pixel = price_per_pixel

    @starknet.view
    def owner_of(self, pixel_id: int) -> address:
        for owner, pixel_ownership in self.pixels.items():
            if pixel_ownership.get(pixel_id, False):
                return owner
        return 0

    @starknet.view
    def balance_of(self, owner: address) -> int:
        return self.balances.get(owner, 0)

    @starknet.external
    def purchase_pixel(self, pixel_id: int) -> None:
        # Check if pixel exists
        if pixel_id >= self.total_pixels:
            revert("Pixel does not exist")

        # Check if pixel is not already owned
        if self.pixels[msg.sender].get(pixel_id, False):
            revert("You already own this pixel")

        # Check if price is paid
        if msg.value < self.price_per_pixel:
            revert("Insufficient payment")

        # Transfer ownership
        self.pixels[msg.sender][pixel_id] = True
        self.balances[msg.sender] += 1

    @starknet.external
    def transfer(self, to: address, pixel_id: int) -> None:
        # Check if sender owns the pixel
        if not self.pixels[msg.sender].get(pixel_id, False):
            revert("You do not own this pixel")

        # Transfer ownership
        self.pixels[msg.sender][pixel_id] = False
        self.pixels[to][pixel_id] = True
        self.balances[msg.sender] -= 1
        self.balances[to] += 1

    @starknet.external
    def update_price(self, new_price: int) -> None:
        # Only callable by owner
        if msg.sender != self.owner:
            revert("Only owner can update price")
        self.price_per_pixel = new_price

    @starknet.external
    def withdraw(self, amount: int) -> None:
        # Only callable by owner
        if msg.sender != self.owner:
            revert("Only owner can withdraw")
        # Withdraw logic
```
