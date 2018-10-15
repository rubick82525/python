# coding = utf-8
def clearBlankLine():
    file1 = open('c:/shiyanlou/test.cfg', 'r') 
    file2 = open('c:/shiyanlou/test1.cfg', 'w')
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()
