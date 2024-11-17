def find_winner(n):
    digit_sum = sum(int(digit) for digit in str(n))
    if digit_sum % 2 == 0:
        print("Vignesh")
    else:
        print("Charan")
n = input()
find_winner(n)
