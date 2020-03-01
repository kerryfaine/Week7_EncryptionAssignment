class certauth: 
    """Simulated certificate authority"""

    go = 'successful handshake'
    noGo = 'bad handshake - goodbye'

    def registerMe(self, theServer, theKey):
        #check to see if file exists before appending
            reg = open("registry.txt", "r+")
            doesExist = False 

            contents = reg.readlines() 
            for x in contents: 
                if(theServer in x):
                    doesExist = True
            
            #if it doesn't already exist, add it
            if(doesExist == False):
                reg.write(theServer + "\t" + theKey + "\n")
                
            reg.close()

    def validateMe(self, theServer):
        try:
            reg = open("registry.txt", "r")
            contents = reg.readlines()
            for x in contents: 
                if(theServer.decode("utf-8") in x):
                    result = x.split()
                    return result[1]
        except: 
            return 'none'   
        
        finally: 
            reg.close()

    def encryptMe(self, text):
        result = ""
        s = 4

        #encrypt using Caesar Cipher
        for i in range(len(text)):
            char = text[i]

            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result
