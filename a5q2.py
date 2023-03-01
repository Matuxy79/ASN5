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
        else:
            q.enqueue(character)
        
        character = file.readline().strip()

    #printing the result to console once done
    if q.is_empty():
        print("The space monsters were all defeated\n")
        print("Godzilla beat: \n" + godzilla_defeat)
        print("Mothra beat: \n" + mothra_defeat)
    else:
        print("The space monsters won because of " + q.peek())

main()
