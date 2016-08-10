d00={k:v for k in "ABC" for v in "XYZ"}
print(d00)
d01={k:v for v in "XYZ" for k in "ABC"}
print(d01)

m="f"
d1={m+n:v for v in "qwe" for m in "ABC" for n in "XYZ"}
d2={m+n:v for v in m for m in "ABC" for n in "XYZ"}
d3={m+n:v for v in m for m in "ABC" for n in m}
d4={m+n:v for m in "ABC" for n in "XYZ" for v in m }
print(d1)
print(d2)
print(d3)
print(d4)