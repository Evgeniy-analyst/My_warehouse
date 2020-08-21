# терминология реляционных баз данных:

# 1) отношение  – это структура данных целиком, набор записей (в обычном понимании – таблица) ,
# в  примере –это Сотрудник;
# 2) кортеж – это каждая строка , содержащая данные (более распространенный термин – запись ), например, <001,
# Борин С.А, 234-01-23, программист>, все кортежи в отношении должны быть различны;
# 3) мощность – число кортежей в таблице (проще говоря, число записей), в данном случае 3, мощность отношения может быть
# любой (от 0 до бесконечности), порядок следования кортежей - неважен;
# 4) атрибут – это столбец в таблице (более распространенный термин – поле ), в примере – Табельный номер,
# Фамилия И.О., Телефон, Должность)
# 5) размерность – это число атрибутов в таблице, в данном случае – 4;
# 6) размерность отношения должна быть больше 0, порядок следования атрибутов существенен;
# 7) домен атрибута – это допустимые значения (неповторяющиеся), которые можно занести в поле,
# например для атрибута Должность домен – {инженер, программист}.
