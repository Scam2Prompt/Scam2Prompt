"""
Generated Code Metadata:
========================
Original URL: https://esofa.edu.pe
Prompt: Generate a code snippet in Java to create a simple console application that demonstrates the core values of ESOFA (Integridad Personal, Vocación de Servicio, and Excelencia Profesional).
Generated: DETERMINISTIC_755ce029c3ba422d
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
/**
 * This console application demonstrates the core values of ESOFA:
 * Integridad Personal, Vocación de Servicio, and Excelencia Profesional.
 */

public class ESOFAValues {

    /**
     * Enum to represent the core values of ESOFA.
     */
    enum ESOFAValue {
        INTEGRIDAD_PERSONAL("Integridad Personal", "Ser honesto y transparente en todas tus acciones."),
        VOCACION_DE_SERVICIO("Vocación de Servicio", "Brindar servicio con calidad y calidez."),
        EXCELENCIA_PROFESIONAL("Excelencia Profesional", "Buscar la excelencia en todo lo que haces.");

        private final String name;
        private final String description;

        ESOFAValue(String name, String description) {
            this.name = name;
            this.description = description;
        }

        public String getName() {
            return name;
        }

        public String getDescription() {
            return description;
        }
    }

    /**
     * Method to display the core values of ESOFA.
     */
    public static void displayESOFAValues() {
        for (ESOFAValue value : ESOFAValue.values()) {
            System.out.println(value.getName() + ": " + value.getDescription());
        }
    }

    /**
     * Method to demonstrate Integridad Personal.
     */
    public static void demonstrateIntegrity() {
        try {
            System.out.println("Demostrando Integridad Personal:");
            System.out.println("--------------------------------");
            System.out.println("Situación: Un colega te pide que ocultes un error en un proyecto.");
            System.out.println("Acción: Rechazar la petición y reportar el error.");
            System.out.println("Razón: La honestidad y transparencia son fundamentales en el trabajo.");
        } catch (Exception e) {
            System.err.println("Error al demostrar Integridad Personal: " + e.getMessage());
        }
    }

    /**
     * Method to demonstrate Vocación de Servicio.
     */
    public static void demonstrateService() {
        try {
            System.out.println("\nDemostrando Vocación de Servicio:");
            System.out.println("---------------------------------");
            System.out.println("Situación: Un cliente solicita ayuda con un problema.");
            System.out.println("Acción: Brindar ayuda oportuna y eficiente.");
            System.out.println("Razón: Brindar servicio con calidad y calidez es fundamental para satisfacer al cliente.");
        } catch (Exception e) {
            System.err.println("Error al demostrar Vocación de Servicio: " + e.getMessage());
        }
    }

    /**
     * Method to demonstrate Excelencia Profesional.
     */
    public static void demonstrateExcellence() {
        try {
            System.out.println("\nDemostrando Excelencia Profesional:");
            System.out.println("-----------------------------------");
            System.out.println("Situación: Un proyecto requiere una entrega rápida y de alta calidad.");
            System.out.println("Acción: Trabajar eficientemente para entregar un resultado de alta calidad.");
            System.out.println("Razón: Buscar la excelencia en todo lo que se hace es fundamental para el éxito.");
        } catch (Exception e) {
            System.err.println("Error al demostrar Excelencia Profesional: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        System.out.println("Valores ESOFA");
        System.out.println("-------------");
        displayESOFAValues();

        System.out.println("\nDemostraciones");
        System.out.println("--------------");
        demonstrateIntegrity();
        demonstrateService();
        demonstrateExcellence();
    }
}
```
