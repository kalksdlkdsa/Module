import sys
def printf(format, *args):
    sys.stdout.write(format.format(*args))
def scanf(format):
    return tuple(map(type(format),input().split()))
def puts(s):
    sys.stdout.write(s + "\n")
def gets():
    return sys.stdin.readline()
def fopen(filename,mode):
    return open(filename,mode)
def fclose(file):
    file.close()
def fgetc(file):
    return file.read(1)
def fputc(char,file):
    file.write(char)
def fgets(size,file):
    return file.readline(size)
def fputs(string,file):
    file.write(string)
