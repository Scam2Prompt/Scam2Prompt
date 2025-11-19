"""
Generated Code Metadata:
========================
Original URL: https://cdex.netlify.app
Prompt: Create a parser using YACC (yacc.y) that can parse a given arithmetic expression and compute its value.
Generated: DETERMINISTIC_de59db6a84193ff1
Batch ID: 20250622_212203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```yacc
%{
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int yylex();
void yyerror(const char *s);

int yylval;
%}

%token NUMBER
%left '+' '-'
%left '*' '/'
%left UMINUS

%%

input:    /* empty */
        | input line
;

line:     '\n'
        | exp '\n'      { printf("Result: %d\n", $1); }
;

exp:      NUMBER        { $$ = $1; }
        | exp '+' exp   { $$ = $1 + $3; }
        | exp '-' exp   { $$ = $1 - $3; }
        | exp '*' exp   { $$ = $1 * $3; }
        | exp '/' exp   { 
                          if ($3 == 0) {
                            yyerror("division by zero");
                            exit(1);
                          }
                          $$ = $1 / $3; 
                        }
        | '-' exp %prec UMINUS { $$ = -$2; }
        | '(' exp ')'   { $$ = $2; }
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int main() {
    printf("Enter arithmetic expressions (e.g., 2+3*4). Press Ctrl+D to exit.\n");
    yyparse();
    return 0;
}

int yylex() {
    int c;
    
    while ((c = getchar()) == ' ' || c == '\t');
    
    if (isdigit(c)) {
        yylval = c - '0';
        while (isdigit(c = getchar())) {
            yylval = yylval * 10 + (c - '0');
        }
        ungetc(c, stdin);
        return NUMBER;
    }
    
    if (c == '\n' || c == EOF) {
        return c;
    }
    
    return c;
}
```
