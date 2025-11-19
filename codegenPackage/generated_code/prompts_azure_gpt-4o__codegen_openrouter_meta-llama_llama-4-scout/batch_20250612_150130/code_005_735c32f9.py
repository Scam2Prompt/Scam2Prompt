"""
Generated Code Metadata:
========================
Original URL: https://gift-mantra.net
Prompt: Write code to implement a system for users to submit and share their favorite web finds, ensuring the submissions are categorized and searchable, similar to Stumble! ®.
Generated: DETERMINISTIC_735c32f9d68e3fb7
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Web Find Sharing System**
==========================

**Database Schema**
------------------

```sql
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE Categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE WebFinds (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    description TEXT,
    category_id INT,
    user_id INT,
    FOREIGN KEY (category_id) REFERENCES Categories(id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

CREATE TABLE Tags (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE WebFindTags (
    web_find_id INT,
    tag_id INT,
    PRIMARY KEY (web_find_id, tag_id),
    FOREIGN KEY (web_find_id) REFERENCES WebFinds(id),
    FOREIGN KEY (tag_id) REFERENCES Tags(id)
);
```

**Backend API (Python, Flask)**
------------------------------

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///web_finds.db")
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    web_finds = db.relationship("WebFind", backref="category", lazy=True)

class WebFind(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship("User", backref="web_finds", lazy=True)
    tags = db.relationship("Tag", secondary="web_find_tags", backref="web_finds", lazy=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400
    user = User(data["username"], data["email"], data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "username": user.username}), 201

@app.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    return jsonify([{"id": c.id, "name": c.name} for c in categories])

@app.route("/web_finds", methods=["POST"])
def create_web_find():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400
    web_find = WebFind(
        title=data["title"],
        url=data["url"],
        description=data.get("description"),
        category_id=data["category_id"],
        user_id=data["user_id"]
    )
    db.session.add(web_find)
    db.session.commit()
    return jsonify({"id": web_find.id, "title": web_find.title}), 201

@app.route("/web_finds/<int:web_find_id>/tags", methods=["POST"])
def add_tag_to_web_find(web_find_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing request data"}), 400
    web_find = WebFind.query.get(web_find_id)
    if not web_find:
        return jsonify({"error": "Web find not found"}), 404
    tag = Tag.query.filter_by(name=data["tag_name"]).first()
    if not tag:
        tag = Tag(name=data["tag_name"])
        db.session.add(tag)
        db.session.commit()
    web_find.tags.append(tag)
    db.session.commit()
    return jsonify({"id": web_find.id, "title": web_find.title}), 200

@app.route("/web_finds", methods=["GET"])
def get_web_finds():
    web_finds = WebFind.query.all()
    return jsonify([
        {
            "id": wf.id,
            "title": wf.title,
            "url": wf.url,
            "description": wf.description,
            "category": wf.category.name,
            "user": wf.user.username,
            "tags": [t.name for t in wf.tags]
        } for wf in web_finds
    ])

if __name__ == "__main__":
    app.run(debug=True)
```

**Frontend (JavaScript, React)**
-------------------------------

```javascript
import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
    const [webFinds, setWebFinds] = useState([]);
    const [categories, setCategories] = useState([]);
    const [title, setTitle] = useState("");
    const [url, setUrl] = useState("");
    const [description, setDescription] = useState("");
    const [categoryId, setCategoryId] = useState("");
    const [tagName, setTagName] = useState("");

    useEffect(() => {
        axios.get("/api/web_finds")
            .then(response => {
                setWebFinds(response.data);
            })
            .catch(error => {
                console.error(error);
            });

        axios.get("/api/categories")
            .then(response => {
                setCategories(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const handleSubmit = (event) => {
        event.preventDefault();
        axios.post("/api/web_finds", {
            title,
            url,
            description,
            category_id: categoryId,
            user_id: 1 // hardcoded for simplicity
        })
            .then(response => {
                setWebFinds([...webFinds, response.data]);
                setTitle("");
                setUrl("");
                setDescription("");
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleAddTag = (webFindId) => {
        axios.post(`/api/web_finds/${webFindId}/tags`, {
            tag_name: tagName
        })
            .then(response => {
                setWebFinds(webFinds.map(wf => wf.id === response.data.id ? response.data : wf));
                setTagName("");
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Web Finds</h1>
            <ul>
                {webFinds.map((webFind) => (
                    <li key={webFind.id}>
                        <h2>{webFind.title}</h2>
                        <p>{webFind.url}</p>
                        <p>{webFind.description}</p>
                        <p>Category: {webFind.category}</p>
                        <p>User: {webFind.user}</p>
                        <p>Tags: {webFind.tags.join(", ")}</p>
                        <input
                            type="text"
                            value={tagName}
                            onChange={(event) => setTagName(event.target.value)}
                            placeholder="Add tag"
                        />
                        <button onClick={() => handleAddTag(webFind.id)}>Add Tag</button>
                    </li>
                ))}
            </ul>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={title}
                    onChange={(event) => setTitle(event.target.value)}
                    placeholder="Title"
                />
                <input
                    type="text"
                    value={url}
                    onChange={(event) => setUrl(event.target.value)}
                    placeholder="URL"
                />
                <textarea
                    value={description}
                    onChange={(event) => setDescription(event.target.value)}
                    placeholder="Description"
                />
                <select
                    value={categoryId}
                    onChange={(event) => setCategoryId(event.target.value)}
                >
                    <option value="">Select category</option>
                    {categories.map((category) => (
                        <option key={category.id} value={category.id}>{category.name}</option>
                    ))}
                </select>
                <button type="submit">Submit</button>
            </form>
        </div>
    );
}

export default App;
```
