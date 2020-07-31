# Use this playground to experiment with list methods, using Test Run

name = 'Ejiro'
student = name
name = 'John'

print(name)
print(student)

scores = ['A', 'B', 'A', 'F', 'A']
grades = scores
scores = ['B', 'B', 'B', 'A']

print(scores)
print(grades)
print(len(scores))
print(max(scores))
print(min(scores))
print(min(grades))
print(sorted(scores))
print(sorted(grades, reverse=True))