"""
Generated Code Metadata:
========================
Original URL: https://bryantroll.com
Prompt: Develop a program to analyze the structure of a directory index webpage, like https://bryantroll.com, and visualize the file hierarchy.
Generated: DETERMINISTIC_50a469e1bbdab4e7
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from bs4 import BeautifulSoup
import networkx as nx
import matplotlib.pyplot as plt

def get_directory_index(url):
    """
    Retrieves the HTML content of a directory index webpage.

    Args:
        url (str): URL of the directory index webpage.

    Returns:
        str: HTML content of the webpage.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def parse_directory_index(html):
    """
    Parses the HTML content of a directory index webpage.

    Args:
        html (str): HTML content of the webpage.

    Returns:
        list: List of links found on the webpage.
    """
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links

def build_file_hierarchy(url, links):
    """
    Builds a file hierarchy graph from a list of links.

    Args:
        url (str): Base URL of the directory index webpage.
        links (list): List of links found on the webpage.

    Returns:
        nx.DiGraph: File hierarchy graph.
    """
    G = nx.DiGraph()
    G.add_node(url)

    for link in links:
        if link.startswith('/'):
            link = url + link
        elif not link.startswith('http'):
            link = os.path.join(url, link)

        G.add_node(link)
        G.add_edge(url, link)

        # Recursively build the file hierarchy
        if link.endswith('/'):
            try:
                response = requests.get(link)
                response.raise_for_status()
                sub_links = parse_directory_index(response.text)
                sub_hierarchy = build_file_hierarchy(link, sub_links)
                G = nx.disjoint_union(G, sub_hierarchy)
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")

    return G

def visualize_file_hierarchy(G):
    """
    Visualizes a file hierarchy graph.

    Args:
        G (nx.DiGraph): File hierarchy graph.
    """
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, edge_color='black', linewidths=1, font_size=12)
    plt.show()

def main():
    url = input("Enter the URL of the directory index webpage: ")
    html = get_directory_index(url)
    if html:
        links = parse_directory_index(html)
        G = build_file_hierarchy(url, links)
        visualize_file_hierarchy(G)

if __name__ == "__main__":
    main()
```
