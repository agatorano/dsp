# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples both are containers that contain an array of elements. However, the difference comes with mutability and the implied significance that comes with that. Tuples are immutable, which means that they are valued by index. Each index represents a generalized piece of information that holds a value (year, age, etc). Lists are bags of information with no order. The only important element of a list is the "name" of the elements. Tuples will work as keys, because they would pair based on the type of information at the index. When used as keys in a dictionary, they would often contain the name of the data that that element will contain. Example: ```{'names':['Mary','John','Allen'],'age':[19,32,15,55]}```

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are the same in that they contain an array of elements, similar also to tuples. What is unique with sets are that they can only contain unique elements and that they do not have fixed orientation. Lists may have mutable orientation, but sets have indices that virtually randomly decided at access time. Finding elements in sets is done more quickly. This is because they are implemented using dictionaries and are therefore keyed hash functions. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> A lamda is a function that is set to a variable. This can be used for creating short simple reusable functions, or to create functions that will be used as arguments in a group of python functions. A simple example would be 
>>```
>>f = lambda x: x*x
>>f(2)
>>4
>>``` 
>>This computes the square of a number. 
>>Another example using sort would be:
>>```
>> x = [1, 9, 7, 86, 5, 4, 6, 7, 3, 2, 1, 3, 4]
>> sorted(x, key=lambda x: x%2==0)
>> [1, 9, 7, 5, 7, 3, 1, 3, 86, 4, 6, 2, 4]
>>```
>> this seperates the even and odd numbers. It sorts based on wheter a number is divisible by 2. 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension gives you a way to create lists using a custom function. It is similar to lambda in that it is a way to implement a light weight function that you can create in line. The function in this case just places items into a list. 
>>
>> Here is a simple example:
>>```
>>a = [x for x in range(20)]
>>0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>```
>> It can also be used to replace map
>> ```
>> x = [1,2,3,4,5,6,7,8]
>> new_list = [i+2 for i in x]
>> [3, 4, 5, 6, 7, 8, 9, 10]
>> x = [1,2,3,4,5,6,7,8]
>> y = lambda x: x+2
>> x = map(y,x)
>> [3, 4, 5, 6, 7, 8, 9, 10]
>> ```
>> It can also be used to replace Filter
>> ``` 
>> x = [1,2,3,4,5,6,7,8]
>> x = [i for i in x if i%2]
>> [1, 3, 5, 7]
>> x = [1,2,3,4,5,6,7,8]
>> x = filter(lambda x:x%2, x)
>>```
>>
>> These are identical functions. List comprehensions can be clearer at times but filter/map can be a shorter function. 
>>
>> Set and Dictionary comprehensions are just as easy to do
>>```
>> x = [1,1,1,2,2,2,2,3,3,3,3,3,4,4,5,5,7]
>> x = {i for i in x}
>> set([1, 2, 3, 4, 5, 7])
>>
>> y = ('name','age','year')
>> x = ['John','24','2015']
>> z = {i:j for i,j in zip(y,x)}
>> {'age': '24', 'name': 'John', 'year': '2015'}
>>```
>>
>> This shows how easily you can use comprehension to create complicated custom data structures using one line.

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





