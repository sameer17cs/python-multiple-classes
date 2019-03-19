# MultiClass
- It is a small library helps to create mulitple classes from a template class
- If you have a use-case where you have a class, and you want to create multiple classes of same type with different names and usage
- Works with ```python3```
# FYI
- This library was created when i was working with a very specific (or wierd)  use case of creating multiple classes

# How To Use
 1) Create your class to be used as template, example ```TemplateClass``` 
 2) Import ```MultiClass```
     ```sh
     import multiClass
    multiClassObject = multiClass.MultiClass(TemplateClass)
     ```
3) Create classes using ```name-prefix``` and ```count``` of classes
     ```sh
     classArray = multiClassObject.create("Template",10)
     ```
     1) It will return an array of size ```count```
     2) Each array element is a class of type ```TemplateClass```
     3) Name of classes will be ```name-prefix1```,```name-prefix2```,```name-prefix3```...
     
3) Create classes using array of class name
     ```sh
     nameArray = ["classNameA","classNameB","classNameC","classNameD"]
     classArray = multiClassObject.create(nameArray)
     ```
     1) It will return an array
     2) Each array element is a class of type ```TemplateClass```
     3) Name of classes will be taken from nameArray (in order)

