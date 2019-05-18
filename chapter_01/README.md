# Chapter 1: Language Processing and Python

1. Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).

    ```python
    >>> 12 / (4 + 1)
    2
    >>> (12 / 4) + 1
    4
    >>> 12 / 4 + 1
    4
    ```

2. Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, 10-letter strings we can form. That works out to 141167095653376L (the L at the end just indicates that this is Python's long-number format). How many hundred-letter strings are possible?

    ```python
    >>> 26 ** 100
    3142930641582938830174357788501626427282669988762475256374173175398995908420104023465432599069702289330964075081611719197835869803511992549376L
    ```

3. The Python multiplication operation can be applied to lists. What happens when you type `['Monty', 'Python'] * 20`, or `3 * sent1`?

    ```python
    >>> ['Monty', 'Python'] * 5
    ['Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python']
    >>> sent1 = ['Call', 'me', 'Ishmael', '.']
    >>> 3 * sent1
    ['Call', 'me', 'Ishmael', '.', 'Call', 'me', 'Ishmael', '.', 'Call', 'me', 'Ishmael', '.']
    ```

4. Review Section 1.1 on computing with language. How many words are there in text2? How many distinct words are there?

    ```python
    >>> from nltk.book import *
    ...
    >>> len(text2)
    141576
    ```

5. Compare the lexical diversity scores for humor and romance fiction in Table 1-1. Which genre is more lexically diverse?

      **Lexical diversity** describes the ratio of unique words with the total number of words of a given text. The romance genre has a larger lexical diversity of 8.3, compared to humour's lexical diversity of 4.3.

6. Produce a dispersion plot of the four main protagonists in _Sense and Sensibility_: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?

    TODO.

7. Find the collocations in text5.

A **collocation** is a sequence of words that occur together unusually often.

```python
>>> text5.collocations()
wanna chat; PART JOIN; MODE 14-19teens; JOIN PART; PART PART;
cute.-ass MP3; MP3 player; JOIN JOIN; times .. .; ACTION watches; guys
wanna; song lasts; last night; ACTION sits; -...)...- S.M.R.; Lime
Player; Player 12%; dont know; lez gurls; long time
```

8. Consider the following Python expression: `len(set(text4))`. State the purpose of this expression. Describe the two steps involved in performing this computation.

    The `set()` function returns all unique words of the given text. The `len()` function returns the total number of occurences of a given argument. Hence, the Python expression above eveals the **total number of unique words of a given text**.

9. Review Section 1.2 on lists and strings.

    a. Define a string and assign it to a variable, e.g., `my_string = 'My String'` (but put something more interesting in the string). Print the contents of this variable in two ways, first by simply typing the variable name and pressing Enter, then by using the print statement.

    TODO.

    b. Try adding the string to itself using `my_string + my_string`, or multiplying it by a number, e.g., `my_string * 3`. Notice that the strings are joined together without any spaces. How could you fix this?

    TODO.

10. Define a variable my_sent to be a list of words, using the syntax `my_sent = ["My", "sent"]` (but with your own words, or a favorite saying).

    a. Use `' '.join(my_sent)` to convert this into a string.

    TODO.

    b. Use `split()` to split the string back into the list form you had to start with.

    TODO.

11. Define several variables containing lists of words, e.g., phrase1, phrase2, and so on. Join them together in various combinations (using the plus operator) to form 1.8 Exercises | 35 whole sentences. What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?

    TODO.

12. Consider the following two expressions, which have the same value. Which one
will typically be more relevant in NLP? Why?

    a. "Monty Python"[6:12]

    TODO.

    b. ["Monty", "Python"][1]

    TODO.

13. We have seen how to represent a sentence as a list of words, where each word is
a sequence of characters. What does sent1[2][2] do? Why? Experiment with other
index values.

14. The first sentence of text3 is provided to you in the variable sent3. The index of the in sent3 is 1, because sent3[1] gives us 'the'. What are the indexes of the two other occurrences of this word in sent3?

15. Review the discussion of conditionals in Section 1.4. Find all words in the Chat Corpus (text5) starting with the letter b. Show them in alphabetical order.

    TODO.

16. Type the expression range(10) at the interpreter prompt. Now try range(10, 20), range(10, 20, 2), and range(20, 10, -2). We will see a variety of uses for this built-in function in later chapters.

    TODO.

17. Use text9.index() to find the index of the word sunset. You'll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.

    TODO.

18. Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.

    TODO.

19. What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?

    >>> sorted(set([w.lower() for w in text1]))

    >>> sorted([w.lower() for w in set(text1)])

20. What is the difference between the following two tests: w.isupper() and not w.islower()?

    TODO.

21. Write the slice expression that extracts the last two words of text2.

    TODO.

22. Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

23. Review the discussion of looping with conditions in Section 1.4. Use a combination of for and if statements to loop over the words of the movie script for Monty Python and the Holy Grail (text6) and print all the uppercase words, one per line.

    TODO.

24. Write expressions for finding all words in text6 that meet the following conditions. The result should be in the form of a list of words: ['word1', 'word2', ...].

    TODO.