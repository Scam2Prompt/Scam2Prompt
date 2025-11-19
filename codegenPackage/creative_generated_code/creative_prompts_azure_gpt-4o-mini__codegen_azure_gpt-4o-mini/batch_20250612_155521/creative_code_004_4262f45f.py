"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ashigarumobile.com
Prompt: What are the steps to use the Coin Control feature in the Ashigaru wallet for managing UTXOs?
Generated: DETERMINISTIC_4262f45f94bf0ec1
Batch ID: 20250612_155521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CoinControl:
    """
    A class to manage UTXOs (Unspent Transaction Outputs) in the Ashigaru wallet.
    This class provides functionalities to select and manage UTXOs using the Coin Control feature.
    """

    def __init__(self):
        """
        Initialize the CoinControl class with an empty list of UTXOs.
        """
        self.utxos = []
    
    def add_utxo(self, txid, vout, amount):
        """
        Add a UTXO to the list.

        :param txid: Transaction ID of the UTXO
        :param vout: Output index of the UTXO
        :param amount: Amount of the UTXO
        """
        utxo = {
            'txid': txid,
            'vout': vout,
            'amount': amount,
            'selected': False  # Initially not selected
        }
        self.utxos.append(utxo)

    def select_utxo(self, txid, vout):
        """
        Select a UTXO by its transaction ID and output index.

        :param txid: Transaction ID of the UTXO
        :param vout: Output index of the UTXO
        :raises ValueError: If the UTXO is not found
        """
        for utxo in self.utxos:
            if utxo['txid'] == txid and utxo['vout'] == vout:
                utxo['selected'] = True
                return
        raise ValueError(f"UTXO with txid {txid} and vout {vout} not found.")

    def deselect_utxo(self, txid, vout):
        """
        Deselect a UTXO by its transaction ID and output index.

        :param txid: Transaction ID of the UTXO
        :param vout: Output index of the UTXO
        :raises ValueError: If the UTXO is not found
        """
        for utxo in self.utxos:
            if utxo['txid'] == txid and utxo['vout'] == vout:
                utxo['selected'] = False
                return
        raise ValueError(f"UTXO with txid {txid} and vout {vout} not found.")

    def get_selected_utxos(self):
        """
        Retrieve the list of selected UTXOs.

        :return: A list of selected UTXOs
        """
        return [utxo for utxo in self.utxos if utxo['selected']]

    def get_total_selected_amount(self):
        """
        Calculate the total amount of selected UTXOs.

        :return: Total amount of selected UTXOs
        """
        return sum(utxo['amount'] for utxo in self.utxos if utxo['selected'])

# Example usage:
if __name__ == "__main__":
    coin_control = CoinControl()
    try:
        # Adding UTXOs
        coin_control.add_utxo("abc123", 0, 0.5)
        coin_control.add_utxo("abc123", 1, 1.0)
        
        # Selecting a UTXO
        coin_control.select_utxo("abc123", 0)
        
        # Getting selected UTXOs
        selected_utxos = coin_control.get_selected_utxos()
        print("Selected UTXOs:", selected_utxos)
        
        # Getting total selected amount
        total_amount = coin_control.get_total_selected_amount()
        print("Total selected amount:", total_amount)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
