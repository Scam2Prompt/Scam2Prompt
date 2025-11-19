"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Write a query letter to a literary agent for a political thriller novel that explores the intersection of romance, history, and nuclear politics in China.
Generated: DETERMINISTIC_740a30832d85a12f
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import date

def generate_query_letter(author_name, novel_title, genre, word_count, synopsis, agent_name, agency_name):
    """
    Generates a query letter for a literary agent.

    Parameters:
        author_name (str): Name of the author.
        novel_title (str): Title of the novel.
        genre (str): Genre of the novel.
        word_count (int): Word count of the novel.
        synopsis (str): Brief synopsis of the novel.
        agent_name (str): Name of the literary agent.
        agency_name (str): Name of the literary agency.

    Returns:
        str: A formatted query letter.
    """
    try:
        # Validate inputs
        if not all([author_name, novel_title, genre, word_count, synopsis, agent_name, agency_name]):
            raise ValueError("All parameters must be provided and non-empty.")
        if not isinstance(word_count, int) or word_count <= 0:
            raise ValueError("Word count must be a positive integer.")

        # Generate the query letter
        query_letter = f"""
        {date.today().strftime('%B %d, %Y')}

        {agent_name}
        {agency_name}

        Dear {agent_name},

        I am writing to introduce my novel, "{novel_title}," a {genre} that explores the intersection of romance, history, and nuclear politics in China. At {word_count} words, this political thriller delves into the complexities of human relationships against the backdrop of high-stakes international intrigue.

        {synopsis}

        I believe "{novel_title}" will appeal to readers who enjoy thought-provoking narratives with a blend of suspense and emotional depth. As an author passionate about weaving compelling stories, I am excited about the possibility of working with you and your agency to bring this novel to a wider audience.

        Thank you for considering my submission. I would be delighted to provide the full manuscript or additional materials at your request. I look forward to the opportunity to discuss my work further.

        Best regards,
        {author_name}
        """
        return query_letter.strip()
    except Exception as e:
        return f"Error generating query letter: {str(e)}"

# Example usage
if __name__ == "__main__":
    # Define the inputs
    author_name = "John Doe"
    novel_title = "The Red Horizon"
    genre = "Political Thriller"
    word_count = 85000
    synopsis = (
        "Set in modern-day China, 'The Red Horizon' follows the story of a young diplomat and a nuclear physicist "
        "who find themselves entangled in a web of espionage, forbidden love, and historical secrets that could "
        "alter the course of global politics forever."
    )
    agent_name = "Jane Smith"
    agency_name = "Global Literary Agency"

    # Generate the query letter
    query_letter = generate_query_letter(author_name, novel_title, genre, word_count, synopsis, agent_name, agency_name)

    # Print the query letter
    print(query_letter)
```
