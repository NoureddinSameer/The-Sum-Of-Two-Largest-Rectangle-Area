'''
Prepared By: eng.Noureddin Sameer Nazir Alzarie
Contact Info: https://linktr.ee/noureddin_sameer_nazir_alzarie
'''
'''This program is to get the sum of areas of the two largest rectangles from a list '''
'''Here I create a function that calculates and returns the sum of the two largest rectangular areas that can be obtained from the list and
name it "TheSumOfTwoLargestRectangleArea" that takes two parameters,
the first parameter is a list and the second parameter is a type of integer and
I use the second parameter as a flag '''
def TheSumOfTwoLargestRectangleArea(fList,flag3):
    '''Here I create(declare) a variable and name it "max1" and I initialized it with zero '''
    max1 =0 #----->C 
    '''Here I create(declare) a variable and name it "flag1" and I initialized it with zero '''
    flag1=0 #----->C 
    '''Here I create(declare) a variable and name it "mfirst" and I initialized it with zero '''
    mfirst=0 #----->C 
    '''Here I create(declare) a variable and name it "flag2" and I initialized it with zero '''
    flag2=0 #----->C 
    '''Here I create(declare) a variable and name it "LHeightsOfFirst" and I initialized it with zero '''
    LHeightsOfFirst=0 #----->C 
    '''Here I use one of types of repetition(for loop),from 0 to the length of fList-1 and increasing by one'''
    for i in range(len(fList)):#----->n  
        '''Here I use one of types of repetition(for loop), from i to the length of fList-1
        and increasing by one'''
        for j in range(i,len(fList)):#----->n  
            '''Here I create(declare) a variable and name it "min1" and I initialized it with
            the value that is stored in fList[i] '''
            min1=fList[i]#----->C 
            '''Here I use one of types of repetition(for loop), from i+1 to j and increasing by one '''
            for y in range(i+1,j+1):#---->n  
                '''Here I use one of the types of selection(if statement) to check if min1 is greater than fList[y]
                if the condition is true, then the instructions that exist inside the if body(block)
                will be executed '''
                if(min1>fList[y]):
                    '''Here I store the value of fList[y] in the variable min1 '''
                    min1=fList[y]#----->C 
            '''Here I store the value of min1 in the variable Hight '''
            Hight=min1 #----->C 
            '''Here I create(declare) a variable and name it "Width" and I initialized it with j-i+1 '''
            Width= j-i+1 #----->C 
            '''Here I use one of the types of selection(if statement) to check if max1 is less than Hight*Width
            if the condition is true, then the instructions that exist inside
            the if body(block) will be executed '''
            if(max1<Hight*Width):
                '''Here I store the value of Hight*Width in the variable max1'''
                max1=Hight*Width #----->C 
            '''Here I use one of the types of selection(if statement) to check if flag1 is equal to zero
            if the condition is true, then the instructions that exist inside the if body(block)
            will be executed '''
            if(flag1==0):
                '''Here I store the value of max1 in the variable mfirst '''
                mfirst=max1 #----->C 
                '''Here I store the value of Hight in the variable LHeightsOfFirst '''
                LHeightsOfFirst=Hight #----->C 
                '''Here I store one in the variable flag1 '''
                flag1=1 #----->C 
            '''Here I use one of the types of selection(if statement) to check if max1 is greater than mfirst
            if the condition is true, then the instructions that exist inside the if body(block)
            will be executed '''
            if(max1>mfirst):
                '''Here I store the value of max1 in the variable mfirst '''
                mfirst=max1 #----->C 
                '''Here I store the value of Hight in the variable LHeightsOfFirst '''
                LHeightsOfFirst=Hight #----->C 
                '''Here I store the value of Width in the variable WfirstW '''
                WfirstW=Width #----->C 
            '''Here I use one of the types of selection(if statement) to check if max1 is equal to mfirst
            and j is not equal to zero if the condition is true, then the instructions that exist inside
            the if body(block) will be executed '''
            if(max1==mfirst and j!=0):
                '''Here I use one of the types of selection(if statement) to check if max1 is equal to Hight*Width
                if the condition is true, then the instructions that exist inside the if body(block)
                will be executed '''
                if(max1==Hight*Width):
                    '''Here I use one of the types of selection(if statement) to check if flag2 is equal to zero
                    if the condition is true, then the instructions that exist inside the if body(block)
                    will be executed '''
                    if(flag2==0):
                        '''Here I store the value of Hight in the variable LHeightsOfFirst '''
                        LHeightsOfFirst=Hight #----->C 
                        '''Here I store the value of Width in the variable WfisrtW '''
                        WfisrtW=Width #----->C
                        '''Here I store one in the variable flag2 '''
                        flag2=1 #----->C 
                    '''Here I use one of the types of selection(if statement) to check if LHeightsOfFirst
                    is greater than Hight if the condition is true, then the instructions that exist inside
                    the if body(block) will be executed '''
                    if(LHeightsOfFirst<Hight):
                        '''Here I store the value of Hight in the variable LHeightsOfFirst '''
                        LHeightsOfFirst=Hight #----->C
                        '''Here I store the value of Width in the variable WfirstW '''
                        WfirstW=Width #----->C
    '''Here I use one of the types of selection(if statement) to check if flag3 is not equal to zero
    if the condition is true, then the instructions that exist inside the if body(block) will be executed '''
    if(flag3!=0):
        '''Here I return the value of max1 '''
        return max1 #----->C
    '''Here I create(declare) a variable and name it "m" and I initialized it with
    the value that is stored in max1 '''
    m=max1
    '''Here I use one of the types of selection(if...else statement) to check if LHeightsOfFirst is
    greater than one if the condition is true, then the instructions that exist inside the if body(block)
    will be executed if the condition is false then the instructions
    that exist inside the else body(block) will be executed '''
    if(LHeightsOfFirst>1):
        '''Here I store zero in the variable count '''
        count=0 #----->C 
        '''Here I use one of types of repetition(for loop), from 0 to the length of fList-1
        and increasing by one'''
        for i in range(len(fList)):#----->n 
            '''Here I use one of the types of selection(if...else statement) to check
            if fList[i] is greater than or equal to LHeightsOfFirst
            if the condition is true, then the instructions that exist inside the if body(block) will be executed
            if the condition is false then the instructions that exist inside
            the else body(block) will be executed '''
            if(fList[i]>=LHeightsOfFirst):
                '''Here I increase the value that is stored in variable count by one '''
                count=count+1 #----->C 
                '''Here I use one of the types of selection(if statement) to check if count is equal to one
                if the condition is true, then
                the instructions that exist inside the if body will be executed '''
                if(count==1):
                    '''Here I create(declare) a variable and name it "index" and I initialized it with i '''
                    index=i #----->C 
            else:
                '''Here I store zero in the variable count '''
                count=0 #----->C 
            '''Here I use one of the types of selection(if statement) to check if count is equal to
            WfirstW if the condition is true, then the instructions that
            exist inside the if body(block) will be executed '''
            if(count==WfirstW ):
                '''Here I use one of types of repetition(for loop), from index to the length of fList-1
                and increasing by one '''
                for j in range(index,len(fList)):
                    '''Here I subtract the value that is stored in LHeightsOfFirst from fList[j] '''
                    fList[j]=fList[j]-LHeightsOfFirst
                    '''Here I subtract one from WfirstW '''
                    WfirstW=WfirstW-1 #----->C
                    '''Here I use one of the types of selection(if statement) to check
                    if WfirstW is equal to zero if the condition is
                    true, then the instructions that exist inside the if body(block) will be executed '''
                    if(WfirstW==0):
                        '''Here I use the break statement that terminates the current loop '''
                        break #----->C
    else:
        '''Here I use one of types of repetition(for loop), from 0 to
        the length of fList-1 and increasing by one '''
        for i in range(len(fList)):
            '''Here I use one of the types of selection(if statement) to
            check if fList[i] is equal to one if the condition is
            true, then the instructions that exist inside the if body(block) will be executed '''
            if(fList[i]==1):
                '''Here I subtract the value that is stored in LHeightsOfFirst from fList[i] '''
                fList[i]=fList[i]-LHeightsOfFirst
                '''Here I subtract one from m '''
                m=m-1 #----->C 
            '''Here I use one of the types of selection(if statement) to check
            if fList[i] is equal to one if the condition is
            true, then the instructions that exist inside the if body(block) will be executed '''
            if(m==0):
                '''Here I use the break statement that terminates the current loop '''
                break #----->C 
    ''' Here I call the function "TheSumOfTwoLargestRectangleArea" that take two arguments and
    then I return the value of (max1 + the value of the second-largest rectangular area that will
    return from calling the function "TheSumOfTwoLargestRectangleArea")
    that represent the sum of the two largest rectangular areas from a list '''
    return max1+TheSumOfTwoLargestRectangleArea(fList,1)
'''Here I create(declare) a variable and name it "n" and I initialized it with the value that I will take it from the user (input)'''
n=eval(input()) #----->C
'''Here I create a list and name it "list" '''
list=[] #----->C
'''Here I use one of types of repetition(for loop), from 0 to n-1 and increasing by one '''
for i in range(n):
    '''Here I add the value that I will take it from the user to list (input) '''
    list=list+[eval(input())] #----->C
'''Here I call the function "TheSumOfTwoLargestRectangleArea" that takes two arguments
and then I print the value that is returned from it (output)'''
print(TheSumOfTwoLargestRectangleArea(list,0)) #----->C 
'''
Samples of the inputs:
#4,2,3,5,7,6,1 ----> The output will be 21
#2,2,3,5,4,5 ----> The output will be 18
#4,5,3,4,3 ----> The output will be 17
#4,2,3,5,4,5 ----> The output will be 18
#2,1,1,3,3 ----> The output will be 9
#2,2,3,5,4,5 ----> The output will be 18
#0,0,1,1 ----> The output will be 2
#0,1,0 ----> The output will be 1
#1,0,1 ----> The output will be 2
#1,1,1 ----> The output will be 3
'''

