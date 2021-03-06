import random

###############################################################################

# Блоки добавления едитниц


def edin1p (a, j):

    a = a + '*((j++)-' + str(j) + ')'

    return a


def edin2p (a, j):

    a = a + '*(' + str(j) + '*i-(j*i*j)/(' + str(j) + ')' + ')'

    return a



def edin3p (a, j):

    a = a + '*(i*i/((j++)-' + str(j+1) + '))'

    return a




def edin1l (a, j):

    a = a + '((j++)-' + str(j) + ')*'

    return a




def edin2l (a, j):

    a = a + '(' + str(j) + '*i-(j*i*j)/(' + str(j) + ')' + ')*'

    return a



def edin3l (a, j):

    a = a + '(i*i/((j++)-' + str(j+1) + '))*'

    return a

#############################################################################

#Блоки добавления двоек


def dvoi1 (a, j):

    a = a + '/(' + str(j) + '/j+' + 'i*i/(' + str(j-2) + '-((j--)--)))'

    return a



def dvoi2 (a, j):

    a = a + '/(' + '2*j*j/' + str(j*j) + ')'

    return a

############################################################################

#Блоки создания начальных чисел


def chislo1 (n, j):

    a = ''
    a = a + 'i*(i--)*(j*j-' + str(j*j) + ')+(' + str(n-j) + '+j)'

    return a



def chislo2 (n, j):

    a = ''
    a = a + '(' + str(n+j) + '-j)*(j++)/' + str(j+1)

    return a

#############################################################################

# Основная функция, генерирующая из блоков (блоки возможно добавлять новые)

# выражение, вычисляющее заданное число

# Вводится необходимое число и значение известной перемнной 'j'


def osnovnoy_raschet(n, j):

    random.seed()

    
# Заданное число разбивается на части

    if n % 2 != 0:

        ch = (n + 1) / 2

        ch2 = (n - 1) / 2

    else:

        ch = n / 2

        ch2 = n / 2
 
    
# Формируется выражение, вычисляющее число, из блоков, отобранных
 
# генератором случайных чисел


    k = random.randrange(1,2,1)

    if k == 1:

        x = chislo1 (ch, j)

    if k == 2:

        x = chislo2 (ch, j)



    k = random.randrange(1,2,1)

    if k == 1:

        x = dvoi1 (x, j)

    if k == 2:

        x = dvoi1 (x, j)



    for l in range(random.randrange(0,5,1)):

        k = random.randrange(0,6,1)


        if k == 0:

            x = x

        if k == 1:

            x = edin1p (x, j)

        if k == 2:

            x = edin2p (x, j)

        if k == 3:

            x = edin3p (x, j)

        if k == 4:

            x = edin1l (x, j)

        if k == 5:

            x = edin2l (x, j)

        if k == 6:

            x = edin3l (x, j)


    x = '((' + x + ')+('


    k = random.randrange(1,2,1)

    if k == 1:

       a = chislo1 (ch2, j)

    if k == 2:

       a = chislo2 (ch2, j)



    k = random.randrange(1,2,1)

    if k == 1:

        a = dvoi1 (a, j)

    if k == 2:

        a = dvoi1 (a, j)

    
    
    for l in range(random.randrange(0,5,1)):

        k = random.randrange(0,6,1)

        if k == 0:

            a = a
 
       if k == 1:

            a = edin1p (a, j)

        if k == 2:

            a = edin2p (a, j)

        if k == 3:

            a = edin3p (a, j)

        if k == 4:

            a = edin1l (a, j)

        if k == 5:

            a = edin2l (a, j)

        if k == 6:

            a = edin3l (a, j)



    x = x + a + '))'


    for l in range(random.randrange(0,5,1)):

        k = random.randrange(0,6,1)



        if k == 0:

            x = x

        if k == 1:

            x = edin1p (x, j)

        if k == 2:

            x = edin2p (x, j)

        if k == 3:

            x = edin3p (x, j)

        if k == 4:

            x = edin1l (x, j)

        if k == 5:

            x = edin2l (x, j)

        if k == 6:

            x = edin3l (x, j)


    
   return x
