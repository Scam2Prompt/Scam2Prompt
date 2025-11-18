"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nectars.vercel.app
Prompt: Generate an Elixir function that calculates the distribution of NFTs (16 base, 8 bonus, 1 legendary) when upgrading Nectar to Nectar of Immortality.
Generated: DETERMINISTIC_65d9b6aefeb18630
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```elixir
defmodule NFTDistribution do
  @moduledoc """
  Module for calculating NFT distribution when upgrading Nectar to Nectar of Immortality.
  """

  @base_nft_count 16   # Number of base NFTs
  @bonus_nft_count 8   # Number of bonus NFTs
  @legendary_nft_count 1  # Number of legendary NFTs

  @doc """
  Calculates the distribution of NFTs when upgrading Nectar to Nectar of Immortality.

  ## Parameters:
    - nectar_quantity: The number of Nectar being upgraded (integer >= 1).

  ## Returns:
    - A map containing the count of each NFT type:
      %{
        :base => count_of_base_nfts,
        :bonus => count_of_bonus_nfts,
        :legendary => count_of_legendary_nfts
      }

  ## Examples:
      iex> NFTDistribution.calculate_distribution(3)
      %{base: 48, bonus: 24, legendary: 3}

      iex> NFTDistribution.calculate_distribution(1)
      %{base: 16, bonus: 8, legendary: 1}

  """
  def calculate_distribution(nectar_quantity) when is_integer(nectar_quantity) and nectar_quantity > 0 do
    try do
      %{
        base: nectar_quantity * @base_nft_count,
        bonus: nectar_quantity * @bonus_nft_count,
        legendary: nectar_quantity * @legendary_nft_count
      }
    rescue
      e -> {:error, "Failed to calculate distribution: #{e.message}"}
    end
  end

  def calculate_distribution(_invalid_input) do
    {:error, "Invalid input: nectar_quantity must be an integer greater than 0"}
  end
end
```
