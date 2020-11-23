def getMultiplesOfFive(num):
    numToString = str(num)
    if len(numToString) < 2:
        numToString = '0' + numToString

    zeros = len(numToString) - 1
    times = int('1' + '0' * zeros)

    multiple_1 = (int(numToString[0]) + 1) * times
    multiple_2 = multiple_1 - 5

    return [multiple_2, multiple_1]

def getRoundedGrade(multiple, grade):
    rounded = grade

    diff = multiple - grade

    if diff < 3:
        rounded = multiple
    else:
        rounded = grade
  
    return rounded

def gradingStudents(grades):
    roundedGrades = []

    for grade in grades:
        if grade % 5 == 0 or grade < 38:
            roundedGrades.append(grade)
        else:
            multiples = getMultiplesOfFive(grade)
            roundedNum = 0

            if grade > multiples[0]:
                roundedNum = getRoundedGrade(multiples[1], grade)
            else:
                roundedNum = getRoundedGrade(multiples[0], grade)
            
            roundedGrades.append(roundedNum)

    return roundedGrades

def main(): 
    print('Grading Students script')

    totalGrades = int(input('Enter the total grades tha will be rounded: '))

    gradesToRound = []

    for _ in range(0, totalGrades):
        newGrade = int(input('Enter a grade between 0 and 100: '))
        gradesToRound.append(newGrade)

    print('INPUT GRADES: ', gradesToRound)

    result = gradingStudents(gradesToRound)

    print('OUTPUT GRADES: ', result)

# Call main() function.
if __name__ == '__main__':
  main()