
from random import choice as cho
from time import time

deck = [2,3,4]*8+[5,6,7,8,9,10,11]*4
print("Blackjack not losing probability simulator")
times = int(input("How many games should I simulate? "))

def main(track_score):
  list_main = []; happnd = 0
  for i in range(times):
    cards = deck[:]
    score = 0
    list_iter = []
    r = cho(cards);cards.remove(r);score += r
    r = cho(cards);cards.remove(r);score += r
    if score >= 21:
      ends = True
    else:
      ends = False
    while ends == False:
      if score == track_score:
        happnd += 1
        list_main += [happnd]
        while ends == False:
          r = cho(cards);cards.remove(r);score += r
          list_iter += [score]
          if score >= 21:
            list_main[happnd-1] = list_iter
            ends = True
      r = cho(cards);cards.remove(r)
      score += r
      if score >= 21:
        ends = True
  return list_main

not_lose_prob = []
start = time()
for i in range(11,21):
  not_lose = 0
  xx = main(i)
  twentyones = [j for j in xx if j==[21]]
  not_loses = [j for j in xx if len(j)>1]
  not_lose = len(twentyones)+len(not_loses)
  #for j in xx:
  #  if j[0] == [21] or len(j) > 1:
  #    not_lose += 1
  not_lose_prob += [not_lose*100/len(xx)]
time_op = time()-start

print("[Points right now, Probability of not losing with next card]")
for points, prob in enumerate(not_lose_prob,11):
  print("For",points,"points, probabilty of not losing with next card is",round(prob,3),"%")
print("Calculated in ",time_op,"s.",sep="")


#1000000:
#[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 91.83553576350107, 84.06544676744095, 76.59137811121118, 68.7132279835776, 61.090550067264445, 53.28710455045981, 45.79943786847036, 30.518850317282567, 15.212944969150316, 0.0, 0.0]

#10000000:
#[100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 91.9413502903184, 84.1877544847332, 76.60945904320947, 68.721694982861, 61.004103919791746, 53.33456432004861, 45.74171199541941, 30.452071732100872, 15.179250753065293, 0.0, 0.0]