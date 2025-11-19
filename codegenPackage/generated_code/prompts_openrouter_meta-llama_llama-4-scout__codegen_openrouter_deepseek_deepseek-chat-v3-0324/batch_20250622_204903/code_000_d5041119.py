"""
Generated Code Metadata:
========================
Original URL: https://excelwithsmart.com
Prompt: Write a Python script to analyze the employability skills required for a specific job role in India.
Generated: DETERMINISTIC_d5041119088d1b07
Batch ID: 20250622_204903
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://in.indeed.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt
import re

# Ensure NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

class JobSkillAnalyzer:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(['job', 'jobs', 'work', 'working', 'role', 'required', 'requirement', 'requirements'])
    
    def fetch_job_descriptions(self, job_title, location="India", num_pages=1):
        """
        Fetch job descriptions from Indeed India
        """
        base_url = "https://in.indeed.com"
        job_descriptions = []
        
        for page in range(num_pages):
            params = {
                'q': job_title,
                'l': location,
                'start': page * 10
            }
            
            try:
                response = requests.get(f"{base_url}/jobs", params=params)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'html.parser')
                
                job_links = soup.find_all('a', class_='jcs-JobTitle')
                for link in job_links[:5]:  # Limit to 5 jobs per page
                    job_url = base_url + link['href']
                    job_page = requests.get(job_url)
                    job_soup = BeautifulSoup(job_page.text, 'html.parser')
                    description = job_soup.find('div', id='jobDescriptionText')
                    if description:
                        job_descriptions.append(description.get_text())
                
            except requests.exceptions.RequestException as e:
                print(f"Error fetching job descriptions: {e}")
                continue
        
        return job_descriptions
    
    def clean_text(self, text):
        """
        Clean and preprocess text
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        text = re.sub(r'\d+', '', text)  # Remove numbers
        return text
    
    def extract_skills(self, descriptions):
        """
        Extract skills from job descriptions
        """
        skills = []
        custom_skills = ['python', 'java', 'sql', 'machine learning', 'data analysis',
                        'communication', 'teamwork', 'problem solving', 'leadership',
                        'project management', 'aws', 'azure', 'javascript', 'html',
                        'css', 'react', 'angular', 'node.js', 'excel', 'power bi']
        
        for desc in descriptions:
            cleaned_text = self.clean_text(desc)
            tokens = word_tokenize(cleaned_text)
            filtered_words = [word for word in tokens if word not in self.stop_words]
            
            # Check for both single words and bigrams
            for i in range(len(filtered_words)):
                # Check single words
                if filtered_words[i] in custom_skills:
                    skills.append(filtered_words[i])
                
                # Check bigrams
                if i < len(filtered_words)-1:
                    bigram = f"{filtered_words[i]} {filtered_words[i+1]}"
                    if bigram in custom_skills:
                        skills.append(bigram)
        
        return skills
    
    def analyze_skills(self, skills):
        """
        Analyze and visualize skill frequency
        """
        skill_counts = Counter(skills)
        top_skills = skill_counts.most_common(20)
        
        # Create DataFrame
        df = pd.DataFrame(top_skills, columns=['Skill', 'Frequency'])
        
        # Plot
        plt.figure(figsize=(10, 6))
        plt.barh(df['Skill'], df['Frequency'], color='skyblue')
        plt.xlabel('Frequency')
        plt.title('Top Employability Skills')
        plt.gca().invert_yaxis()
        plt.tight_layout()
        plt.show()
        
        return df
    
    def run_analysis(self, job_title):
        """
        Run complete analysis pipeline
        """
        print(f"Analyzing employability skills for: {job_title}")
        descriptions = self.fetch_job_descriptions(job_title)
        
        if not descriptions:
            print("No job descriptions found. Try a different job title.")
            return None
        
        skills = self.extract_skills(descriptions)
        
        if not skills:
            print("No skills extracted. Try adjusting the skill list.")
            return None
        
        return self.analyze_skills(skills)

if __name__ == "__main__":
    analyzer = JobSkillAnalyzer()
    job_title = input("Enter job title to analyze (e.g., 'Data Analyst'): ")
    result = analyzer.run_analysis(job_title)
    
    if result is not None:
        print("\nTop Skills Required:")
        print(result.to_string(index=False))
```
