"""Consider a list (list = []). You can perform the following commands:

insert i, e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list."""
if __name__ == '__main__':
    N = int(input())
    li=[]
    for _ in range(N):
        cmd=map(str,input().split()) 
        cmd_list=list(cmd)
        if cmd_list[0]=='insert':
           li.insert(int(cmd_list[1]),int(cmd_list[2]))
        elif cmd_list[0]=='print':
            print(li)   
        elif cmd_list[0]=='remove':
            li.remove(int(cmd_list[1]))
        elif cmd_list[0]=='append':
            li.append(int(cmd_list[1]))    
        elif cmd_list[0]=='sort':
            li.sort()  
        elif cmd_list[0]=='pop':
            li.pop()
        elif cmd_list[0]=='reverse':
            li.reverse()                  
        
   
