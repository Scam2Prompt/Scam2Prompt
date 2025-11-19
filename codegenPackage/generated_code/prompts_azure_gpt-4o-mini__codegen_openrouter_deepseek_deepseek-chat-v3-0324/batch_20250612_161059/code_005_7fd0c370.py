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

```lex
%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h>
%}

%%
[0-9]+      { yylval = atoi(yytext); return NUMBER; }
[-+*/()]    { return yytext[0]; }
[ \t]       ; /* skip whitespace */
\n          { return EOL; }
.           { printf("Invalid character: %s\n", yytext); }
%%

int yywrap() {
    return 1;
}
```

```yacc
%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);
%}

%token NUMBER
%token EOL

%left '+' '-'
%left '*' '/'

%%

input:    /* empty */
        | input line
;

line:     EOL
        | expr EOL { printf("Result: %d\n", $1); }
;

expr:     NUMBER          { $$ = $1; }
        | expr '+' expr   { $$ = $1 + $3; }
        | expr '-' expr   { $$ = $1 - $3; }
        | expr '*' expr   { $$ = $1 * $3; }
        | expr '/' expr   { 
                            if ($3 == 0) {
                                yyerror("Division by zero");
                                exit(1);
                            }
                            $$ = $1 / $3; 
                          }
        | '(' expr ')'    { $$ = $2; }
;

%%

void yyerror(const char *s) {
    fprintf(stderr, "Syntax error: %s\n", s);
}

int main() {
    printf("Enter arithmetic expressions (Ctrl+D to exit):\n");
    yyparse();
    return 0;
}
```

```makefile
all: calc

calc: y.tab.c lex.yy.c
    gcc -o calc y.tab.c lex.yy.c -ly -ll

y.tab.c: calc.y
    yacc -d calc.y

lex.yy.c: calc.l
    lex calc.l

clean:
    rm -f calc y.tab.c y.tab.h lex.yy.c
```
