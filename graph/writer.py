import random, time, threading

'''
writer will take sensor reading and write it to file.
'''

def write_force1():
    while True:
        output = random.randint(1,100)
        force1_output = open('force1_output.txt', 'wt')
        force1_output.write(str(output))
        force1_output.close()
        time.sleep(.1)

force1_thread = threading.Thread(target=write_force1)
        
if __name__=='__main__':
    force1_thread.start()
