n = int(input('Введите число от 3 до 20: '))
password = []
for i in range(1, int(n-1)):
    for j in range(1+i, int(n)):
        if n % (i + j) == 0:
            password.extend([i] + [j])
print('пароль: ', *password)