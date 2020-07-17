# На этапе трансляции (когда программа запускается на выполнение), в консоли выдается сообщение об ошибке,
# которое включает:
# номер строки, в которой допущена ошибка (line 2 на следующем рисунке);
# оператор с ошибкой, под ним помечается место возможной ошибки (print("Hello, world!),
# возможное место ошибки - последний символ строки);
# название ошибки и пояснение к ней (название: SyntaxError, пояснение: EOL while scanning string literal).

IndentationError: unexpected indent:
# для операторов невложенных блоков: есть пробелы в начале строки (см. описание ошибки 2);
# для вложенных блоков – операторы имеют разный отступ относительно основной конструкции (см. описание ошибки 7).
IndentationError: expected an indented block:
# после  символа «:» в основной конструкции операторы во вложенном блоке записаны без отступа
# (см. описание ошибки 6).
NameError: name 'Print' is not defined (в кавычках может быть указано имя функции или переменной)
# (см. описание ошибки 5):
#ошибка при записи названия функции или переменной (см. описание ошибки 4).
SyntaxError: EOL while scanning string literal :
# пропущена кавычка или разные кавычки (двойная и одинарная) используются в начале и в конце строки
# (см. описание ошибки 1).
SyntaxError: unexpected EOF while parsing :
# пропущена закрывающая скобка (см. описание ошибки 2).
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Hello, world!")?
# (ошибка может возникнуть при неверном написании любого оператора):
# неверно записан оператор (аргументы print не заключены в скобки) (см. описание ошибки 4).
SyntaxError: invalid syntax:
# несоответствие скобок (открывающих скобок больше, чем закрывающих, или наоборот) (см. описание ошибки 3):
# пропущена запятая между аргументами оператора print(см. описание ошибки 1);
# ошибка при написании арифметической операции (* * вместо **, / / вместо // и пр.);(см. описание ошибки 3)
# пропущен символ «:» перед вложенным блоком (см. описание ошибки 5).
TypeError: compute_len() missing 1 required positional argument: 'y_1' (имя функции и аргумента может быть любым) :
# несоответствие количества аргументов при описании функции и вызове (см. описание ошибки 3).
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType':
# в переменную, используемую в выражении, занесен результат вычисления функции,
# но функция не возвращает никакого значения (пропущен оператор return) (см. описание ошибки 5).
UnboundLocalError: local variable 's' referenced before assignment:
# переменная, используемая в выражении, заранее не определена (см. описание ошибки 4);
# в функции используется переменная, которая определена в основном блоке, а в функции к ней обращаться нельзя
# (см. описание ошибки 6).
ValueError: math domain error:
# В качестве аргумента функции модуля math передано недопустимое значение  (см. описание ошибки 1).
ValueError: invalid literal for int():
# в консоли вводится значение, несоответствующее типу переменной в программе (см. описание ошибки 2).