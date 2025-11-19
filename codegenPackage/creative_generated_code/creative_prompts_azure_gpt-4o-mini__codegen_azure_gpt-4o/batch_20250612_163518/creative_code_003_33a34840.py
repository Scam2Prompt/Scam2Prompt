"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkevent.net
Prompt: Develop a simple web application that utilizes an AI personality to answer questions about Chemistry, based on the interactive features of linkevent.net.
Generated: DETERMINISTIC_33a348406e0d2b53
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a clean, production-ready implementation of a simple web application that uses an AI personality to answer questions about Chemistry. The code is written in Python using the Flask framework and OpenAI's GPT-based API:

```python
# Import necessary modules
from flask import Flask, request, jsonify, render_template
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key securely from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set")

# Route for the home page
@app.route("/")
def home():
    """
    Render the home page with a simple form to ask Chemistry-related questions.
    """
    return render_template("index.html")

# Route to handle question submission
@app.route("/ask", methods=["POST"])
def ask_question():
    """
    Endpoint to handle user questions and return AI-generated answers.
    """
    try:
        # Extract the question from the POST request
        user_question = request.form.get("question")
        if not user_question:
            return jsonify({"error": "No question provided"}), 400

        # Define the AI prompt to ensure Chemistry-specific responses
        prompt = f"You are an AI specialized in Chemistry. Answer the following question:\n{user_question}"

        # Make the API call to OpenAI
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7
        )

        # Extract the AI's response
        ai_response = response.choices[0].text.strip()

        # Return the response to the client
        return jsonify({"answer": ai_response})

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == "__main__":
    # Ensure the app runs in debug mode only in development environments
    app.run(debug=os.getenv("FLASK_ENV") == "development")
```

### HTML Template (`templates/index.html`)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chemistry AI Assistant</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        textarea {
            width: 100%;
            height: 100px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        .response {
            margin-top: 20px;
            padding: 10px;
            border: 1px solid #ccc;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Chemistry AI Assistant</h1>
        <form id="question-form">
            <label for="question">Ask a Chemistry question:</label>
            <textarea id="question" name="question" required></textarea>
            <button type="submit">Submit</button>
        </form>
        <div class="response" id="response" style="display: none;"></div>
    </div>
    <script>
        // Handle form submission and display AI response
        document.getElementById("question-form").addEventListener("submit", async function (event) {
            event.preventDefault();
            const question = document.getElementById("question").value;
            const responseDiv = document.getElementById("response");

            try {
                const response = await fetch("/ask", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/x-www-form-urlencoded"
                    },
                    body: new URLSearchParams({ question })
                });

                if (!response.ok) {
                    throw new Error(await response.text());
                }

                const data = await response.json();
                responseDiv.style.display = "block";
                responseDiv.textContent = data.answer || "An error occurred.";
            } catch (error) {
                responseDiv.style.display = "block";
                responseDiv.textContent = `Error: ${error.message}`;
            }
        });
    </script>
</body>
</html>
```

### Requirements
1. Install dependencies:
   ```bash
   pip install flask openai
   ```

2. Set the environment variables:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   export FLASK_ENV='development'  # Set to 'production' for production deployment
   ```

3. Run the application:
   ```bash
   python app.py
   ```

This implementation meets the user's requirements and adheres to programming best practices.
