odd_number = 0
summ_x = 0
while odd_number != 1000:
    odd_number = 1 + odd_number
    if odd_number % 2 != 0:
        cube_number_1 = odd_number ** 3
        cube_number = cube_number_1
        summ = 0
        while cube_number > 0:
            number = cube_number % 10
            summ += number
            cube_number = cube_number // 10
        summ_1 = summ % 7
        if summ_1 == 0:
            summ_x = summ_x + odd_number
            print (odd_number, "^3: ", cube_number_1, "sum: ",  summ_x, "[", summ, "]")
