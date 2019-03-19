class MultiClass:
  def __init__(self, templateClass):

    self.templateClass = templateClass

    self.allObjects = {}

    for key in templateClass.__dict__:

        if callable(templateClass.__dict__.get(key)):
              self.allObjects[key] = templateClass.__dict__.get(key)

  def create(self,name, *args):
      multiClassArray = []
      if (isinstance(name, str)):
          for i in range(1,args[0]+1):
              oneClass = type(name + str(i), (self.templateClass,),self.allObjects)
              multiClassArray.append(oneClass)
      else:
          for i in name:
              oneClass = type(i, (self.templateClass,),self.allObjects)
              multiClassArray.append(oneClass)

      return multiClassArray


