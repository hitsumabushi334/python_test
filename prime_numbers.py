def is_prime(n):
    # 1は素数ではない
    if n < 2:
        return False
    # 2は素数
    if n == 2:
        return True
    # 偶数は素数ではない（2を除く）
    if n % 2 == 0:
        return False
    # 3以上の奇数で割り切れるかチェック
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 1から100までの素数を表示
print("1から100までの素数:")
prime_numbers = [num for num in range(1, 101) if is_prime(num)]
print(prime_numbers)