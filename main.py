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
        # print(digits)
        # digits=int(digits)
        current_array.append(digits)
    return current_array
def KaprekarsConstant(subResult):
    # print(f"trying for number : {subResult}")
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
        # print(f"Lowest number : {lownumber}")
        # print(f"High number: {highnumber}")
        # repeat_process(subResult,iteration)
        subResult = highnumber - lownumber
        iteration+=1
        if iteration == 7:
            break
    # print(f"""iteration :{iteration} - {highnumber} - {lownumber} = {subResult}""")

    print(f"iteration for {number} - {iteration} == {subResult} ")
    return iteration

    # if subResult != 6174:
    #     print(f"iteration for {number} - {iteration} == {subResult} ")
iterresults = {}
results={}
for i in range(1000,10000):
    results[i]=KaprekarsConstant(i)

for number,iteration in results.items():
    if iteration!=0:
        print(f"iteration for {number} - {iteration} ")
print("\n\nThese following numbers does not obey kaprekar's constant")
for number,iteration in results.items():
    if iteration==0:
        print(f"iteration for {number} - {iteration} ")
