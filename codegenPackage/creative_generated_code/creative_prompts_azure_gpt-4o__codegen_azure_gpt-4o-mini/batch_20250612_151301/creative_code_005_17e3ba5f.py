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
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selecionar Exames e Especialidades</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        label {
            display: block;
            margin-bottom: 10px;
        }
        select {
            padding: 10px;
            font-size: 16px;
            margin-bottom: 20px;
        }
    </style>
</head>
<body>

    <h1>Selecione seu Exame e Especialidade</h1>

    <form id="exam-specialty-form">
        <!-- Dropdown for selecting medical exams -->
        <label for="medical-exams">Exames:</label>
        <select id="medical-exams" name="medical-exams" required>
            <option value="">Selecione um exame...</option>
            <option value="ecoendoscopia-baixa">Ecoendoscopia Baixa</option>
            <option value="teste-intolerancia-lactose">Teste de Intolerância à Lactose</option>
            <!-- Add more exams as needed -->
        </select>

        <!-- Dropdown for selecting specialties -->
        <label for="specialties">Especialidades:</label>
        <select id="specialties" name="specialties" required>
            <option value="">Selecione uma especialidade...</option>
            <option value="nutricao">Nutrição</option>
            <option value="hepatologia">Hepatologia</option>
            <!-- Add more specialties as needed -->
        </select>

        <!-- Submit button -->
        <button type="submit">Enviar</button>
    </form>

    <script>
        // Function to handle form submission
        document.getElementById('exam-specialty-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Retrieve selected values
            const selectedExam = document.getElementById('medical-exams').value;
            const selectedSpecialty = document.getElementById('specialties').value;

            // Basic validation to ensure selections are made
            if (!selectedExam || !selectedSpecialty) {
                alert('Por favor, selecione um exame e uma especialidade.');
                return;
            }

            // Here you can handle the selected values as needed
            console.log(`Exame selecionado: ${selectedExam}`);
            console.log(`Especialidade selecionada: ${selectedSpecialty}`);

            // Example of sending data to a server (replace with actual endpoint)
            // const xhr = new XMLHttpRequest();
            // xhr.open('POST', 'your-server-endpoint', true);
            // xhr.setRequestHeader('Content-Type', 'application/json');
            // xhr.onload = function() {
            //     if (xhr.status === 200) {
            //         alert('Dados enviados com sucesso!');
            //     } else {
            //         alert('Erro ao enviar dados. Tente novamente.');
            //     }
            // };
            // xhr.send(JSON.stringify({ exam: selectedExam, specialty: selectedSpecialty }));
        });
    </script>

</body>
</html>
```
