def primeGenerator (num):
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
            prime_list.append(i) 
        else:
            prime = True
    return prime_list # Add to list

print(primeGenerator(9))    

