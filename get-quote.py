import random
def a():
  print("Keep it logically awesome.1111")
  
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #print(quotes)
  print(quotes[0])
  print(quotes[-1])
  print(quotes[len(quotes)-1])
  last = len(quotes)-1
  rnd = random.randint(0,last)
  print(quotes[rnd])

if __name__== "__main__":
  a()
