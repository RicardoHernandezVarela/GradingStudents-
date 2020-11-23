def gradingStudents(grades):
  roundedGrades = []

  for grade in grades:
    if grade % 5 == 0 or grade < 38:
      roundedGrades.append(grade)
    else:
      print('Round grades here!!!')

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