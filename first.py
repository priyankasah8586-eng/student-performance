import matplotlib.pyplot as plt

subjects = ['Math', 'Science', 'English', 'History', 'Art']
scores = [85, 90, 78, 92, 88]

plt.bar(subjects, scores)
plt.xlabel('Subjects')
plt.ylabel('Scores')
plt.title('Student Performance')
plt.show()
