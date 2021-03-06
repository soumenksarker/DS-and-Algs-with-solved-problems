class Node:
   def __init__(self, init_data):
      self.data = init_data
      self.next = None
      
   def get_data(self):
     return self.data
 
   def get_next(self):
     return self.next
    
   def set_data(self, new_data):
      self.data = newdata
      
   def set_next(self, new_next):
      self.next = new_next

class OrderedList():
    def __init__(self):
        self.head = None





        
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.get_data() == item :
                found = True
            else:
               if current.get_next() > item:
                   stop = True
               else:
                   current = current.get_next()
        return found
    def add(self,item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item)
        if previous == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)
l  = []
l.append(OrderedList())
for i in l:
    print(i)
