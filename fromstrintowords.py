#!/usr/bin/python
import sys


def output(lvl, arg):
    
    print(f"Уровень {lvl}:")
    
    if isinstance(arg, list):
        if not arg:                     #catch error for empty line
            return
        if isinstance(arg[0], str):
            [print('\t', word) for word in arg]
        else:
            [print('\t', k, v) for k, v in arg]

    elif isinstance(arg, dict):
        [print('\t', k, v) for k, v in arg.items()]
    
    print()


def main(words:list):

    output('1', words)                 #just out whole list

    sorted_words = sorted(words)       #sort elems
    output('2', sorted_words)
    
    words_without_doubles = []
    for word in sorted_words:         #loop for delete doubles
        if word not in words_without_doubles:
            words_without_doubles.append(word)
    output('3', words_without_doubles)

    counted_words = {}
    for word in words:                #loop for count each elem
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1
    output('4', counted_words)

    sorted_counted_words = sorted(
        counted_words.items(),
        key=lambda v: (-v[1], v[0]) #func for sort
    )
    output('5', sorted_counted_words)


if __name__ == "__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1:])
    else:
        for line in sys.stdin:
            main(line.split())
