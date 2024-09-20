boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
counts = zip(boys, girls)
for count in counts:
    print(
        f"{boys[0]} и {girls[0]}\n{boys[1]} и {girls[1]}\n{boys[2]} и {girls[2]}\n{boys[3]} и {girls[3]}\n{boys[4]} и {girls[4]}")
    break
