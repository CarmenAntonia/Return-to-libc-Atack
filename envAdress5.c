#include <stdio.h>
#include <stdlib.h> 

int main(){
	char* shell = (char *)getenv("MYSHELL");
	char* arg = getenv("ARG");

	if (shell){
        	printf("Value: %s\n", shell);
		printf("Address: %x\n", (unsigned int)shell);
	}
	if (arg){
        	printf("Value: %s\n", arg);
		printf("Address: %x\n", (unsigned int)arg);
	}
	return 1;
}