number = int(input("Какой верхний предел интервала?: "))
procent = 0
while procent < number:
    procent += 1
    procent_remains = procent % 10
    # print(procent_remains)
    if 5 <= procent < 21:
        print(procent, "процентов")
    else:
        if procent_remains == 1:
            print(procent, "процент")

        elif 1 < procent_remains <= 4:
            print(procent, "процента")

        elif procent_remains == 0 or 5 <= procent_remains <10:
            print(procent, "процентов")
