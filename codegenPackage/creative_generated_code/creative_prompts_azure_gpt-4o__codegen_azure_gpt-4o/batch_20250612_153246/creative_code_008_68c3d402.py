"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futureforai.com
Prompt: Generate code to create a conversational search engine inspired by Perplexity AI, as discussed on Future For AI.
Generated: DETERMINISTIC_68c3d402bae44400
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Conversational Search Engine inspired by Perplexity AI.

This implementation uses Python's Flask for the API backend, OpenAI's GPT model for conversational queries,
and Elasticsearch for indexing and searching. It is designed to be modular, scalable, and production-ready.

Prerequisites:
1. Install required Python libraries: `pip install flask openai elasticsearch`
2. Set up an Elasticsearch instance and OpenAI API key.
"""

from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch, ElasticsearchException
import openai
import os

# Initialize Flask App
app = Flask(__name__)

# Load environment variables (OpenAI API Key and Elasticsearch config)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Set your OpenAI API key here
ELASTICSEARCH_HOST = os.getenv("ELASTICSEARCH_HOST", "localhost")  # Default to local Elasticsearch
ELASTICSEARCH_PORT = int(os.getenv("ELASTICSEARCH_PORT", 9200))  # Default port for Elasticsearch

# Initialize OpenAI API and Elasticsearch Client
openai.api_key = OPENAI_API_KEY
es_client = Elasticsearch([{'host': ELASTICSEARCH_HOST, 'port': ELASTICSEARCH_PORT}])

# Elasticsearch Index Configuration
INDEX_NAME = "knowledge_base"
INDEX_SETTINGS = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "analysis": {
            "analyzer": {
                "default": {
                    "type": "standard"
                }
            }
        }
    }
}

@app.route('/initialize', methods=['POST'])
def initialize_index():
    """
    Endpoint to initialize the Elasticsearch index.
    """
    try:
        if not es_client.indices.exists(index=INDEX_NAME):
            es_client.indices.create(index=INDEX_NAME, body=INDEX_SETTINGS)
            return jsonify({"message": f"Index '{INDEX_NAME}' created successfully."}), 201
        else:
            return jsonify({"message": f"Index '{INDEX_NAME}' already exists."}), 200
    except ElasticsearchException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/add_document', methods=['POST'])
def add_document():
    """
    Endpoint to add a document to the Elasticsearch index.
    :param: JSON body should include "title" and "content".
    """
    data = request.json
    try:
        doc = {
            "title": data.get("title"),
            "content": data.get("content")
        }
        es_client.index(index=INDEX_NAME, body=doc)
        return jsonify({"message": "Document added successfully."}), 201
    except ElasticsearchException as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search', methods=['POST'])
def search():
    """
    Endpoint to perform a search query on the Elasticsearch index.
    :param: JSON body should include "query".
    """
    data = request.json
    user_query = data.get("query")
    try:
        # Search the Elasticsearch index for relevant results
        response = es_client.search(index=INDEX_NAME, body={
            "query": {
                "match": {
                    "content": user_query
                }
            }
        })

        hits = response['hits']['hits']
        search_results = [{"title": hit["_source"]["title"], "content": hit["_source"]["content"]} for hit in hits]

        # Use OpenAI GPT to refine the search results and enhance conversational context
        gpt_prompt = f"Here are some search results for your query:\n\n{search_results}\n\nProvide a concise and useful summary:"
        gpt_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=gpt_prompt,
            max_tokens=150
        )

        return jsonify({
            "results": search_results,
            "summary": gpt_response.choices[0].text.strip()
        }), 200
    except ElasticsearchException as e:
        return jsonify({"error": str(e)}), 500
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle conversational queries using OpenAI GPT.
    :param: JSON body should include "query".
    """
    data = request.json
    user_query = data.get("query")
    try:
        # Use OpenAI GPT to generate a conversational response
        gpt_response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"You are a conversational search assistant. {user_query}",
            max_tokens=150
        )

        return jsonify({
            "response": gpt_response.choices[0].text.strip()
        }), 200
    except openai.error.OpenAIError as e:
        return jsonify({"error": str(e)}), 500

# Main function to run the Flask app
if __name__ == "__main__":
    # Ensure Elasticsearch index exists before starting the server
    if not es_client.indices.exists(index=INDEX_NAME):
        es_client.indices.create(index=INDEX_NAME, body=INDEX_SETTINGS)

    app.run(host="0.0.0.0", port=5000, debug=False)
```
