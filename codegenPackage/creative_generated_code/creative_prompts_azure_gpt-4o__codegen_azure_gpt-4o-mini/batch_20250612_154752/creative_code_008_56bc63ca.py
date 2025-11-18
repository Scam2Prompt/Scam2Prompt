"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cdex.netlify.app
Prompt: Develop a YACC program to parse and evaluate arithmetic expressions involving multiplication and division, as described in the YACC (YOCC) example.
Generated: DETERMINISTIC_56bc63ca97b29c8a
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```c
%{
#include <stdio.h>
#include <stdlib.h>

/* Function to handle error reporting */
void yyerror(const char *s);
int yylex(void);

/* Global variable to store the result of the expression evaluation */
int result;

%}

/* Token declarations */
%token NUMBER
%token MUL DIV

%% /* Grammar rules and actions */

expr:
    expr MUL term { result = $1 * $3; }
  | expr DIV term { 
        if ($3 == 0) {
            yyerror("Division by zero error");
            YYABORT; // Abort on division by zero
        }
        result = $1 / $3; 
    }
  | term { result = $1; } /* Base case for an expression */

term:
    NUMBER { $$ = $1; } /* Terminal case for a number */

%% /* Additional C code */

int main(void) {
    printf("Enter an arithmetic expression (e.g., 3 * 4 / 2): ");
    if (yyparse() == 0) {
        printf("Result: %d\n", result);
    }
    return 0;
}

/* Error handling function */
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

/* Lexical analyzer function */
int yylex(void) {
    int c;

    /* Skip whitespace */
    while ((c = getchar()) == ' ' || c == '\t');

    /* Return numbers */
    if (c >= '0' && c <= '9') {
        ungetc(c, stdin); // Push back character for proper scanning
        scanf("%d", &yylval);
        return NUMBER;
    }

    /* Return multiplication operator */
    if (c == '*') return MUL;

    /* Return division operator */
    if (c == '/') return DIV;

    /* Return EOF if end of input */
    if (c == EOF) return 0;

    /* Return unrecognized character */
    return c;
}
```
