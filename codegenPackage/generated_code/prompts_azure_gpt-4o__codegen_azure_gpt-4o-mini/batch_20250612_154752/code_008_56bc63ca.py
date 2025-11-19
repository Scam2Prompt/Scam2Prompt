"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Develop a YACC program to parse and evaluate arithmetic expressions involving multiplication and division, as described in the YACC (YOCC) example.
Generated: DETERMINISTIC_56bc63ca97b29c8a
Batch ID: 20250612_154752
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
int yylex(void);
void yyerror(const char *s);
%}

%token NUMBER
%left '+' '-'
%left '*' '/'

// Grammar rules
%%
expression:
    expression '+' expression { $$ = $1 + $3; }
    | expression '-' expression { $$ = $1 - $3; }
    | expression '*' expression { $$ = $1 * $3; }
    | expression '/' expression {
        if ($3 == 0) {
            yyerror("Division by zero");
            YYABORT;
        }
        $$ = $1 / $3;
    }
    | '(' expression ')' { $$ = $2; }
    | NUMBER { $$ = $1; }
    ;

%%

// Error handling function
void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

// Main function
int main(void) {
    printf("Enter an arithmetic expression: ");
    if (yyparse() == 0) {
        printf("Expression evaluated successfully.\n");
    } else {
        fprintf(stderr, "Failed to evaluate expression.\n");
    }
    return 0;
}
```

```lex
%{
#include "y.tab.h"
%}

%%

// Match numbers
[0-9]+  { yylval = atoi(yytext); return NUMBER; }

// Match operators and parentheses
[+\-*/()] { return yytext[0]; }

// Ignore whitespace
[ \t\n]  { /* ignore whitespace */ }

// Handle invalid characters
.        { yyerror("Invalid character"); }

%%

// Main function for the lexer
int main(void) {
    yylex();
    return 0;
}
```
