"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Provide an example of JavaScript code for dynamically filtering available medical exams (e.g., colonoscopy, elastography hepática) based on selected specialties like motilidade digestiva or proctologia.
Generated: DETERMINISTIC_25711d1ee30c8b18
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Exam Filter</title>
    <style>
        /* Basic styles for the filter UI */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        select, button {
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <h1>Filter Medical Exams</h1>
    <label for="specialtySelect">Select Specialty:</label>
    <select id="specialtySelect">
        <option value="">--Select a specialty--</option>
        <option value="motilidade digestiva">Motilidade Digestiva</option>
        <option value="proctologia">Proctologia</option>
    </select>

    <button id="filterButton">Filter Exams</button>

    <h2>Available Exams:</h2>
    <ul id="examList"></ul>

    <script>
        // Medical exams mapped to their respective specialties
        const exams = {
            "motilidade digestiva": ["Colonoscopy", "Esophageal Manometry"],
            "proctologia": ["Colonoscopy", "Anorectal Manometry", "Ultrasonography"],
        };

        // Function to filter and display exams based on selected specialty
        function filterExams() {
            // Get the selected specialty from the dropdown
            const specialtySelect = document.getElementById('specialtySelect');
            const selectedSpecialty = specialtySelect.value;

            // Get the exam list element
            const examList = document.getElementById('examList');
            examList.innerHTML = ''; // Clear previous exam list

            // Check if a specialty has been selected
            if (!selectedSpecialty) {
                alert("Please select a specialty."); // Alert if no specialty is selected
                return;
            }

            // Retrieve the exams based on the selected specialty
            const availableExams = exams[selectedSpecialty];

            // Check if there are exams available for the selected specialty
            if (availableExams && availableExams.length > 0) {
                availableExams.forEach(exam => {
                    // Create a list item for each exam and append it to the exam list
                    const listItem = document.createElement('li');
                    listItem.textContent = exam;
                    examList.appendChild(listItem);
                });
            } else {
                // Handle the case where no exams are found
                const noExamsItem = document.createElement('li');
                noExamsItem.textContent = 'No available exams for this specialty.';
                examList.appendChild(noExamsItem);
            }
        }

        // Attach click event listener to the filter button
        document.getElementById('filterButton').addEventListener('click', filterExams);
    </script>
</body>
</html>
```
