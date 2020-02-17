def encrypter(string, key):
    val = ""
    new_str = ""
    new_val = 0
    dic = {0:"a", 1:'b',2:'c', 3:"d", 4:'e',5:'f', 6: 'g', 7:"h", 8:'i', 9:"j", 10:'k',11:'l', 12:'m', 13:'n', 14:'o', 15:'p', 
       16:'q', 17:'r', 18:'s', 19:'t', 20:'u', 21:'v', 22:'w', 23:'x', 24:'y', 25:'z', 26: " ", 27:"!"}
    
    dic2 = {"a":0,'b':1, 'c':2,"d":3, 'e':4 ,'f':5, 'g':6, "h":7, 'i':8, "j":9, 'k':10,'l':11, 'm':12, 'n':13, 'o':14,'p':15, 
       'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25, " ": 26, "!":27}
 
    
    for i in string:
        new_val = dic2[i] + key
        if new_val >= len(dic): 
            new_val = new_val - len(dic)
            new_str += dic[new_val]
            #print(new_val)
        elif new_val < 0:    
                new_val +=len(dic)
                new_str += dic[new_val]
                #print(new_val)
        else:
            new_str +=dic[dic2[i]+key]
            #print(new_val)
    print("Your message is: "+ new_str)
    print("Your message is: "+ new_str)
