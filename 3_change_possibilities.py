def change_possibilities(amount, denominations, index, memo = {}):
    if amount == 0: return 1
    if index >= len(denominations): return 0

    key = str(amount) + ":" + str(index)
    if key in memo: return memo[key]

    combos, coin = 0, denominations[index]
    for i in range(amount//coin + 1):
        remaining = amount - coin * i
        combos += change_possibilities(remaining, denominations, index + 1, memo)

    memo[key] = combos
    return memo[key]

if __name__ == '__main__':
    denominations = [1, 2, 3]
    print(change_possibilities(4, denominations, 0))
