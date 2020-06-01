#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int a[100], n = 100, i = 0, j = 0, t = 0, fl = 1;
  FILE *fptr;
  fptr = fopen("../random.txt", "r");
  if (fptr == NULL) {
    printf("error");
    exit(1);
  }
  while (fscanf(fptr, "%d", &a[i]) == 1) {
    i++;
  }
  for (i = 0; i < n - 1; i++) {
    fl = 0;
    for (j = 0; j < n - i - 1; ++j) {
      if (a[j] > a[j + 1]) {
        fl = 1;
        t = a[j];
        a[j] = a[j + 1];
        a[j + 1] = t;
      }
    }

    if (fl == 0)
      break;
  }
  for (i = 0; i < n; ++i) {
    printf("%d\n", a[i]);
  }
  return 0;
}
