# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром
# Цезаря и возвращает его. Шифр Цезаря заменяет каждую букву в тексте на букву, 
# которая отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, 
# то пусть ваша функция кодирует сдвиг алфавита на 3 позиции:
# А→Г,А→Г,
# Б→Д,Б→Д,
# В→Е,В→Е,
# ……
# Э→А,Э→А,
# Ю→Б,Ю→Б,
# Я→ВЯ→В
# Все символы, кроме русских букв должны остаться неизменными. 
# Маленькие буквы должны превращаться в маленькие, большие — в большие.

def encrypt_caesar(msg, shift=3):
    small_symbols1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    big_symbols1 = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(small_symbols1)
    small_symbols2 = small_symbols1[shift:] + small_symbols1[:shift]
    big_symbols2 = big_symbols1[shift:] + big_symbols1[:shift]
    translation = msg.maketrans(small_symbols1 + big_symbols1, small_symbols2 + big_symbols2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)


print("Введите строку для шифрования: ")
str = encrypt_caesar(input(), 5)
print(str)
print(decrypt_caesar(str, 5))