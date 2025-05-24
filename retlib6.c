#include <stdlib.h>
#include <stdio.h>
#include <string.h>
/* Changing this size will change the layout of the stack.
* Instructors can change this value each year, so students
* won’t be able to use the solutions from the past.
* Suggested value: between 0 and 200 (cannot exceed 300, or
* the program won’t have a buffer-overflow problem). */
#ifndef BUF_SIZE
#define BUF_SIZE 12
#endif
void foo()
{
static int count = 0;
count++;
printf("Hello world: %d\n", count);
}
int bof(FILE *badfile)
{
char buffer[BUF_SIZE];

unsigned int *framep;
asm("mov %%ebp, %0" : "=r" (framep));

printf("Frame Pointer (EBP) inside bof():  0x%.8x\n", (unsigned)framep);
printf("Buffer's address inside bof():     0x%.8x\n", (unsigned)&buffer);

/* The following statement has a buffer overflow problem */
fread(buffer, sizeof(char), 300, badfile);
return 1;
}
int main(int argc, char **argv)
{
FILE *badfile;
/* Change the size of the dummy array to randomize the parameters
for this lab. Need to use the array at least once */
char dummy[BUF_SIZE*5]; memset(dummy, 0, BUF_SIZE*5);
printf("Address of foo(): 0x%.8x\n", (unsigned int)foo);
badfile = fopen("badfile", "r");
bof(badfile);
printf("Returned Properly\n");
fclose(badfile);
return 1;
}