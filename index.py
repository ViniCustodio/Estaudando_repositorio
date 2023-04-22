n = int(input("Qual tabuada você deseja realizar? "))
p = 1
while p < 11:
    t = n * p
    print("{} x {} = {}".format(n, p, t))
    p = p + 1

i = int(input("Qual seu ano de nascimento? "))
a = 2023
v = a - i
if v >= 18:
    print("Você tem {} anos ou mais, então você pode votar esse ano!".format(v))
else: 
    print("Você tem {} anos de idade, isso significa que você é menor e não pode votar esse ano. :C".format(v))

r = int(input("Digite sua senha: "))
s = int(1234)
while r != s:
    print("Senha incorreta, tente novamente: ")
    r = int(input("Digite sua senha: "))
print("ACESSO PERMITIDO! :D")
        