def say_hello():
    import sys
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            print ("Hello " + sys.argv[i] + "!")
    else:
            print ("Hello World!")
say_hello()
