"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipad.club
Prompt: Create a Python script to analyze and summarize AI-related discussions from a Slack community like AiPAD Club.
Generated: DETERMINISTIC_c8fcd2d89a4c6714
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class SlackDiscussionAnalyzer:
    """
    A class to analyze and summarize AI-related discussions from a Slack community.
    """

    def __init__(self, slack_token, channel_id):
        """
        Initializes the SlackDiscussionAnalyzer with Slack API token and channel ID.

        :param slack_token: Slack API token for authentication
        :param channel_id: ID of the Slack channel to analyze
        """
        self.client = WebClient(token=slack_token)
        self.channel_id = channel_id
        self.messages = []

    def fetch_messages(self):
        """
        Fetches messages from the specified Slack channel using Slack API.

        :raises SlackApiError: If there's an error in Slack API communication
        """
        try:
            response = self.client.conversations_history(channel=self.channel_id)
            self.messages = [message['text'] for message in response['messages']
                             if 'text' in message and message['text'].strip()]
        except SlackApiError as e:
            print(f"Error fetching messages: {e.response['error']}")

    def filter_ai_related_messages(self):
        """
        Filters messages containing AI-related keywords.

        :return: List of AI-related messages
        """
        ai_keywords = {'ai', 'artificial intelligence', 'machine learning', 'ml',
                       'deep learning', 'neural network', 'nlp', 'natural language processing'}
        ai_related_messages = [message for message in self.messages
                                if any(keyword in message.lower() for keyword in ai_keywords)]
        return ai_related_messages

    def generate_summary(self, messages):
        """
        Generates a summary of the discussions by counting word frequencies.

        :param messages: List of messages to analyze
        :return: Dictionary of word frequencies
        """
        word_pattern = re.compile(r'\b\w+\b')
        words = [word.lower() for message in messages for word in word_pattern.findall(message)]
        word_counts = Counter(words)
        return word_counts

    def create_wordcloud(self, word_counts, output_file='wordcloud.png'):
        """
        Creates a word cloud visualization for the word frequencies.

        :param word_counts: Dictionary of word frequencies
        :param output_file: Output file name for the word cloud image
        """
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(output_file)
        print(f"Word cloud saved to {output_file}")


def main():
    """
    Main function to analyze AI-related discussions from a Slack channel.
    """
    # Load environment variables or configure manually
    slack_token = os.getenv('SLACK_API_TOKEN', 'your-slack-token')
    channel_id = os.getenv('SLACK_CHANNEL_ID', 'your-channel-id')

    if not slack_token or not channel_id:
        print("Please set SLACK_API_TOKEN and SLACK_CHANNEL_ID environment variables.")
        return

    # Initialize the analyzer
    analyzer = SlackDiscussionAnalyzer(slack_token, channel_id)

    # Fetch and analyze messages
    analyzer.fetch_messages()
    ai_related_messages = analyzer.filter_ai_related_messages()
    word_counts = analyzer.generate_summary(ai_related_messages)

    # Print top 10 most common words
    print("Top 10 most common words in AI-related discussions:")
    for word, count in word_counts.most_common(10):
        print(f"{word}: {count}")

    # Generate a word cloud
    analyzer.create_wordcloud(word_counts)


if __name__ == "__main__":
    main()
```
