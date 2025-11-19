"""
Generated Code Metadata:
========================
Original URL: https://kraken-darknet-tor.com
Prompt: Create a basic implementation of a reputation system, similar to the one used by Blacksprut/Блэкспрут, using a graph database and Cypher query language.
Generated: DETERMINISTIC_18b3805c092cc84c
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Reputation System Implementation**
=====================================

**Dependencies**
---------------

* Neo4j Graph Database
* Cypher Query Language
* Python 3.x
* neo4j Python Driver

**Code**
------

```python
from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

class ReputationSystem:
    def __init__(self, uri, auth):
        self.driver = GraphDatabase.driver(uri, auth=auth)

    def close(self):
        self.driver.close()

    def create_user(self, user_id):
        """Create a new user node"""
        with self.driver.session() as session:
            try:
                result = session.run("CREATE (u:User {id: $user_id}) RETURN u", user_id=user_id)
                return result.single()["u"]
            except ServiceUnavailable as e:
                print(f"Error creating user: {e}")

    def create_post(self, post_id, user_id):
        """Create a new post node and relate it to the user"""
        with self.driver.session() as session:
            try:
                user_node = session.run("MATCH (u:User {id: $user_id}) RETURN u", user_id=user_id).single()["u"]
                result = session.run("CREATE (p:Post {id: $post_id})-[:POSTED_BY]->(u) RETURN p", post_id=post_id)
                return result.single()["p"]
            except ServiceUnavailable as e:
                print(f"Error creating post: {e}")

    def rate_post(self, post_id, user_id, rating):
        """Create a new rating node and relate it to the post and user"""
        with self.driver.session() as session:
            try:
                post_node = session.run("MATCH (p:Post {id: $post_id}) RETURN p", post_id=post_id).single()["p"]
                user_node = session.run("MATCH (u:User {id: $user_id}) RETURN u", user_id=user_id).single()["u"]
                result = session.run("CREATE (r:Rating {rating: $rating})-[:RATED_POST]->(p)-[:RATED_BY]->(u) RETURN r", rating=rating, post_id=post_id, user_id=user_id)
                return result.single()["r"]
            except ServiceUnavailable as e:
                print(f"Error rating post: {e}")

    def get_user_reputation(self, user_id):
        """Calculate the reputation of a user based on ratings of their posts"""
        with self.driver.session() as session:
            try:
                result = session.run("""
                    MATCH (u:User {id: $user_id})-[:POSTED_BY]->(p:Post)<-[:RATED_POST]-(r:Rating)
                    RETURN SUM(r.rating) AS reputation
                """, user_id=user_id)
                return result.single()["reputation"]
            except ServiceUnavailable as e:
                print(f"Error getting user reputation: {e}")

    def get_post_reputation(self, post_id):
        """Calculate the reputation of a post based on ratings"""
        with self.driver.session() as session:
            try:
                result = session.run("""
                    MATCH (p:Post {id: $post_id})<-[:RATED_POST]-(r:Rating)
                    RETURN SUM(r.rating) AS reputation
                """, post_id=post_id)
                return result.single()["reputation"]
            except ServiceUnavailable as e:
                print(f"Error getting post reputation: {e}")

# Example usage
if __name__ == "__main__":
    uri = "bolt://localhost:7687"
    auth = ("neo4j", "password")

    reputation_system = ReputationSystem(uri, auth)

    user_id = "user1"
    post_id = "post1"

    user_node = reputation_system.create_user(user_id)
    post_node = reputation_system.create_post(post_id, user_id)

    rating_node = reputation_system.rate_post(post_id, user_id, 5)

    user_reputation = reputation_system.get_user_reputation(user_id)
    post_reputation = reputation_system.get_post_reputation(post_id)

    print(f"User reputation: {user_reputation}")
    print(f"Post reputation: {post_reputation}")

    reputation_system.close()
```

**Cypher Indexes**
-----------------

Create the following indexes in your Neo4j database:

```cypher
CREATE INDEX ON :User(id)
CREATE INDEX ON :Post(id)
```

**Constraints**
--------------

Create the following constraints in your Neo4j database:

```cypher
CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE
CREATE CONSTRAINT ON (p:Post) ASSERT p.id IS UNIQUE
```
