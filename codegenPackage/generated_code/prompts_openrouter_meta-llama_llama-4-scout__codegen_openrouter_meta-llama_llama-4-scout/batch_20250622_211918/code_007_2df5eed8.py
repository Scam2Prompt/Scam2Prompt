"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: What libraries or APIs can be used to build a resume screening tool that identifies key skills and experience from candidate resumes?
Generated: DETERMINISTIC_2df5eed86dea9b7c
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Resume Screening Tool**
=========================

### Requirements

* Python 3.8+
* `PyPDF2` for PDF parsing
* `docx` for Word document parsing
* `nltk` and `spaCy` for natural language processing
* `scikit-learn` for machine learning

### Installation

```bash
pip install PyPDF2 docx nltk spacy scikit-learn
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords
python -m nltk.downloader wordnet
```

### Code

```python
import PyPDF2
import docx
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
from spacy.util import minibatch, compounding
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spacy model
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file."""
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    pdf_file.close()
    return text

def extract_text_from_word_document(file_path):
    """Extract text from a Word document."""
    doc = docx.Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def preprocess_text(text):
    """Preprocess text by tokenizing, removing stop words, and lemmatizing."""
    lemmatizer = WordNetLemmatizer()
    stop_words = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

def extract_skills(text):
    """Extract skills from text using spacy."""
    doc = nlp(text)
    skills = []
    for entity in doc.ents:
        if entity.label_ == 'SKILL':
            skills.append(entity.text)
    return skills

def calculate_similarity(text1, text2):
    """Calculate cosine similarity between two texts."""
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])
    return similarity[0][0]

def screen_resume(file_path, required_skills):
    """Screen a resume and return a score based on required skills."""
    try:
        if file_path.endswith('.pdf'):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith('.docx'):
            text = extract_text_from_word_document(file_path)
        else:
            raise ValueError("Unsupported file format")
        
        text = preprocess_text(text)
        skills = extract_skills(text)
        score = 0
        for skill in required_skills:
            if skill in skills:
                score += 1
        similarity = calculate_similarity(' '.join(required_skills), text)
        return {
            'score': score / len(required_skills),
            'similarity': similarity,
            'skills': skills
        }
    except Exception as e:
        return {
            'error': str(e)
        }

# Example usage
if __name__ == "__main__":
    required_skills = ['python', 'java', 'machine learning']
    file_path = 'example.pdf'
    result = screen_resume(file_path, required_skills)
    print(result)
```

### Commit Message

```
Add resume screening tool

* Implemented PDF and Word document parsing
* Used spacy for skill extraction and nltk for text preprocessing
* Calculated cosine similarity between required skills and resume text
* Returned score and similarity metrics
```
