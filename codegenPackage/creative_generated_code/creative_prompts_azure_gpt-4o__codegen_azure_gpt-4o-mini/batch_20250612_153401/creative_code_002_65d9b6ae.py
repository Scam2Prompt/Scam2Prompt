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
defmodule NFTDistributor do
  @moduledoc """
  A module for distributing NFTs when upgrading Nectar to Nectar of Immortality.
  It calculates the distribution based on defined counts for base, bonus, and legendary NFTs.
  """

  @base_nfts 16
  @bonus_nfts 8
  @legendary_nfts 1

  @doc """
  Distributes NFTs when upgrading Nectar to Nectar of Immortality.

  ## Examples

      iex> NFTDistributor.distribute_nfts()
      {:ok, %{base: 16, bonus: 8, legendary: 1}}

  ## Errors

  Raises an error if the NFT counts are invalid.
  """
  def distribute_nfts do
    try do
      %{
        base: calculate_nfts(@base_nfts),
        bonus: calculate_nfts(@bonus_nfts),
        legendary: calculate_nfts(@legendary_nfts)
      }
      |> validate_nfts()
      |> then(&{:ok, &1})
    rescue
      e in RuntimeError -> {:error, e.message}
    end
  end

  defp calculate_nfts(count) when is_integer(count) and count >= 0 do
    count
  end

  defp calculate_nfts(_count) do
    raise "NFT count must be a non-negative integer"
  end

  defp validate_nfts(%{base: base, bonus: bonus, legendary: legendary}) do
    if base < 0 or bonus < 0 or legendary < 0 do
      raise "NFT distribution cannot have negative values"
    end

    %{base: base, bonus: bonus, legendary: legendary}
  end
end
```
