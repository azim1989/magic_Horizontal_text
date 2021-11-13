a = ["..######..", "..#....#..", "..######..", "..#....#..", "..#....#.."]
b = ["..######..", "..#....#..", "..#####...", "..#....#..", "..######.."]
c = ["..######..","..#.......","..#.......","..#.......","..######.."]
d = ["..#####...","..#....#..","..#....#..","..#....#..","..#####..."]
e = ["..######..","..#.......","..#####...","..#.......","..######.."]
f = ["..######..","..#.......","..#####...","..#.......","..#......."]
g = ["..######..","..#.......","..#####...","..#....#..","..#####..."]
h = ["..#....#..","..#....#..","..######..","..#....#..","..#....#.."]
i = ["..######..","....##....","....##....","....##....","..######.."]
j = ["..######..","....##....","....##....","..#.##....","..####...."]
k = ["..#...#...","..#..#....","..##......","..#..#....","..#...#..."]
l = ["..#.......","..#.......","..#.......","..#.......","..######.."]
m = ["..#....#..","..##..##..","..#.##.#..","..#....#..","..#....#.."]
n = ["..#....#..","..##...#..","..#.#..#..","..#..#.#..","..#...##.."]
o = ["..######..","..#....#..","..#....#..","..#....#..","..######.."]
p = ["..######..","..#....#..","..######..","..#.......","..#......."]
q = ["..######..","..#....#..","..#.#..#..","..#..#.#..","..######.."]
r = ["..######..","..#....#..","..#.##....","..#...#...","..#....#.."]
s = ["..######..","..#.......","..######..",".......#..","..######.."]
t = ["..######..","....##....","....##....","....##....","....##...."]
u = ["..#....#..","..#....#..","..#....#..","..#....#..","..######.."]
v = ["..#....#..","..#....#..","..#....#..","...#..#...","....##...."]
w = ["..#....#..","..#....#..","..#.##.#..","..##..##..","..#....#.."]
x = ["..#....#..","...#..#...","....##....","...#..#...","..#....#.."]
y = ["..#....#..","...#..#...","....##....","....##....","....##...."]
z = ["..######..","......#...",".....#....","....#.....","..######.."]
space = ["..........","..........","..........","..........",".........."]
dot =["..........","..........","..........","...####...","...####..."]


list_name = []
input_1 = input("Please enter your name : \njust Letters and space and dot allowed \n")
cunt = 0
len_t = len(input_1)
text = ""

for letter in input_1:
    list_name.append(letter)


for xx in range(5):
    text = ""
    cunt = 0
    for letters in list_name:
        cunt += 1
        if letters == "a":
            text += str(a[xx])
            if cunt == len_t:
                print(text)
        if letters == "b":
            text += str(b[xx])
            if cunt == len_t:
                print(text)
        if letters == "c":
            text += str(c[xx])
            if cunt == len_t:
                print(text)
        if letters == "d":
            text += str(d[xx])
            if cunt == len_t:
                print(text)
        if letters == "e":
            text += str(e[xx])
            if cunt == len_t:
                print(text)
        if letters == "f":
            text += str(f[xx])
            if cunt == len_t:
                print(text)
        if letters == "g":
            text += str(g[xx])
            if cunt == len_t:
                print(text)
        if letters == "h":
            text += str(h[xx])
            if cunt == len_t:
                print(text)
        if letters == "i":
            text += str(i[xx])
            if cunt == len_t:
                print(text)
        if letters == "j":
            text += str(j[xx])
            if cunt == len_t:
                print(text)
        if letters == "k":
            text += str(k[xx])
            if cunt == len_t:
                print(text)
        if letters == "l":
            text += str(l[xx])
            if cunt == len_t:
                print(text)
        if letters == "m":
            text += str(m[xx])
            if cunt == len_t:
                print(text)
        if letters == "n":
            text += str(n[xx])
            if cunt == len_t:
                print(text)
        if letters == "o":
            text += str(o[xx])
            if cunt == len_t:
                print(text)
        if letters == "p":
            text += str(p[xx])
            if cunt == len_t:
                print(text)
        if letters == "q":
            text += str(q[xx])
            if cunt == len_t:
                print(text)
        if letters == "r":
            text += str(r[xx])
            if cunt == len_t:
                print(text)
        if letters == "s":
            text += str(s[xx])
        if letters == "t":
            text += str(t[xx])
            if cunt == len_t:
                print(text)
        if letters == "u":
            text += str(u[xx])
            if cunt == len_t:
                print(text)
        if letters == "v":
            text += str(v[xx])
            if cunt == len_t:
                print(text)
        if letters == "w":
            text += str(w[xx])
            if cunt == len_t:
                print(text)
        if letters == "x":
            text += str(x[xx])
            if cunt == len_t:
                print(text)
        if letters == "y":
            text += str(y[xx])
            if cunt == len_t:
                print(text)
        if letters == "z":
            text += str(z[xx])
            if cunt == len_t:
                print(text)
        if letters == " ":
            text += str(space[xx])
            if cunt == len_t:
                print(text)

        if letters == ".":
            text += str(dot[xx])
            if cunt == len_t:
                print(text)