def main(): 
    print('MAIN main')

    totalGrades = int(input('Enter the total grades tha will be rounded: '))

    gradesToRound = []

    for _ in range(0, totalGrades):
        newGrade = int(input('Enter a grade between 0 and 100: '))
        gradesToRound.append(newGrade)

    print(gradesToRound)

# Call main() function.
if __name__ == '__main__':
  main()