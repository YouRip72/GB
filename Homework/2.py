uzer_second = int(input('Введите время в секундах:' ))
second = uzer_second % 60
minutes = uzer_second // 60
clock = minutes // 60
s_m_c = f"{clock:02}:{minutes:02}:{second:02}"
print(s_m_c)

