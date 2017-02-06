def primeGenerator (num):
    if type(num) != int:
        return 'wrong arg'
    if num < 0 or type(num) != int:
        return 'wrong arg'
    prime_list = [] # define an empty list
    for i in range (1,num + 1):
        prime = True 
        j = 2
        while j < i:
            if i % j == 0:
                prime = False
                j = j + 1
            else:
                j = j + 1
        if prime:
            prime_list.append(i) # adding a prime number to the list
        else:
            prime = True
    return prime_list # return list of prime Number found

   

