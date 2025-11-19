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
/* 
 * YACC program to parse arithmetic expressions and handle syntax errors.
 * This program supports addition, subtraction, multiplication, and division.
 * It also includes error handling for invalid syntax.
 */

%{
#include <stdio.h>
#include <stdlib.h>

/* Function declarations */
void yyerror(const char *s);
int yylex();
%}

/* Tokens */
%token NUMBER
%left '+' '-'
%left '*' '/'
%right UMINUS

/* Grammar rules */
%%
input:
    /* Empty input */
    | input line
;

line:
    '\n' /* Ignore empty lines */
    | expr '\n' { printf("Result: %d\n", $1); }
;

expr:
    NUMBER { $$ = $1; }
    | expr '+' expr { $$ = $1 + $3; }
    | expr '-' expr { $$ = $1 - $3; }
    | expr '*' expr { $$ = $1 * $3; }
    | expr '/' expr {
        if ($3 == 0) {
            yyerror("Division by zero");
            $$ = 0;
        } else {
            $$ = $1 / $3;
        }
    }
    | '-' expr %prec UMINUS { $$ = -$2; }
    | '(' expr ')' { $$ = $2; }
;

%%

/* Error handling function */
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

/* Main function */
int main() {
    printf("Enter arithmetic expressions (Ctrl+D to exit):\n");
    yyparse();
    return 0;
}

/* Lexer implementation */
#include <ctype.h>

int yylex() {
    int c;

    /* Skip whitespace */
    while ((c = getchar()) == ' ' || c == '\t');

    /* Return numbers */
    if (isdigit(c)) {
        ungetc(c, stdin);
        int num;
        scanf("%d", &num);
        return NUMBER;
    }

    /* Return operators and parentheses */
    if (c == '+' || c == '-' || c == '*' || c == '/' || c == '(' || c == ')') {
        return c;
    }

    /* End of input */
    if (c == '\n' || c == EOF) {
        return c;
    }

    /* Invalid character */
    yyerror("Invalid character");
    return 0;
}
```

To compile and run this program:
1. Save the code in a file named `parser.y`.
2. Use `yacc` to generate the parser: `yacc -d parser.y`.
3. Use `lex` to generate the lexer: Create a corresponding `lexer.l` file if needed.
4. Compile the generated files with `gcc`: `gcc y.tab.c -o parser`.
5. Run the program: `./parser`.
