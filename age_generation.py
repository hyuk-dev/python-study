born=int(input('What year were you born?'))
korean=str(input('Are you Korean?(y/n) '))
if born > 1954 and born < 1964:
    print('baby boomer')

if born < 1925:
  print('The Greatest Generation')

if born < 1946 and born > 1924:
  print('The Silent Generation')

if born < 1954 and born > 1945:
  if korean=='y':
    print('The Silent Generation')
  else:
    print('baby boomer')