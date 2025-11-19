"""
Generated Code Metadata:
========================
Original URL: https://gastrolife.net
Prompt: Write code to generate a dropdown menu for selecting medical exams (e.g., ecoendoscopia baixa, teste de intolerância à lactose) and specialties (e.g., nutrição, hepatologia) as described on the Gastrolife website.
Generated: DETERMINISTIC_17e3ba5f13a189d3
Batch ID: 20250612_151301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gastrolife - Agendamento de Exames</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        select, button {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #3498db;
            color: white;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Agendamento de Exames</h1>
        
        <div class="form-group">
            <label for="specialty">Especialidade:</label>
            <select id="specialty" name="specialty">
                <option value="">Selecione uma especialidade</option>
                <option value="nutricao">Nutrição</option>
                <option value="hepatologia">Hepatologia</option>
                <option value="gastroenterologia">Gastroenterologia</option>
                <option value="endoscopia">Endoscopia</option>
                <option value="coloproctologia">Coloproctologia</option>
            </select>
        </div>

        <div class="form-group">
            <label for="exam">Exame:</label>
            <select id="exam" name="exam" disabled>
                <option value="">Selecione um exame</option>
                <!-- Exams will be populated dynamically -->
            </select>
        </div>

        <button id="submitBtn" disabled>Agendar Exame</button>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const specialtySelect = document.getElementById('specialty');
            const examSelect = document.getElementById('exam');
            const submitBtn = document.getElementById('submitBtn');

            // Exams data structure
            const examsBySpecialty = {
                'nutricao': [
                    { value: 'teste_intolerancia_lactose', label: 'Teste de Intolerância à Lactose' },
                    { value: 'teste_intolerancia_gluten', label: 'Teste de Intolerância ao Glúten' },
                    { value: 'avaliacao_nutricional', label: 'Avaliação Nutricional' }
                ],
                'hepatologia': [
                    { value: 'elastografia_hepatica', label: 'Elastografia Hepática' },
                    { value: 'biopsia_hepatica', label: 'Biópsia Hepática' },
                    { value: 'teste_fibrose_hepatica', label: 'Teste de Fibrose Hepática' }
                ],
                'gastroenterologia': [
                    { value: 'endoscopia_alta', label: 'Endoscopia Digestiva Alta' },
                    { value: 'colonoscopia', label: 'Colonoscopia' },
                    { value: 'manometria_esofagica', label: 'Manometria Esofágica' }
                ],
                'endoscopia': [
                    { value: 'ecoendoscopia_alta', label: 'Ecoendoscopia Alta' },
                    { value: 'ecoendoscopia_baixa', label: 'Ecoendoscopia Baixa' },
                    { value: 'cpre', label: 'CPRE (Colangiopancreatografia Retrógrada Endoscópica)' }
                ],
                'coloproctologia': [
                    { value: 'anuscopia', label: 'Anuscopia' },
                    { value: 'retossigmoidoscopia', label: 'Retossigmoidoscopia' },
                    { value: 'teste_balloon_expulsion', label: 'Teste Balloon Expulsion' }
                ]
            };

            // Handle specialty selection change
            specialtySelect.addEventListener('change', function() {
                const selectedSpecialty = this.value;
                
                // Reset exam dropdown
                examSelect.innerHTML = '<option value="">Selecione um exame</option>';
                examSelect.disabled = !selectedSpecialty;
                submitBtn.disabled = true;
                
                if (selectedSpecialty) {
                    // Populate exams based on selected specialty
                    examsBySpecialty[selectedSpecialty].forEach(exam => {
                        const option = document.createElement('option');
                        option.value = exam.value;
                        option.textContent = exam.label;
                        examSelect.appendChild(option);
                    });
                }
            });

            // Handle exam selection change
            examSelect.addEventListener('change', function() {
                submitBtn.disabled = !this.value;
            });

            // Handle form submission
            submitBtn.addEventListener('click', function() {
                const specialty = specialtySelect.options[specialtySelect.selectedIndex].text;
                const exam = examSelect.options[examSelect.selectedIndex].text;
                
                alert(`Exame agendado com sucesso!\n\nEspecialidade: ${specialty}\nExame: ${exam}`);
            });
        });
    </script>
</body>
</html>
```
