#John Matukutire
#11303324
#CMPT 145 CRN 27177
#L16

#Importing Queue ADT
from Queue.py import Queue

def main():
    q = Queue
    file = open("monsters2.txt","r")
    character = file.readline().strip()
    godzilla_defeat = ""
    mothra_defeat = ""
    while character:
        if character == "Godzilla":
            if not q.is_empty():
                godzilla_defeat += q.dequeue + "\n"
        elif character == "Mothra":
            if not q.is_empty():
                mothra_defeat += q.dequeue + "\n"
