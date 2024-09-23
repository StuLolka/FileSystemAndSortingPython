import text
from resources import (buble_sort_ascending, buble_sort_descending,
                       shaker_sort_ascending, shaker_sort_descending)

# №1
with open("source_data.txt", encoding="UTF-8") as file_in:
    lines = file_in.readlines()
    name = lines[0][:-1]
    id_ = int(lines[1])

with open("result.txt", "w", encoding="UTF-8") as file_out:
    file_out.write(str(text.ex_1 % (name, id_)) + "\n")


# №2
name_without_spaces = name.replace(" ", "")
name_len = len(name_without_spaces)
result = id_ // name_len

with open("result.txt", "a", encoding="UTF-8") as file_out:
    file_out.write(f"{text.ex_2} {result}\n")


# №3
is_ascending = result % 2 == 0

with open("result.txt", "a", encoding="UTF-8") as file_out:
    if is_ascending:
        file_out.write(str(text.ex_3_ascending % result) + "\n")
    else:
        file_out.write(str(text.ex_3_descending % result) + "\n")


# №4
name_utf = [ord(char) for char in name_without_spaces]

with open("result.txt", "a", encoding="UTF-8") as file_out:
    file_out.write(f"{text.ex_4} {name_utf}\n")


# №5
shaker_sort_ascending_name_utf = shaker_sort_ascending(name_utf)
buble_sort_ascending_name_utf = buble_sort_ascending(name_utf)
shaker_sort_descending_name_utf = shaker_sort_descending(name_utf)
buble_sort_descending_name_utf = buble_sort_descending(name_utf)
sorted_name_utf = shaker_sort_ascending_name_utf if is_ascending \
                    else shaker_sort_descending_name_utf

with open("result.txt", "a", encoding="UTF-8") as file_out:
    if is_ascending:
        file_out.write(f"{text.ex_5_ascending} {sorted_name_utf}\n")
    else:
        file_out.write(f"{text.ex_5_descending} {sorted_name_utf}\n")


# №6
average = round(sum(name_utf) / len(name_utf), 3)

with open("result.txt", "a", encoding="UTF-8") as file_out:
    file_out.write(f"{text.ex_6} {average}\n")


# №7
square_average = round((sum([i ** 2 for i in name_utf])
                        / len(name_utf)) ** 0.5, 3)

with open("result.txt", "a", encoding="UTF-8") as file_out:
    file_out.write(f"{text.ex_7} {square_average}")
