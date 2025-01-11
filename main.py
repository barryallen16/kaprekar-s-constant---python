def get_lowNum(numArray):
    numArray.sort()
    Lownum = "".join([str(x) for x in numArray])
    Lownum=int(Lownum)
    return Lownum
def get_highnum(numArray):
    numArray.sort(reverse=True)
    Highnum="".join([str(x) for x in numArray])
    Highnum=int(Highnum)
    return Highnum
def convert_intToArray(current_num):
    conv_str=str(current_num)
    current_array=[]
    for digits in conv_str:
        current_array.append(digits)
    return current_array
def KaprekarsConstant(subResult):
    number = subResult
    iteration =0
    while subResult!=6174:
        conv_arrayno = convert_intToArray(subResult)
        while len(conv_arrayno) != 4:
            conv_arrayno.append('0')
        highnumber = get_highnum(conv_arrayno)
        lownumber = get_lowNum(conv_arrayno)
        if highnumber==lownumber:
            break
        subResult = highnumber - lownumber
        iteration+=1
        if iteration == 7:
            break
    return iteration
iterationGroup = {}
results={}
for i in range(1000,10000):
    iteration=KaprekarsConstant(i)
    if iteration not in iterationGroup:
        iterationGroup[iteration]=[]
    iterationGroup[iteration].append(i)
sortedGroup={k: iterationGroup[k] for k in sorted(iterationGroup)}
for iteration,numbers in sortedGroup.items():
    if iteration!=0:
        print(f"Numbers that take {iteration} iterations to reach 6174 : {len(numbers)} ")
        #uncomment the following line to see the actual numbers
        #print(numbers)
if 0 in iterationGroup:
    print("\nNumbers that does not obey kaprekar's constant..")
    print(sortedGroup[0])
