import sys

def get_letter(init,exp,up):
    return chr(int(ord('A')+(init-ord('A')+nb_letters_ch//(26**exp)+up)%26))

x = input().split("-")
n = int(input())
number = int(x[1])
cde = format((number+n)%999,'03d')
nb_letters_ch = (number+n)//999
g = get_letter(ord(x[2][1]),0,0)
f = get_letter(ord(x[2][0]),1,0 if g>=x[2][1] else 1)
b = get_letter(ord(x[0][1]),2,0 if f>=x[2][0] else 1)
a = get_letter(ord(x[0][0]),3,0 if b>=x[0][1] else 1)

print('-'.join([a+b,cde,f+g]))