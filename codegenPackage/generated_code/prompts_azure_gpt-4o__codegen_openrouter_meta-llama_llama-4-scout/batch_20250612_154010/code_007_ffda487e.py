"""
Generated Code Metadata:
========================
Original URL: https://colegiodepsicologosoruro.org
Prompt: Write code to analyze and visualize data on psychologists' participation in international courses and seminars, as mentioned in the Colegio de Psicólogos de Oruro's partnerships.
Generated: DETERMINISTIC_ffda487ed42c2a20
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV file
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("The file does not exist")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty")
        return None
    except pd.errors.ParserError:
        print("Error parsing the file")
        return None

# Analyze data on psychologists' participation
def analyze_participation(data):
    # Calculate total number of psychologists
    total_psychologists = data['psychologist_id'].nunique()
    
    # Calculate number of psychologists by country
    psychologists_by_country = data['country'].value_counts().reset_index()
    psychologists_by_country.columns = ['Country', 'Number of Psychologists']
    
    # Calculate number of courses and seminars
    total_courses = data['course_id'].nunique()
    total_seminars = data['seminar_id'].nunique()
    
    return total_psychologists, psychologists_by_country, total_courses, total_seminars

# Visualize data on psychologists' participation
def visualize_participation(data, psychologists_by_country):
    # Plot bar chart of psychologists by country
    plt.figure(figsize=(10,6))
    sns.barplot(x='Country', y='Number of Psychologists', data=psychologists_by_country)
    plt.title('Psychologists by Country')
    plt.xlabel('Country')
    plt.ylabel('Number of Psychologists')
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig('psychologists_by_country.png')
    
    # Plot pie chart of course and seminar distribution
    course_seminar_distribution = [data['course_id'].nunique(), data['seminar_id'].nunique()]
    labels = ['Courses', 'Seminars']
    plt.figure(figsize=(8,8))
    plt.pie(course_seminar_distribution, labels=labels, autopct='%1.1f%%')
    plt.title('Course and Seminar Distribution')
    plt.savefig('course_seminar_distribution.png')

# Main function
def main():
    file_path = 'psychologists_participation.csv'  # replace with actual file path
    data = load_data(file_path)
    
    if data is not None:
        total_psychologists, psychologists_by_country, total_courses, total_seminars = analyze_participation(data)
        
        print(f'Total Psychologists: {total_psychologists}')
        print(psychologists_by_country)
        print(f'Total Courses: {total_courses}')
        print(f'Total Seminars: {total_seminars}')
        
        visualize_participation(data, psychologists_by_country)

if __name__ == "__main__":
    main()
```

```sql
-- psychologists_participation.sql

CREATE TABLE psychologists (
    psychologist_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE seminars (
    seminar_id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE partnerships (
    partnership_id INT PRIMARY KEY,
    psychologist_id INT,
    course_id INT,
    seminar_id INT,
    country VARCHAR(255) NOT NULL,
    FOREIGN KEY (psychologist_id) REFERENCES psychologists(psychologist_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (seminar_id) REFERENCES seminars(seminar_id)
);

-- Insert sample data
INSERT INTO psychologists (psychologist_id, name)
VALUES
(1, 'John Doe'),
(2, 'Jane Smith'),
(3, 'Bob Johnson');

INSERT INTO courses (course_id, name)
VALUES
(1, 'Course 1'),
(2, 'Course 2'),
(3, 'Course 3');

INSERT INTO seminars (seminar_id, name)
VALUES
(1, 'Seminar 1'),
(2, 'Seminar 2'),
(3, 'Seminar 3');

INSERT INTO partnerships (partnership_id, psychologist_id, course_id, seminar_id, country)
VALUES
(1, 1, 1, 1, 'USA'),
(2, 1, 2, 2, 'Canada'),
(3, 2, 1, 3, 'Mexico'),
(4, 3, 3, 1, 'USA'),
(5, 1, 3, 2, 'Canada');
```

```csv
# psychologists_participation.csv

psychologist_id,course_id,seminar_id,country
1,1,1,USA
1,2,2,Canada
2,1,3,Mexico
3,3,1,USA
1,3,2,Canada
```
