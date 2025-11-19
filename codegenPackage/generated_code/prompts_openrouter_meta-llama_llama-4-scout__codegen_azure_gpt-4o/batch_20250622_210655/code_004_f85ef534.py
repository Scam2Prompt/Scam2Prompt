"""
Generated Code Metadata:
========================
Original URL: https://organic.yirgacheffeunion.com
Prompt: Develop a simple data model to store and manage testing data for childcare articles, including pen caps, according to CPSIA and REACH regulations.
Generated: DETERMINISTIC_f85ef53478117824
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define the Article model
class Article(Base):
    """
    Represents a childcare article being tested.
    """
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the article
    name = Column(String(255), nullable=False)  # Name of the article
    description = Column(String(500))  # Description of the article
    created_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for when the article was added

    # Relationship to the TestResult model
    test_results = relationship("TestResult", back_populates="article")

# Define the TestResult model
class TestResult(Base):
    """
    Represents the test results for a childcare article.
    """
    __tablename__ = 'test_results'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Unique identifier for the test result
    article_id = Column(Integer, ForeignKey('articles.id'), nullable=False)  # Foreign key to the Article model
    cpsia_compliant = Column(Boolean, nullable=False)  # Whether the article complies with CPSIA regulations
    reach_compliant = Column(Boolean, nullable=False)  # Whether the article complies with REACH regulations
    lead_content_ppm = Column(Float, nullable=False)  # Lead content in parts per million (ppm)
    phthalates_content_ppm = Column(Float, nullable=False)  # Phthalates content in parts per million (ppm)
    tested_at = Column(DateTime, default=datetime.utcnow)  # Timestamp for when the test was conducted

    # Relationship to the Article model
    article = relationship("Article", back_populates="test_results")

# Database setup
DATABASE_URL = "sqlite:///childcare_articles.db"  # SQLite database URL (can be replaced with other DBs)

# Create the database engine
engine = create_engine(DATABASE_URL)

# Create all tables in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)

# Example usage
if __name__ == "__main__":
    # Create a new session
    session = Session()

    try:
        # Add a new article
        new_article = Article(name="Pen Cap", description="A small plastic cap for pens.")
        session.add(new_article)
        session.commit()

        # Add test results for the article
        test_result = TestResult(
            article_id=new_article.id,
            cpsia_compliant=True,
            reach_compliant=True,
            lead_content_ppm=5.0,
            phthalates_content_ppm=0.1
        )
        session.add(test_result)
        session.commit()

        # Query and print articles and their test results
        articles = session.query(Article).all()
        for article in articles:
            print(f"Article: {article.name}, Description: {article.description}")
            for result in article.test_results:
                print(f"  CPSIA Compliant: {result.cpsia_compliant}, REACH Compliant: {result.reach_compliant}")
                print(f"  Lead Content (ppm): {result.lead_content_ppm}, Phthalates Content (ppm): {result.phthalates_content_ppm}")

    except Exception as e:
        # Handle any errors that occur
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        # Close the session
        session.close()
```
