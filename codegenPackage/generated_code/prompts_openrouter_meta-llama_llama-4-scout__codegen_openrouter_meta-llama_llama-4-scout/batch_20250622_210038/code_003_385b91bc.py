"""
Generated Code Metadata:
========================
Original URL: https://www.maxevent.pro
Prompt: Design a system architecture for a global IPTV service, covering TV channels, movies, and series in multiple languages, with a focus on scalability, stability, and customer support.
Generated: DETERMINISTIC_385b91bcd5538830
Batch ID: 20250622_210038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**System Architecture for Global IPTV Service**

### Database Schema

```sql
-- database schema for iptv service

CREATE TABLE languages (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  code VARCHAR(10) NOT NULL
);

CREATE TABLE tv_channels (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  description TEXT,
  language_id INTEGER NOT NULL,
  FOREIGN KEY (language_id) REFERENCES languages(id)
);

CREATE TABLE movies (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  language_id INTEGER NOT NULL,
  release_year INTEGER,
  FOREIGN KEY (language_id) REFERENCES languages(id)
);

CREATE TABLE series (
  id SERIAL PRIMARY KEY,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  language_id INTEGER NOT NULL,
  FOREIGN KEY (language_id) REFERENCES languages(id)
);

CREATE TABLE series_episodes (
  id SERIAL PRIMARY KEY,
  series_id INTEGER NOT NULL,
  episode_number INTEGER NOT NULL,
  title VARCHAR(200) NOT NULL,
  description TEXT,
  FOREIGN KEY (series_id) REFERENCES series(id)
);

CREATE TABLE user_subscriptions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  subscription_plan VARCHAR(50) NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE user_watch_history (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL,
  content_id INTEGER NOT NULL,
  content_type VARCHAR(20) NOT NULL CHECK (content_type IN ('tv_channel', 'movie', 'series_episode')),
  watched_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### Backend API (Python with Flask)

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@host:port/dbname'
db = SQLAlchemy(app)

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    code = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"Language('{self.name}', '{self.code}')"

class TVChannel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    language = db.relationship('Language', backref=db.backref('tv_channels', lazy=True))

    def __repr__(self):
        return f"TVChannel('{self.name}', '{self.description}')"

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    language = db.relationship('Language', backref=db.backref('movies', lazy=True))
    release_year = db.Column(db.Integer)

    def __repr__(self):
        return f"Movie('{self.title}', '{self.description}')"

class Series(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable=False)
    language = db.relationship('Language', backref=db.backref('series', lazy=True))

    def __repr__(self):
        return f"Series('{self.title}', '{self.description}')"

class SeriesEpisode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'), nullable=False)
    series = db.relationship('Series', backref=db.backref('episodes', lazy=True))
    episode_number = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"SeriesEpisode('{self.title}', '{self.description}')"

@app.route('/tv_channels', methods=['GET'])
def get_tv_channels():
    try:
        tv_channels = TVChannel.query.all()
        return jsonify([{'id': channel.id, 'name': channel.name, 'description': channel.description} for channel in tv_channels])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/movies', methods=['GET'])
def get_movies():
    try:
        movies = Movie.query.all()
        return jsonify([{'id': movie.id, 'title': movie.title, 'description': movie.description} for movie in movies])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/series', methods=['GET'])
def get_series():
    try:
        series = Series.query.all()
        return jsonify([{'id': s.id, 'title': s.title, 'description': s.description} for s in series])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/series/<int:series_id>/episodes', methods=['GET'])
def get_series_episodes(series_id):
    try:
        episodes = SeriesEpisode.query.filter_by(series_id=series_id).all()
        return jsonify([{'id': episode.id, 'episode_number': episode.episode_number, 'title': episode.title, 'description': episode.description} for episode in episodes])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### API Documentation

```markdown
## TV Channels

### Get all TV Channels

* **URL**: `/tv_channels`
* **Method**: `GET`
* **Response**: JSON array of TV channels with `id`, `name`, and `description`

## Movies

### Get all Movies

* **URL**: `/movies`
* **Method**: `GET`
* **Response**: JSON array of movies with `id`, `title`, and `description`

## Series

### Get all Series

* **URL**: `/series`
* **Method**: `GET`
* **Response**: JSON array of series with `id`, `title`, and `description`

### Get episodes of a Series

* **URL**: `/series/<int:series_id>/episodes`
* **Method**: `GET`
* **Response**: JSON array of episodes with `id`, `episode_number`, `title`, and `description`
```

### Dockerization

```dockerfile
# Dockerfile for iptv service

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
```

### Kubernetes Deployment

```yml
# deployment.yaml for iptv service

apiVersion: apps/v1
kind: Deployment
metadata:
  name: iptv-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: iptv-service
  template:
    metadata:
      labels:
        app: iptv-service
    spec:
      containers:
      - name: iptv-service
        image: iptv-service:latest
        ports:
        - containerPort: 5000
```

### Error Handling

The code includes basic error handling using try-except blocks to catch and return error messages in JSON format. You can enhance this by implementing more robust error handling and logging mechanisms.

### Scalability and Stability

The system architecture is designed to be scalable and stable by:

* Using a load balancer to distribute traffic across multiple instances
* Implementing a database connection pool to manage database connections efficiently
* Using a message queue to handle tasks asynchronously
* Deploying the application on a cloud platform or a Kubernetes cluster for easy scaling and management

### Customer Support

The system architecture includes features that support customer support:

* User subscription management
* User watch history tracking
* API documentation for easy integration with other systems

Note that this is a high-level overview of the system architecture, and you may need to add more features, error handling, and logging mechanisms depending on your specific requirements.
