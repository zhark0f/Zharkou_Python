def is_correct_brackets(line):
    while "()" in line or "[]" in line or "{}" in line or "/**/" in line:
        line = line.replace("()", "")
        line = line.replace("[]", "")
        line = line.replace("{}", "")
        line = line.replace("/**/", "")
    return not line


line = input("Введите скобочную последовательность, состоящую из символов (), [], {}, /**/: ")
info_line = "Неправильная"
if is_correct_brackets(line):
    info_line = "Правильная"
print("Введенная скобочная последовательность - ", info_line)
