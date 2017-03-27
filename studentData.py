#Nancy Mariano
#01/17/2017


import sys 
import os  

#checks for empty or nonexistent file
def checkRun(studInfoFile):

    try:
        return(os.path.exists(studInfoFile) or os.path.getsize(studInfoFile) > 0)
    
    except: 
        return False 

def addStudent(studInfo, idNum, fName, lName, department, numClasses, courseInfo): 

    studInfoList = open(studInfo, "a")
    studInfoList.write(idNum + " ") 
    studInfoList.write(fName + " ")
    studInfoList.write(lName + " ")
    studInfoList.write(department + " ")
    studInfoList.write(numClasses + " ")
    for value in courseInfo: 
        studInfoList.write(value + " ")
    studInfoList.write("\n")
    studInfoList.close() 

def processFile(studInfoFile): 
    studInfoList = open(studInfoFile, "r")
    studInfo = studInfoList.readlines()
    splitInfo = [] 
    
    for x in studInfo:       
        temp = x.split() 
        temp = mkSubDict(temp)
        splitInfo.append(temp)
        
    return splitInfo 
        
    
    

#additionalParseFile
#creates a dictionary for each student
def mkSubDict(currentStudent):

    sID = 0
    fName = 1
    lName = 2
    major = 3
    numClasses = 4     
    classInfo = 5 
        

    newSubDict = {'id':currentStudent[sID], 
                  'lName':currentStudent[lName],
                  'fName':currentStudent[fName],
                  'major':currentStudent[major], 
                  'numClasses':currentStudent[numClasses], 
                  }

    #makes a list of lists within class info
    #each list contains information for one course
    if (currentStudent[numClasses] == '0'):  
        newSubDict['classInfo'] = 'None' 
    else :
        temp = currentStudent[classInfo:]
        temp = [temp[x:x+4] for x in range(0,len(temp),4)]
        newSubDict['classInfo'] = temp   

    return newSubDict 


def createStudentDict(studentInfo):

    numStudents = len(studentInfo)
    studentDict = {} 

    for element in studentInfo:
        currentID = element.get('id')
        currentClasses = element.get('classInfo')
        studentDict[currentID] = (element.get('major'),processGPA(currentClasses))

    return studentDict 

def processGPA(currentClasses): 

    gpa = 0
    totalCred = 0
    gpaPoints = 0 
    counter = 0 

    gpaDict = {'A': 4.0, 'A-': 3.7, 
               'B+': 3.3, 'B': 3.0, 'B-': 2.7,
               'C+': 2.3, 'C': 2.0, 'C-': 1.7,
               'D+': 1.3, 'D': 1.0, 'D-': 0.7,
               'F': 0
    } 

    if(currentClasses != 'None'):
        for element in currentClasses:
            totalCred += int(element[2])
            gpaPoints += (gpaDict.get(element[3]) * int(element[2])) 
        gpa = (gpaPoints/ totalCred)

    return gpa 
        
def createRoster(studentInfo, department, course): 
    roster = []
    
    for student in studentInfo:
        thisInfo = student.get('classInfo')
       
        for element in thisInfo: 
            if(element[0] == department and element[1] == course):
                    roster.append((student.get('id'), student.get('fName'), 
                                   student.get('lName'), element[3]))

    return roster 

def createCourseSet(studentInfo, department):
    courseSet = [] 

    for student in studentInfo: 
        thisInfo = student.get('classInfo')

        for element in thisInfo:
            if (element[0] == department):
                courseSet.append(department + " " + element[1])

    courseSet = set(courseSet) 
    return courseSet

def printStudents(studentInfo, studentDict):
    studentInfo = sorted(studentInfo, key = lambda k: k['id'])
    
    for student in studentInfo:
        sID = student.get('id')
        print(sID, student.get('fName'), student.get('lName'),
              studentDict[sID][0], studentDict[sID][1])
        print()


#1 
#assuming command line will be run like: python3 hw1.py testFile.txt
studInfoFile = sys.argv[1]  
if(checkRun(studInfoFile)):

#2 
    addStudent(studInfoFile, '7444', 'Bob', 'Dole', 'History', '1', ['CPSC', '1430', '5', 'D-'])
#3
    masterInfo = processFile(studInfoFile) 
#4
    print("Step 4:")
    print()
    print(masterInfo)
    print() 
    print()
    print()
#5
    masterDict = createStudentDict(masterInfo)
#6 
    print("Step 6:")
    print()
    print(masterDict)
    print() 
    print()
    print()

#7
    cpsc1420Roster = createRoster(masterInfo, 'CPSC', '1420')

#8
    print("Step 8:")
    print()
    print(cpsc1420Roster) 
    print()
    print()
#9
    math2340Roster = createRoster(masterInfo, 'Math', '2340')

#10
    print("Step 10:")
    print() 
    print(math2340Roster)
    print()
    print()

#11
    cpscCourseSet = createCourseSet(masterInfo, 'CPSC') 

#12
    print("Step 12:")
    print()
    print(cpscCourseSet) 
    print()
    print()

#13
    print("Step 13:") 
    print()
    printStudents(masterInfo, masterDict)  
    print()
    print()

else: 
    print("File empty or does not exist. Program abort...")
