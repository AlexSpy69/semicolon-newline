import sys


def help_() -> None:
    print("python -m semicolon_newline (filename) (spaces)")
    print("filename: name of the file")
    print("spaces: number of spaces used for indentation (-1 for tab indentation)")


def semicolon_newline(string: str, spaces: int) -> str:
    string = string.replace(' '*spaces, '\t') if spaces != -1 else string
    new_string = ''
    in_bracket = False
    indentation = 0
    prev_char = ''
    for char in string:
        match char:
            case '(':
                in_bracket = True
                new_string += char
            case ')':
                in_bracket = False
                new_string += char
            case ';':
                new_string += ';' if in_bracket else '\n' + \
                                                     (indentation + 1) * '\t' + ';'
            case '\t':
                if prev_char != '\t':
                    indentation = 0
                indentation += 1
                new_string += char
            case _:
                new_string += char
        prev_char = char

    return new_string.replace('\t', ' '*spaces) \
        if spaces != -1 else new_string


def main() -> None:
    if len(sys.argv) != 3:
        help_()
        return
    file_in = open(sys.argv[1], 'r')
    file_out = open(sys.argv[1] + '.out', 'w+')
    file_out.write(semicolon_newline(file_in.read(), int(sys.argv[2])))
    file_in.close()
    file_out.close()
