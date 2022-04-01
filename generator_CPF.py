from random import randint
print('-=-'* 20)
print("WELCOME TO GENERATOR CPF")
print('-=-'* 20)
def formatting_CPF(a):
    a = list(a)
    a.insert(3, ".")
    a.insert(7, '.')
    a.insert(11, '-')
    return ''.join(a)
while True:
    cpf = str(randint(10000000000,
    12345678911))
    new_cpf = cpf[:9]

    mult = 10
    total_mult = 0
    count = 1

    while count <= 2:
        for i in new_cpf:
            i = int(i)
            total_mult += i * mult
            mult -= 1

        mult = 11
        overvalue = 11 - (total_mult % 11)
        total_mult = 0
        if overvalue >= 10:
            new_cpf += "0"
        else:
            new_cpf += str(overvalue)
        count += 1
    if cpf == new_cpf:
        print(formatting_CPF(cpf))
        break



if cpf == new_cpf:
        print(f'{formatting_CPF(cpf)} e um CPF valido')
else:
    print(f'{formatting_CPF(cpf)} e um CPF invalido')

print('-=-'* 20)
print("TEMPORARY CPF USE WITH MODERATION")
print('SEE YOU NEXT TIME')

