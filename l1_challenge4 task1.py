#Task 1a The Office I - Outed
def outed(meet, boss):
  happiness = 0
  counter = 0
  for k,v in meet.items():
      counter +=1
      if k == boss:
          happiness += v*2
      else:
          happiness += v
  if happiness/counter <= 5:
      return 'Get Out Now!'
  else:
      return 'Nice Work Champ!'

#Task 1b The Office II - Boredom Score
def boredom(staff):
    scores = {
    "accounts":1,
    "finance":2,
    "canteen":10,
    "regulation":3,
    "trading":6,
    "change":6,
    "IS":8,
    "retail":5,
    "cleaning":4,
    "pissing about":25}
    
    boredom_score = 0
    for dep in staff.values():
        boredom_score += scores.get(dep)
    if boredom_score <= 80:
        return 'kill me now'
    elif boredom_score < 100 and boredom_score > 80:
        return 'i can handle this'
    else:
        return 'party time!!'
