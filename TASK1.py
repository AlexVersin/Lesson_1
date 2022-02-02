duration = int(input("Введи время в секундах: "))

#Вывод в секундах
if duration < 60:
    print(duration, "сек")

#Вывод с минутами
elif 60 <= duration < 3600:
    duration_m = duration // 60
    duration_s = duration % 60
    if duration_s > 0:
        print(duration_m, " мин ", duration_s, " сек ")
    else:
        print(duration_m, " мин")

#Вывод с часами
elif 3600 <= duration < 86400:
    duration_h = duration // 3600
    duration_h_remains = duration % 3600
    if duration_h_remains >= 60: # МИНУТЫ
        duration_m = duration_h_remains // 60
        duration_m_remains = duration_h_remains % 60
        if 0 < duration_m_remains < 60:
            print(duration_h, " час ", duration_m, " мин ", duration_m_remains, " сек ")
        else:
            print(duration_h, " час ", duration_m, " мин")
    elif 0 < duration_h_remains < 60: # СЕКУНДЫ
        print(duration_h, " час ", duration_h_remains, " сек ")
    else:
        print(duration_h, " час ")

# Вывод с сутками
elif duration >= 86400:
    duration_d = duration // 86400
    durations_d_remains = duration % 86400

    if 3600 <= durations_d_remains < 86400: # ЧАСЫ
        duration_h = durations_d_remains // 3600
        duration_h_remains = durations_d_remains % 3600
        if duration_h_remains >= 60: #МИНУТЫ
            duration_m = duration_h_remains // 60
            duration_m_remains = duration_h_remains % 60
            if 0 < duration_m_remains < 60: #СЕКУНДЫ
                print(duration_d, " дн ", duration_h, " час ", duration_m, " мин ", duration_m_remains, " сек ")
            else:
                print(duration_d, " дн ", duration_h, " час ", duration_m, " мин ")
        elif duration_h_remains < 60: #СЕКУНДЫ
            duration_s = duration_h_remains % 60
            print(duration_d, " дн ", duration_h, " час ", duration_s, " сек ")
        else:
            print(duration_d, " дн ", duration_h, " час ")

    elif 60 <= durations_d_remains < 3600: # МИНУТЫ
        duration_m = durations_d_remains // 60
        duration_m_remains = durations_d_remains % 60
        if duration_m_remains < 60:
            print(duration_d, " дн ", duration_m, " мин ", duration_m_remains, " сек ")
        else:
            print(duration_d, " дн ", duration_m, " мин ")

    elif durations_d_remains < 60:
        print(duration_d, " дн ", durations_d_remains, "сек")

    else:
        print(duration_d, " дн ")
