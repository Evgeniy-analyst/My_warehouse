def compute_income(deposit, interest_rate, amount_months):
    ci = deposite * interest_rate_1 ** amount_months_1
    return ci


x = 73600  # float(input())

k = 7.52  # float(input())

n = 16  # int(input())

deposite = x
interest_rate_1 = 1 + k / (12 * 100)
amount_months_1 = n

c = compute_income(x, k, n)

# вычислить прибыль с помощью функции
s = (x - c) * -1
# вывести результат
print(round(s))
