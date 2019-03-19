import multiClass

class Template:
  def __init__(self, offset):
    self.offset = offset

  counter=0

  def showOffset(self):
      self.counter = self.counter + 1
      print(str(self.offset) + "-" + str(self.counter))


classNamePrefix = 'Template'
countOfClasses = 10
classNameArray = ['mClass1','mClass2','mClass3','mClass4']

# create MultiClass instance
multiClassObject = multiClass.MultiClass(Template)

# create classes by name prefix and count
multiClassArray1 = multiClassObject.create('Template',10)
for i,j in enumerate(multiClassArray1):
    print('class with name prefix:' + j.__name__)

# create classes by classNameArray
multiClassArray2 = multiClassObject.create(classNameArray)
for i,j in enumerate(multiClassArray2):
    print('class with name from array:' + j.__name__)



