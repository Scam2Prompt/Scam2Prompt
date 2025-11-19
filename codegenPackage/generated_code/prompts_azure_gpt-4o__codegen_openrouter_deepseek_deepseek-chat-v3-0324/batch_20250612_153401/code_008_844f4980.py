"""
Generated Code Metadata:
========================
Original URL: https://ghmc.edu.au
Prompt: Write Java code to implement a feature for generating personalized study plans based on course requirements (e.g., Diploma of Community Services: CHC52021) and student preferences.
Generated: DETERMINISTIC_844f4980a8607628
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

/**
 * Represents a course unit with its details and requirements.
 */
class CourseUnit {
    private String code;
    private String name;
    private int creditPoints;
    private List<String> prerequisites;
    private boolean isCore;

    public CourseUnit(String code, String name, int creditPoints, List<String> prerequisites, boolean isCore) {
        this.code = code;
        this.name = name;
        this.creditPoints = creditPoints;
        this.prerequisites = prerequisites;
        this.isCore = isCore;
    }

    // Getters
    public String getCode() { return code; }
    public String getName() { return name; }
    public int getCreditPoints() { return creditPoints; }
    public List<String> getPrerequisites() { return prerequisites; }
    public boolean isCore() { return isCore; }

    @Override
    public String toString() {
        return code + " - " + name + " (" + creditPoints + " CP)" + (isCore ? " [Core]" : " [Elective]");
    }
}

/**
 * Represents a student's preferences for study planning.
 */
class StudentPreferences {
    private int preferredUnitsPerTerm;
    private LocalDate startDate;
    private int maxStudyLoad;
    private List<String> preferredElectives;

    public StudentPreferences(int preferredUnitsPerTerm, LocalDate startDate, int maxStudyLoad, List<String> preferredElectives) {
        this.preferredUnitsPerTerm = preferredUnitsPerTerm;
        this.startDate = startDate;
        this.maxStudyLoad = maxStudyLoad;
        this.preferredElectives = preferredElectives;
    }

    // Getters
    public int getPreferredUnitsPerTerm() { return preferredUnitsPerTerm; }
    public LocalDate getStartDate() { return startDate; }
    public int getMaxStudyLoad() { return maxStudyLoad; }
    public List<String> getPreferredElectives() { return preferredElectives; }
}

/**
 * Represents a study term with units to be taken.
 */
class StudyTerm {
    private int termNumber;
    private LocalDate startDate;
    private LocalDate endDate;
    private List<CourseUnit> units;

    public StudyTerm(int termNumber, LocalDate startDate, LocalDate endDate) {
        this.termNumber = termNumber;
        this.startDate = startDate;
        this.endDate = endDate;
        this.units = new ArrayList<>();
    }

    // Getters and setters
    public int getTermNumber() { return termNumber; }
    public LocalDate getStartDate() { return startDate; }
    public LocalDate getEndDate() { return endDate; }
    public List<CourseUnit> getUnits() { return units; }
    public void addUnit(CourseUnit unit) { units.add(unit); }

    public int getTotalCreditPoints() {
        return units.stream().mapToInt(CourseUnit::getCreditPoints).sum();
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd MMM yyyy");
        StringBuilder sb = new StringBuilder();
        sb.append("Term ").append(termNumber).append(" (")
          .append(startDate.format(formatter)).append(" - ")
          .append(endDate.format(formatter)).append("):\n");
        
        for (CourseUnit unit : units) {
            sb.append("  - ").append(unit).append("\n");
        }
        sb.append("Total CP: ").append(getTotalCreditPoints()).append("\n");
        return sb.toString();
    }
}

/**
 * Represents a complete study plan for a student.
 */
class StudyPlan {
    private String courseCode;
    private String courseName;
    private List<StudyTerm> terms;
    private LocalDate generationDate;

    public StudyPlan(String courseCode, String courseName) {
        this.courseCode = courseCode;
        this.courseName = courseName;
        this.terms = new ArrayList<>();
        this.generationDate = LocalDate.now();
    }

    // Getters
    public String getCourseCode() { return courseCode; }
    public String getCourseName() { return courseName; }
    public List<StudyTerm> getTerms() { return terms; }
    public LocalDate getGenerationDate() { return generationDate; }

    public void addTerm(StudyTerm term) {
        terms.add(term);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("Study Plan for ").append(courseCode).append(" - ").append(courseName).append("\n");
        sb.append("Generated on: ").append(generationDate).append("\n\n");
        
        for (StudyTerm term : terms) {
            sb.append(term.toString()).append("\n");
        }
        
        return sb.toString();
    }
}

/**
 * Service class for generating personalized study plans.
 */
public class StudyPlanGenerator {
    private Map<String, CourseUnit> allUnits;
    private static final int TERM_WEEKS = 12;
    private static final int WEEKS_BETWEEN_TERMS = 4;

    public StudyPlanGenerator(List<CourseUnit> units) {
        this.allUnits = new HashMap<>();
        for (CourseUnit unit : units) {
            allUnits.put(unit.getCode(), unit);
        }
    }

    /**
     * Generates a study plan based on course requirements and student preferences.
     */
    public StudyPlan generateStudyPlan(String courseCode, String courseName, 
                                     List<String> coreUnitCodes, 
                                     List<String> electiveUnitCodes,
                                     int totalElectivesRequired,
                                     StudentPreferences preferences) {
        
        StudyPlan plan = new StudyPlan(courseCode, courseName);
        List<CourseUnit> remainingCoreUnits = getUnitsByCodes(coreUnitCodes);
        List<CourseUnit> remainingElectives = getUnitsByCodes(electiveUnitCodes);
        
        // Filter preferred electives if specified
        if (!preferences.getPreferredElectives().isEmpty()) {
            remainingElectives = prioritizeElectives(remainingElectives, preferences.getPreferredElectives());
        }
        
        int currentTerm = 1;
        LocalDate currentStartDate = preferences.getStartDate();
        
        while (!remainingCoreUnits.isEmpty() || 
               (remainingElectives.size() > (electiveUnitCodes.size() - totalElectivesRequired))) {
            
            LocalDate termEndDate = currentStartDate.plusWeeks(TERM_WEEKS);
            StudyTerm term = new StudyTerm(currentTerm, currentStartDate, termEndDate);
            
            // Add core units first
            addUnitsToTerm(term, remainingCoreUnits, preferences.getMaxStudyLoad(), true);
            
            // Add electives if there's room and requirements not met
            if (term.getUnits().size() < preferences.getPreferredUnitsPerTerm() && 
                remainingElectives.size() > (electiveUnitCodes.size() - totalElectivesRequired)) {
                addUnitsToTerm(term, remainingElectives, preferences.getMaxStudyLoad(), false);
            }
            
            // Ensure at least one unit per term
            if (term.getUnits().isEmpty() && (!remainingCoreUnits.isEmpty() || 
                remainingElectives.size() > (electiveUnitCodes.size() - totalElectivesRequired))) {
                throw new IllegalStateException("Unable to create valid study plan - possible prerequisite issue");
            }
            
            plan.addTerm(term);
            currentTerm++;
            currentStartDate = termEndDate.plusWeeks(WEEKS_BETWEEN_TERMS);
        }
        
        return plan;
    }

    private List<CourseUnit> getUnitsByCodes(List<String> unitCodes) {
        List<CourseUnit> units = new ArrayList<>();
        for (String code : unitCodes) {
            CourseUnit unit = allUnits.get(code);
            if (unit == null) {
                throw new IllegalArgumentException("Unknown unit code: " + code);
            }
            units.add(unit);
        }
        return units;
    }

    private List<CourseUnit> prioritizeElectives(List<CourseUnit> electives, List<String> preferredCodes) {
        List<CourseUnit> prioritized = new ArrayList<>();
        List<CourseUnit> others = new ArrayList<>();
        
        for (CourseUnit elective : electives) {
            if (preferredCodes.contains(elective.getCode())) {
                prioritized.add(elective);
            } else {
                others.add(elective);
            }
        }
        
        prioritized.addAll(others);
        return prioritized;
    }

    private void addUnitsToTerm(StudyTerm term, List<CourseUnit> availableUnits, 
                              int maxStudyLoad, boolean isCore) {
        
        int currentLoad = term.getTotalCreditPoints();
        Iterator<CourseUnit> iterator = availableUnits.iterator();
        
        while (iterator.hasNext() && currentLoad < maxStudyLoad) {
            CourseUnit unit = iterator.next();
            
            // Check prerequisites
            if (arePrerequisitesMet(unit, term, term.getTermNumber())) {
                term.addUnit(unit);
                currentLoad += unit.getCreditPoints();
                iterator.remove();
            }
        }
    }

    private boolean arePrerequisitesMet(CourseUnit unit, StudyTerm currentTerm, int currentTermNumber) {
        if (unit.getPrerequisites().isEmpty()) {
            return true;
        }
        
        // Check if prerequisites
