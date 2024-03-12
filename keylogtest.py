from pynput.keyboard import Listener
from pynput.keyboard import Controller
from pynput.mouse import Listener
from pynput.mouse import Controller
"""
fl=open("log.txt", 'a'); #saving instance of log.txt after opening, to fl
fl.write("");
fl.close(); 

"""

def cmouse():
	mouse=Controller();
	mouse.position=(10, 20) # Position is in px
'''
def lmouse(x, y):
	print("Position="+format((x,y)));
	
def ckb():
	kb=Controller();
	kb.type("Fuck You"); 
	'''
'''def wtf(key):
	ks=(str(key).replace("'"," "));
	with open("log.txt", 'a') as fl:
		fl.write(ks);
		
with Listener(on_press=wtf) as listen: #saving instance of Listener(...) as listen
	listen.join(); '''
