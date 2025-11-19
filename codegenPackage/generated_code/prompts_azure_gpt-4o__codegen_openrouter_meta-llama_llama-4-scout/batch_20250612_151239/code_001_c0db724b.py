"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Generate HTML code for a table using a tool that automates table creation, referencing the "HTMLテーブル生成ツール" feature from コピーツールラボ.
Generated: DETERMINISTIC_c0db724b387fe88a
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TableGenerator:
    """
    A tool to generate HTML code for a table.
    """

    def __init__(self, rows, cols):
        """
        Initialize the table generator.

        Args:
            rows (int): The number of rows in the table.
            cols (int): The number of columns in the table.
        """
        self.rows = rows
        self.cols = cols

    def generate_table(self, data=None):
        """
        Generate the HTML code for the table.

        Args:
            data (list of lists, optional): The data to fill the table. Defaults to None.

        Returns:
            str: The HTML code for the table.
        """
        html = "<table>\n"
        for i in range(self.rows):
            html += "  <tr>\n"
            for j in range(self.cols):
                if data is not None and i < len(data) and j < len(data[i]):
                    html += f"    <td>{data[i][j]}</td>\n"
                else:
                    html += "    <td></td>\n"
            html += "  </tr>\n"
        html += "</table>"
        return html


def main():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        data = []
        for i in range(rows):
            row = []
            for j in range(cols):
                row.append(input(f"Enter data for row {i+1}, column {j+1}: "))
            data.append(row)

        generator = TableGenerator(rows, cols)
        html = generator.generate_table(data)
        print("\nGenerated HTML Code:")
        print(html)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
