def prime(n):
      prime = True
      for i in range(2, n):
          if (n%i == 0):
              return False
              break
      if prime:
              return True
