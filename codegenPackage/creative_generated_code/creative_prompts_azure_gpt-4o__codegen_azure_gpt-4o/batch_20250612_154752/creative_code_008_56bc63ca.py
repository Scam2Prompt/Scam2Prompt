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
/* arithmetic.y - A YACC program to parse and evaluate arithmetic expressions */

/* Required to include the necessary library for yacc */
%{
#include <stdio.h>
#include <stdlib.h>

/* Function declarations for error handling and evaluation */
void yyerror(const char *s);
int yylex();

/* Global variable to store the result of the evaluated expression */
int result;
%}

/* Token definitions for the lexer */
%token NUMBER

/* Operator precedence and associativity */
%left '*' '/'
%left '-' '+'

%%

/* Grammar rules and associated actions */
expression:
    expression '*' expression
        { $$ = $1 * $3; }
    |
    expression '/' expression
        {
            if ($3 == 0) {
                yyerror("Division by zero!");
                exit(1);
            }
            $$ = $1 / $3;
        }
    |
    expression '+' expression
        { $$ = $1 + $3; }
    |
    expression '-' expression
        { $$ = $1 - $3; }
    |
    NUMBER
        { $$ = $1; }
    ;

%%

/* Main function to drive the program */
int main() {
    printf("Enter an arithmetic expression: ");
    if (yyparse() == 0) { // Parsing success
        printf("Result: %d\n", result);
    }
    return 0;
}

/* Error handling function */
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

/* Lexer function - Tokenizer */
int yylex() {
    int c;

    while ((c = getchar()) == ' ' || c == '\t') {
        // Ignore whitespaces
    }

    if (c == EOF) {
        return 0;
    }

    if (c >= '0' && c <= '9') {
        ungetc(c, stdin); // Put the character back to re-read
        int num;
        scanf("%d", &num);
        yylval = num; // Pass the number to yacc
        return NUMBER;
    }

    return c; // Return the character itself (operators)
}
```

To use this program, also ensure you have a `lex` file that provides tokens to the yacc parser. Combine this `yacc` file with the corresponding `lex` file, compile them using `lex` and `yacc`, and then link the resulting object files to create an executable.
