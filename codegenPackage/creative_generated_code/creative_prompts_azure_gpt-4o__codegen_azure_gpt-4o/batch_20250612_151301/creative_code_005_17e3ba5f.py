"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gastrolife.net
Prompt: Write code to generate a dropdown menu for selecting medical exams (e.g., ecoendoscopia baixa, teste de intolerância à lactose) and specialties (e.g., nutrição, hepatologia) as described on the Gastrolife website.
Generated: DETERMINISTIC_17e3ba5f13a189d3
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
  <title>Medical Exams and Specialties Dropdown</title>
  <!-- Include basic styling for dropdowns -->
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    label {
      font-weight: bold;
      display: block;
      margin-bottom: 5px;
    }
    select {
      width: 100%;
      padding: 8px;
      margin-bottom: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  </style>
</head>
<body>
  <h1>Select Medical Exams and Specialties</h1>

  <!-- Dropdown for medical exams -->
  <label for="medical-exams">Medical Exams:</label>
  <select id="medical-exams">
    <option value="" disabled selected>Choose an exam</option>
    <option value="ecoendoscopia-baixa">Ecoendoscopia Baixa</option>
    <option value="teste-intolerancia-lactose">Teste de Intolerância à Lactose</option>
    <option value="colonoscopia">Colonoscopia</option>
    <option value="endoscopia-digestiva">Endoscopia Digestiva</option>
    <option value="ultrassom-abdominal">Ultrassom Abdominal</option>
    <!-- Add more options as needed -->
  </select>

  <!-- Dropdown for specialties -->
  <label for="specialties">Specialties:</label>
  <select id="specialties">
    <option value="" disabled selected>Choose a specialty</option>
    <option value="nutricao">Nutrição</option>
    <option value="hepatologia">Hepatologia</option>
    <option value="gastroenterologia">Gastroenterologia</option>
    <option value="endocrinologia">Endocrinologia</option>
    <option value="pediatria">Pediatria</option>
    <!-- Add more options as needed -->
  </select>

  <!-- JavaScript for basic validation -->
  <script>
    // Add event listeners to ensure a selection is made
    document.getElementById('medical-exams').addEventListener('change', function() {
      console.log(`Selected Exam: ${this.value}`);
    });

    document.getElementById('specialties').addEventListener('change', function() {
      console.log(`Selected Specialty: ${this.value}`);
    });
  </script>
</body>
</html>
```
