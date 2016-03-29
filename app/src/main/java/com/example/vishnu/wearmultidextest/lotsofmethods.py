from __future__ import print_function

f0= open('LotsOfMethods0.java', 'w')
f1= open('LotsOfMethods1.java', 'w')
print("package com.example.vishnu.wearmultidextest;", file=f0)
print("package com.example.vishnu.wearmultidextest;", file=f1)
print("public class LotsOfMethods0 {", file=f0)
print("public class LotsOfMethods1 {", file=f1)

for x in range(0, 32677):
    print("public void someMethod{}()".format(x), file=f0)
    print("{", file=f0)
    print("}", file=f0)

for x in range(32678, 65536):
    print("public void someMethod{}()".format(x), file=f1)
    print("{", file=f1)
    print("}", file=f1)


print("}", file=f0)
print("}", file=f1)
