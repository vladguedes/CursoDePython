'''Método format'''

a = 'AAAAA'
b = 'BBBBB'
c = 1.1
string = 'A={nome2} B={0} C={nome2} D={nome3:.2f} E={0}'
formato = string.format(a, nome2=b, nome3=c)

print(formato)

string = 'A={0} B={nome2} C={nome3}'
formato = string.format(
    a, nome2=b, nome3=c
)

print(formato)