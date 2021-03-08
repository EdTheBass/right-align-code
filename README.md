# Right-Align-Code
Ever wanted to right-align your code? If so, I'll put aside the fact you desperately need help and give you this program.

To right-align your code, just execute the program and pass in your input and output files with `python right-align.py input-file output-file`.

For example, let's make this your input file, `input.c`.
```
#include <stdlib.h>

int main() {
    printf("Hello World!\n");
    return 0;
}
```

If you run `python right-align.py input.c output.c` you'll see this.

```
                                                                                                    #include <stdlib.h>
                                                                                                                       
                                                                                                           int main() {
                                                                                              printf("Hello World!\n");
                                                                                                              return 0;
                                                                                                                       }
```

I'm not going to thank you for using this, hopefully nobody does.
