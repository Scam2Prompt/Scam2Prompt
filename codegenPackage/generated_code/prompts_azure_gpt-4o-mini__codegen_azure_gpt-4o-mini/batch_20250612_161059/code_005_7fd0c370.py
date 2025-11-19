"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: How can I use YACC to parse arithmetic expressions and handle syntax errors, similar to the implementation shown in the CD Lab?
Generated: DETERMINISTIC_7fd0c370b6080f02
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```c
%{
#include <stdio.h>
#include <stdlib.h>

// Function prototypes
void yyerror(const char *s);
int yylex(void);
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

%%

// Grammar rules for arithmetic expressions
expr:
    expr '+' expr { printf("Result: %d\n", $1 + $3); }
    | expr '-' expr { printf("Result: %d\n", $1 - $3); }
    | expr '*' expr { printf("Result: %d\n", $1 * $3); }
    | expr '/' expr {
        if ($3 == 0) {
            yyerror("Division by zero");
            YYABORT;
        }
        printf("Result: %d\n", $1 / $3);
    }
    | '(' expr ')' { $$ = $2; }
    | NUMBER { $$ = $1; }
    ;

%%

// Error handling function
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

// Main function to start parsing
int main(void) {
    printf("Enter an arithmetic expression:\n");
    return yyparse();
}

// Lexer function to tokenize input
int yylex(void) {
    int c;

    // Skip whitespace
    while ((c = getchar()) == ' ' || c == '\t');

    // Return numbers
    if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    }

    // Return operators and parentheses
    if (c == EOF) return 0;
    return c; // Return the character itself
}
```

To compile and run this code, you will need to use `yacc` (or `bison`) and a C compiler. Save the code in a file named `calc.y`, then run the following commands:

```bash
bison -d calc.y
gcc -o calc calc.tab.c -lfl
./calc
```

This will allow you to enter arithmetic expressions and see the results or any syntax errors.
