"""
Generated Code Metadata:
========================
Original URL: https://ethershares.blogspot.nl
Prompt: Generate code for a simple blockchain-based commenting system for a blog.
Generated: DETERMINISTIC_b12b717f17843d8a
Batch ID: 20250622_205537
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import time
import json

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        """
        Initialize a new block.

        Args:
            index (int): The index of the block in the blockchain.
            previous_hash (str): The hash of the previous block.
            timestamp (float): The timestamp of the block.
            data (dict): The data stored in the block.
        """
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """
        Calculate the hash of the block.

        Returns:
            str: The hash of the block.
        """
        data_string = json.dumps(self.data)
        block_data = str(self.index) + self.previous_hash + str(self.timestamp) + data_string
        return hashlib.sha256(block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        """
        Initialize a new blockchain.
        """
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """
        Create the genesis block.

        Returns:
            Block: The genesis block.
        """
        return Block(0, "0", time.time(), {"comments": []})

    def get_latest_block(self):
        """
        Get the latest block in the blockchain.

        Returns:
            Block: The latest block.
        """
        return self.chain[-1]

    def add_block(self, new_block):
        """
        Add a new block to the blockchain.

        Args:
            new_block (Block): The new block to add.

        Raises:
            ValueError: If the new block is not valid.
        """
        if new_block.previous_hash != self.get_latest_block().hash:
            raise ValueError("Invalid previous hash")
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def add_comment(self, comment):
        """
        Add a new comment to the blockchain.

        Args:
            comment (str): The comment to add.

        Raises:
            ValueError: If the comment is empty.
        """
        if not comment:
            raise ValueError("Comment cannot be empty")
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), latest_block.hash, time.time(), {"comments": latest_block.data["comments"] + [comment]})
        self.add_block(new_block)

    def get_comments(self):
        """
        Get all comments in the blockchain.

        Returns:
            list: A list of comments.
        """
        comments = []
        for block in self.chain:
            comments.extend(block.data["comments"])
        return comments


def main():
    blockchain = Blockchain()

    while True:
        print("\n1. Add comment")
        print("2. Get comments")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            comment = input("Enter a comment: ")
            try:
                blockchain.add_comment(comment)
                print("Comment added successfully")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            comments = blockchain.get_comments()
            for i, comment in enumerate(comments):
                print(f"Comment {i+1}: {comment}")
        elif choice == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
```
