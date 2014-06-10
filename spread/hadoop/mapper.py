#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-
import sys


states = ('B', 'M', 'E', 'S')


def regularize(char):
    if char == 12288:
        return 32
    if 65280 < char < 65375:
        return char - 65248
    if ord('A') <= char <= ord('Z'):
        char += 32
        return char
    return char


def unicodify(word):
    if not type(word) is unicode:
        try:
            word = word.decode('utf-8')
        except:
            word = word.decode('gbk', 'ignore')

    word = word.replace('\n', '')
    return word


def start_mapper():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            uword = unicodify(word)
            if len(uword) == 1:
                print "%s\t%s" % ('S', 1)
            elif len(uword) > 1:
                print "%s\t%s" % ('B', 1)


def emit_mapper():
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        for word in words:
            uword = unicodify(word)
            if len(uword) == 1:
                print "%s\t%s\t%s" % ('S', uword[0].encode('utf-8'), 1)
            elif len(uword) > 1:
                print "%s\t%s\t%s" % ('B', uword[0].encode('utf-8'), 1)
                for each in uword[1:-1]:
                    print "%s\t%s\t%s" % ('M', each.encode('utf-8'), 1)
                print "%s\t%s\t%s" % ('E', uword[-1].encode('utf-8'), 1)


def trans_mapper():
    prev = None
    current = None
    for line in sys.stdin:
        line = line.strip()
        words = line.split()
        first_word = words[0]
        first_word = unicodify(first_word)
        if len(first_word) == 1:
            prev = 'S'
        elif len(first_word) > 1:
            prev = 'B'
            for each in first_word[1:-1]:
                current = 'M'
                print '%s\t%s\t%s' % (prev, current, 1)
                prev = current
            current = 'E'
            print '%s\t%s\t%s' % (prev, current, 1)
            prev = current
        for word in words[1:]:
            word = unicodify(word)
            if len(word) == 1:
                current = 'S'
                print "%s\t%s\t%s" % (prev, current, 1)
                prev = current
            elif len(word) > 1:
                current = 'B'
                print "%s\t%s\t%s" % (prev, current, 1)
                prev = current
                for each in word[1:-1]:
                    current = 'M'
                    print "%s\t%s\t%s" % (prev, current, 1)
                    prev = current
                current = 'E'
                print "%s\t%s\t%s" % (prev, current, 1)
                prev = current
            

if __name__ == '__main__':
    trans_mapper()
