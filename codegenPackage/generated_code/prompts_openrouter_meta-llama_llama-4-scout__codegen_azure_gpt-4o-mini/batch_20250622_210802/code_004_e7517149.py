"""
Generated Code Metadata:
========================
Original URL: https://nectars.vercel.app
Prompt: Design an Elixir function to calculate the total value of NFTs contained within a rarest Nectar of Immortality, considering 16 base, 8 bonus, and 1 legendary NFT.
Generated: DETERMINISTIC_e75171497b8fb4b7
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```elixir
defmodule NFTCalculator do
  @moduledoc """
  A module for calculating the total value of NFTs contained within a rarest Nectar of Immortality.
  """

  @doc """
  Calculates the total value of NFTs.

  ## Parameters
  - base_value: The value of a single base NFT.
  - bonus_value: The value of a single bonus NFT.
  - legendary_value: The value of a single legendary NFT.

  ## Returns
  - The total value of all NFTs.

  ## Examples
      iex> NFTCalculator.calculate_total_value(100, 200, 500)
      1800
  """
  @spec calculate_total_value(non_neg_integer(), non_neg_integer(), non_neg_integer()) :: non_neg_integer()
  def calculate_total_value(base_value, bonus_value, legendary_value) when is_integer(base_value) and is_integer(bonus_value) and is_integer(legendary_value) do
    # Define the quantities of each type of NFT
    base_nfts = 16
    bonus_nfts = 8
    legendary_nfts = 1

    # Calculate the total value
    total_value = (base_nfts * base_value) + (bonus_nfts * bonus_value) + (legendary_nfts * legendary_value)

    # Return the total value
    total_value
  end

  def calculate_total_value(_, _, _) do
    # Handle invalid input types
    raise ArgumentError, message: "All values must be non-negative integers."
  end
end

# Example usage:
# total_value = NFTCalculator.calculate_total_value(100, 200, 500)
# IO.puts("Total NFT Value: #{total_value}")
```
