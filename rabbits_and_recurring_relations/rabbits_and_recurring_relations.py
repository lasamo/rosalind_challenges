def rabbits_and_recurring_relations(n, k):
    if n > 40 or k > 5:
        print('ValueError: The input is not valid')
    total_rabbits = 1
    f_n1 = 1
    f_n2 = 1
    for i in range(n+2):
        f_n = f_n1 + f_n2
        f_n1 = f_n2
        f_n2 = f_n
        if i != 1:
            total_rabbits += k
    return total_rabbits


print(rabbits_and_recurring_relations(35, 5))
