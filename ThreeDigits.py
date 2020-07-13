import sys


class Node(object):
    def __init__(self):
        self.parent=None
        self.child=[]
        self.nodedata=None
        self.digit=0

def expand(fringe_in,newdata,oldnode,digit):  #set up new child
    buffer=True
    child=Node()
    if(newdata>=100):
        child.nodedata=str(newdata)
    if(newdata<100 and newdata>=10):
        child.nodedata='0'+str(newdata)
    if(newdata<10 and newdata>=0):
        child.nodedata='00'+str(newdata)
    child.parent=oldnode
    child.digit=digit
    oldnode.child.append(child)
    index1=0
    '''for x in fringe:
        if x.nodedata==str(newdata) and x.digit==digit:
            buffer=False'''
    for y in forbidden:
        if y!='':
            if int(y)==newdata:
                buffer=False
    if buffer==True:
        fringe_in.append(child)

def checklist(input1,number):#check the list
    for x in input1:
        if x==number:
            return True
    return False

def height(input_node):
    i=0
    bufferno=input_node
    while(bufferno.parent!=None):
        i+=1
        bufferno=bufferno.parent

    return i

algorithm=sys.argv[1]        #get the arguement from the commend line
filename=sys.argv[2]
file=open(filename)
start=(file.readline()).replace('\n','')
end=file.readline()
forbidden=(file.readline()).split(',')
forbidden[-1]=forbidden[-1].replace('\n','')

path=[]
expanded=[]
fringe=[]
root=Node()
root.nodedata=start
fringe.append(root)
#print(forbidden)
#print(expanded)

def BFS():
    while (len(expanded)<1000):
        changebuffer=[-100,+100,-10,+10,-1,+1]
        if (fringe==[]):
            break
        else:
            running=fringe.pop(0)
        check1=True
        for x in expanded:
            if x.nodedata==running.nodedata and x.digit==running.digit:
                check1=False
        if check1==True:
            expanded.append(running)
        #print("g data",running.nodedata)
        if int(running.nodedata)==int(end):
            break
        if (running.digit==0):
            if(running.nodedata[0]=='0'):
                changebuffer.remove(-100)
            if(running.nodedata[0]=='9'):
                changebuffer.remove(+100)
            if(running.nodedata[1]=='0'):
                changebuffer.remove(-10)
            if(running.nodedata[1]=='9'):
                changebuffer.remove(+10)
            if(running.nodedata[2]=='0'):
                changebuffer.remove(-1)
            if(running.nodedata[2]=='9'):
                changebuffer.remove(+1)
            for x in changebuffer:
                if(x==100 or x==-100):
                    expand(fringe,int(running.nodedata)+x,running,1)
                if(x==10 or x==-10):
                    expand(fringe,int(running.nodedata)+x,running,2)
                if(x==1 or x==-1):
                    expand(fringe,int(running.nodedata)+x,running,3)
        if (running.digit==1):

            changebuffer.remove(-100)
            changebuffer.remove(+100)
            if(running.nodedata[1]=='0'):
                changebuffer.remove(-10)
            if(running.nodedata[1]=='9'):
                changebuffer.remove(+10)
            if(running.nodedata[2]=='0'):
                changebuffer.remove(-1)
            if(running.nodedata[2]=='9'):
                changebuffer.remove(+1)
            for x in changebuffer:
                if(x==100 or x==-100):
                    expand(fringe,int(running.nodedata)+x,running,1)
                if(x==10 or x==-10):
                    expand(fringe,int(running.nodedata)+x,running,2)
                if(x==1 or x==-1):
                    expand(fringe,int(running.nodedata)+x,running,3)
        if (running.digit==2):
            changebuffer.remove(-10)
            changebuffer.remove(+10)
            if(running.nodedata[0]=='0'):
                changebuffer.remove(-100)
            if(running.nodedata[0]=='9'):
                changebuffer.remove(+100)
            if(running.nodedata[2]=='0'):
                changebuffer.remove(-1)
            if(running.nodedata[2]=='9'):
                changebuffer.remove(+1)
            for x in changebuffer:
                if(x==100 or x==-100):
                    expand(fringe,int(running.nodedata)+x,running,1)
                if(x==10 or x==-10):
                    expand(fringe,int(running.nodedata)+x,running,2)
                if(x==1 or x==-1):
                    expand(fringe,int(running.nodedata)+x,running,3)
        if (running.digit==3):
            changebuffer.remove(-1)
            changebuffer.remove(+1)
            if(running.nodedata[0]=='0'):
                changebuffer.remove(-100)
            if(running.nodedata[0]=='9'):
                changebuffer.remove(+100)
            if(running.nodedata[1]=='0'):
                changebuffer.remove(-10)
            if(running.nodedata[1]=='9'):
                changebuffer.remove(+10)
            for x in changebuffer:
                if(x==100 or x==-100):
                    expand(fringe,int(running.nodedata)+x,running,1)
                if(x==10 or x==-10):
                    expand(fringe,int(running.nodedata)+x,running,2)
                if(x==1 or x==-1):
                    expand(fringe,int(running.nodedata)+x,running,3)
            #print(expanded[0].nodedata)
    buffernode=expanded[len(expanded)-1]
    while True:
        path.append(buffernode.nodedata)
        if(buffernode.parent==None):
            break
        else:
            buffernode=buffernode.parent
    path.reverse()
    '''for x in fringe:
        print("f data:",x.nodedata)

    for y in expanded:
        print("expanded1:",y.nodedata)'''


def DFS():
    while(len(expanded)<1000):
        changebuffer=[+1,-1,+10,-10,+100,-100]
        if(fringe==[]):
            break
        else:
            running=fringe.pop(-1)
        check1=True
        for x in expanded:
            if x.nodedata==running.nodedata and x.digit==running.digit:
                check1=False
        if check1==True:
            expanded.append(running)
            if int(running.nodedata)==int(end):
                break
            if (running.digit==0):
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==1):

                changebuffer.remove(-100)
                changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==2):
                changebuffer.remove(-10)
                changebuffer.remove(+10)
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==3):
                changebuffer.remove(-1)
                changebuffer.remove(+1)
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
    buffernode=expanded[len(expanded)-1]
    while True:
        path.append(buffernode.nodedata)
        if(buffernode.parent==None):
            break
        else:
            buffernode=buffernode.parent
    path.reverse()


def IDS():
    limit=0
    expandedI=[]
    while(len(expanded)<1000):
        changebuffer=[+1,-1,+10,-10,+100,-100]
        if(len(fringe)==0):
            limit+=1
            fringe.append(root)
            expandedI=[]
        running=fringe.pop(-1)
        check1=True
        for x in expandedI:
            if x.nodedata==running.nodedata and x.digit==running.digit:
                check1=False
        if check1==True:
            expandedI.append(running)
            expanded.append(running)
            if int(running.nodedata)==int(end):
                break

            generation=0
            buffer1node=running
            while(True):
                if(buffer1node.parent!=None):
                    generation+=1
                    buffer1node=buffer1node.parent
                else:
                    break

            if(generation<limit):
                if (running.digit==0):
                    if(running.nodedata[0]=='0'):
                        changebuffer.remove(-100)
                    if(running.nodedata[0]=='9'):
                        changebuffer.remove(+100)
                    if(running.nodedata[1]=='0'):
                        changebuffer.remove(-10)
                    if(running.nodedata[1]=='9'):
                        changebuffer.remove(+10)
                    if(running.nodedata[2]=='0'):
                        changebuffer.remove(-1)
                    if(running.nodedata[2]=='9'):
                        changebuffer.remove(+1)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)

                if (running.digit==1):
                    changebuffer.remove(-100)
                    changebuffer.remove(+100)
                    if(running.nodedata[1]=='0'):
                        changebuffer.remove(-10)
                    if(running.nodedata[1]=='9'):
                        changebuffer.remove(+10)
                    if(running.nodedata[2]=='0'):
                        changebuffer.remove(-1)
                    if(running.nodedata[2]=='9'):
                        changebuffer.remove(+1)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)

                if (running.digit==2):
                    changebuffer.remove(-10)
                    changebuffer.remove(+10)
                    if(running.nodedata[0]=='0'):
                        changebuffer.remove(-100)
                    if(running.nodedata[0]=='9'):
                        changebuffer.remove(+100)
                    if(running.nodedata[2]=='0'):
                        changebuffer.remove(-1)
                    if(running.nodedata[2]=='9'):
                        changebuffer.remove(+1)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)

                if (running.digit==3):
                    changebuffer.remove(-1)
                    changebuffer.remove(+1)
                    if(running.nodedata[0]=='0'):
                        changebuffer.remove(-100)
                    if(running.nodedata[0]=='9'):
                        changebuffer.remove(+100)
                    if(running.nodedata[1]=='0'):
                        changebuffer.remove(-10)
                    if(running.nodedata[1]=='9'):
                        changebuffer.remove(+10)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)
    buffernode=expanded[len(expanded)-1]
    while True:
        path.append(buffernode.nodedata)
        if(buffernode.parent==None):
            break
        else:
            buffernode=buffernode.parent
    path.reverse()


def Greedy():
    while(len(expanded)<1000):
        changebuffer=[-100,+100,-10,+10,-1,+1]
        if(fringe==[]):
            break
        buffernode=None
        value=1000
        for n in fringe:
            #print(n.nodedata)
            valuebuf=abs(int(n.nodedata[0])-int(end[0]))+abs(int(n.nodedata[1])-int(end[1]))+abs(int(n.nodedata[2])-int(end[2]))
            if(valuebuf<=value):
                buffernode=n
                value=valuebuf
        #print("I am out")
        fringe.remove(buffernode)
        running=buffernode
        #print(running.nodedata)
        check1=True
        for x in expanded:
            if x.nodedata==running.nodedata and x.digit==running.digit:
                check1=False
        if check1==True:
            expanded.append(running)
            if int(running.nodedata)==int(end):
                break
            if (running.digit==0):
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==1):

                changebuffer.remove(-100)
                changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)

            if (running.digit==2):
                changebuffer.remove(-10)
                changebuffer.remove(+10)
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==3):
                changebuffer.remove(-1)
                changebuffer.remove(+1)
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
    buffernode=expanded[len(expanded)-1]
    while True:
        path.append(buffernode.nodedata)
        if(buffernode.parent==None):
            break
        else:
            buffernode=buffernode.parent
    path.reverse()

def hill():
    current_V=100
    Nosol_buffer=False
    while(len(expanded)<1000):
        changebuffer=[-100,+100,-10,+10,-1,+1]
        if(fringe==[]):
            break

        if(len(fringe)==1):
            running=fringe.pop(0)
            check1=True
            for x in expanded:
                if x.nodedata==running.nodedata and x.digit==running.digit:
                    check1=False
            if check1==True:
                expanded.append(running)
                if int(running.nodedata)==int(end):
                    break
                current_V=abs(int(running.nodedata[0])-int(end[0]))+abs(int(running.nodedata[1])-int(end[1]))+abs(int(running.nodedata[2])-int(end[2]))
                if (running.digit==0):
                    if(running.nodedata[0]=='0'):
                        changebuffer.remove(-100)
                    if(running.nodedata[0]=='9'):
                        changebuffer.remove(+100)
                    if(running.nodedata[1]=='0'):
                        changebuffer.remove(-10)
                    if(running.nodedata[1]=='9'):
                        changebuffer.remove(+10)
                    if(running.nodedata[2]=='0'):
                        changebuffer.remove(-1)
                    if(running.nodedata[2]=='9'):
                        changebuffer.remove(+1)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)
                if (running.digit==1):

                    changebuffer.remove(-100)
                    changebuffer.remove(+100)
                    if(running.nodedata[1]=='0'):
                        changebuffer.remove(-10)
                    if(running.nodedata[1]=='9'):
                        changebuffer.remove(+10)
                    if(running.nodedata[2]=='0'):
                        changebuffer.remove(-1)
                    if(running.nodedata[2]=='9'):
                        changebuffer.remove(+1)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)
                if (running.digit==2):
                    changebuffer.remove(-10)
                    changebuffer.remove(+10)
                    if(running.nodedata[0]=='0'):
                        changebuffer.remove(-100)
                    if(running.nodedata[0]=='9'):
                        changebuffer.remove(+100)
                    if(running.nodedata[2]=='0'):
                        changebuffer.remove(-1)
                    if(running.nodedata[2]=='9'):
                        changebuffer.remove(+1)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)
                if (running.digit==3):
                    changebuffer.remove(-1)
                    changebuffer.remove(+1)
                    if(running.nodedata[0]=='0'):
                        changebuffer.remove(-100)
                    if(running.nodedata[0]=='9'):
                        changebuffer.remove(+100)
                    if(running.nodedata[1]=='0'):
                        changebuffer.remove(-10)
                    if(running.nodedata[1]=='9'):
                        changebuffer.remove(+10)
                    for x in changebuffer:
                        if(x==100 or x==-100):
                            expand(fringe,int(running.nodedata)+x,running,1)
                        if(x==10 or x==-10):
                            expand(fringe,int(running.nodedata)+x,running,2)
                        if(x==1 or x==-1):
                            expand(fringe,int(running.nodedata)+x,running,3)
        else:
            buffernode=None
            value=100
            for n in fringe:
                #expanded.append(n)
                #print("L",n.nodedata)
                valuebuf=abs(int(n.nodedata[0])-int(end[0]))+abs(int(n.nodedata[1])-int(end[1]))+abs(int(n.nodedata[2])-int(end[2]))
                #print('V',valuebuf)
                if(valuebuf<=value):
                    buffernode=n
                    value=valuebuf
            if(value<=current_V):
                fringe.clear()
                fringe.append(buffernode)
            else:
                Nosol_buffer=True
                break
    if(Nosol_buffer==False and len(expanded)<1000):
        buffernod=expanded[len(expanded)-1]
        while True:
            path.append(buffernod.nodedata)
            if(buffernod.parent==None):
                break
            else:
                buffernod=buffernod.parent
        path.reverse()

        i3=0
        for z in path:
            print(z,end='')
            if i3==(len(path)-1):
                print()
            else:
                print(',',end='')
            i3+=1
    else:
        print("No solution found")

def A_star():
    while(len(expanded)<1000):
        changebuffer=[-100,+100,-10,+10,-1,+1]
        if(fringe==[]):
            break
        buffernode=None
        value=1000
        for n in fringe:
            #print(n.nodedata)
            valuebuf=abs(int(n.nodedata[0])-int(end[0]))+abs(int(n.nodedata[1])-int(end[1]))+abs(int(n.nodedata[2])-int(end[2]))+height(n)
            if(valuebuf<=value):
                buffernode=n
                value=valuebuf
        #print("I am out")
        fringe.remove(buffernode)
        running=buffernode
        #print(running.nodedata)
        check1=True
        for x in expanded:
            if x.nodedata==running.nodedata and x.digit==running.digit:
                check1=False
        if check1==True:
            expanded.append(running)
            if int(running.nodedata)==int(end):
                break
            if (running.digit==0):
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==1):

                changebuffer.remove(-100)
                changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)

            if (running.digit==2):
                changebuffer.remove(-10)
                changebuffer.remove(+10)
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[2]=='0'):
                    changebuffer.remove(-1)
                if(running.nodedata[2]=='9'):
                    changebuffer.remove(+1)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
            if (running.digit==3):
                changebuffer.remove(-1)
                changebuffer.remove(+1)
                if(running.nodedata[0]=='0'):
                    changebuffer.remove(-100)
                if(running.nodedata[0]=='9'):
                    changebuffer.remove(+100)
                if(running.nodedata[1]=='0'):
                    changebuffer.remove(-10)
                if(running.nodedata[1]=='9'):
                    changebuffer.remove(+10)
                for x in changebuffer:
                    if(x==100 or x==-100):
                        expand(fringe,int(running.nodedata)+x,running,1)
                    if(x==10 or x==-10):
                        expand(fringe,int(running.nodedata)+x,running,2)
                    if(x==1 or x==-1):
                        expand(fringe,int(running.nodedata)+x,running,3)
    buffernode=expanded[len(expanded)-1]
    while True:
        path.append(buffernode.nodedata)
        if(buffernode.parent==None):
            break
        else:
            buffernode=buffernode.parent
    path.reverse()



if algorithm=='B':
    BFS()
    #print(path)
    index=0
    if(len(expanded)<1000):
        for z in path:
            print(z,end='')
            if index==(len(path)-1):
                print()
            else:
                print(',',end='')
            index+=1
    else:
        print("No solution found")
    j=0
    for y in expanded:
        #print("#",j)
        #print(" ")
        print(y.nodedata,end='')
        if j!=(len(expanded)-1):
            print(',',end='')
        j+=1

if algorithm=='D':
    DFS()
    index=0
    if(len(expanded)<1000):
        for z in path:
            print(z,end='')
            if index==(len(path)-1):
                print()
            else:
                print(',',end='')
            index+=1
    else:
        print("No solution found")
    j=0
    for y in expanded:
        #print("#",j)
        #print(" ")
        print(y.nodedata,end='')
        if j!=(len(expanded)-1):
            print(',',end='')
        j+=1
    #print("J: ",j)
if algorithm=='I':
    IDS()
    index=0
    #print(path)
    if(len(expanded)<1000):
        for z in path:
            print(z,end='')
            if index==(len(path)-1):
                print()
            else:
                print(',',end='')
            index+=1
        #print("index: ",index)

    else:
        print("No solution found")
    j=0
    for y in expanded:
        #print("#",j)
        #print(" ")
        print(y.nodedata,end='')
        if j!=(len(expanded)-1):
            print(',',end='')
        j+=1
    #print("J: ",j)

if algorithm=='G':
    Greedy()
    index=0
    if(len(expanded)<1000):
        for z in path:
            print(z,end='')
            if index==(len(path)-1):
                print()
            else:
                print(',',end='')
            index+=1
            #print("index: ",index)

    else:
        print("No solution found")
    j=0
    for y in expanded:
            #print("#",j)
            #print(" ")
        print(y.nodedata,end='')
        if j!=(len(expanded)-1):
            print(',',end='')
        j+=1
        #print("J: ",j)
if algorithm=='H':
    hill()
    j=0
    for y in expanded:
        #print("#",j)
        #print(" ")
        print(y.nodedata,end='')
        if j!=(len(expanded)-1):
            print(',',end='')
        j+=1
if algorithm=='A':
    A_star()
    index=0
    #print(path)
    if(len(expanded)<1000):
        for z in path:
            print(z,end='')
            if index==(len(path)-1):
                print()
            else:
                print(',',end='')
            index+=1
        #print("index: ",index)

    else:
        print("No solution found")
    j=0
    for y in expanded:
        #print("#",j)
        #print(" ")
        print(y.nodedata,end='')
        if j!=(len(expanded)-1):
            print(',',end='')
        j+=1
