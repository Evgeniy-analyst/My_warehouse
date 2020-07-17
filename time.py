#Дано значение времени в 12-ти часовом формате h:m:s.
# Определить угол в градусах между положением часовой
# стрелки в начале суток и ее положением в h часов, m минут и s секунд.
# Допустимыми значениями считать целое число часов от 0 до 11,
# минут и секунд от 0 до 59. Если введены другие значения - вывести "error".
# put your python code here
h = int(input())
m = int(input())
s = int(input())

if h > 11 or h < 0 or m < 0 or m > 59 or s < 0 or s > 59:
    print("error")
    exit()
def time_deg(h, m, s):
    deg_time = h * h_1 + m * m_1 + s * s_1
    return deg_time


h_1 = 360/12
m_1 = h_1/60
s_1 = m_1/60

A = time_deg(h, m, s)
print(round(A, 2))