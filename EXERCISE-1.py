score1 = float(input("Enter the score for test 1: "))
score2 = float(input("Enter the score for test 2: "))
score3 = float(input("Enter the score for test 3: "))
average = (score1 + score2 + score3) / 3
print("The average score is: {:.2f}".format(average))
if average > 95:
    print("Excellent performance!")
    print("Keep up the great work!")