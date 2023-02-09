print('Welcome!')
print('This is a quiz game')

q_no = 0
score = 0

wanna_play = input('Do you want to play the qiuz? (y or n) : ').lower()
print(wanna_play)
if wanna_play == 'y':
    print('Okay! \n')
else:
    print('Quiz will be quit.')
    quit()

rules = ('Note : the spellings & spacings of the answers should be correct. \n')
print(rules)

#-------q1

q1 = input('What does "IT" stands for : ').lower()
if q1 == ('information technology'):
    q_no += 1
    score += 1
    print('Hurray!')
    print(f'you completed {q_no} question and got {score}')
else:
    print('The correct answer is "Information Technology" ')
    q_no += 1
    print(f'you completed {q_no} question and got {score}')

print()

#-------q2

q2 = input('What does "HTML" stands for : ').lower()
if q2 == ('hyper text markup language'):
    q_no += 1
    score += 1
    print('Hurray!')
    print(f'you completed {q_no} question and got {score}')
else:
    print('The correct answer is "Hyper Text Markup Language" ')
    q_no += 1
    print(f'you completed {q_no} question and got {score}')

print()

#-------q3

q3 = input('What does "GPU" stands for : ').lower()
if q3 == ('graphical processing unit'):
    q_no += 1
    score += 1
    print('Hurray!')
    print(f'you completed {q_no} question and got {score}')
else:
    print('The correct answer is "Graphical Processing Unit" ')
    q_no += 1
    print(f'you completed {q_no} question and got {score}')

print()

#-------q4

q4 = input('What does "RAM and ROM" stands for : (separate answer by ", ") ').lower()
if q4 == ('random access memory, read only memory'):
    q_no += 1
    score += 1
    print('Hurray!')
    print(f'you completed {q_no} question and got {score}')
else:
    print('The correct answer is "random access memory, read only memory" ')
    q_no += 1
    print(f'you completed {q_no} question and got {score}')

print()

#-------q5

q5 = input('What does "PHP stands for? ').lower()
if q5 == ("hypertext preprocessor"):
    q_no += 1
    score += 1
    print('Hurray!')
    print(f'you completed {q_no} question and got {score}')
else:
    print('The correct answer is "hypertext preprocessor" ')
    q_no += 1
    print(f'you completed {q_no} question and got {score}')

#-------total

print(f'\nnumber of question completed is {q_no}')
print(f'your score is {score} !!!')

try:
    percentage = (score *100) /  q_no

except ZeroDivisionError:
    print('0% quetions are correct')

print(f'{percentage}% questions are correct.')

