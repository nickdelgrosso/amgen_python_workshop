
# Python Built-In Type Methods

All Python objects are **Objects**, which means they have **Properties/Attributes** (data) and **Methods** (functions) associated with them.  These are accessible via the **Dot Notation**. 

For example, here we use a string **Class**'s *title()* method:


```python
film = 'the lion king'
bigfilm = film.title()
bigfilm
```

    'The Lion King'

# Exercises

## The Variable Subject

You want to label your figure title with the subject code, and the subject code changes depending on which subject is being shown!  How could you stick a subject's name in your title string?


```python
subject = 'NOP234'
title = "Mean Values of SUBJECT's data over Time"
```


If you had formatted your title string in the following way, though, another string method would be more useful.  Which method would you use for this title:


```python
subject1 = 'NOP234'
subject2 = 'GHS673'
title = "Performance Comparison between Subjects {} and {}"
```


## One more!

You have a list of subjects, and you want to add another subject to that list!  How would you do it?


```python
subjects = ['NOP234', 'GHS673', 'JGL212']
new_subject = 'ASF193'
```


## Add Lots at once!

Now, a bunch of new subjects appeared!  How do you add them to the main list, using a list method?


```python
subjects = ['NOP234', 'GHS673', 'JGL212']
new_subjects = ['ASF193', 'THW994', 'JJZ231']
```


## Nice and Neat.

Please sort the following subjects into alphabetical order.  It looks better that way, doesn't it?


```python
subjects = ['NOP234', 'GHS673', 'jGL212', 'ASF193', 'THW994', 'JJZ231']
```



## The Bad Subject

Oh, no, 'JGL202' was a terrible subject; he intentionally ruined your study!  How do you remove him from the list?


```python
subjects = ['NOP234', 'GHS673', 'JGL212', 'ASF193', 'THW994', 'JJZ231']

```



## The Limited Abstract

The conference says it only takes abstracts that have a maximum word count of 100 words.  Did our abstract make the cut?  

**hint: the len() function is useful here**


```python
abstract = """We analyze the locomotor behavior of the rat during exploration, 
and show that digitally collected data (time series of positions) 
provide a sufftcient basis for establishing that the rat uses several distinct modes of motion (first, second, 
third, and sometimes fourth gear). The distinction between these modes is obtained by first segmenting the 
time series into sequences of data points occurring between arrests (as ascertained within the resolution of 
the data acquisition system). The statistical distribution of the maximal amount of motion occurring within 
each of these episodes is then analyzed and shown to be multi modal. This enables us to decompose motion into 
distinct modes."""

```



## The Balloon Seller

A balloon seller (oops, I mean the balloon Scientist!) is giving out free balloons to all the, umm, researchers in the neighborhood.  He has three balloons, and wants to give them to Jenny, Manny, and Benny.  

How can he assign them to them one at a time?


```python
balloons = ['red', 'blue', 'green']
```


