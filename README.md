# Right-Align-Code
Right align go oogabooga you have lost your sanity

To right-align your code, just execute the program and pass in your input and output files with `python right-align.py input-file output-file`.

For example, let's make this your input file, `input.c`.
```c
#include <stdlib.h>

int main() {
    printf("Hello World!\n");
    return 0;
}
```

If you run `python right_align.py input.c output.c` you'll see this.

```c
                                                                                #include <stdlib.h>
                                                                                                   
                                                                                       int main() {
                                                                          printf("Hello World!\n");
                                                                                          return 0;
                                                                                                   }
```

I'm not going to thank you for using this, hopefully nobody does.
