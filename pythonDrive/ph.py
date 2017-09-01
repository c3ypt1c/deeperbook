import sys;
q=True
for x in sys.argv[1].lower():
    e=False
    for y in sys.argv[2].lower():
        if x==y:
            e=True;break
    q=q and e
    if not q:break
print(q)
