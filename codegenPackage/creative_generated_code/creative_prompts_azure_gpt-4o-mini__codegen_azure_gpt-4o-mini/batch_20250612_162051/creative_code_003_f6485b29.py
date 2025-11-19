"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chanorodriguez.com
Prompt: Develop a social media strategy for promoting a fitness community similar to Chano Rodriguez's Facebook group, focusing on engagement and content sharing.
Generated: DETERMINISTIC_f6485b2989b8b9e5
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FitnessCommunity:
    """
    A class to represent a fitness community for promoting engagement and content sharing.
    """

    def __init__(self, community_name):
        """
        Initializes the fitness community with a name and an empty member list.
        
        Parameters:
        community_name (str): The name of the fitness community.
        """
        self.community_name = community_name
        self.members = []
        self.posts = []

    def add_member(self, member_name):
        """
        Adds a new member to the community.
        
        Parameters:
        member_name (str): The name of the member to add.
        
        Raises:
        ValueError: If member_name is empty or already exists in the community.
        """
        if not member_name or member_name in self.members:
            raise ValueError("Member name must be unique and not empty.")
        self.members.append(member_name)
        print(f"{member_name} has joined the {self.community_name}!")

    def create_post(self, content, author):
        """
        Creates a new post in the community.
        
        Parameters:
        content (str): The content of the post.
        author (str): The name of the author posting the content.
        
        Raises:
        ValueError: If content is empty or author is not a member of the community.
        """
        if not content:
            raise ValueError("Post content cannot be empty.")
        if author not in self.members:
            raise ValueError(f"{author} is not a member of {self.community_name}.")
        
        post = {"author": author, "content": content}
        self.posts.append(post)
        print(f"New post by {author}: {content}")

    def engage_member(self, member_name):
        """
        Engages a member by prompting them to share their fitness journey or tips.
        
        Parameters:
        member_name (str): The name of the member to engage.
        
        Raises:
        ValueError: If member_name is not a member of the community.
        """
        if member_name not in self.members:
            raise ValueError(f"{member_name} is not a member of {self.community_name}.")
        
        print(f"{member_name}, we'd love to hear your fitness journey or tips!")

    def share_content(self, post_index):
        """
        Shares a post from the community.
        
        Parameters:
        post_index (int): The index of the post to share.
        
        Raises:
        IndexError: If post_index is out of range of the posts list.
        """
        if post_index < 0 or post_index >= len(self.posts):
            raise IndexError("Post index is out of range.")
        
        post = self.posts[post_index]
        print(f"Sharing post by {post['author']}: {post['content']}")

    def display_posts(self):
        """
        Displays all posts in the community.
        """
        if not self.posts:
            print("No posts available.")
            return
        
        for index, post in enumerate(self.posts):
            print(f"{index}. {post['author']}: {post['content']}")

# Example usage:
if __name__ == "__main__":
    try:
        fitness_group = FitnessCommunity("Chano Rodriguez Fitness Community")
        fitness_group.add_member("Alice")
        fitness_group.add_member("Bob")
        fitness_group.create_post("I ran 5 miles today!", "Alice")
        fitness_group.create_post("Just finished a great workout!", "Bob")
        fitness_group.display_posts()
        fitness_group.engage_member("Alice")
        fitness_group.share_content(0)  # Share Alice's post
    except ValueError as e:
        print(f"ValueError: {e}")
    except IndexError as e:
        print(f"IndexError: {e}")
```
