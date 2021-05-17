num_list = []
while True:
    n = input("Input int number: ")
    if n == "end":
        break
    num_list.append(int(n))

def quadra_and_sum_func(num_list):
    theSum = 0
    for i in range(len(num_list)):
        num_list[i] = num_list[i] * num_list[i]

    for i in num_list:
        theSum = theSum + i

    print(theSum)

quadra_and_sum_func(num_list)
