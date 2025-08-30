# Programming - Sums

### Problem Statement

    Just keep adding, just keep adding, just keep adding

By looking at the attached code `server.py` 

```py
n = 123456

nums = [str(random.randint(0, 696969)) for _ in range(n)]

print(' '.join(nums), flush=True)
```
It prints a list of `123456` random numbers seperated by a whitespace.

```py
ranges = []
for _ in range(n):
    l = random.randint(0, n - 2)
    r = random.randint(l, n - 1)
    ranges.append(f"{l} {r}") #inclusive on [l, r] 0 indexed
    print(l, r)
```
It builds an array of `n` ranges of the type `(l, r)` and prints these line by line seperated by a whitespace.

```py
big_input = ' '.join(nums) + "\n" + "\n".join(ranges) + "\n"

proc = subprocess.Popen(
    ['./solve'],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = proc.communicate(input=big_input)
```

There is already an assembled binary code `solve` and this code runs that file and gives it the input as `big_input` which is the list of random numbers and the list of ranges.

```py
out_lines = stdout.splitlines()
ans = [int(x) for x in out_lines[:n]]

urnums = []
for _ in range(n):
    urnums.append(int(input()))
```
It creates an array `ans` of the numbers which are expected to be from us.<br>
`urnums` contains what we are going to input to the python program.

```py
if ans != urnums:
    print("wawawawawawawawawa")
    sys.exit(1)

if time.time() - start > 100:
    print("tletletletletletle")
    sys.exit(1)

print(open('flag.txt', 'r').readline())
```

We need to make `ans` and `urnums` equal and that will be done by computing these `(l, r)` range sums ourselves, but the program also terminates if we don't do it quickly.

So we write a code of our own which will help us do this, I used a python script which can use the server address and can run on google collab.

In the end it gives us the flag.

`scriptCTF{1_w4n7_m0r3_5um5}`


