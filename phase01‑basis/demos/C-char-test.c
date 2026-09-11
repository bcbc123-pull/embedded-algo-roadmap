#include <stdio.h>
int main(void) {
    char c = 0xff;
    printf("%d\n", (int)c);   // 有符号 → -1；无符号 → 255
    return 0;
}
