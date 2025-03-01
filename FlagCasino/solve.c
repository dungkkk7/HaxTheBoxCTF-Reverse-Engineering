#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned int check[] = {
        0x244B28BE, 0x0AF77805, 0x110DFC17, 0x07AFC3A1, 0x6AFEC533,
        0x4ED659A2, 0x33C5D4B0, 0x286582B8, 0x43383720, 0x055A14FC,
        0x19195F9F, 0x43383720, 0x63149380, 0x615AB299, 0x6AFEC533,
        0x6C6FCFB8, 0x43383720, 0x0F3DA237, 0x6AFEC533, 0x615AB299,
        0x286582B8, 0x055A14FC, 0x3AE44994, 0x06D7DFE9, 0x4ED659A2,
        0x0CCD4ACD, 0x57D8ED64, 0x615AB299, 0x22E9BC2A
    };
    int check_size = sizeof(check) / sizeof(check[0]);

    for (int i = 0; i < check_size; ++i) {
        for (int v4 = 0; v4 < 256; ++v4) {
            srand(v4);
            if (rand() == check[i]) {
                printf("check[%d] = 0x%08X -> v4 = %d\n", i, check[i], v4);
                break;
            }
        }
    }

    return 0;
}
