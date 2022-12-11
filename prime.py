list1 = [5, 9, 8, 11, 15, 19, 25]
prime_list = []
for x in list1:
    for i in range(2, (x//2)+1):
        if x%i == 0:
            break
    else:
        prime_list.append(x)
    
print(prime_list)
# this is for testing for to push into github
