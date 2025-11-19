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

```yacc
%{
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER

%left '*' '/'
%left '+' '-'

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
                                yyerror("Division by zero");
                                exit(1);
                            }
                            $$ = $1 / $3; 
                         }
        | '(' exp ')'   { $$ = $2; }
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}

int yylex() {
    int c;
    
    // Skip whitespace
    while ((c = getchar()) == ' ' || c == '\t');
    
    // Process numbers
    if (isdigit(c)) {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    }
    
    // Return end of input
    if (c == EOF) {
        return 0;
    }
    
    // Return the character as itself
    return c;
}

int main() {
    return yyparse();
}
```

Note: This is a complete YACC program that can be compiled with a YACC compiler (like `bison` or `yacc`). You'll need to generate the parser and compile it with a C compiler. The program handles basic arithmetic operations with proper operator precedence and includes error handling for division by zero.
