#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    name_list=[]
    score_list=[]
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        name_list.append(name)
        score_list.append(score)
    score_list=list(set(score_list))
    score_list.sort()
    sec=score_list[1]
    out=[i[0] for i in records if i[1]==sec] 
    out.sort()
    for i in out:
        print(i)      
     
        
        

